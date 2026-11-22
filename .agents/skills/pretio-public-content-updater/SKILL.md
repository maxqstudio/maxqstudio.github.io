---
name: pretio-public-content-updater
description: Maintain Pretio official retailer Catalog Promo entries and discounted Product Highlights by country every 12 hours, using per-catalog checklists, isolated context checkpoints, validated evidence, strict existing JSON fields, expiry cleanup, and safe GitHub publication.
---

# Pretio Public Content Updater

**Purpose:** Keep the public Pretio catalog directory and discounted product highlights reliable across supported countries. Never invent a retailer, product, discount, reference price, URL, image, date or location. No new JSON fields are permitted in either production dataset.

**Repository:** \`maxqstudio/maxqstudio.github.io\` (GitHub Pages). Android \`maxqstudio/pretio\` is a **read-only compatibility reference**.

## Read first
- \`pretio/promos/catalog_app.json\` — catalog v2, 74 current entries spanning 24 country codes (counts may change).
- \`pretio/promos/highlights/index.json\` — highlight INDEX **v2**, \`schema_version: 2\`.
- \`pretio/promos/highlights/CC.json\` — country highlight FEED **v1**, \`schema_version: 1\`.
- \`pretio/data/currency.json\` — read-only currency coverage, currently seven countries.
- \`pretio/promos/location.json\`, \`pretio/location/v2/index.json\` — read-only geography.
- \`pretio/promos/highlights/UPDATER_CONTRACT.md\` — updated compatibility rules.
- \`references/catalog-rules.md\`, \`references/highlight-rules.md\`, \`references/operations.md\`.
- \`templates/CATALOG_CHECKLIST.md\` and \`templates/COMPACT_HANDOFF.md\`.

## Fundamental rules

1. **Discounted products only.** A highlight requires retailer evidence of both an actual \`normal_price\` and a strictly lower \`promo_price\` for the SAME product, size, channel and location. No regular-priced items, general cashback slogans, undocumented "up to X% off" claims, inferred original prices, or missing images. At least one NEW qualified product per country per 12-hour cycle is the **target**, not permission to fabricate. If unmet, mark \`TARGET_MISSED\` and include the reason.
2. **Use ONLY existing production fields.** Strict key allowlists in \`references/catalog-rules.md\` and \`references/highlight-rules.md\`; do not add \`discount_percent\`, \`confidence\`, \`status\`, \`country_code\`, internal evidence links or any other new field to highlight items. Do not add metadata to catalog entries. Store checkpoints/audit OUTSIDE production JSON (work artifacts/audit files).
3. **One catalog per bounded agent context.** Select \`(country, catalog_id)\`, complete its checklist, validate findings, update the candidate highlight feed, write a compact handoff, then **start a fresh isolated catalog task with ONLY its handoff plus the next catalog input**. Do not carry entire HTML dumps, previous transcripts or other catalogs' raw evidence into next context. See \`references/operations.md\`.
4. **Every catalog in every eligible country.** Iterate all \`catalog_app.json\` active official catalog entries per country (not just currently populated highlight feeds). Distribute workloads with bounded concurrency. A scheduler orchestrates sequential per-retailer tasks and parallel independent country jobs.
5. **Prefer stable catalog directory URLs.** Prefer official canonical "offers/catalog" links that update their content in place. If an official catalog URL changes for every promotional period, its catalog entry MUST include evidence-backed \`valid_until\`; never publish a rotating/dated link with null/missing expiry. Reject and flag changed domains for review. Never synthesize expiry dates.
6. **Remove expired highlighted products.** At each candidate build, prune items with \`valid_until\` strictly earlier than today's date in the source market, or with positive source evidence that an offer ended. A verified expiry is deleted even when today's retailer fetch fails. Undated/unreachable items are **stale/unverified**, NOT automatically proven expired; do not claim they are current. Surface for immediate verification and suppress from current-offer claims. Avoid wiping the whole feed because a crawl fails.
7. **Strict read/write boundaries.** Catalog-maintenance writes ONLY \`pretio/promos/catalog_app.json\`; highlight-maintenance writes ONLY \`pretio/promos/highlights/**\`. Both may use separately scoped code, docs and tests changes on an approved PR. Never alter legal pages, \`pretio/promos/location.json\`, \`pretio/location/v2/**\`, \`pretio/data/currency.json\`, \`pretio/localization/**\`, or Android without a separate approved project. Coupled updates validate against the final catalog + feed snapshot.
8. **Do not bypass access restrictions.** Official public sources only; respect ToS, robots, rate limits, copyright and image licenses. No CAPTCHA circumvention, login scraping, stealth or proxy rotation. Use HTTP first, Playwright only where permitted, OCR/LLM as evidence extraction assistance (never as a source of truth).
9. **Only publish verified data.** Default mode AUDIT or PREPARE (draft branch/PR), never merge/deploy unattended solely because this skill exists. Scheduled PUBLISH requires independent Owner-approved policy + tests + rollback plan.

## Per-catalog execution loop

For every **country → retailer catalog**:
1. Read current stable catalog entry, the previous per-catalog handoff, and matching existing highlights.
2. Create a fresh checklist from \`templates/CATALOG_CHECKLIST.md\`. Record retailer, canonical URL, scope, observation timestamp, and evidence.
3. Validate official link, stable-vs-periodic classification, URL expiry rule, source/host restrictions and location context.
4. Extract all **eligible discounted products**, verify each normal/promo pair + image + currency + dates + catalog ID, reject otherwise. Prioritize NEW products, then re-verify retained ones.
5. Delete proven expired products from the country candidate; do not clear unrelated products or overwrite good data due to fetch failure. Deduplicate across retailers/catalogs, max 80 per country and 20 per retailer.
6. Save candidate changes and checklist/receipt **outside the live JSON feed**, then **compact to \`templates/COMPACT_HANDOFF.md\`** (max about 400 words, no raw HTML, secrets, image bytes or detailed irrelevant history).
7. Mark \`CATALOG_DONE\` only after checklist, checkpoint and validity checks complete. Queue next catalog using a clean context and previous handoff. A failed source still produces a completion receipt with failure reason.
8. When all catalogs for a country finish, reconcile candidates; target ≥1 **new verified** unique product per country per cycle. If not possible, \`TARGET_MISSED\` with catalog-by-catalog reasons. Never fabricate a product to reach the target.
9. Run strict JSON validator and cross-dataset checks; compute exact feed SHA-256; atomically stage country feed + index + audit. No partial publish, no SHA mismatch, no schema migration.

## Schedule and operating modes

- Intended cadence: \`17 1,13 * * *\` in GitHub Actions (UTC) = **09:17 / 21:17 WITA**. Scheduling is best-effort; run \`workflow_dispatch\` for manual verification. **This skill alone does not start an autonomous bot.**
- AUDIT / DRY_RUN (default): no tracked production changes; emit report and potential PR.
- PREPARE: isolated branch, schema checks, sources and evidence, candidate changes, Draft PR for review.
- PUBLISH: only an approved, separately implemented deterministic publisher can write after CI/approval; never use the LLM to free-form commit directly to \`main\`.
- Counters: attempted catalogs, verified catalogs, failed sources, new verified highlights, expired removed, country \`TARGET_MET\`/\`TARGET_MISSED\`, blocked countries, changed links, next schedule.
- For countries without a currency entry: \`BLOCKED_CURRENCY_METADATA\`. **Do not invent or add currency mapping in the highlight feed**; require a separate approved currency-catalog + Android compatibility update first.

## Stop conditions

- Any new production JSON field, unsupported app schema, unapproved host, missing source price pair or invalid image.
- Missing country currency, unverifiable geography, broken index hash, an attempted link rotation without \`valid_until\`, or unrelated paths modified.
- Significant surge in expired removals or source failures → quarantine and review, except individually proven expired products which should be removed by the safe expiry-cleanup phase.

Deliver a structured run report with PR/commit, tests PASS/FAIL, per-country delta, missed targets, and any requested Owner actions. Never claim a run, scraper, or scheduler exists or passes without execution evidence.
