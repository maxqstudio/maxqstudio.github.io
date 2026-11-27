---
name: pretio-public-content-updater
description: Research and update Pretio official retailer catalogs, direct online shops, marketplace seller offers and discounted Product Highlights, with Google Shopping as authorized discovery only, strict evidence/schema gates, per-source checklists, and Owner-scoped one-off or approved recurring operations.
---

# Pretio Public Content Updater

**Purpose:** Keep the public Pretio catalog directory and discounted product highlights reliable across supported countries, covering **physical retailer catalogs, independent online shops, verified marketplace seller storefronts, and public online offers**. Google Shopping may help discover candidate merchant links by an authorized method, **never serve as final price proof**. Never invent a retailer, product, discount, reference price, seller, URL, image, date or location. No new JSON fields are permitted in either production dataset.

**Repository:** `maxqstudio/maxqstudio.github.io` (GitHub Pages). Android `maxqstudio/pretio` is a **read-only compatibility reference**.

## Read first
- `pretio/promos/catalog_app.json` — catalog v2, 74 current entries spanning 24 country codes (counts may change).
- `pretio/promos/highlights/index.json` — highlight INDEX **v2**, `schema_version: 2`.
- `pretio/promos/highlights/CC.json` — country highlight FEED **v1**, `schema_version: 1`.
- `pretio/data/currency.json` — read-only currency coverage, currently seven countries.
- `pretio/promos/location.json`, `pretio/location/v2/index.json` — read-only geography.
- `pretio/promos/highlights/UPDATER_CONTRACT.md` — updated compatibility rules.
- `references/catalog-rules.md`, `references/highlight-rules.md`, **`references/product-name-normalization.md`**, **`references/global-catalog-discovery.md`**, **`references/online-shop-marketplace-rules.md`**, `references/operations.md`.
- `templates/CATALOG_CHECKLIST.md`, **`templates/ONLINE_SHOP_CHECKLIST.md`**, and `templates/COMPACT_HANDOFF.md`.

## Online-commerce coverage (mandatory when researching products)

**Do not restrict research to supermarket or brick-and-mortar retailer catalogs.** Research eligible **online merchants**, **direct web shops**, **official marketplace stores**, and **public marketplace product listings** within the run's authorized countries.

- **Stage A — registered catalog manifest:** attempt every existing `(country_code, catalog_id)` with a terminal checkpoint as before. Already registered online stores are first-class sources, not skipped.
- **Stage B — additional online-shop discovery:** within the same Owner-scoped countries, investigate authorized online store/platform sources and record every identified seller/store as an **audit-only discovery candidate**. This is a bounded discovery pass, **separate from the registered manifest**: `74/74` receipts proves registered-catalog coverage, not that all online shops were crawled.
- Google Shopping may be used only through **permitted discovery methods**; product price and discount must be verified directly at the real seller/storefront, never copied from Google Shopping results or snippets. Do not automate scraping Google Search/Shopping contrary to access rules.
- Distinguish marketplace platform versus actual seller/store ID. Validate the **same seller's** normal and promo prices for the **same product/variant, shipping market and purchase channel**. An ad, MSRP, another seller's price, member/first-user coupon, cashback, payment-method discount, or geographic guess is not eligible proof.
- Do not add unapproved domains/sellers automatically. Any **new** merchant/store/catalog ID requires separate Owner-reviewed catalog registration and matching official host before its offers become publishable. Unregistered but verified offers remain audit-only. Do not weaken Android, catalog or highlight schema gates.
- Bound per-market search and pagination, record how much was actually inspected, checkpoint and compact per shop. **Complete one-off work and stop; do not enable a scheduler.**

**Read `references/online-shop-marketplace-rules.md` in full.** It controls merchant identity, Google Shopping discovery, online evidence, image validation, catalog registration and production mapping; use the `ONLINE_SHOP_CHECKLIST.md` template for every discovered shop.

## Mandatory deletion of expired items and obsolete promotional catalogs

