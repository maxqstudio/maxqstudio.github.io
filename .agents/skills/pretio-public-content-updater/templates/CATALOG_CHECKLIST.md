# Pretio — per-catalog update checklist

Create a **new copy for EVERY (country, catalog_id) in the frozen complete manifest EVERY 12-hour cycle**, including countries without highlight-feed currency support. Save as a run artifact, NOT inside `catalog_app.json` or `CC.json`. A checked catalog with no update still requires a completed checklist and terminal receipt; do not drop it silently.

Run ID: `<UTC run id>`  
Country: `<ISO2>` | Catalog ID: `<accepted catalog id>` | Retailer: `<accepted merchant>`  
Official URL: `<official HTTPS URL>` | Checked UTC: `<timestamp>`  
Mode: `AUDIT / PREPARE / PUBLISH`  
Manifest work-unit number: `<N of manifest_total>` | Attempt number: `<1..bounded retry limit>`

## 1. Catalog Promo source
- [ ] Exact `catalog_id`, country, location rules and current original record loaded
- [ ] Official retailer source verified; links, redirects, allowed host, ToS/robots checked
- [ ] **Permanent/canonical catalog URL** prioritized and verified as working and updating in-place
- [ ] If periodic/rotating URL, verified **real `valid_until`** from source before accepting (no guessed date)
- [ ] Confirm national vs city/store scope; no extrapolation from a single store
- [ ] `last_verified_at` only changed after actual positive verification
- [ ] No extra catalog JSON keys or schema changes

## Explicit scope / one-off validation

- [ ] Confirm mode: global scheduled scan **OR** Owner-explicit `ONE_OFF(country_code=ID)` (never both for this run)
- [ ] If ONE_OFF: manifest includes ONLY requested country; external sources for other countries are untouched; no cron/second cycle created
- [ ] Complete every official catalog in the selected country once, including skipped or failed entries, and STOP after its own closing gate

## 2. Product Highlights — discounted items ONLY
- [ ] All eligible discounted products on this catalog checked; candidates listed
- [ ] Each has same-product explicit **normal and promo prices** from original retailer; `promo_price < normal_price`
- [ ] Product name/size/brand and currency verified; no guessed fields
- [ ] Product image decodable, same exact item, official/authorized source
- [ ] Exact approved `catalog_id` and official item source URL verified; if no product-specific URL exists, approved retailer catalog promo landing page may be `source_url` **only with exact product and price evidence on the page/linked official leaflet**
- [ ] Unavailable optional fields omitted; missing required image/price/source proof means skip item
- [ ] Item's geographic offer applicability supported (not just a catalog marked national)
- [ ] `observed_at` factual; known `valid_from` and `valid_until` retained
- [ ] **Expired** items (`valid_until` before market today or explicit ending proof) removed from candidate country feed
- [ ] No item contains any field outside approved item allowlist
- [ ] Rejected items recorded separately with reasons; no fabricated filler for 12-hour quota

## 3. Skip-or-update decision (always select one)
- [ ] **UPDATED** — accepted source-backed catalog or discounted-product changes staged in candidate only
- [ ] **SKIPPED_NO_CHANGE** — catalog verified but unchanged; no JSON churn
- [ ] **SKIPPED_NO_PROMO** — catalog checked; no eligible discounted product
- [ ] **SKIPPED_UNAVAILABLE / SKIPPED_BLOCKED** — fetch failed after bounded retries or legal/access block; preserve existing nonexpired data
- [ ] **SKIPPED_UNVERIFIED** — missing price pair/image/locality/rotating-link expiry; never invent
- [ ] **BLOCKED_CURRENCY_METADATA** — catalog checked, but cannot publish highlight for unsupported country
- [ ] **FAILED** — unexpected catalog-level error; log diagnostics, move on; do not abandon other catalog entries
- [ ] Skip status is recorded in checkpoint/audit only, NOT a new production JSON field

## 4. Checkpoint and context compact
- [ ] Accepted new product IDs and observed evidence recorded in run artifact
- [ ] Rejected candidates, source failures and location restrictions recorded
- [ ] Candidate country feed saved; unchanged good items retained
- [ ] Compact handoff written using `COMPACT_HANDOFF.md` (**max ~400 words**)
- [ ] Mark `CATALOG_DONE`, release raw evidence from next agent context
- [ ] Dispatch next catalog as NEW isolated task with compact handoff only

## 5. Cycle completion and country closing gate (after ALL manifest catalogs)
- [ ] Every country and every catalog from frozen manifest has a terminal receipt, even when skipped, blocked or failed
- [ ] `terminal_receipts == manifest_total`; `pending == 0` — otherwise flag `INCOMPLETE`, resume remaining units, do not report done
- [ ] Never stop because 1 new product per country was already found; finish every remaining catalog
- [ ] Target **≥1 NEW confirmed discounted product / country / run** checked; if missed report `TARGET_MISSED`
- [ ] 80/country, 20/retailer, unique ID, currency metadata and expiry validation PASS
- [ ] All feed fields match existing schema and all referenced `catalog_id` exist
- [ ] Index v2 entries/revisions and SHA-256 match exact staged bytes
- [ ] Diff confined to allowed writer paths; CI/approval/rollback ready

Final result: `<UPDATED / SKIPPED_NO_CHANGE / SKIPPED_NO_PROMO / SKIPPED_UNAVAILABLE / SKIPPED_BLOCKED / SKIPPED_UNVERIFIED / BLOCKED_CURRENCY_METADATA / FAILED>`  
Accepted NEW product IDs: `<ids or none>`  
Expired deleted IDs: `<ids or none>`  
Compact handoff artifact: `<artifact path>`
