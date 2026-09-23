#!/usr/bin/env python3
"""Validate generated Pretio location v2 files and source coverage."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

INDEX_SCHEMA = "pretio.location.index.v2"
COUNTRY_SCHEMA = "pretio.location.country.v2"
BASE_URL = "https://maxqstudio.dev/pretio/location/v2/"
MINIMUM_PLACE_DEPTH = {
    "CL": 346,
    "DE": 17,
    "CH": 27,
    "RS": 26,
    "US": 52,
    "ZA": 10,
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--legacy-location", type=Path, required=True)
    parser.add_argument("--source-country-info", type=Path, required=True)
    args = parser.parse_args()
    index_path = args.directory / "index.json"
    index_bytes = index_path.read_bytes()
    index = json.loads(index_bytes.decode("utf-8"), object_pairs_hook=unique_object)
    if index.get("schema") != INDEX_SCHEMA or index.get("schema_version") != 2:
        fail("invalid index schema")
    if not isinstance(index.get("revision"), str) or not index["revision"].strip():
        fail("missing index revision")
    entries = index.get("countries")
    if not isinstance(entries, list) or not entries:
        fail("empty country index")
    codes = [item.get("code") for item in entries]
    if len(codes) != len(set(codes)) or codes != sorted(codes):
        fail("country codes are duplicate or not deterministic")
    if index.get("default_country_code") not in set(codes):
        fail("default country is not indexed")

    expected_codes = {
        line.split("\t")[0]
        for line in args.source_country_info.read_text(encoding="utf-8").splitlines()
        if line and not line.startswith("#")
        and re.fullmatch(r"[A-Z]{2}", line.split("\t")[0])
        and line.split("\t")[0] not in {"AN", "CS", "XK"}
    }
    if set(codes) != expected_codes:
        fail("index country set differs from the filtered GeoNames country source")
    json_files = {
        path.stem for path in args.directory.glob("*.json") if path.name != "index.json"
    }
    if json_files != set(codes):
        fail("country JSON file set differs from index")

    total_subdivisions = 0
    total_places = 0
    reports = {}
    for entry in entries:
        code = entry.get("code")
        name = entry.get("name")
        url = entry.get("url")
        revision = entry.get("revision")
        declared_sha = entry.get("sha256")
        if not isinstance(code, str) or not re.fullmatch(r"[A-Z]{2}", code):
            fail(f"invalid country code: {code!r}")
        if not isinstance(name, str) or not name.strip():
            fail(f"empty country name: {code}")
        if url != f"{BASE_URL}{code}.json" or not url.startswith("https://"):
            fail(f"invalid canonical HTTPS URL: {code}")
        if not isinstance(revision, str) or not revision.strip():
            fail(f"missing revision: {code}")
        if not isinstance(declared_sha, str) or not re.fullmatch(r"[0-9a-f]{64}", declared_sha):
            fail(f"invalid SHA-256 field: {code}")
        path = args.directory / f"{code}.json"
        raw_bytes = path.read_bytes()
        actual_sha = digest(raw_bytes)
        if actual_sha != declared_sha:
            fail(f"country file SHA mismatch: {code}")
        country = json.loads(raw_bytes.decode("utf-8"), object_pairs_hook=unique_object)
        if country.get("schema") != COUNTRY_SCHEMA or country.get("schema_version") != 2:
            fail(f"invalid country schema: {code}")
        if country.get("country_code") != code or country.get("country") != name:
            fail(f"country identity mismatch: {code}")
        if country.get("revision") != revision:
            fail(f"country revision mismatch: {code}")
        source = country.get("source")
        if not isinstance(source, dict) or source.get("name") != "GeoNames":
            fail(f"missing source provenance: {code}")
        if source.get("license") != "CC BY 4.0" or source.get("attribution") != "GeoNames.org":
            fail(f"invalid source license/attribution: {code}")
        provinces = country.get("provinces")
        root_cities = country.get("root_cities")
        if not isinstance(provinces, list) or not isinstance(root_cities, list):
            fail(f"missing subdivision/place arrays: {code}")
        province_codes = set()
        city_codes = set()
        places = len(root_cities)
        for city in root_cities:
            if city.get("type") != "city" or not isinstance(city.get("city"), str) or not city["city"].strip():
                fail(f"invalid root place: {code}")
            city_code = city.get("city_code")
            if not isinstance(city_code, str) or not city_code or city_code in city_codes:
                fail(f"duplicate/empty place identity: {code}/{city_code}")
            city_codes.add(city_code)
        for province in provinces:
            if province.get("type") != "province" or not isinstance(province.get("province"), str) or not province["province"].strip():
                fail(f"invalid subdivision: {code}")
            province_code = province.get("province_code")
            if not isinstance(province_code, str) or not province_code or province_code in province_codes:
                fail(f"duplicate/empty subdivision identity: {code}/{province_code}")
            province_codes.add(province_code)
            cities = province.get("cities")
            if not isinstance(cities, list):
                fail(f"invalid place list: {code}/{province_code}")
            places += len(cities)
            for city in cities:
                if city.get("type") != "city" or not isinstance(city.get("city"), str) or not city["city"].strip():
                    fail(f"invalid place: {code}/{province_code}")
                city_code = city.get("city_code")
                if not isinstance(city_code, str) or not city_code or city_code in city_codes:
                    fail(f"duplicate/empty place identity: {code}/{city_code}")
                city_codes.add(city_code)
                if city.get("province_code") not in (None, province_code):
                    fail(f"place linked to wrong subdivision: {code}/{city_code}")
        if entry.get("subdivision_count") != len(provinces) or entry.get("place_count") != places:
            fail(f"index counts mismatch: {code}")
        total_subdivisions += len(provinces)
        total_places += places
        reports[code] = {"subdivisions": len(provinces), "places": places, "sha256": actual_sha}

    legacy = json.loads(args.legacy_location.read_text(encoding="utf-8"))
    for code in {"ID", "CL", "RS", "US", "ZA", "DE", "CH"}:
        legacy_country = next(item for item in legacy["countries"] if item["country_code"] == code)
        country = json.loads((args.directory / f"{code}.json").read_text(encoding="utf-8"))
        by_code = {item["province_code"]: item for item in country["provinces"]}
        for province in legacy_country["provinces"]:
            preserved = by_code.get(province["province_code"])
            if preserved is None:
                fail(f"legacy subdivision identity lost: {code}/{province['province_code']}")
            preserved_city_codes = {item["city_code"] for item in preserved["cities"]}
            for city in province["cities"]:
                if city["city_code"] not in preserved_city_codes:
                    fail(f"legacy place identity lost: {code}/{city['city_code']}")

    for code, minimum in MINIMUM_PLACE_DEPTH.items():
        if reports[code]["places"] < minimum:
            fail(f"representative-only place depth remains: {code}")

    print(json.dumps({
        "result": "PASS",
        "country_count": len(entries),
        "subdivision_count": total_subdivisions,
        "place_count": total_places,
        "source_admin_level": "GeoNames P populated places (cities500 extract), not a complete municipality register",
        "legacy_place_identities_preserved": True,
        "depth_regression_countries": {
            code: reports[code] for code in sorted(set(MINIMUM_PLACE_DEPTH) | {"ID"})
        },
    }, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
