"""Deterministic integrity tests for the documented Pretio 2026-11-23 one-off run.

These checks verify consistency of the saved repository evidence only. They DO
NOT independently prove which external pages were visited, which search
queries were issued, whether robots/Terms were respected, or whether permission
to link was granted. Successful CI must never be presented as audit clearance.
The original operator report and independent HOLD remain authoritative.
"""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re
import unittest


REPO = Path(__file__).resolve().parents[2]
RUN = REPO / "pretio/promos/highlights/audit/oneoff-global-2026-11-23"
DISCOVERY = RUN / "discovery"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class OneOffAuditEvidenceIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = read_json(RUN / "registered-manifest.json")
        cls.registered_progress = read_json(RUN / "registered/progress.json")
        cls.receipts = read_json(RUN / "registered/terminal-receipts.json")
        cls.register = read_json(RUN / "country-discovery-register.json")
        cls.discovery_progress = read_json(DISCOVERY / "progress.json")
        cls.metadata = read_json(RUN / "run-metadata.json")

    def test_frozen_manifest_and_registered_receipts_match_exactly(self):
        units = self.manifest["work_units"]
        work_ids = [u["work_id"] for u in units]
        receipt_ids = [r["work_id"] for r in self.receipts]
        self.assertEqual(len(units), self.manifest["manifest_total"])
        self.assertEqual(len(work_ids), len(set(work_ids)), "Duplicate frozen work_id")
        self.assertEqual(work_ids, receipt_ids, "Receipts must preserve frozen manifest ordering")
        self.assertEqual(len(receipt_ids), len(set(receipt_ids)))
        self.assertEqual(
            Counter(r["status"] for r in self.receipts),
            Counter(self.registered_progress["status_counts"]),
        )
        progress = self.registered_progress
        self.assertEqual(progress["manifest_total"], len(units))
        self.assertEqual(progress["terminal_receipts"], len(receipt_ids))
        self.assertEqual(progress["pending"], len(units) - len(receipt_ids))
        self.assertEqual(progress["pending_work_ids"], [])
        self.assertEqual(progress["scope"], "ONE_OFF_GLOBAL")
        self.assertEqual(progress["cycle_status"], "COMPLETED")
        self.assertEqual(self.metadata["registered_manifest"]["terminal_receipts"], len(receipt_ids))

        receipt_dir = RUN / "registered/receipts"
        all_raw = sorted(receipt_dir.glob("*.json"))
        self.assertEqual(len(all_raw), len(units), "Missing/extra per-catalog receipt files")
        from_files = {read_json(p)["work_id"]: read_json(p)["status"] for p in all_raw}
        self.assertEqual(from_files, {r["work_id"]: r["status"] for r in self.receipts})

    def test_country_register_matches_partial_discovery_accounting(self):
        rows = self.register["markets"]
        progress = self.discovery_progress
        self.assertEqual(len(rows), self.register["candidate_country_count"])
        self.assertEqual(len(rows), progress["candidate_country_count"])
        self.assertEqual(len({m["code"] for m in rows}), len(rows))
        selected = [m for m in rows if m["selected"]]
        outside = [m for m in rows if not m["selected"]]
        self.assertEqual(len(selected), self.register["selected_count"])
        self.assertEqual(len(selected), progress["selected_count"])
        self.assertEqual(len(outside), len(rows) - len(selected))
        self.assertEqual(
            set(m["selection_rank"] for m in selected),
            set(range(1, len(selected) + 1)),
        )
        dispositions = Counter(m["disposition"] for m in selected)
        pending = dispositions.pop("PENDING_RESEARCH", 0)
        self.assertEqual(pending, progress["pending_disposition_count"])
        self.assertEqual(sum(dispositions.values()), progress["terminal_disposition_count"])
        self.assertEqual(dict(dispositions), progress["disposition_counts"])
        self.assertEqual(progress["selected_count"], pending + sum(dispositions.values()))
        self.assertEqual(progress["status"], "INCOMPLETE")
        self.assertEqual(self.metadata["status"], "INCOMPLETE")
        self.assertEqual(self.metadata["country_discovery"]["pending_disposition_count"], pending)
        self.assertEqual(self.metadata["country_discovery"]["terminal_disposition_count"], sum(dispositions.values()))
        self.assertEqual(progress["verified_official_catalog_count"], 0)

    def test_every_terminal_country_has_checkpoint_and_handoff(self):
        selected_terminal = [
            m for m in self.register["markets"]
            if m["selected"] and m["disposition"] != "PENDING_RESEARCH"
        ]
        checkpoints = sorted((DISCOVERY / "checkpoints").glob("*.md"))
        handoffs = sorted((DISCOVERY / "handoffs").glob("*.md"))
        checkpoint_by_country = [p.name[:2] for p in checkpoints]
        handoff_by_country = [p.name[:2] for p in handoffs]
        expected = {m["code"] for m in selected_terminal}
        self.assertEqual(set(checkpoint_by_country), expected)
        self.assertEqual(set(handoff_by_country), expected)
        self.assertEqual(len(checkpoint_by_country), len(set(checkpoint_by_country)))
        self.assertEqual(len(handoff_by_country), len(set(handoff_by_country)))
        declared = {p.removeprefix("checkpoints/") for p in self.discovery_progress["checkpoint_paths"]}
        self.assertEqual(declared, {p.name for p in checkpoints})

    def test_za_final_status_is_explicit_and_initial_status_superseded(self):
        za = next(m for m in self.register["markets"] if m["code"] == "ZA")
        self.assertEqual(za["disposition"], "NEEDS_CATALOG_APPROVAL")
        checkpoint = (DISCOVERY / "checkpoints/ZA-south-africa.md").read_text(encoding="utf-8")
        handoff = (DISCOVERY / "handoffs/ZA-south-africa.md").read_text(encoding="utf-8")
        for doc in (checkpoint, handoff):
            self.assertIn("NEEDS_CATALOG_APPROVAL", doc)
            self.assertIn("SKIPPED_UNVERIFIED", doc)
            self.assertIn("superseded", doc.lower())
            self.assertIn("Newton Park SPAR", doc)
            self.assertIn("local", doc.lower())

    def test_query_ledger_sum_does_not_falsely_clear_provenance(self):
        ledger = (DISCOVERY / "query-reconciliation-audit.md").read_text(encoding="utf-8")
        pattern = re.compile(r"^\| ([A-Z]{2}) \| (\d+) \| (\d+) \| (\d+) \|", re.M)
        count_rows = pattern.findall(ledger)
        self.assertEqual(len(count_rows), self.discovery_progress["terminal_disposition_count"])
        self.assertEqual(len({code for code, *_ in count_rows}), len(count_rows))
        subtotal = [sum(int(row[i]) for row in count_rows) for i in (1, 2, 3)]
        self.assertEqual(subtotal, [33, 34, 35], "Update ledger and cited evidence if narrative changes")
        claimed = self.discovery_progress["bounded_searches_used"]
        reported = [
            claimed["catalog_promo_searches"],
            claimed["online_shop_marketplace_searches"],
            claimed["official_leads_opened"],
        ]
        self.assertEqual([a - b for a, b in zip(reported, subtotal)], [3, 5, 4])
        self.assertIn("NOT VERIFIED", ledger)
        self.assertIn("NOT_VERIFIED", self.discovery_progress["provenance_audit"])
        self.assertEqual(
            {code: catalog for code, catalog, _, _ in count_rows if code in {"CL", "CO", "EC"}},
            {"CL": "2", "CO": "2", "EC": "2"},
            "Three over-budget Catalog Promo queries must not be double-counted",
        )

    def test_incident_and_permission_hold_not_misrepresented_as_pass(self):
        deviations = (DISCOVERY / "deviations.md").read_text(encoding="utf-8")
        iq = (DISCOVERY / "checkpoints/IQ-iraq.md").read_text(encoding="utf-8")
        report = (RUN / "run-report.md").read_text(encoding="utf-8")
        for doc in (deviations, iq, report):
            self.assertIn("Taawon", doc)
            self.assertIn("GPTBot", doc)
        self.assertIn("Pick n Pay", deviations)
        self.assertIn("04:00", deviations)
        self.assertIn("08:45", deviations)
        self.assertIn("unauthorized access-policy deviation", deviations)
        self.assertIn("outside the permitted visit window", deviations)
        self.assertIn("HOLD", report)
        self.assertIn("Issue #61", report)
        self.assertIn("HOLD", self.discovery_progress["compliance_audit"])

    def test_owner_source_exclusions_are_enforced_in_run_evidence(self):
        policy = read_json(RUN / "source-exclusions.json")
        self.assertEqual(policy["scope"], "ONE_OFF_GLOBAL")
        self.assertEqual(policy["run_id"], self.register["run_id"])
        self.assertEqual(
            policy["decision"],
            "OWNER_EXCLUDE_NONCOMPLIANT_ACCESS_FROM_CRAWL_RESULTS",
        )
        self.assertTrue(policy["retain_historical_evidence"])
        self.assertTrue(policy["do_not_modify_frozen_registered_manifest"])
        self.assertTrue(policy["do_not_modify_historical_query_counts"])
        self.assertTrue(policy["do_not_modify_preexisting_public_catalog_or_highlight_items"])

        sources = policy["excluded_sources"]
        self.assertEqual(
            {(s["country"], s["catalog_id"]) for s in sources},
            {
                ("IQ", "taawon-iq-weekly-offers"),
                ("ZA", "pnp-za-country"),
            },
        )
        receipts = {r["work_id"]: r["status"] for r in self.receipts}
        markets = {m["code"]: m["disposition"] for m in self.register["markets"]}
        for s in sources:
            self.assertEqual(receipts[s["registered_work_id"]], s["registered_receipt"])
            self.assertEqual(markets[s["country"]], s["market_disposition"])
            self.assertTrue(s["exclude_current_run_content"])
            self.assertTrue(s["exclude_from_verified_coverage"])
            self.assertTrue(s["exclude_from_product_highlights_candidates"])
            self.assertTrue(s["exclude_from_catalog_approval"])
            self.assertTrue(s["historical_attempts_still_counted"])
        self.assertEqual(self.discovery_progress["product_candidates_accepted"], 0)
        self.assertEqual(self.discovery_progress["verified_official_catalog_count"], 0)
        self.assertIn("HOLD", policy["audit_verdict"])
        report = (RUN / "run-report.md").read_text(encoding="utf-8")
        self.assertIn("source-exclusions.json", report)
        self.assertIn("historical", report.lower())

    def test_retired_catalog_has_no_highlight_foreign_key(self):
        catalog = read_json(REPO / "pretio/promos/catalog_app.json")
        catalog_ids = {item["id"] for item in catalog["items"]}
        self.assertNotIn("lidl-es-country", catalog_ids)
        self.assertEqual(len(catalog_ids), len(catalog["items"]))
        index = read_json(REPO / "pretio/promos/highlights/index.json")
        for country in index["countries"]:
            feed = read_json(REPO / "pretio/promos/highlights" / f"{country['code']}.json")
            for item in feed["items"]:
                self.assertNotEqual(item["catalog_id"], "lidl-es-country")
                self.assertIn(item["catalog_id"], catalog_ids)


if __name__ == "__main__":
    unittest.main()
