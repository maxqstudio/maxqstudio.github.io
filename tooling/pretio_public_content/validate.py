#!/usr/bin/env python3
"""Pretio public catalog + highlights invariant checker and deterministic expiry pruner.

Read-only by default. --prune-expired deliberately rewrites only country highlight
feeds and the highlights index. Online evidence/image decode is a separate gate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo

CAT_TOP = {"allowed_hosts", "location_contract", "schema", "items", "catalog_revision", "schema_version"}
CAT_REQUIRED = {"id", "merchant", "publisher", "title", "summary", "coverage_type", "coverage_label", "content_type", "url", "source_type", "status", "sort_order", "locations"}
CAT_OPTIONAL = {"valid_from", "valid_until", "last_verified_at", "logo_url", "image_url", "logo_revision", "image_revision"}
LOC_KEYS = {"type", "country", "country_code", "province", "province_code", "city", "city_code", "location_key"}
FEED_TOP = {"schema", "schema_version", "country", "currency", "revision", "generated_at", "items"}
ITEM_REQUIRED = {"id", "catalog_id", "retailer", "product_name", "normal_price", "promo_price", "currency", "image_url", "source_url", "observed_at"}
ITEM_OPTIONAL = {"brand", "package_size", "valid_from", "valid_until", "logo_url", "image_revision", "logo_revision"}
INDEX_TOP = {"schema", "schema_version", "revision", "countries"}
INDEX_ENTRY = {"code", "document_id", "revision", "sha256", "url"}
TIMEZONE = {"ID": "Asia/Jakarta", "CL": "America/Santiago", "RS": "Europe/Belgrade", "US": "America/Los_Angeles", "ZA": "Africa/Johannesburg", "DE": "Europe/Berlin", "CH": "Europe/Zurich"}
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")
DEC_RE = re.compile(r"^(0|[1-9]\d*)(\.\d+)?$")
UTC_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")


class Invalid(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Invalid(message)


def strict_keys(obj: object, required: set[str], optional: set[str], where: str) -> dict:
    require(isinstance(obj, dict), f"{where}: object required")
    actual = set(obj)
    extra, missing = actual - required - optional, required - actual
    require(not extra, f"{where}: unsupported keys: {sorted(extra)}")
    require(not missing, f"{where}: missing keys: {sorted(missing)}")
    return obj


def read(path: Path):
    return json.loads(path.read_bytes())


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_url(value, where):
    require(isinstance(value, str), f"{where}: URL string required")
    u = urlsplit(value)
    require(u.scheme == "https" and bool(u.hostname) and not u.username and not u.password and u.port in (None, 443), f"{where}: invalid HTTPS URL")
    return (u.hostname or "").lower()


def parse_day(value, where):
    if value is None:
        return None
    require(isinstance(value, str), f"{where}: ISO date required")
    require(re.fullmatch(r"\\d{4}-\\d{2}-\\d{2}(?:T\\d{2}:\\d{2}:\\d{2}(?:Z|[+-]\\d{2}:\\d{2}))?", value) is not None,
            f"{where}: invalid date format")
    try:
        # Some catalog validity dates have a sourced timezone offset.
        return date.fromisoformat(value[:10])
    except ValueError as exc:
        raise Invalid(f"{where}: invalid date") from exc


def parse_timestamp(value, where):
    require(isinstance(value, str) and UTC_RE.fullmatch(value) is not None, f"{where}: UTC timestamp required")
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise Invalid(f"{where}: malformed timestamp") from exc


def parse_decimal(value, where):
    require(isinstance(value, str) and DEC_RE.fullmatch(value) is not None, f"{where}: canonical decimal string required")
    try:
        return Decimal(value)
    except InvalidOperation as exc:
        raise Invalid(f"{where}: invalid decimal") from exc


def official_match(source: str, catalog: str) -> bool:
    def normal(host):
        return host.removeprefix("www.")
    a, b = normal(source), normal(catalog)
    return a == b or a.endswith("." + b)


def country_today(code: str, override: date | None = None) -> date:
    if override:
        return override
    return datetime.now(ZoneInfo(TIMEZONE.get(code, "UTC"))).date()


def load_catalog(root: Path):
    path = root / "pretio/promos/catalog_app.json"
    doc = strict_keys(read(path), CAT_TOP, set(), "catalog")
    require(doc["schema"] == "pretio.catalog_app.v2" and doc["schema_version"] == 2, "catalog: schema must be v2")
    hosts = doc["allowed_hosts"]
    require(isinstance(hosts, list) and hosts and len(set(hosts)) == len(hosts), "catalog: unique allowed_hosts required")
    require(all(isinstance(x, str) and re.fullmatch(r"[a-z0-9.-]+", x) for x in hosts), "catalog: invalid host")
    require(isinstance(doc["location_contract"], dict), "catalog: missing location contract")
    require(isinstance(doc["items"], list), "catalog: items must be a list")
    ids, mapping = set(), {}
    for i, raw in enumerate(doc["items"]):
        where = f"catalog.items[{i}]"
        item = strict_keys(raw, CAT_REQUIRED, CAT_OPTIONAL, where)
        require(isinstance(item["id"], str) and item["id"] and item["id"] not in ids, f"{where}: duplicate/missing id")
        ids.add(item["id"])
        for name in ["merchant", "publisher", "title", "summary", "coverage_label"]:
            require(isinstance(item[name], str) and bool(item[name].strip()), f"{where}.{name}: required text")
        require(item["coverage_type"] == "national" and item["content_type"] == "webview", f"{where}: unsupported catalog type")
        require(item["source_type"] in ("official_retailer", "official_digital_channel"), f"{where}: unsupported source")
        require(item["status"] == "active", f"{where}: unsupported status")
        require(isinstance(item["sort_order"], int) and not isinstance(item["sort_order"], bool), f"{where}: sort_order integer required")
        require(parse_url(item["url"], where + ".url") in hosts, f"{where}: URL host not allowlisted")
        for key in ("image_url", "logo_url"):
            if item.get(key):
                require(parse_url(item[key], where + "." + key) in hosts, f"{where}.{key}: image host not allowlisted")
        for key in ("image_revision", "logo_revision"):
            if item.get(key):
                require(item.get(key.replace("_revision", "_url")), f"{where}: revision without URL")
        for key in ("valid_from", "valid_until"):
            parse_day(item.get(key), where + "." + key)
        if item.get("valid_from") and item.get("valid_until"):
            require(parse_day(item["valid_from"], where) <= parse_day(item["valid_until"], where), f"{where}: invalid date range")
        locs = item["locations"]
        require(isinstance(locs, list) and bool(locs), f"{where}: location required")
        codes = set()
        for k, loc in enumerate(locs):
            l = strict_keys(loc, {"type", "country_code"}, LOC_KEYS - {"type", "country_code"}, f"{where}.locations[{k}]")
            require(l["type"] in ("country", "province", "city"), f"{where}: invalid location type")
            require(isinstance(l["country_code"], str) and re.fullmatch(r"[A-Z]{2}", l["country_code"]), f"{where}: invalid ISO country")
            codes.add(l["country_code"])
        require(len(codes) == 1, f"{where}: mixed countries")
        mapping[item["id"]] = item
    return doc, mapping


def validate_catalog_link_changes(baseline_path: Path, root: Path):
    """Changed catalog URLs must carry a documented period end; approve canonical migration separately."""
    baseline = read(baseline_path)
    require(isinstance(baseline, dict) and isinstance(baseline.get("items"), list), "baseline: invalid catalog")
    old = {item["id"]: item for item in baseline["items"] if isinstance(item, dict) and "id" in item}
    candidate, _ = load_catalog(root)
    for item in candidate["items"]:
        previous = old.get(item["id"])
        if previous is not None and previous.get("url") != item["url"]:
            require(item.get("valid_until") is not None,
                    f"{item['id']}: changed period URL needs evidenced valid_until; canonical migration requires separate owner review")
    return True


def load_currency(root: Path):
    doc = read(root / "pretio/data/currency.json")
    require(doc.get("schema") == "pretio.currency.v1" and doc.get("schema_version") == 1, "currency: incompatible schema")
    result = {}
    for currency in doc["currencies"]:
        for cc in currency["countries"]:
            require(cc not in result, f"currency: duplicate mapping for {cc}")
            result[cc] = currency["code"]
    return result


def validate_highlight_item(item, where, cc, currency, catalogs, today):
    strict_keys(item, ITEM_REQUIRED, ITEM_OPTIONAL, where)
    require(isinstance(item["id"], str) and bool(ID_RE.fullmatch(item["id"])), f"{where}: invalid id")
    for name in ["catalog_id", "retailer", "product_name"]:
        require(isinstance(item[name], str) and bool(item[name].strip()), f"{where}.{name}: required text")
    require(item["catalog_id"] in catalogs, f"{where}: unknown catalog id")
    cat = catalogs[item["catalog_id"]]
    require(any(l["country_code"] == cc for l in cat["locations"]), f"{where}: cross-country catalog id")
    require(item["currency"] == currency, f"{where}: currency mismatch")
    original = parse_decimal(item["normal_price"], where + ".normal_price")
    reduced = parse_decimal(item["promo_price"], where + ".promo_price")
    require(original > 0 and reduced >= 0 and reduced < original, f"{where}: not a verified discount")
    official_host = parse_url(cat["url"], where + ".catalog_url")
    source_host = parse_url(item["source_url"], where + ".source_url")
    require(official_match(source_host, official_host), f"{where}: source is not the catalog's official website")
    parse_url(item["image_url"], where + ".image_url")
    if item.get("logo_url"):
        parse_url(item["logo_url"], where + ".logo_url")
    if item.get("image_revision"):
        require(item.get("image_url"), f"{where}: revision without image")
    if item.get("logo_revision"):
        require(item.get("logo_url"), f"{where}: revision without logo")
    parse_timestamp(item["observed_at"], where + ".observed_at")
    begin, end = parse_day(item.get("valid_from"), where + ".valid_from"), parse_day(item.get("valid_until"), where + ".valid_until")
    require(not (begin and end and end < begin), f"{where}: invalid validity range")
    return bool(end and end < today)


def validate(root: Path, as_of: date | None = None, strict_expiry: bool = False):
    report = {"countries": {}, "warnings": []}
    _, catalogs = load_catalog(root)
    currencies = load_currency(root)
    index_path = root / "pretio/promos/highlights/index.json"
    index = strict_keys(read(index_path), INDEX_TOP, set(), "highlights.index")
    require(index["schema"] == "pretio.product_highlights.index.v2" and index["schema_version"] == 2, "highlights.index: v2 required")
    require(isinstance(index["revision"], str) and index["revision"], "highlights.index: missing revision")
    require(isinstance(index["countries"], list), "highlights.index: countries must be list")
    country_codes = set()
    for row in index["countries"]:
        strict_keys(row, INDEX_ENTRY, set(), "highlights.index.entry")
        cc = row["code"]
        require(isinstance(cc, str) and re.fullmatch(r"[A-Z]{2}", cc) and cc not in country_codes, "highlights.index: invalid/duplicate country")
        country_codes.add(cc)
        require(row["document_id"] == cc, f"{cc}: index document_id mismatch")
        require(row["url"] == f"https://maxqstudio.dev/pretio/promos/highlights/{cc}.json", f"{cc}: noncanonical index URL")
        path = root / f"pretio/promos/highlights/{cc}.json"
        require(path.is_file(), f"{cc}: referenced country feed missing")
        require(isinstance(row["sha256"], str) and row["sha256"].lower() == digest(path), f"{cc}: index SHA256 mismatch")
        feed = strict_keys(read(path), FEED_TOP, set(), f"{cc}: feed")
        require(feed["schema"] == "pretio.product_highlights.v1" and feed["schema_version"] == 1, f"{cc}: feed v1 required")
        require(feed["country"] == cc, f"{cc}: country mismatch")
        require(cc in currencies, f"{cc}: BLOCKED_CURRENCY_METADATA")
        require(feed["currency"] == currencies[cc], f"{cc}: currency mismatch")
        require(feed["revision"] == row["revision"], f"{cc}: feed/index revision mismatch")
        parse_timestamp(feed["generated_at"], f"{cc}.generated_at")
        items = feed["items"]
        require(isinstance(items, list) and len(items) <= 80, f"{cc}: country exceeds max 80")
        ids, counts, expired = set(), {}, []
        today = country_today(cc, as_of)
        for i, item in enumerate(items):
            where = f"{cc}.items[{i}]"
            is_expired = validate_highlight_item(item, where, cc, currencies[cc], catalogs, today)
            require(item["id"] not in ids, f"{where}: duplicate id")
            ids.add(item["id"])
            counts[item["retailer"]] = counts.get(item["retailer"], 0) + 1
            require(counts[item["retailer"]] <= 20, f"{where}: retailer exceeds max 20")
            if is_expired:
                expired.append(item["id"])
        if expired:
            msg = f"{cc}: {len(expired)} expired products present; remove during next staged publication: {expired[:10]}"
            if strict_expiry:
                raise Invalid(msg)
            report["warnings"].append(msg)
        report["countries"][cc] = {"items": len(items), "expired": len(expired), "currency": feed["currency"]}
    return report


def prune_expired(root: Path, as_of: date | None = None):
    """Explicit, deterministic maintenance; never a response to failed crawling."""
    initial = validate(root, as_of, strict_expiry=False)
    idx_path = root / "pretio/promos/highlights/index.json"
    index = read(idx_path)
    now = datetime.now(timezone.utc).replace(microsecond=0)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    utc = now.isoformat().replace("+00:00", "Z")
    changed = {}
    for entry in index["countries"]:
        cc = entry["code"]
        if initial["countries"][cc]["expired"] == 0:
            continue
        path = root / f"pretio/promos/highlights/{cc}.json"
        feed = read(path)
        today = country_today(cc, as_of)
        kept = [item for item in feed["items"] if not (item.get("valid_until") and parse_day(item["valid_until"], "valid_until") < today)]
        if len(kept) == len(feed["items"]):
            continue
        removed = [item["id"] for item in feed["items"] if item not in kept]
        feed["items"] = kept
        feed["generated_at"] = utc
        feed["revision"] = f"pretio-highlights-{cc}-{stamp}"
        path.write_text(json.dumps(feed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        entry["revision"] = feed["revision"]
        entry["sha256"] = digest(path)
        changed[cc] = removed
    if changed:
        index["revision"] = utc
        idx_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    validate(root, as_of, strict_expiry=True)
    return changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2], help="Git repository root")
    parser.add_argument("--as-of", type=date.fromisoformat, help="Override local-market date in YYYY-MM-DD for deterministic tests")
    parser.add_argument("--strict-expiry", action="store_true", help="Fail if any explicit expiration date has passed")
    parser.add_argument("--prune-expired", action="store_true", help="Explicitly delete proven date-expired highlight products and regenerate v2 index hashes")
    parser.add_argument("--baseline-catalog", type=Path, help="Compare old catalog JSON; changed URLs must have source-backed valid_until")
    args = parser.parse_args()
    try:
        if args.baseline_catalog:
            validate_catalog_link_changes(args.baseline_catalog, args.root)
        if args.prune_expired:
            changed = prune_expired(args.root, args.as_of)
            print(json.dumps({"expired_removed_by_country": changed, "status": "PRUNED"}, indent=2))
        report = validate(args.root, args.as_of, strict_expiry=args.strict_expiry or args.prune_expired)
        print(json.dumps({"status": "VALID", **report}, indent=2))
    except (Invalid, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"VALIDATION_FAILED: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
