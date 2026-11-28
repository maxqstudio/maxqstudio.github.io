import json
import shutil
import tempfile
import unittest
from datetime import date
from pathlib import Path

from validate import Invalid, digest, read
from validate_location_highlights import (
    SCHEMA, validate_candidate, build_candidate_index, validate_locations,
)

ROOT = Path(__file__).resolve().parents[2]
TODAY = date(2026, 11, 28)


class LocationHighlightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.candidate = Path(self.temp.name) / "candidate"
        self.candidate.mkdir()
        for rel in ("pretio/promos/catalog_app.json", "pretio/data/currency.json"):
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, path)
        self.loc_dir = self.root / "pretio/location/v2"
        self.loc_dir.mkdir(parents=True)
        self.country = {
            "schema": "pretio.location.country.v2", "schema_version": 2,
            "country_code": "DE", "country": "Germany", "revision": "fixture",
            "provinces": [{
                "type": "province", "province_code": "DE-BY", "province": "Bavaria",
                "cities": [{"type": "city", "city_code": "MUC", "city": "Munich"}],
            }],
            "root_cities": [{"type": "city", "city_code": "ROOT", "city": "Root city"}],
        }
        self.write(self.loc_dir / "DE.json", self.country)
        self.write(self.loc_dir / "index.json", {
            "schema": "pretio.location.index.v2", "schema_version": 2,
            "countries": [{"code": "DE", "name": "Germany", "revision": "fixture",
                "url": "https://maxqstudio.dev/pretio/location/v2/DE.json",
                "sha256": digest(self.loc_dir / "DE.json"),
                "subdivision_count": 1, "place_count": 2}],
        })
        self.national = {"type": "country", "country_code": "DE", "country": "Germany"}
        self.province = dict(self.national, type="province", province_code="DE-BY",
                             province="Bavaria")
        self.city = dict(self.province, type="city", city_code="MUC", city="Munich")
        self.root_city = dict(self.national, type="city", city_code="ROOT", city="Root city")
        cat = next(x for x in read(self.root / "pretio/promos/catalog_app.json")["items"]
                   if x["id"] == "rewe-de-country")
        self.item = {"id": "fixture-only", "catalog_id": cat["id"], "retailer": cat["merchant"],
                     "product_name": "Synthetic test item", "normal_price": "3.99",
                     "promo_price": "1.99", "currency": "EUR",
                     "image_url": "https://example.invalid/fixture.png",
                     "source_url": cat["url"], "observed_at": "2026-11-28T00:00:00Z",
                     "valid_until": "2026-11-30", "locations": [self.city]}
        self.feed = {"schema": SCHEMA, "schema_version": 2, "country": "DE",
                     "currency": "EUR", "revision": "fixture", "generated_at": "2026-11-28T00:00:00Z",
                     "items": [self.item]}
        self.write(self.candidate / "DE.json", self.feed)

    @staticmethod
    def write(path, data):
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def stage(self):
        return build_candidate_index(self.root, self.candidate, TODAY)

    def test_valid_city_province_national_and_root_city(self):
        self.feed["items"] = [dict(self.item, id=str(i), locations=[loc])
                              for i, loc in enumerate([self.city, self.province, self.national, self.root_city])]
        self.write(self.candidate / "DE.json", self.feed)
        result = self.stage()
        self.assertEqual(result, validate_candidate(self.root, self.candidate, TODAY))
        self.assertEqual(result["schema_version"], 3)
        self.assertEqual(result["countries"][0]["sha256"], digest(self.candidate / "DE.json"))

    def test_multiple_locations_and_invalid_rules(self):
        directory = ("Germany", {"DE-BY": "Bavaria", "DE-BE": "Berlin"},
                     {"MUC": ("DE-BY", "Munich")})
        berlin = dict(self.province, province_code="DE-BE", province="Berlin")
        validate_locations([self.province, berlin], "DE", directory, "test")
        for rules in ([], [self.national, self.city], [self.city, self.city],
                      [dict(self.city, province_code="DE-BE", province="Berlin")],
                      [dict(self.city, city="wrong")],
                      [dict(self.city, country_code="ID")],
                      [dict(self.national, city="Munich")],
                      [dict(self.city, store="unrepresentable")]):
            with self.subTest(rules=rules), self.assertRaises(Invalid):
                validate_locations(rules, "DE", directory, "test")

    def test_missing_location_rejects_before_index_write(self):
        self.item.pop("locations")
        self.write(self.candidate / "DE.json", self.feed)
        with self.assertRaises(Invalid):
            self.stage()
        self.assertFalse((self.candidate / "index.json").exists())

    def test_expired_or_invalid_discount_rejected(self):
        for patch in ({"valid_until": "2026-11-27"}, {"promo_price": "9.99"},
                      {"valid_until": "2026-11-30T00:00:00Z"}):
            self.feed["items"] = [dict(self.item, **patch)]
            self.write(self.candidate / "DE.json", self.feed)
            with self.subTest(patch=patch), self.assertRaises(Invalid):
                self.stage()

    def test_location_authority_hash_mismatch(self):
        path = self.loc_dir / "DE.json"
        path.write_bytes(path.read_bytes() + b"\n")
        with self.assertRaisesRegex(Invalid, "location index binding mismatch"):
            self.stage()

    def test_feed_byte_or_index_binding_change_rejected(self):
        self.stage()
        path = self.candidate / "DE.json"
        path.write_bytes(path.read_bytes() + b"\n")
        with self.assertRaisesRegex(Invalid, "binding/hash/revision mismatch"):
            validate_candidate(self.root, self.candidate, TODAY)

    def test_duplicate_ids_and_unsupported_fields(self):
        for items in ([self.item, self.item], [dict(self.item, unapproved_field=True)]):
            self.feed["items"] = items
            self.write(self.candidate / "DE.json", self.feed)
            with self.assertRaises(Invalid):
                self.stage()

    def test_existing_index_and_public_target_never_written(self):
        self.stage()
        before = (self.candidate / "index.json").read_bytes()
        with self.assertRaises(Invalid):
            self.stage()
        self.assertEqual(before, (self.candidate / "index.json").read_bytes())
        public = self.root / "pretio/promos/highlights/v2"
        public.mkdir(parents=True)
        with self.assertRaisesRegex(Invalid, "outside|public"):
            build_candidate_index(self.root, public, TODAY)
        self.assertFalse((public / "index.json").exists())


if __name__ == "__main__":
    unittest.main()
