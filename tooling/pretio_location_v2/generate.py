#!/usr/bin/env python3
"""Generate Pretio location v2 feeds from a pinned GeoNames snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
import zipfile
from collections import defaultdict
from pathlib import Path

SCHEMA_INDEX = "pretio.location.index.v2"
SCHEMA_COUNTRY = "pretio.location.country.v2"
EXCLUDED_NON_ISO = {"AN", "CS", "XK"}
LEGACY_ALIASES = {
    "ID": {
        "ID.01": "11", "ID.26": "12", "ID.24": "13", "ID.37": "14",
        "ID.05": "15", "ID.32": "16", "ID.03": "17", "ID.15": "18",
        "ID.35": "19", "ID.40": "21", "ID.04": "31", "ID.30": "32",
        "ID.07": "33", "ID.10": "34", "ID.08": "35", "ID.33": "36",
        "ID.02": "51", "ID.17": "52", "ID.18": "53", "ID.11": "61",
        "ID.13": "62", "ID.12": "63", "ID.14": "64", "ID.42": "65",
        "ID.31": "71", "ID.21": "72", "ID.38": "73", "ID.22": "74",
        "ID.34": "75", "ID.41": "76", "ID.28": "81", "ID.29": "82",
        "ID.39": "91", "ID.36": "92", "ID.PS": "93", "ID.PT": "94",
        "ID.PE": "95", "ID.PD": "96",
    },
    "CL": {
        "CL.16": "CL-AP", "CL.15": "CL-TA", "CL.03": "CL-AN",
        "CL.05": "CL-AT", "CL.02": "CL-AI", "CL.01": "CL-VS",
        "CL.07": "CL-CO", "CL.08": "CL-LI", "CL.06": "CL-BI",
        "CL.18": "CL-NB", "CL.11": "CL-ML", "CL.12": "CL-RM",
        "CL.04": "CL-AR", "CL.17": "CL-LR", "CL.14": "CL-LL",
        "CL.10": "CL-MA",
    },
    "DE": {
        "DE.01": "DE-BW", "DE.02": "DE-BY", "DE.03": "DE-HB",
        "DE.04": "DE-HH", "DE.05": "DE-HE", "DE.06": "DE-NI",
        "DE.07": "DE-NW", "DE.08": "DE-RP", "DE.09": "DE-SL",
        "DE.10": "DE-SH", "DE.11": "DE-BB", "DE.12": "DE-MV",
        "DE.13": "DE-SN", "DE.14": "DE-ST", "DE.15": "DE-TH",
        "DE.16": "DE-BE",
    },
    "US": {f"US.{code}": f"US-{code}" for code in (
        "AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI "
        "MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT "
        "VT VA WA WV WI WY DC"
    ).split()},
    "CH": {f"CH.{code}": f"CH-{code}" for code in (
        "AG AI AR BE BL BS FR GE GL GR JU LU NE NW OW SG SH SO SZ TG TI UR "
        "VD VS ZG ZH"
    ).split()},
    "ZA": {
        "ZA.03": "ZA-FS", "ZA.02": "ZA-NL", "ZA.05": "ZA-EC",
        "ZA.06": "ZA-GP", "ZA.07": "ZA-MP", "ZA.08": "ZA-NC",
        "ZA.09": "ZA-LP", "ZA.10": "ZA-NW", "ZA.11": "ZA-WC",
    },
}


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def read_tsv(path: Path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#"):
            yield line.split("\t")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_legacy(path: Path):
    raw = json.loads(path.read_text(encoding="utf-8"))
    if raw.get("schema_version") != 1 or not isinstance(raw.get("countries"), list):
        raise ValueError("legacy location source is not schema v1")
    return {item["country_code"]: item for item in raw["countries"]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--legacy-location", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--snapshot-date", required=True)
    args = parser.parse_args()
    source = args.source_dir
    output = args.output_dir
    output.mkdir(parents=True, exist_ok=True)

    country_rows = list(read_tsv(source / "countryInfo.txt"))
    iso_rows = [
        row for row in country_rows
        if len(row) > 4 and re.fullmatch(r"[A-Z]{2}", row[0])
        and row[0] not in EXCLUDED_NON_ISO and row[4].strip()
    ]
    country_codes = [row[0] for row in iso_rows]
    if len(country_codes) != len(set(country_codes)):
        raise ValueError("duplicate country code in GeoNames countryInfo")
    countries = {
        row[0]: {"code": row[0], "name": row[4].strip()}
        for row in iso_rows
    }

    admin1_by_country = defaultdict(list)
    admin1_by_code = {}
    for row in read_tsv(source / "admin1CodesASCII.txt"):
        if len(row) < 4:
            continue
        code, name, ascii_name, geoname_id = row[:4]
        country, _, subdivision = code.partition(".")
        if country not in countries or not subdivision or not geoname_id.isdigit():
            continue
        if code in admin1_by_code:
            raise ValueError(f"duplicate ADM1 code: {code}")
        entry = {
            "source_code": code,
            "geoname_id": geoname_id,
            "name": name.strip(),
            "ascii_name": ascii_name.strip(),
        }
        admin1_by_code[code] = entry
        admin1_by_country[country].append(entry)

    places_by_country = defaultdict(list)
    archive = zipfile.ZipFile(source / "cities500.zip")
    members = [name for name in archive.namelist() if name.endswith(".txt")]
    if len(members) != 1:
        raise ValueError("cities500 archive must contain exactly one TSV")
    with archive.open(members[0]) as stream:
        for raw in stream:
            row = raw.decode("utf-8").rstrip("\r\n").split("\t")
            if len(row) < 19 or row[6] != "P" or row[8] not in countries:
                continue
            geoname_id, name, ascii_name = row[0], row[1].strip(), row[2].strip()
            if not geoname_id.isdigit() or not name:
                continue
            admin1_code = f"{row[8]}.{row[10]}" if row[10] else None
            admin1 = admin1_by_code.get(admin1_code) if admin1_code else None
            places_by_country[row[8]].append({
                "type": "city",
                "city_code": f"geonames:{geoname_id}",
                "city": name,
                "source_id": geoname_id,
                "source_code": row[7],
                "admin1_source_code": admin1_code if admin1 else None,
                "admin2_source_code": f"{admin1_code}.{row[11]}" if admin1_code and row[11] else None,
                "population": int(row[14]) if row[14].isdigit() else 0,
                "modified": row[18],
            })

    legacy = load_legacy(args.legacy_location)
    index_countries = []
    stats = {"countries": 0, "subdivisions": 0, "places": 0, "geonames_places": 0, "legacy_places": 0}
    base_url = "https://maxqstudio.dev/pretio/location/v2"
    for code in sorted(countries):
        country = countries[code]
        raw_legacy = legacy.get(code)
        divisions = []
        division_by_source = {}
        division_by_code = {}
        if raw_legacy:
            for old in raw_legacy.get("provinces", []):
                province_code = str(old["province_code"]).strip()
                item = {
                    "type": "province",
                    "province_code": province_code,
                    "province": old["province"].strip(),
                    "source": "pretio.location.v1",
                    "cities": [],
                }
                for old_city in old.get("cities", []):
                    item["cities"].append({
                        "type": "city",
                        "city_code": str(old_city["city_code"]),
                        "city": old_city["city"].strip(),
                        "source": "pretio.location.v1",
                    })
                    stats["legacy_places"] += 1
                divisions.append(item)
                division_by_code[province_code] = item

        for adm in sorted(admin1_by_country[code], key=lambda item: int(item["geoname_id"])):
            province_code = LEGACY_ALIASES.get(code, {}).get(adm["source_code"])
            if province_code is None and code == "RS":
                province_code = None
            target = division_by_code.get(province_code) if province_code else None
            if target is None:
                target = {
                    "type": "province",
                    "province_code": f"geonames:{adm['geoname_id']}",
                    "province": adm["name"],
                    "source": "geonames.admin1",
                    "source_code": adm["source_code"],
                    "source_id": adm["geoname_id"],
                    "cities": [],
                }
                divisions.append(target)
                division_by_code[target["province_code"]] = target
            target["source_code"] = adm["source_code"]
            target["source_id"] = adm["geoname_id"]
            division_by_source[adm["source_code"]] = target

        root_places = []
        for place in sorted(places_by_country[code], key=lambda item: int(item["source_id"])):
            target = division_by_source.get(place["admin1_source_code"])
            if target is None:
                root_places.append({
                    key: value for key, value in place.items()
                    if key not in {"admin1_source_code", "admin2_source_code"}
                })
                continue
            normalized_name = normalized(place["city"])
            legacy_names = target.get("_city_name_index")
            if legacy_names is None:
                legacy_names = {
                    normalized(old["city"]) for old in target["cities"]
                }
                target["_city_name_index"] = legacy_names
            if normalized_name in legacy_names:
                continue
            target["cities"].append({
                **{
                    key: value for key, value in place.items()
                    if key not in {"admin1_source_code", "admin2_source_code"}
                },
                "province_code": target["province_code"],
            })
            legacy_names.add(normalized_name)
            stats["geonames_places"] += 1

        for division in divisions:
            division.pop("_city_name_index", None)
            division["cities"].sort(key=lambda item: (normalized(item["city"]), item["city_code"]))
        root_places.sort(key=lambda item: (normalized(item["city"]), item["city_code"]))
        stats["geonames_places"] += len(root_places)
        revision = f"geonames-{args.snapshot_date}-{code.lower()}"
        payload = {
            "schema": SCHEMA_COUNTRY,
            "schema_version": 2,
            "country_code": code,
            "country": country["name"],
            "revision": revision,
            "source": {
                "name": "GeoNames",
                "snapshot_date": args.snapshot_date,
                "license": "CC BY 4.0",
                "license_url": "https://creativecommons.org/licenses/by/4.0/",
                "attribution": "GeoNames.org",
                "legacy_supplement": "Pretio location v1 accepted source" if raw_legacy else None,
            },
            "provinces": divisions,
            "root_cities": root_places,
        }
        encoded = (json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
        (output / f"{code}.json").write_bytes(encoded)
        digest = sha256(encoded)
        province_count = len(divisions)
        city_count = sum(len(item["cities"]) for item in divisions) + len(root_places)
        stats["countries"] += 1
        stats["subdivisions"] += province_count
        stats["places"] += city_count
        index_countries.append({
            "code": code,
            "name": country["name"],
            "url": f"{base_url}/{code}.json",
            "revision": revision,
            "sha256": digest,
            "subdivision_count": province_count,
            "place_count": city_count,
        })

    index = {
        "schema": SCHEMA_INDEX,
        "schema_version": 2,
        "revision": f"geonames-{args.snapshot_date}",
        "default_country_code": "ID",
        "countries": index_countries,
    }
    (output / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(stats, sort_keys=True))


if __name__ == "__main__":
    main()
