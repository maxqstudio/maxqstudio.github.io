#!/usr/bin/env python3
"""Single-writer, resumable audit ledger. No network or production writes."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path

from manifest import build_manifest, coverage

DISCOVERY = {"CHECKED", "SKIPPED_BLOCKED", "SKIPPED_UNAVAILABLE", "SKIPPED_UNVERIFIED", "FAILED"}
ROOT = Path(__file__).resolve().parents[2]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


def init_ledger(catalog, run_id, base_sha, kind, markets, country=None):
    if not isinstance(run_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]{1,100}", run_id):
        raise ValueError("Invalid run ID")
    if not re.fullmatch(r"[a-f0-9]{40}", base_sha):
        raise ValueError("Expected full baseline SHA")
    if kind not in {"catalog", "highlights"}:
        raise ValueError("Invalid writer")
    work = build_manifest(catalog, country)
    if not work:
        raise ValueError("Empty registered manifest")
    if (not isinstance(markets, list) or not markets
            or any(not isinstance(x, str) or not re.fullmatch(r"[A-Z]{2}", x) for x in markets)
            or len(set(markets)) != len(markets)):
        raise ValueError("Expected unique explicit discovery market codes")
    registered = {x["country"] for x in work}
    if not registered.issubset(markets) or (country and set(markets) != {country}):
        raise ValueError("Discovery markets do not cover registered scope")
    if kind == "highlights" and set(markets) != registered:
        raise ValueError("Highlights discovery must match registered markets")
    plan = {"run_id": run_id, "base_sha": base_sha, "kind": kind,
            "country": country, "work_units": work, "discovery_markets": sorted(markets)}
    return {"version": 1, "plan": plan, "plan_sha256": digest(plan),
            "catalog_receipts": [], "discovery_receipts": []}


def summary(ledger):
    if ledger.get("version") != 1 or digest(ledger["plan"]) != ledger["plan_sha256"]:
        raise ValueError("Frozen checkpoint plan mismatch")
    plan = ledger["plan"]
    work = plan["work_units"]
    if not work or len({x["work_id"] for x in work}) != len(work):
        raise ValueError("Empty or duplicate work manifest")
    result = coverage(work, ledger["catalog_receipts"])
    pending_ids = set(result["pending_work_ids"])
    result["next_catalog"] = next((x for x in work if x["work_id"] in pending_ids), None)
    for receipt in ledger["catalog_receipts"]:
        require_evidence(receipt)
    markets = set(plan["discovery_markets"])
    observed = set()
    for receipt in ledger["discovery_receipts"]:
        require_evidence(receipt)
        key = receipt.get("work_id")
        if key not in markets or key in observed or receipt.get("status") not in DISCOVERY:
            raise ValueError("Invalid or duplicate discovery receipt")
        observed.add(key)
    if observed and pending_ids:
        raise ValueError("Discovery cannot begin before registered manifest is terminal")
    result.update({"run_id": plan["run_id"], "base_sha": plan["base_sha"], "kind": plan["kind"],
                   "registered_status": result["cycle_status"],
                   "discovery_total": len(markets), "discovery_terminal": len(observed),
                   "discovery_pending": sorted(markets - observed),
                   "next_discovery": sorted(markets - observed)[0] if not pending_ids and markets - observed else None,
                   "cycle_status": "RESEARCH_TERMINAL" if not pending_ids and markets == observed else "INCOMPLETE"})
    return result


def require_evidence(receipt):
    if (not isinstance(receipt.get("evidence"), str) or not receipt["evidence"].strip()
            or not isinstance(receipt.get("reason"), str) or not receipt["reason"].strip()):
        raise ValueError("Receipt requires a reason and durable evidence/checklist reference")


def record(ledger, phase, work_id, status, reason, evidence):
    summary(ledger)
    if phase not in {"catalog", "discovery"}:
        raise ValueError("Invalid phase")
    key = phase + "_receipts"
    receipt = {"work_id": work_id, "status": status, "reason": reason, "evidence": evidence}
    existing = [r for r in ledger[key] if r["work_id"] == work_id]
    if existing:
        if existing[0] == receipt:
            return ledger  # exact retry is idempotent
        raise ValueError("Conflicting terminal receipt; review separately")
    candidate = {**ledger, key: [*ledger[key], receipt]}
    summary(candidate)
    return candidate


def write_atomic(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, prefix=".checkpoint-")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, required=True, help="Audit-only file outside the repository")
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("init")
    create.add_argument("--run-id", required=True)
    create.add_argument("--base-sha", required=True)
    create.add_argument("--kind", choices=["catalog", "highlights"], required=True)
    create.add_argument("--catalog", type=Path, required=True, help="Catalog snapshot from baseline SHA")
    create.add_argument("--markets", type=Path, required=True, help="Reviewed JSON list of discovery market codes")
    create.add_argument("--country")
    add = sub.add_parser("record")
    add.add_argument("--phase", choices=["catalog", "discovery"], required=True)
    add.add_argument("--work-id", required=True)
    add.add_argument("--status", required=True)
    add.add_argument("--reason", required=True)
    add.add_argument("--evidence", required=True)
    sub.add_parser("status")
    args = parser.parse_args()
    path = args.ledger.resolve()
    if path.is_relative_to(ROOT):
        raise ValueError("Keep audit ledger outside the repository")
    # One writer per run; the scheduler must not dispatch concurrent ledger writers.
    if args.command == "init":
        if path.exists():
            raise ValueError("Ledger already exists; resume it instead")
        ledger = init_ledger(json.loads(args.catalog.read_text(encoding="utf-8")),
                             args.run_id, args.base_sha, args.kind,
                             json.loads(args.markets.read_text(encoding="utf-8")), args.country)
        write_atomic(path, ledger)
    else:
        ledger = json.loads(path.read_text(encoding="utf-8"))
        if args.command == "record":
            ledger = record(ledger, args.phase, args.work_id, args.status, args.reason, args.evidence)
            write_atomic(path, ledger)
    state = summary(ledger)
    print(json.dumps(state, ensure_ascii=False, indent=2))
    return 2 if args.command == "status" and state["cycle_status"] == "INCOMPLETE" else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"CHECKPOINT_FAILED: {exc}", file=sys.stderr)
        sys.exit(1)
