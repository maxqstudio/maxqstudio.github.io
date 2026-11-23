# One-off global crawl — expiry and catalog retirement audit

Run: `pretio-oneoff-global-20261123T040625Z`  
As-of date: `2026-11-23` (Spain-local date for the ES catalog decision)  
Baseline: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`

## Expired dated flyer record (stable landing page remains)

- Removed active catalog entry `lidl-es-country` from `pretio/promos/catalog_app.json`.
- The source record was explicitly titled `Folleto Alimentación 16/11`, described offers as valid 16–22 November 2026, and recorded `valid_from=2026-11-16T07:00:00+08:00` / `valid_until=2026-11-23T07:00:00+08:00`. The boundary is 2026-11-23 00:00 in Spain; the source summary says the offers ended November 22. The removed data record was period-specific; the URL itself is a stable weekly-flyer hub.
- During the original run, the linked legal notice was checked before opening the flyer, so no successor flyer contents or offer data were inspected. A later, focused page-only audit confirmed that the same official hub URL now lists a 23–29 November 2026 flyer, without extracting product, price or image data. Thus the previous flyer record is expired, while the hub is not obsolete. Official hub URL (non-clickable evidence text): `https://www.lidl.es/c/descubre-nuevas-ofertas-cada-semana-folletos-lidl/s10087402`.
- The official Lidl legal notice (`https://www.lidl.es/c/aviso-legal/s10075786`) prohibits commercial reproduction/distribution/public communication of site contents without authorization and states that linking to the portal from another website requires prior express consent. No written consent is recorded in this run or repository. Keep the active URL out until the Owner confirms permission; do not replace the dated entry with the new flyer or copy its contents in the meantime. Permission is tracked separately in Issue #61.
- Dependency scan across every existing country highlight feed found **zero** `catalog_id: lidl-es-country` references. No highlight needed deletion or migration, so orphan references remain **0**.
- No new host, URL migration, status value, or production schema field was added.

## Product expiry scan

- Baseline strict validator run used `--as-of 2026-11-23 --strict-expiry` and reported **zero expired Product Highlights** across all seven supported feeds. No product IDs were removed.
- No other catalog entry had a source-proven expired period as of the run date at this checkpoint. `kaufland-ro-country` remained valid through Nov 25 and `lidl-it-country` through Nov 26; they are not expired as of Nov 23.

## Counts for this candidate

- `expired_products_removed`: 0
- `obsolete_or_expired_catalogs_removed`: 1 (`lidl-es-country`, the expired period-specific record; not the still-active landing page)
- `catalogs_relinked_to_verified_successor`: 0
- `dependent_highlights_removed_or_migrated`: 0
- `orphan_highlight_refs`: 0
- `deletion_blockers`: none observed

The frozen 74-work-unit manifest and its terminal receipt stay unchanged; this deletion is a separately staged candidate change after the source attempt. ## Final validation record (2026-11-23)

- `python -B tooling/pretio_public_content/validate.py --as-of 2026-11-23 --strict-expiry`: **VALID**, no warnings, zero expired entries in all seven feeds.
- The same strict validator with the `origin/main` catalog baseline: **VALID**, no warnings.
- `python -B -m unittest discover -s tooling/pretio_public_content -p 'test_*.py' -v`: **22 tests passed**.
- Active 73-catalog manifest receipt check: **COMPLETED**, 73 terminal, 0 pending, 0 failed.
- `git diff --check`: **passed**.
- All GitHub Actions workflows passed on code/test commit `294b85e37508ab258a1aea239699bb4ab47e3140` and subsequent documentation commits; exact run IDs, including the targeted Lidl review commit, and the initial stale-count test failure/fix are recorded in `run-report.md`. The latest documentation-only handoff checks are visible on Draft PR #60. No merge or deployment is authorized by this run.