**Never accumulate known-expired or positively obsolete records in LIVE production lists.** For every staged update:
- Delete each Product Highlights item whose verified `valid_until` is before today's market-local day, or whose official source proves the offer ended. This applies even if its source cannot be fetched now. Recalculate the changed feed's revision and exact index v2 hash.
- For an old **period-specific Catalog Promo**, first look for a stable official evergreen replacement. If the existing catalog `id` still identifies the same merchant/source, stage a verified `url` migration under catalog-owner review; otherwise, if the old promo is positively obsolete with no valid successor, remove its entry from the active `catalog_app.json.items` array.
- Do **not** treat a single 404, network error, access block, missing expiry, or old `last_verified_at` as proof of obsolescence. Audit as `STALE_UNVERIFIED`, investigate separately and continue.
- **Deletion integrity gate:** no removed catalog may leave any orphan Product Highlights `catalog_id` reference. Remove proven-expired dependent offers or migrate still-valid verified offers to an approved successor; otherwise HOLD publication. Stage catalog + impacted country feeds + index atomically, validate strict expiry/foreign keys/host/market scope/CI, then request Owner review.
- Audit removed product IDs, removed/replaced catalog IDs, evidence, affected feeds and post-update hashes; keep deletion history OUT of published JSON.

Read `references/catalog-rules.md` and `references/operations.md` for source-backed obsolescence decisions and cross-feed referential integrity.

## Location-first relevance and expired-item cleanup (Owner-locked)

## Owner correction — location-aware offers (27 November 2026)

**Nationwide coverage is NOT required.** A verified regional, province, city, or local-store promotion is legitimate. Record its exact eligible location(s), public price pair for that same area/channel, and official evidence. Do not extrapolate a location-selected price to the whole country. Genuine countrywide online/physical offers use country scope only.

- Research and retain regional candidates with canonical country/province/city codes and names from the existing location directory; record eligible branches/fulfillment restrictions and evidence in audit. Do not invent codes, widen an area, or assume all stores participate.
- **User-facing requirement:** filter by the location explicitly selected by the user; show a clear eligible-area label. Country selection shows countrywide offers; province selection additionally shows matching province offers; city selection additionally shows matching city offers. Unknown/invalid scope, unavailable required location, or nonmatching area fails closed. Never fall back to unrelated local prices. No GPS/address collection requirement.
- A regional promotion is NOT expired, obsolete, or invalid solely because of its geographic restriction. Preserve source evidence and regional candidates; do not delete an existing item solely for being regional. If its old countrywide presentation is misleading, flag for reviewed quarantine/migration rather than treating it as expiry or discarding evidence. Independently proven expiry, false price pairs, or source-rights violations remain separate correction grounds.
- **Compatibility gate:** current production Product Highlights v1 has no item-level locations; do not add unsupported fields or publish regional data to legacy clients as countrywide. Retain such candidates as LOCATION_AWARE_PENDING (audit-only, not a new terminal receipt enum) until the separately versioned location-aware feed, validator, Android reader/filter, visible labels and legacy-safe rollout are implemented and accepted. Catalog Promo v2 already supports explicit country/province/city location rules; use these as the geographical reference. Implementation: https://github.com/maxqstudio/pretio/issues/111. No production schema change in this skill-only revision.
- Regional scope alone is never a reason to skip discovery/extraction where access is permitted; if the precise scope cannot be established/represented, record the blocker, preserve evidence and continue. All access/rights, genuine price, image, expiry, currency, identity, and other acceptance requirements remain unchanged.

