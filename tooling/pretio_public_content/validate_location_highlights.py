#!/usr/bin/env python3
"""Validate/build a DORMANT location-aware highlight candidate index.

No live publication, network requests, or copying legacy v1 data. The input
directory must be outside the repository's public pretio tree. Source evidence
and capable-client acceptance remain separate release gates.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

from validate import (
    Invalid, require, strict_keys, read, digest, load_catalog, load_currency,
    country_today, validate_highlight_item, parse_timestamp, FEED_TOP,
    ITEM_REQUIRED, ITEM_OPTIONAL, INDEX_TOP, INDEX_ENTRY,
)

SCHEMA = "pretio.product_highlights.v2"
INDEX_SCHEMA = "pretio.product_highlights.index.v3"
URL_BASE = "https://maxqstudio.dev/pretio/promos/highlights/v2"
LOCATION_URL_BASE = "https://maxqstudio.dev/pretio/location/v2"
CC = re.compile(r"[A-Z]{2}")
DAY = re.compile(r"\d{4}-\d{2}-\d{2}")
MATCH_FIELDS = {"barcode", "variant", "pack_count"}
TEXT_LIMITS = {
    "catalog_id": 128, "retailer": 80, "product_name": 120, "brand": 80,
    "package_size": 48, "barcode": 32, "variant": 64, "normal_price": 128,
    "promo_price": 128, "image_url": 2048, "source_url": 2048, "logo_url": 2048,
    "image_revision": 256, "logo_revision": 256, "observed_at": 40,
}


def _client_text(value, limit, where):
    require(isinstance(value, str) and value == value.strip() and bool(value)
            and len(value.encode("utf-16-le")) // 2 <= limit, f"{where}: invalid text")


def _revision(value, where):
    _client_text(value, 80, where)
    return value


def _text(value, where):
    require(isinstance(value, str) and bool(value.strip()) and value == value.strip(),
            f"{where}: invalid location identifier/name")
    return value


def _candidate_path(root: Path, candidate: Path) -> Path:
    candidate = candidate.resolve()
    public = (root / "pretio").resolve()
    require(candidate != public and public not in candidate.parents,
            "candidate must not be inside the public pretio tree")
    require(candidate.is_dir(), "candidate directory missing")
    return candidate


def _location_country(root, cc):
    directory = root / "pretio/location/v2"
    index = read(directory / "index.json")
    require(index.get("schema") == "pretio.location.index.v2" and
            index.get("schema_version") == 2, "invalid location index")
    matches = [row for row in index["countries"] if row.get("code") == cc]
    require(len(matches) == 1, f"{cc}: unknown/duplicate location country")
    entry = matches[0]
    path = directory / f"{cc}.json"
    require(entry.get("url") == f"{LOCATION_URL_BASE}/{cc}.json" and
            entry.get("sha256") == digest(path), f"{cc}: location index binding mismatch")
    doc = read(path)
    require(doc.get("schema") == "pretio.location.country.v2" and
            doc.get("schema_version") == 2 and doc.get("country_code") == cc and
            doc.get("country") == entry.get("name") and
            doc.get("revision") == entry.get("revision"), f"{cc}: location identity mismatch")
    name = _text(doc["country"], cc)
    provinces, cities = {}, {}
    raw_provinces, raw_roots = doc.get("provinces"), doc.get("root_cities")
    require(isinstance(raw_provinces, list) and isinstance(raw_roots, list) and
            len(raw_provinces) <= 1000, f"{cc}: invalid location country records")

    def add_city(row, province):
        require(row.get("type") == "city" and row.get("province_code", province) == province,
                f"{cc}: city parent mismatch")
        code = _text(row.get("city_code"), cc)
        require(code not in cities, f"{cc}: duplicate city code")
        cities[code] = (province, _text(row.get("city"), cc))

    for row in raw_provinces:
        require(row.get("type") == "province", f"{cc}: invalid province record")
        code = _text(row.get("province_code"), cc)
        require(code not in provinces, f"{cc}: duplicate province code")
        provinces[code] = _text(row.get("province"), cc)
        require(isinstance(row.get("cities"), list), f"{cc}: invalid city records")
        for city in row["cities"]:
            add_city(city, code)
    for row in raw_roots:
        add_city(row, None)
    require(len(cities) <= 100000 and len(cities) == entry.get("place_count") and
            len(provinces) == entry.get("subdivision_count"), f"{cc}: location count mismatch")
    return name, provinces, cities


def validate_locations(locations, cc, directory, where):
    name, provinces, cities = directory
    require(isinstance(locations, list) and 1 <= len(locations) <= 100,
            f"{where}: missing or excessive locations")
    base = {"type", "country_code", "country"}
    province_keys = {"province_code", "province"}
    city_keys = {"city_code", "city"}
    seen = set()
    for loc in locations:
        require(isinstance(loc, dict), f"{where}: location object required")
        kind = loc.get("type")
        require(kind in ("country", "province", "city"), f"{where}: invalid location type")
        keys = base
        if kind == "province" or (kind == "city" and "province_code" in loc):
            keys = keys | province_keys
        if kind == "city":
            keys = keys | city_keys
        strict_keys(loc, keys, set(), where)
        require(loc["country_code"] == cc and loc["country"] == name,
                f"{where}: cross-country or incorrect country name")
        parent = None
        city = None
        if "province_code" in keys:
            parent = _text(loc["province_code"], where)
            require(parent in provinces and loc["province"] == provinces[parent],
                    f"{where}: unknown or mismatched province")
        if kind == "city":
            city = _text(loc["city_code"], where)
            require(city in cities and cities[city] == (parent, loc["city"]),
                    f"{where}: unknown or mismatched city/parent")
        identity = (kind, parent, city)
        require(identity not in seen, f"{where}: duplicate location")
        seen.add(identity)
    require(("country", None, None) not in seen or len(seen) == 1,
            f"{where}: country scope cannot be mixed with narrower scope")


def _read_client_payload(path):
    with path.open("rb") as stream:
        raw = stream.read(900 * 1024 + 1)
    require(len(raw) <= 900 * 1024, f"{path.name}: exceeds client payload limit")
    return json.loads(raw.decode("utf-8")), hashlib.sha256(raw).hexdigest()


def validate_feed(root, payload, cc, catalogs, currencies, as_of=None):
    feed = strict_keys(payload, FEED_TOP, set(), f"{cc}: feed")
    require(feed["schema"] == SCHEMA and feed["schema_version"] == 2 and
            feed["country"] == cc, f"{cc}: incompatible feed")
    require(cc in currencies and feed["currency"] == currencies[cc],
            f"{cc}: currency mismatch or unsupported market")
    _revision(feed["revision"], cc)
    _client_text(feed["generated_at"], 40, cc)
    parse_timestamp(feed["generated_at"], cc)
    items = feed["items"]
    require(isinstance(items, list) and len(items) <= 80, f"{cc}: invalid item count")
    directory = _location_country(root, cc)
    ids, counts = set(), {}
    for i, item in enumerate(items):
        where = f"{cc}.items[{i}]"
        strict_keys(item, ITEM_REQUIRED | {"locations"}, ITEM_OPTIONAL | MATCH_FIELDS, where)
        validate_locations(item["locations"], cc, directory, where)
        for key, limit in TEXT_LIMITS.items():
            if item.get(key) is not None:
                _client_text(item[key], limit, f"{where}.{key}")
        pack_count = item.get("pack_count")
        require(pack_count is None or (type(pack_count) is int and 1 <= pack_count <= 1000),
                f"{where}: invalid pack_count")
        # v2 retains all existing price, catalog, currency and image gates.
        # The Android reader accepts date-only offer validity; reject timestamps.
        for key in ("valid_from", "valid_until"):
            value = item.get(key)
            require(value is None or (isinstance(value, str) and DAY.fullmatch(value)),
                    f"{where}: validity requires YYYY-MM-DD")
        legacy = {k: v for k, v in item.items() if k not in MATCH_FIELDS | {"locations"}}
        require(not validate_highlight_item(legacy, where, cc, currencies[cc],
                    catalogs, country_today(cc, as_of)), f"{where}: expired product")
        require(item["id"] not in ids, f"{where}: duplicate id")
        ids.add(item["id"])
        counts[item["retailer"]] = counts.get(item["retailer"], 0) + 1
        require(counts[item["retailer"]] <= 20, f"{where}: retailer exceeds max 20")
    return feed


def _bindings(root, candidate, as_of=None):
    _, catalogs = load_catalog(root)
    currencies = load_currency(root)
    paths = sorted(p for p in candidate.glob("*.json") if p.name != "index.json")
    require(paths, "candidate: no country files")
    entries = []
    for path in paths:
        cc = path.stem
        require(CC.fullmatch(cc) is not None and path.is_file() and not path.is_symlink(),
                "candidate: invalid country filename")
        payload, sha = _read_client_payload(path)
        feed = validate_feed(root, payload, cc, catalogs, currencies, as_of)
        entries.append({"code": cc, "document_id": cc, "revision": feed["revision"],
                        "sha256": sha, "url": f"{URL_BASE}/{cc}.json"})
    return entries


def validate_candidate(root, candidate, as_of=None):
    candidate = _candidate_path(root, candidate)
    index_path = candidate / "index.json"
    require(not index_path.is_symlink(), "candidate: index must not be a symlink")
    index_payload, _ = _read_client_payload(index_path)
    index = strict_keys(index_payload, INDEX_TOP, set(), "v2 candidate index")
    require(index["schema"] == INDEX_SCHEMA and index["schema_version"] == 3,
            "candidate: incompatible index")
    _revision(index["revision"], "index")
    require(isinstance(index["countries"], list), "candidate: invalid country bindings")
    for entry in index["countries"]:
        strict_keys(entry, INDEX_ENTRY, set(), "candidate index entry")
    require(index["countries"] == _bindings(root, candidate, as_of),
            "candidate: binding/hash/revision mismatch, duplicate or unindexed country")
    return index


def build_candidate_index(root, candidate, as_of=None):
    candidate = _candidate_path(root, candidate)
    index_path = candidate / "index.json"
    require(not index_path.exists() and not index_path.is_symlink(),
            "candidate: existing index must not be overwritten")
    index = {"schema": INDEX_SCHEMA, "schema_version": 3,
             "revision": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
             "countries": _bindings(root, candidate, as_of)}
    # All feeds validated before a single exclusive index creation.
    # No production files are written; use a fresh staging directory per batch.
    with index_path.open("x", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    return validate_candidate(root, candidate, as_of)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--as-of", type=date.fromisoformat)
    parser.add_argument("--build-index", action="store_true")
    args = parser.parse_args()
    try:
        fn = build_candidate_index if args.build_index else validate_candidate
        result = fn(args.root, args.candidate, args.as_of)
        print(json.dumps({"status": "VALIDATED_CANDIDATE_ONLY", **result}, indent=2))
    except (Invalid, OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(f"VALIDATION_FAILED: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
