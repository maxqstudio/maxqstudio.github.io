"""Build the one-off market selection register from frozen source snapshots.

This script ranks markets only; it performs no network access or crawling.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
AUDIT = Path(__file__).resolve().parent
TARGET = 174

location_index = json.loads((ROOT / "pretio/location/v2/index.json").read_text(encoding="utf-8"))
catalog = json.loads((ROOT / "pretio/promos/catalog_app.json").read_text(encoding="utf-8"))
gdp_payload = json.loads((AUDIT / "worldbank-gdp-2024.json").read_text(encoding="utf-8-sig"))

countries = {row["code"]: row["name"] for row in location_index["countries"]}
registered: dict[str, list[str]] = {}
for item in catalog["items"]:
    for location in item["locations"]:
        code = location.get("country_code") or location.get("country")
        if code in countries:
            registered.setdefault(code, []).append(item["id"])

gdp: dict[str, dict] = {}
for row in gdp_payload[1]:
    code = row.get("country", {}).get("id")
    if code in countries and row.get("date") == "2024" and row.get("value") is not None:
        gdp[code] = row

ranked_gdp = sorted(gdp, key=lambda code: (-gdp[code]["value"], code))
gdp_rank = {code: rank for rank, code in enumerate(ranked_gdp, start=1)}
registered_codes = set(registered)
selected = set(registered_codes)
for code in ranked_gdp:
    if len(selected) >= TARGET:
        break
    selected.add(code)
if len(selected) != TARGET:
    raise SystemExit(f"Could select {len(selected)} markets, expected {TARGET}")

registered_order = sorted(
    registered_codes,
    key=lambda code: (gdp_rank.get(code, 10**9), code),
)
nonregistered_order = [code for code in ranked_gdp if code in selected and code not in registered_codes]
selection_order = registered_order + nonregistered_order
selection_rank = {code: rank for rank, code in enumerate(selection_order, start=1)}

rows = []
for code in sorted(countries):
    selected_here = code in selected
    row = {
        "code": code,
        "name": countries[code],
        "selected": selected_here,
        "selection_rank": selection_rank.get(code),
        "gdp_rank_2024": gdp_rank.get(code),
        "gdp_2024_current_usd": gdp[code]["value"] if code in gdp else None,
        "world_bank_label": gdp[code]["country"]["value"] if code in gdp else None,
        "registered_catalog_count": len(registered.get(code, [])),
        "registered_catalog_ids": sorted(registered.get(code, [])),
        "disposition": "PENDING_RESEARCH" if selected_here else "OUT_OF_SCOPE_BY_MARKET_RANK",
        "research_outcome": "PENDING" if selected_here else "NOT_RESEARCHED",
        "scope_reason": (
            "Registered catalog market included before GDP ranking"
            if code in registered_codes
            else "Selected among highest 2024 current-USD GDP markets in the Pretio location registry"
            if selected_here
            else "Outside this one-off 174-market sample; no conclusion about source availability"
        ),
    }
    rows.append(row)

output = {
    "artifact_type": "pretio.oneoff_global_market_discovery_register.v1",
    "run_id": "pretio-oneoff-global-20261123T040625Z",
    "scope": "ONE_OFF_GLOBAL",
    "base_sha": "73fd02fe14c4935c3a95bca49bba3c1498a9cb54",
    "skill_sha": "73fd02fe14c4935c3a95bca49bba3c1498a9cb54",
    "candidate_country_count": len(countries),
    "registered_catalog_country_count": len(registered_codes),
    "country_target": TARGET,
    "selected_count": len(selected),
    "selection_method": "Include every country with a registered catalog, then add the highest 2024 current-US-dollar GDP markets from the Pretio location-v2 registry until 174 are selected. World Bank aggregate regions are excluded because they do not map to a registry country code. GDP rank is only a market-prioritization proxy, not evidence of catalog or shop availability.",
    "selection_source": "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?date=2024&format=json&per_page=20000",
    "location_source": "pretio/location/v2/index.json",
    "registered_source": "pretio/promos/catalog_app.json",
    "markets": rows,
}
(AUDIT / "country-discovery-register.json").write_text(
    json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({"candidate_country_count": len(countries), "registered_catalog_country_count": len(registered_codes), "selected_count": len(selected), "countries_with_gdp": len(gdp)}))
