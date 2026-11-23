"""Aggregate per-source receipts and verify the frozen global manifest.

This is audit-only bookkeeping. It performs no network requests and mutates no
production catalog or highlight data.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


RUN = Path(__file__).resolve().parent
RECEIPT_DIR = RUN / "registered" / "receipts"
ALLOWED = {
    "UPDATED",
    "SKIPPED_NO_CHANGE",
    "SKIPPED_NO_PROMO",
    "SKIPPED_UNAVAILABLE",
    "SKIPPED_BLOCKED",
    "SKIPPED_UNVERIFIED",
    "BLOCKED_CURRENCY_METADATA",
    "FAILED",
}

manifest = json.loads((RUN / "registered-manifest.json").read_text(encoding="utf-8"))
units = manifest["work_units"]
expected = {unit["work_id"] for unit in units}
if len(expected) != len(units):
    raise SystemExit("Frozen manifest contains duplicate work IDs")

found: dict[str, dict[str, str]] = {}
for path in sorted(RECEIPT_DIR.glob("*.json")):
    receipt = json.loads(path.read_text(encoding="utf-8"))
    work_id, status = receipt.get("work_id"), receipt.get("status")
    if work_id not in expected:
        raise SystemExit(f"Unknown receipt work_id in {path.name}: {work_id}")
    if work_id in found:
        raise SystemExit(f"Duplicate receipt for {work_id}")
    if status not in ALLOWED:
        raise SystemExit(f"Non-terminal/unknown status for {work_id}: {status}")
    found[work_id] = {"work_id": work_id, "status": status}

ordered = [found[unit["work_id"]] for unit in units if unit["work_id"] in found]
missing = [unit["work_id"] for unit in units if unit["work_id"] not in found]
counts = Counter(row["status"] for row in ordered)

(RUN / "registered" / "terminal-receipts.json").write_text(
    json.dumps(ordered, indent=2) + "\n", encoding="utf-8"
)
(RUN / "registered" / "progress.json").write_text(
    json.dumps(
        {
            "run_id": "pretio-oneoff-global-20261123T040625Z",
            "scope": "ONE_OFF_GLOBAL",
            "manifest_total": len(units),
            "terminal_receipts": len(ordered),
            "pending": len(missing),
            "cycle_status": "COMPLETED" if not missing else "INCOMPLETE",
            "status_counts": dict(sorted(counts.items())),
            "pending_work_ids": missing,
        },
        indent=2,
    )
    + "\n",
    encoding="utf-8",
)
print(
    json.dumps(
        {
            "manifest_total": len(units),
            "terminal_receipts": len(ordered),
            "pending": len(missing),
            "status_counts": dict(sorted(counts.items())),
        }
    )
)
