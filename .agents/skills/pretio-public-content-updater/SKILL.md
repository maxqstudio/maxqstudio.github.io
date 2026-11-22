---
name: pretio-public-content-updater
description: Maintain Pretio official retailer Catalog Promo entries and discounted Product Highlights by country every 12 hours, using per-catalog checklists, isolated context checkpoints, validated evidence, strict existing JSON fields, expiry cleanup, and safe GitHub publication.
---

# Pretio Public Content Updater

**Purpose:** Keep the public Pretio catalog directory and discounted product highlights reliable across supported countries. Never invent a retailer, product, discount, reference price, URL, image, date or location. No new JSON fields are permitted in either production dataset.

**Repository:** `maxqstudio/maxqstudio.github.io` (GitHub Pages). Android `maxqstudio/pretio` is a **read-only compatibility reference**.

## Read first
- `pretio/promos/catalog_app.json` — catalog v2, 74 current entries spanning 24 country codes (counts may change).
- `pretio/promos/highlights/index.json` — highlight INDEX **v2**, `schema_version: 2`.
- `pretio/promos/highlights/CC.json` — country highlight FEED **v1**, `schema_version: 1`.
- `pretio/data/currency.json` — read-only currency coverage, currently seven countries.
- `pretio/promos/location.json`, `pretio/location/v2/index.json` — read-only geography.
- `pretio/promos/highlights/UPDATER_CONTRACT.md` — updated compatibility rules.
- `references/catalog-rules.md`, `references/highlight-rules.md`, `references/operations.md`.
- `templates/CATALOG_CHECKLIST.md` and `templates/COMPACT_HANDOFF.md`.

## Fundamental rules

1. **Discounted products only.** A highlight requires retailer evidence of both an actual `normal_price` and a strictly lower `promo_price` for the SAME product, size, channel and location. No regular-priced items, general cashback slogans, undocumented "up to X% off" claims, inferred original prices, or missing images. At least one NEW qualified product per country per 12-hour cycle is the **target**, not permission to fabricate. If unmet, mark `TARGET_MISSED` and include the reason.
2. **Use ONLY existing production fields.** Strict key allowlists in `references/catalog-rules.md` and `references/highlight-rules.md`; do not add `discount_percent`, `confidence`, `status`, `country_code`, internal evidence links or any other new field to highlight items. Do not add metadata to catalog entries. Store checkpoints/audit OUTSIDE production JSON (work artifacts/audit files).
3. **One catalog per bounded agent context.** Select `(country, catalog_id)`, complete its checklist, validate findings, update the candidate highlight feed, write a compact handoff, then **start a fresh isolated catalog task with ONLY its handoff plus the next catalog input**. Do not carry entire HTML dumps, previous transcripts or other catalogs' raw evidence into next context. See `references/operations.md`.
4. **Every catalog in EVERY listed country, EACH 12-hour cycle, no early exit.** At cycle start, snapshot all active official catalog entries from `catalog_app.json` and expand to a de-duplicated exhaustive manifest of `(country_code, catalog_id)` work units. This manifest is the full required coverage, including countries lacking highlight feeds/currency mappings. Do not stop when one product is found, one country meets its growth target, an individual source fails, the bot's context is full, or a time budget is reached. Every manifest work unit must receive a terminal receipt after one bounded attempt (plus limited retries where justified). Distribute workloads with bounded concurrency; country workers may run in parallel. Countries without supported currency can still have their catalog URL checked; their highlight write is skipped with `BLOCKED_CURRENCY_METADATA`.
5. **Prefer stable catalog directory URLs.** Prefer official canonical "offers/catalog" links that update their content in place. If an official catalog URL changes for every promotional period, its catalog entry MUST include evidence-backed `valid_until`; never publish a rotating/dated link with null/missing expiry. Reject and flag changed domains for review. Never synthesize expiry dates.
6. **Remove expired highlighted products.** At each candidate build, prune items with `valid_until` strictly earlier than today's date in the source market, or with positive source evidence that an offer ended. A verified expiry is deleted even when today's retailer fetch fails. Undated/unreachable items are **stale/unverified**, NOT automatically proven expired; do not claim they are current. Surface for immediate verification and suppress from current-offer claims. Avoid wiping the whole feed because a crawl fails.
7. **Strict read/write boundaries.** Catalog-maintenance writes ONLY `pretio/promos/catalog_app.json`; highlight-maintenance writes ONLY `pretio/promos/highlights/**`. Both may use separately scoped code, docs and tests changes on an approved PR. Never alter legal pages, `pretio/promos/location.json`, `pretio/location/v2/**`, `pretio/data/currency.json`, `pretio/localization/**`, or Android without a separate approved project. Coupled updates validate against the final catalog + feed snapshot.
8. **Do not bypass access restrictions.** Official public sources only; respect ToS, robots, rate limits, copyright and image licenses. No CAPTCHA circumvention, login scraping, stealth or proxy rotation. Use HTTP first, Playwright only where permitted, OCR/LLM as evidence extraction assistance (never as a source of truth).
9. **Only publish verified data.** Default mode AUDIT or PREPARE (draft branch/PR), never merge/deploy unattended solely because this skill exists. Scheduled PUBLISH requires independent Owner-approved policy + tests + rollback plan.

## Execution support

Generate full, country-inclusive work units with `python3 tooling/pretio_public_content/manifest.py`. Pass per-catalog terminal receipts to `--receipts <path>` and require `cycle_status=COMPLETED` before declaring a cycle finished. A completed scan may have zero updates. A dedicated 12-hour runner/crawler still needs to be implemented; this manifest tool **does not** scrape, schedule or publish.

