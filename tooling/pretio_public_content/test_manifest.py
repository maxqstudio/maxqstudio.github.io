import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("manifest.py")
spec = importlib.util.spec_from_file_location("pretio_manifest", MODULE)
manifest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(manifest)


class ExhaustiveCatalogManifestTests(unittest.TestCase):
    def test_all_countries_and_active_catalogs_are_included(self):
        catalog = json.loads((ROOT / "pretio/promos/catalog_app.json").read_text(encoding="utf-8"))
        records = manifest.build_manifest(catalog)
        expected = {(loc["country_code"], item["id"])
                    for item in catalog["items"] if item["status"] == "active"
                    for loc in item["locations"]}
        self.assertEqual({(x["country"], x["catalog_id"]) for x in records}, expected)
        self.assertEqual(len(records), len(expected))
        # Unsupported currency does NOT drop a country from the scheduled scan.
        currencies = json.loads((ROOT / "pretio/data/currency.json").read_text(encoding="utf-8"))
        covered = {code for cur in currencies["currencies"] for code in cur["countries"]}
        self.assertTrue(any(entry["country"] not in covered for entry in records))

    def test_no_early_stop_after_a_valid_update(self):
        catalog = {
            "schema": "pretio.catalog_app.v2", "schema_version": 2,
            "items": [
                {"id": "a", "status": "active", "locations": [{"country_code": "DE"}], "merchant": "A", "url": "https://example.com/a"},
                {"id": "b", "status": "active", "locations": [{"country_code": "DE"}], "merchant": "B", "url": "https://example.com/b"},
                {"id": "c", "status": "active", "locations": [{"country_code": "CL"}], "merchant": "C", "url": "https://example.com/c"},
            ],
        }
        work = manifest.build_manifest(catalog)
        self.assertEqual(len(work), 3)
        only_one = [{"work_id": work[0]["work_id"], "status": "UPDATED"}]
        result = manifest.coverage(work, only_one)
        self.assertEqual(result["cycle_status"], "INCOMPLETE")
        self.assertEqual(result["pending"], 2)
        receipts = only_one + [{"work_id": work[1]["work_id"], "status": "SKIPPED_NO_PROMO"},
                               {"work_id": work[2]["work_id"], "status": "SKIPPED_UNAVAILABLE"}]
        done = manifest.coverage(work, receipts)
        self.assertEqual(done["cycle_status"], "COMPLETED")
        self.assertEqual(done["pending"], 0)
        self.assertEqual(done["updated"], 1)
        self.assertEqual(done["skipped"], 2)

    def test_one_off_indonesia_runs_only_indonesia_once(self):
        catalog = json.loads((ROOT / "pretio/promos/catalog_app.json").read_text(encoding="utf-8"))
        all_work = manifest.build_manifest(catalog)
        scoped = manifest.build_manifest(catalog, country="ID")
        self.assertGreater(len(all_work), len(scoped))
        self.assertGreater(len(scoped), 0)
        self.assertTrue(all(entry["country"] == "ID" for entry in scoped))
        self.assertEqual(len(scoped), sum(1 for x in all_work if x["country"] == "ID"))
        receipts = [{"work_id": x["work_id"], "status": "SKIPPED_NO_CHANGE"} for x in scoped]
        self.assertEqual(manifest.coverage(scoped, receipts)["cycle_status"], "COMPLETED")
        foreign = next(x for x in all_work if x["country"] != "ID")
        receipts.append({"work_id": foreign["work_id"], "status": "UPDATED"})
        with self.assertRaisesRegex(ValueError, "Unexpected catalog receipt"):
            manifest.coverage(scoped, receipts)

    def test_invalid_or_missing_one_off_country_rejected(self):
        catalog = json.loads((ROOT / "pretio/promos/catalog_app.json").read_text(encoding="utf-8"))
        with self.assertRaisesRegex(ValueError, "explicit ISO country"):
            manifest.build_manifest(catalog, country="indonesia")
        with self.assertRaisesRegex(ValueError, "No active catalogs"):
            manifest.build_manifest(catalog, country="AQ")

    def test_duplicate_country_locations_do_not_duplicate_work(self):
        catalog = {"schema": "pretio.catalog_app.v2", "schema_version": 2, "items": [
            {"id": "shop", "status": "active", "locations": [{"country_code": "ID", "province_code": "31"},
                                                              {"country_code": "ID", "province_code": "32"}],
             "merchant": "Store", "url": "https://example.com"}
        ]}
        self.assertEqual(len(manifest.build_manifest(catalog)), 1)

    def test_receipts_must_be_unique_terminal_and_known(self):
        work = [{"work_id": "ID:one"}, {"work_id": "DE:two"}]
        for invalid in (
            [{"work_id": "ID:one", "status": "UPDATED"}, {"work_id": "ID:one", "status": "SKIPPED_NO_CHANGE"}],
            [{"work_id": "ID:one", "status": "PENDING"}],
            [{"work_id": "XX:unknown", "status": "FAILED"}],
        ):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                manifest.coverage(work, invalid)


if __name__ == "__main__":
    unittest.main()
