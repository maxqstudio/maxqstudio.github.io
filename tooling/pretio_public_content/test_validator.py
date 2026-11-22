import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[2]
MOD = HERE.parent / "validate.py"
spec = importlib.util.spec_from_file_location("pretio_validator", MOD)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class StrictPretioValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for relative in (
            "pretio/promos/catalog_app.json",
            "pretio/promos/highlights/index.json",
            "pretio/data/currency.json",
        ):
            src = ROOT / relative
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, target)
        index = validator.read(self.root / "pretio/promos/highlights/index.json")
        for row in index["countries"]:
            relative = "pretio/promos/highlights/" + row["code"] + ".json"
            shutil.copy2(ROOT / relative, self.root / relative)

    def tearDown(self):
        self.temp.cleanup()

    def file(self, rel):
        return self.root / rel

    def rewrite(self, rel, data):
        self.file(rel).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if rel.startswith("pretio/promos/highlights/") and rel.endswith(".json") and not rel.endswith("/index.json"):
            cc = Path(rel).stem
            indexfile = self.file("pretio/promos/highlights/index.json")
            index = validator.read(indexfile)
            for row in index["countries"]:
                if row["code"] == cc:
                    row["sha256"] = validator.digest(self.file(rel))
                    row["revision"] = data["revision"]
                    break
            indexfile.write_text(json.dumps(index, indent=2) + "\n")

    def test_baseline_validates_and_reports_expired_without_wiping(self):
        report = validator.validate(self.root, validator.date(2026, 11, 22))
        self.assertEqual(len(report["countries"]), 7)
        self.assertEqual(report["countries"]["DE"]["items"], 1)
        self.assertGreaterEqual(report["countries"]["CH"]["expired"], 1)

    def test_unknown_discount_percent_field_is_rejected(self):
        p = "pretio/promos/highlights/DE.json"
        feed = validator.read(self.file(p))
        feed["items"][0]["discount_percent"] = 30
        self.rewrite(p, feed)
        with self.assertRaisesRegex(validator.Invalid, "unsupported keys"):
            validator.validate(self.root, validator.date(2026, 11, 22))

    def test_regular_price_cannot_be_published_as_highlight(self):
        p = "pretio/promos/highlights/DE.json"
        feed = validator.read(self.file(p))
        feed["items"][0]["promo_price"] = feed["items"][0]["normal_price"]
        self.rewrite(p, feed)
        with self.assertRaisesRegex(validator.Invalid, "not a verified discount"):
            validator.validate(self.root, validator.date(2026, 11, 22))

    def test_unknown_catalog_fields_rejected(self):
        p = "pretio/promos/catalog_app.json"
        c = validator.read(self.file(p))
        c["items"][0]["marketing_score"] = 99
        self.rewrite(p, c)
        with self.assertRaisesRegex(validator.Invalid, "unsupported keys"):
            validator.validate(self.root)

    def test_strict_mode_requires_expired_items_removed(self):
        with self.assertRaisesRegex(validator.Invalid, "expired products present"):
            validator.validate(self.root, validator.date(2026, 11, 22), strict_expiry=True)

    def test_prune_removes_only_date_expired_and_updates_hashes(self):
        de_before = self.file("pretio/promos/highlights/DE.json").read_bytes()
        changes = validator.prune_expired(self.root, validator.date(2026, 11, 22))
        self.assertEqual(len(changes["CH"]), 4)
        self.assertEqual(len(changes["ZA"]), 4)
        self.assertNotIn("DE", changes)
        self.assertEqual(self.file("pretio/promos/highlights/DE.json").read_bytes(), de_before)
        self.assertEqual(validator.validate(self.root, validator.date(2026, 11, 22), strict_expiry=True)["countries"]["CH"]["items"], 0)
        self.assertEqual(validator.prune_expired(self.root, validator.date(2026, 11, 22)), {})

    def test_rotating_catalog_url_requires_valid_until(self):
        catalog_rel = "pretio/promos/catalog_app.json"
        baseline_path = self.root / "baseline-catalog.json"
        shutil.copy2(self.file(catalog_rel), baseline_path)
        catalog = validator.read(self.file(catalog_rel))
        catalog["items"][0]["url"] = "https://www.indomaret.co.id/promosi/weekly-november"
        catalog["items"][0]["valid_until"] = None
        self.rewrite(catalog_rel, catalog)
        with self.assertRaisesRegex(validator.Invalid, "needs evidenced valid_until"):
            validator.validate_catalog_link_changes(baseline_path, self.root)
        catalog["items"][0]["valid_until"] = "2026-11-30"
        self.rewrite(catalog_rel, catalog)
        self.assertTrue(validator.validate_catalog_link_changes(baseline_path, self.root))

    def test_missing_currency_blocks_new_country_feed(self):
        idx_p = "pretio/promos/highlights/index.json"
        index = validator.read(self.file(idx_p))
        cc = "ES"
        feed = {
            "schema": "pretio.product_highlights.v1", "schema_version": 1,
            "country": cc, "currency": "EUR", "revision": "es-test",
            "generated_at": "2026-11-22T12:00:00Z", "items": []
        }
        path = self.file(f"pretio/promos/highlights/{cc}.json")
        path.write_text(json.dumps(feed), encoding="utf-8")
        index["countries"].append({"code": cc, "document_id": cc, "revision": "es-test",
                                    "sha256": validator.digest(path),
                                    "url": f"https://maxqstudio.dev/pretio/promos/highlights/{cc}.json"})
        self.rewrite(idx_p, index)
        with self.assertRaisesRegex(validator.Invalid, "BLOCKED_CURRENCY_METADATA"):
            validator.validate(self.root)

    def test_index_hash_must_match_exact_feed_bytes(self):
        p = self.file("pretio/promos/highlights/DE.json")
        p.write_bytes(p.read_bytes() + b"\n")
        with self.assertRaisesRegex(validator.Invalid, "SHA256 mismatch"):
            validator.validate(self.root)


if __name__ == "__main__":
    unittest.main()