## Complete-cycle algorithm (MANDATORY)

The **12-hour cycle** means **attempt EVERY catalog of EVERY country**, not stop after the first discount. "Skip" means **finish that catalog with a recorded reason, then proceed to the next catalog**. Never silently omit one from the manifest.

1. **Snapshot and enumerate**: read `catalog_app.json` once, derive every unique `(country_code, catalog_id)` from the locations of every active official catalog, and record `manifest_total`. Sort deterministically: country code, evergreen catalog first, then catalog ID. Existing country feeds, available currencies, successes/failures or the one-new-product target do **not** reduce the manifest.
2. **Process one catalog** in its own isolated context with a checklist. Verify current canonical official catalog, location validity, and **all obtainable real discounted product offers**, not just enough offers to hit a quota. For valid new/changed data, stage updates to a country **candidate** feed and catalog candidate. Do not overwrite published feeds during the crawl.
3. **Skip rather than stall** when a catalog is inaccessible, unchanged, has no proven discounts, requires prohibited access, has no compatible currency, lacks verifiable expiry for a rotating URL, or supplies insufficient evidence. Record terminal status `SKIPPED_NO_CHANGE`, `SKIPPED_NO_PROMO`, `SKIPPED_UNAVAILABLE`, `SKIPPED_BLOCKED`, `SKIPPED_UNVERIFIED`, or `BLOCKED_CURRENCY_METADATA` in the checkpoint/audit **only**. Retain unrelated verified data. Use finite source timeouts, bounded retries and no infinite loop.
4. **Checkpoint + compact** for EVERY manifest entry, including failures/skips: complete `CATALOG_CHECKLIST.md`, persist accepted/rejected candidates and a succinct `COMPACT_HANDOFF.md` (max ~400 words), mark it terminal, and launch next catalog as a **fresh isolated task**. Do not reuse raw HTML or an unbounded conversation.
5. **Resume** missing manifest work units on retry/restart; never redo a successfully finalized catalog without an explicit reason. A cycle can terminate only after `terminal_receipts == manifest_total` and there are **zero** pending catalog entries. No global short-circuit, first-success return, per-country early break or skipping unattempted catalogs due to the target being met.
6. **Finalize once after coverage completes**: reconcile all staged valid Catalog Promo and Product Highlights changes, run deterministic expiry deletion (including known expired items from skipped/failed catalogs), enforce strict old field names, existing schemas, item count/currency/geography/official-source validation, and exact feed+index SHA. Publish/prepare **one consistent validated batch**, not piecemeal broken country JSON. A country without changes is left byte-identical.
7. **Complete and stop** the cycle only after manifest exhaustiveness and final validation/reporting. Do not continuously crawl after finishing. Next scheduled run builds a fresh manifest 12 hours later; if validation fails, hold publication, report failure, and still close the completed scan cycle.

**Per-cycle reporting:** `manifest_total`, `attempted`, `terminal_receipts`, `updated`, `skipped_no_change`, `skipped_no_promo`, `skipped_unavailable`, `skipped_unverified`, `failed`, `expired_removed`, `new_discount_products_by_country`, `TARGET_MET/TARGET_MISSED` for each country, `pending`. A healthy finished cycle has `pending = 0`; a partial or interrupted run must be labeled `INCOMPLETE`, not "done". Zero new eligible offers is a valid scan outcome, **not** a reason to keep scanning forever.

## Schedule and operating modes

- Intended cadence: `17 1,13 * * *` in GitHub Actions (UTC) = **09:17 / 21:17 WITA**. Scheduling is best-effort; run `workflow_dispatch` for manual verification. **This skill alone does not start an autonomous bot.**
- AUDIT / DRY_RUN (default): no tracked production changes; emit report and potential PR.
- PREPARE: isolated branch, schema checks, sources and evidence, candidate changes, Draft PR for review.
- PUBLISH: only an approved, separately implemented deterministic publisher can write after CI/approval; never use the LLM to free-form commit directly to `main`.
- Counters: attempted catalogs, verified catalogs, failed sources, new verified highlights, expired removed, country `TARGET_MET`/`TARGET_MISSED`, blocked countries, changed links, next schedule.
- For countries without a currency entry: continue checking ALL their catalogs and record `BLOCKED_CURRENCY_METADATA` for highlight creation. **Do not invent or add currency mapping**; require a separate approved currency-catalog + Android compatibility update first. This blocks highlight publication for that country, NOT the entire scan.

## Skip conditions vs safety gates

- **SKIP ONLY THE CURRENT CATALOG** if the source cannot be fetched after bounded retries, is unchanged, has no eligible discount, is location restricted, lacks proof/imagery, has a rotating link without verified expiry, or its country lacks highlight currency support. Log the reason and continue with the next manifest entry. Invalid source material is never included in output.
- **HOLD PUBLICATION (not scanning)** if any staged result introduces unrecognized fields/schema, unapproved host, missing required proof, invalid currency/location, a broken index hash, a large unexplained deletion, or changes outside permitted paths. Continue the remaining catalog scan; report the publication blocker.
- Only the scheduler's cancellation/deadline/infrastructure failure may leave an incomplete manifest; report `INCOMPLETE`, retain durable receipts and resume the pending work at the next eligible attempt. Never falsely claim all catalogs checked.



Deliver a structured run report with PR/commit, tests PASS/FAIL, per-country delta, missed targets, and any requested Owner actions. Never claim a run, scraper, or scheduler exists or passes without execution evidence.