- **Physical retail:** verify exact eligible branches, province/city, dates and participation rules. Regional promotions qualify for research and location-aware presentation under the Owner correction; a nationwide catalog URL is not proof of a nationwide item.
- **Online stores and marketplace sellers:** verify the public price, product variant and ordering/fulfillment area. Countrywide offers need only country proof; regional delivery or pickup offers qualify at their actual verified scope, subject to the compatibility gate.
- **Expired items MUST be removed from live Product Highlights feed, not retained indefinitely.** On every supported staged publication, delete all existing entries with `valid_until` before the source-market current date or official verified ending evidence, even if source fetch failed. Also remove proven-expired catalog promos from the published active list (or replace with verified new period/evergreen URL under catalog approval). Update feed/index hash and check referential integrity. Keep the historical proof in **bounded separate audit artifacts**, not the live lists. Do not treat an inaccessible source or undated item as verified expired.
- **Regular-price products can be researched** alongside discounts. Record price observations as audit-only until a separate approved schema/Android change supports their public display; current country Product Highlights v1 only permits genuine `normal_price > promo_price` deals.

## Global Catalog Promo discovery and normal-price observations

- **Discovery target approximately 174 countries**, starting with the documented 249-country/territory V2 registry and a justified commercial-market shortlist; do NOT limit discovery to the 24 countries already registered. Treat 174 as an ambitious coverage goal, not an instruction to invent qualified catalogs. Keep country discovery checkpoints separate from registered catalog receipts.
- **Evergreen catalog links FIRST:** prefer a single official permanent promotions/catalog URL with regularly updated content. **Rotating catalog URLs SECOND:** use official period-specific PDFs/pages only when no evergreen equivalent exists; source-backed `valid_until` and a repeatable official parent/index navigation path are required. Obsolete verified period catalogs must be replaced by approved current links or removed safely from active lists.
- **Regular-priced products are allowed in research:** collect actual ordinary prices from authorized official seller listings, even with no discounted offer, but keep them as **audit-only** until an independently approved production schema/UI supports such items. Product Highlights v1 stays discount-only and existing validation must not be weakened. Do not populate a fake normal/promo price pair.
- **Owner one-off remains one-off:** these rules do not schedule, deploy, or run the crawler. Do one scoped research cycle if explicitly requested, then stop; no repeat or cron.

Read `references/global-catalog-discovery.md` in full; it is mandatory for global market research.

## Mandatory product-name normalization (every extracted product)

- Expand receipt/catalog shorthand into natural, readable Indonesian product names before matching, deduplicating or staging: `MYK GRG → Minyak Goreng`, `KCP MNS → Kecap Manis`, `PCH → Pouch`, `BTL → Botol`, `KTG → Kaleng`, `SBN MND → Sabun Mandi`, `DTRGN → Deterjen`. Preserve recognized standard terms `UHT`, `3in1`, `SPF`, `ml`, `g`, `kg`, `L`, `pcs`; normalize unit spacing without changing SKU identity. Do not guess unknown abbreviations.
- The **intermediate extraction** MUST produce separate `productName`, `brand`, `variant`, `packageSize`, and `packCount` fields (use `null` where unverifiable), plus original raw text and source proof in **audit only**. Example: `BIMOLI MYK GRG PCH 2L` → `productName = Bimoli Minyak Goreng 2 L`, `brand = Bimoli`, `variant = Pouch`, `packageSize = 2 L`.
- **Production strict mapping:** current country Product Highlights v1 only supports `product_name`, optional `brand` and `package_size`; `variant` and `packCount` remain separate audit data unless essential identification can be safely represented in existing fields. **Never introduce camelCase or new item JSON keys.** No item may be published if size/variant/pack count identity is ambiguous.
- Matching user-saved products/Watchlist should use brand + normalized name + exact variant/size/pack count where possible; lightweight normalization of user typing belongs to a separate Android PR, not this crawler.

**Read `references/product-name-normalization.md` in full and apply its auditor checks.**

## Fundamental rules

