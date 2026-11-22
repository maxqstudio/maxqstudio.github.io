#!/usr/bin/env python3
"""Build the full 12-hour Pretio catalog work manifest; verify terminal receipt coverage.

No scraping, publishing, or production JSON mutation is performed by this tool.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TERMINAL = {
    "UPDATED",
    "SKIPPED_NO_CHANGE",
    "SKIPPED_NO_PROMO",
    "SKIPPED_UNAVAILABLE",
    "SKIPPED_BLOCKED",
    "SKIPPED_UNVERIFIED",
    "BLOCKED_CURRENCY_METADATA",
    "FAILED",
}


def build_manifest(catalog: dict) -> list[dict]:
    if catalog.get("schema") != "pretio.catalog_app.v2" or catalog.get("schema_version") != 2:
        raise ValueError("Expected Pretio catalog v2")
    raw_items = catalog.get("items")
    if not isinstance(raw_items, list):
        raise ValueError("Missing catalog entries")
    result = {}
    for item in raw_items:
        if not isinstance(item, dict):
            raise ValueError("Invalid catalog entry")
        if item.get("status") != "active":
            continue
        cid = item.get("id")
        locs = item.get("locations")
        if not isinstance(cid, str) or not cid or not isinstance(locs, list) or not locs:
            raise ValueError("Active catalog missing id or location")
        for loc in locs:
            if not isinstance(loc, dict):
                raise ValueError("Invalid location rule")
            cc = loc.get("country_code")
            if not isinstance(cc, str) or not re.fullmatch(r"[A-Z]{2}", cc):
                raise ValueError("Invalid catalog country code")
            key = cc + ":" + cid
            if key not in result:
                result[key] = {
                    "work_id": key,
                    "country": cc,
                    "catalog_id": cid,
                    "retailer": item.get("merchant"),
                    "url": item.get("url"),
                    "valid_until": item.get("valid_until"),
                }
    # Every active country/catalog pair is included, independent of currency or highlights feeds.
    return sorted(result.values(), key=lambda x: (x["country"], x["valid_until"] is not None, x["catalog_id"]))


def coverage(manifest: list[dict], receipts: list[dict]) -> dict:
    if not isinstance(receipts, list):
        raise ValueError("Receipts must be a list")
    expected = {entry["work_id"] for entry in manifest}
    observed: dict[str, str] = {}
    for receipt in receipts:
        if not isinstance(receipt, dict):
            raise ValueError("Invalid receipt")
        key, status = receipt.get("work_id"), receipt.get("status")
        if key not in expected:
            raise ValueError(f"Unexpected catalog receipt: {key}")
        if key in observed:
            raise ValueError(f"Duplicate catalog receipt: {key}")
        if status not in TERMINAL:
            raise ValueError(f"Non-terminal catalog status for {key}: {status}")
        observed[key] = status
    missing = sorted(expected - observed.keys())
    summary = {
        "cycle_status": "COMPLETED" if not missing else "INCOMPLETE",
        "manifest_total": len(expected),
        "terminal_receipts": len(observed),
        "pending": len(missing),
        "updated": sum(s == "UPDATED" for s in observed.values()),
        "skipped": sum(s.startswith("SKIPPED_") or s == "BLOCKED_CURRENCY_METADATA" for s in observed.values()),
        "failed": sum(s == "FAILED" for s in observed.values()),
        "pending_work_ids": missing,
    }
    if summary["manifest_total"] != summary["terminal_receipts"] + summary["pending"]:
        raise ValueError("Manifest accounting mismatch")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--receipts", type=Path, help="Optional JSON array of per-catalog terminal receipts")
    args = parser.parse_args()
    catalog = json.loads((args.root / "pretio/promos/catalog_app.json").read_text(encoding="utf-8"))
    manifest = build_manifest(catalog)
    if args.receipts:
        receipts = json.loads(args.receipts.read_text(encoding="utf-8"))
        result = coverage(manifest, receipts)
        print(json.dumps(result, indent=2))
        return 0 if result["cycle_status"] == "COMPLETED" else 2
    print(json.dumps({"manifest_total": len(manifest), "countries": len(set(x["country"] for x in manifest)), "work_units": manifest}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as exc:
        print(f"MANIFEST_FAILED: {exc}", file=sys.stderr)
        sys.exit(1)
