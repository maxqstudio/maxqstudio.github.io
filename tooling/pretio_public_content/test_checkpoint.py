import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import checkpoint


class CheckpointTests(unittest.TestCase):
    def setUp(self):
        self.catalog = {"schema": "pretio.catalog_app.v2", "schema_version": 2, "items": [
            {"id": "a", "status": "active", "locations": [{"country_code": "ID"}]},
            {"id": "b", "status": "active", "locations": [{"country_code": "DE"}]},
        ]}
        self.ledger = checkpoint.init_ledger(self.catalog, "run-1", "a" * 40, "catalog", ["ID", "DE", "AU"])

    def add(self, ledger, phase, key, status):
        return checkpoint.record(ledger, phase, key, status, "documented outcome", "audit/checklist.md")

    def test_resume_frozen_manifest_and_exact_retry(self):
        ledger = self.add(self.ledger, "catalog", "DE:b", "SKIPPED_BLOCKED")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "run.json"
            checkpoint.write_atomic(path, ledger)
            ledger = json.loads(path.read_text(encoding="utf-8"))
        self.catalog["items"].clear()
        self.assertEqual(checkpoint.summary(ledger)["next_catalog"]["work_id"], "ID:a")
        self.assertEqual(self.add(ledger, "catalog", "DE:b", "SKIPPED_BLOCKED"), ledger)
        with self.assertRaises(ValueError):
            self.add(ledger, "catalog", "DE:b", "UPDATED")

    def test_discovery_is_separate_and_required(self):
        with self.assertRaises(ValueError):
            self.add(self.ledger, "discovery", "AU", "CHECKED")
        ledger = self.add(self.ledger, "catalog", "DE:b", "FAILED")
        ledger = self.add(ledger, "catalog", "ID:a", "SKIPPED_NO_PROMO")
        self.assertEqual(checkpoint.summary(ledger)["registered_status"], "COMPLETED")
        self.assertEqual(checkpoint.summary(ledger)["cycle_status"], "INCOMPLETE")
        for market in ["AU", "DE", "ID"]:
            ledger = self.add(ledger, "discovery", market, "SKIPPED_UNVERIFIED")
        self.assertEqual(checkpoint.summary(ledger)["cycle_status"], "RESEARCH_TERMINAL")
        self.assertEqual(checkpoint.summary(ledger)["discovery_pending"], [])

    def test_scope_and_evidence(self):
        with self.assertRaises(ValueError):
            checkpoint.init_ledger(self.catalog, "run-1", "a" * 40, "highlights", ["ID", "DE", "AU"])
        scoped = checkpoint.init_ledger(self.catalog, "run-1", "a" * 40, "highlights", ["ID"], "ID")
        with self.assertRaises(ValueError):
            self.add(scoped, "catalog", "DE:b", "UPDATED")
        with self.assertRaises(ValueError):
            checkpoint.record(scoped, "catalog", "ID:a", "UPDATED", "", "audit")
        with self.assertRaises(ValueError):
            checkpoint.record(scoped, "catalog", "ID:a", "PENDING", "not done", "audit")

    def test_mutated_plan_rejected(self):
        self.ledger["plan"]["work_units"].pop()
        with self.assertRaisesRegex(ValueError, "plan mismatch"):
            checkpoint.summary(self.ledger)

    def test_duplicate_discovery_receipt_rejected(self):
        ledger = self.add(self.ledger, "catalog", "DE:b", "FAILED")
        ledger = self.add(ledger, "catalog", "ID:a", "FAILED")
        ledger = self.add(ledger, "discovery", "AU", "CHECKED")
        ledger["discovery_receipts"].append(dict(ledger["discovery_receipts"][0]))
        with self.assertRaises(ValueError):
            checkpoint.summary(ledger)


if __name__ == "__main__":
    unittest.main()