1. **Discounted products only.** A highlight requires retailer evidence of both an actual `normal_price` and a strictly lower `promo_price` for the SAME product, size, channel and location. No regular-priced items, general cashback slogans, undocumented "up to X% off" claims, inferred original prices, or missing images. At least one NEW qualified product per country per 12-hour cycle is the **target**, not permission to fabricate. If unmet, mark `TARGET_MISSED` and include the reason.
2. **Required link fallback versus absent optional fields.** `source_url` is a required field, but a dedicated product detail page is **not**: use an official retailer Catalog Promo landing page (for example Indomaret's official promo catalog) when it visibly contains the exact discounted product and both verified prices. Capture proof in a separate run artifact. If the product is not verifiable on any official page, skip that product. Optional unavailable keys (`brand`, `package_size`, `valid_from`, `valid_until`, `logo_url`, `image_revision`, `logo_revision`) are omitted. Never add placeholder fields or skip an otherwise qualified item solely for missing optional metadata.
3. **Use ONLY existing production fields.** Strict key allowlists in `references/catalog-rules.md` and `references/highlight-rules.md`; do not add `discount_percent`, `confidence`, `status`, `country_code`, internal evidence links or any other new field to highlight items. Do not add metadata to catalog entries. Store checkpoints/audit OUTSIDE production JSON (work artifacts/audit files).
4. **One catalog or online storefront per bounded agent context.** Select `(country, catalog_id)`, complete its checklist, validate findings, update the candidate highlight feed, write a compact handoff, then **start a fresh isolated catalog task with ONLY its handoff plus the next catalog input**. Do not carry entire HTML dumps, previous transcripts or other catalogs' raw evidence into next context. See `references/operations.md`.
5. **Every registered catalog in EVERY listed country within the explicit run scope, no early exit.** At cycle start, snapshot all active official catalog entries from `catalog_app.json` and expand to a de-duplicated exhaustive manifest of `(country_code, catalog_id)` work units. This manifest is the full required coverage, including countries lacking highlight feeds/currency mappings. Do not stop when one product is found, one country meets its growth target, an individual source fails, the bot's context is full, or a time budget is reached. Every manifest work unit must receive a terminal receipt after one bounded attempt (plus limited retries where justified). Distribute workloads with bounded concurrency; country workers may run in parallel. Countries without supported currency can still have their catalog URL checked; their highlight write is skipped with `BLOCKED_CURRENCY_METADATA`.
6. **Prefer stable catalog/store directory URLs.** Prefer official canonical "offers/catalog" links that update their content in place. If an official catalog URL changes for every promotional period, its catalog entry MUST include evidence-backed `valid_until`; never publish a rotating/dated link with null/missing expiry. Reject and flag changed domains for review. Never synthesize expiry dates.
7. **Remove expired highlighted products.** At each candidate build, prune items with `valid_until` strictly earlier than today's date in the source market, or with positive source evidence that an offer ended. A verified expiry is deleted even when today's retailer fetch fails. Undated/unreachable items are **stale/unverified**, NOT automatically proven expired; do not claim they are current. Surface for immediate verification and suppress from current-offer claims. Avoid wiping the whole feed because a crawl fails.
8. **Strict read/write boundaries.** Catalog-maintenance writes ONLY `pretio/promos/catalog_app.json`; highlight-maintenance writes ONLY `pretio/promos/highlights/**`. Both may use separately scoped code, docs and tests changes on an approved PR. Never alter legal pages, `pretio/promos/location.json`, `pretio/location/v2/**`, `pretio/data/currency.json`, `pretio/localization/**`, or Android without a separate approved project. Coupled updates validate against the final catalog + feed snapshot.
9. **Do not bypass access restrictions.** Official public sources only; respect ToS, robots, rate limits, copyright and image licenses. No CAPTCHA circumvention, login scraping, stealth or proxy rotation. Use HTTP first, Playwright only where permitted, OCR/LLM as evidence extraction assistance (never as a source of truth).
10. **Only publish verified data.** Default mode AUDIT or PREPARE (draft branch/PR), never merge/deploy unattended solely because this skill exists. Scheduled PUBLISH requires independent Owner-approved policy + tests + rollback plan.

## Explicit Owner one-off scope OVERRIDES global scheduler policy

When the Owner explicitly requests **"kerjakan 1 kali saja untuk Indonesia"** or equivalently "run once for Indonesia", that instruction takes precedence over the normal worldwide 12-hour scan: create **ONE** on-demand run limited to `country_code = ID`, process **all Indonesia catalogs only**, finalize that run and **STOP**. Do NOT inspect, fetch or update other countries, expand to all 24 markets, start a recurrence, create a cron job, run a second cycle, or assume a standing order. Existing scheduled operations are distinct; the one-off request does not implicitly change any pre-existing schedule, but this task must not start one. If a later instruction explicitly names a different country, use that country only.

**Scope lock:** `python3 tooling/pretio_public_content/manifest.py --once --country ID`. Coverage receipts must exactly match those scoped work units; foreign-country receipts are invalid. The Publisher must change only the selected country highlight feed / its index entry, and only selected-country catalog entries when touching the shared `catalog_app.json`. Other countries and their catalog entries must be byte-equivalent in meaning; do not modify their feed files. Scope policy also applies to source-fetch operations, documentation work and retries. `--once` creates only an isolated manifest: it **does not crawl or publish** by itself.

When the user explicitly requests an unrestricted recurring bot, use the global full-country scan below. An explicit one-off command always overrides that default for its own execution.

## Execution support

Generate full, country-inclusive work units with `python3 tooling/pretio_public_content/manifest.py`. Pass per-catalog terminal receipts to `--receipts <path>` and require `cycle_status=COMPLETED` before declaring a cycle finished. A completed scan may have zero updates. A dedicated 12-hour runner/crawler still needs to be implemented; this manifest tool **does not** scrape, schedule or publish.

## Complete-cycle algorithm (MANDATORY)

For a scheduled global run (only if separately approved), attempt EVERY registered catalog in EVERY selected country. For an explicit one-off, attempt EVERY registered catalog and then bound online-store discovery **within that one-off scope**; do not stop after the first discount. "Skip" means **finish that catalog with a recorded reason, then proceed to the next catalog**. Never silently omit one from the manifest.

1. **Snapshot and enumerate registered catalogs**: read `catalog_app.json` once, derive every unique `(country_code, catalog_id)` from the locations of every active official catalog, and record `manifest_total`. Sort deterministically: country code, evergreen catalog first, then catalog ID. Existing country feeds, available currencies, successes/failures or the one-new-product target do **not** reduce the manifest.
2. **Process one catalog** in its own isolated context with a checklist. Verify current canonical official catalog, location validity, and **all obtainable real discounted product offers**, not just enough offers to hit a quota. For valid new/changed data, stage updates to a country **candidate** feed and catalog candidate. Do not overwrite published feeds during the crawl.
3. **Skip rather than stall** when a catalog is inaccessible, unchanged, has no proven discounts, requires prohibited access, has no compatible currency, lacks verifiable expiry for a rotating URL, or supplies insufficient evidence. Record terminal status `SKIPPED_NO_CHANGE`, `SKIPPED_NO_PROMO`, `SKIPPED_UNAVAILABLE`, `SKIPPED_BLOCKED`, `SKIPPED_UNVERIFIED`, or `BLOCKED_CURRENCY_METADATA` in the checkpoint/audit **only**. Retain unrelated verified data. Use finite source timeouts, bounded retries and no infinite loop.
4. **Checkpoint + compact** for EVERY manifest entry, including failures/skips: complete `CATALOG_CHECKLIST.md`, persist accepted/rejected candidates and a succinct `COMPACT_HANDOFF.md` (max ~400 words), mark it terminal, and launch next catalog as a **fresh isolated task**. Do not reuse raw HTML or an unbounded conversation.
5. **Resume** missing manifest work units on retry/restart; never redo a successfully finalized catalog without an explicit reason. A cycle can terminate only after `terminal_receipts == manifest_total` and there are **zero** pending catalog entries. No global short-circuit, first-success return, per-country early break or skipping unattempted catalogs due to the target being met.
6. **Discover additional online shops after processing the registered manifest**: per selected country, perform a bounded authorized seller/store research pass and produce a separate audit-only discovery register using `ONLINE_SHOP_CHECKLIST.md`. Examine sellers found from official web shops, permitted marketplace storefronts, and optionally authorized Google Shopping discovery. If the candidate merchant has no approved catalog ID, request review and do not publish its offers. Report discovery coverage separately from catalog manifest completion. **Then finalize once after coverage completes**: reconcile all staged valid Catalog Promo and Product Highlights changes, run deterministic expiry deletion (including known expired items from skipped/failed catalogs), enforce strict old field names, existing schemas, item count/currency/geography/official-source validation, and exact feed+index SHA. Publish/prepare **one consistent validated batch**, not piecemeal broken country JSON. A country without changes is left byte-identical.
7. **Complete and stop** the cycle only after full registered-manifest coverage, the bounded online-store discovery pass, final validation and reporting. Do not continuously crawl after finishing. Next scheduled run builds a fresh manifest 12 hours later; if validation fails, hold publication, report failure, and still close the completed scan cycle.

**Per-cycle reporting:** Include separate `online_stores_discovered`, `online_stores_checked`, `marketplace_offers_verified`, `awaiting_catalog_approval`, `online_candidates_skipped` and discovery/search bounds in audit only; these do not alter the frozen manifest denominator. Also report `manifest_total`, `attempted`, `terminal_receipts`, `updated`, `skipped_no_change`, `skipped_no_promo`, `skipped_unavailable`, `skipped_unverified`, `failed`, `expired_removed`, `new_discount_products_by_country`, `TARGET_MET/TARGET_MISSED` for each country, `pending`. A healthy finished cycle has `pending = 0`; a partial or interrupted run must be labeled `INCOMPLETE`, not "done". Zero new eligible offers is a valid scan outcome, **not** a reason to keep scanning forever.

## Schedule and operating modes

- Intended cadence: `17 1,13 * * *` in GitHub Actions (UTC) = **09:17 / 21:17 WITA**. Scheduling is best-effort; run `workflow_dispatch` for manual verification. **This skill alone does not start an autonomous bot.**
- AUDIT / DRY_RUN (default): no tracked production changes; emit report and potential PR.
- PREPARE: isolated branch, schema checks, sources and evidence, candidate changes, Draft PR for review.
- PUBLISH: only an approved, separately implemented deterministic publisher can write after CI/approval; never use the LLM to free-form commit directly to `main`.
- Counters: attempted catalogs, verified catalogs, failed sources, new verified highlights, expired removed, country `TARGET_MET`/`TARGET_MISSED`, blocked countries, changed links, next schedule.
- For countries without a currency entry: continue checking ALL their catalogs and record `BLOCKED_CURRENCY_METADATA` for highlight creation. **Do not invent or add currency mapping**; require a separate approved currency-catalog + Android compatibility update first. This blocks highlight publication for that country, NOT the entire scan.

## Skip conditions vs safety gates

- **SKIP ONLY THE CURRENT CATALOG** if it cannot be fetched after bounded retries, is unchanged, has no eligible discount, lacks verifiable location/price/image proof, has a rotating link without verified expiry, or lacks supported currency for highlight publication. Regional scope by itself is not a skip reason; retain eligible regional candidates for migration. Log the reason and continue.
- **HOLD PUBLICATION (not scanning)** if any staged result introduces unrecognized fields/schema, unapproved host, missing required proof, invalid currency/location, a broken index hash, a large unexplained deletion, or changes outside permitted paths. Continue the remaining catalog scan; report the publication blocker.
- Only the scheduler's cancellation/deadline/infrastructure failure may leave an incomplete manifest; report `INCOMPLETE`, retain durable receipts and resume the pending work at the next eligible attempt. Never falsely claim all catalogs checked.



Deliver a structured run report with PR/commit, tests PASS/FAIL, per-country delta, missed targets, and any requested Owner actions. Never claim a run, scraper, or scheduler exists or passes without execution evidence.
