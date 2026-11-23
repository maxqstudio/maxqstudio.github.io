# Pretio catalog checkpoint — Pick n Pay South Africa

- Manifest work unit: `ZA:pnp-za-country`, position **74 of 74**; terminal receipt: `SKIPPED_BLOCKED`.
- Counted as attempted: **yes**. One bounded source check; no retries or product-page exploration.
- Owner scope: `ONE_OFF_GLOBAL`; this isolated context handled only the assigned PnP catalog. No schedule or second cycle.
- Run: `pretio-oneoff-global-20261123T040625Z`; source checks occurred approximately `2026-11-23T10:55–10:56Z`.
- Base/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Completed: South Africa / `pnp-za-country` / Pick n Pay.
- Source kind: physical retailer catalog; its accepted catalog summary states offers may vary by store and region.
- Canonical link: <https://www.pnp.co.za/catalogues>. Its direct tool view returned only a JavaScript loading shell, with no current catalog content or validity dates. Current evergreen content was not verified.
- Robots: <https://www.pnp.co.za/robots.txt> returned `200 text/plain`; it allows one request per 10 seconds, specifies `Crawl-delay: 10`, and permits visits only `04:00–08:45 UTC`. It disallows cart, checkout, account, search and list paths. The source attempts preceded discovery of this schedule and were made outside it; no PnP direct access occurred after the restriction was read.
- Terms/reuse: candidate `/terms-and-conditions` and `/terms` pages were not accessible in the tool view. No applicable commercial reuse or product-image permission was established. Do not inspect, copy, or reuse prices or images in this attempt.
- A search index surfaced a PnP-hosted PDF whose filename identifies a Pinelands edition and encodes `09–29 Nov 2026`. It was not opened directly and is only a non-qualifying lead; it does not verify the canonical page, current full catalog, nationwide coverage, or image rights.
- Result: `SOURCE_BLOCKED`; terminal receipt `SKIPPED_BLOCKED`. Audit classification: `STALE_UNVERIFIED`, not proven obsolete.
- New discounted products accepted: none. Product offers inspected: zero. No expiry inferred.
- Existing ZA feed items carry `valid_until: 2026-11-29`; that date is later than the South African market date `2026-11-23`. They were not source-reverified or changed in this task.
- Evidence: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/evidence/ZA-pnp-za-country.md`.
- Candidate country feed: none. No production JSON, shared progress, or shared terminal-receipts file edited.
- Next manifest input: none; this is work unit 74/74. Parent orchestrator must reconcile global counts and the separate discovery/closing gates.

## Work-unit details

Run ID: `pretio-oneoff-global-20261123T040625Z`
Country: `ZA` | Catalog ID: `pnp-za-country` | Retailer: Pick n Pay
Official URL: <https://www.pnp.co.za/catalogues> | Checked UTC: approximately `2026-11-23T10:55–10:56Z`
Mode: `AUDIT` | Manifest position: `74/74` | Attempt: `1`

## 1. Catalog Promo source

- [x] Loaded frozen manifest row and accepted catalog record: ZA / Pick n Pay / `pnp-za-country`; the canonical URL matches.
- [x] Checked the official robots URL once. It sets a 10-second delay/rate and a `04:00–08:45 UTC` visit window. The attempt was outside that window because the schedule was learned from the robots response; this deviation is recorded above. No requests were made after learning the restriction.
- [ ] Current catalog content, redirects, updated-in-place behavior, exact current dates, and terms could not be verified. The canonical tool view returned a JavaScript loading shell; candidate terms URLs were inaccessible.
- [ ] No permission for commercial reuse of product/pricing data or product images was established. Prices and images were not inspected or copied.
- [ ] National offer participation was not verified. The source record itself warns of store/region variation; the search-index PDF lead is marked Pinelands and cannot establish countrywide applicability.
- [x] Existing `valid_until: null` and `last_verified_at: null` were left unchanged; neither was treated as proof of evergreen validity or expiry.
- [x] No production catalog schema or JSON changed.

## Explicit scope / one-off validation

- [x] Mode: explicit `ONE_OFF_GLOBAL`, using the frozen 74-unit manifest, not a recurring scan.
- [x] This isolated task processed only `ZA:pnp-za-country`; no other country source was checked and no schedule or second cycle was created.
- [x] This receipt closes only this work unit. Whole-run completion and the remaining global phases belong to the parent orchestrator.

## 1B. Online-store / marketplace discovery

- [x] No separate online-shop or marketplace discovery was performed in this registered catalog context.
- [x] No online sellers or product pages were reviewed or mapped.
- [x] Any separate bounded discovery phase remains outside this checkpoint.

## 2. Product Highlights — discounted items only

- [x] Product listings, prices, and images were not inspected because current source access fell outside the robots visit window and reuse permission was unverified.
- [x] Accepted items: none. Product candidates assessed: zero.
- [x] No product name, price pair, product image, validity date, or product-level geography was copied or inferred.
- [x] No ZA feed candidate was created or modified. Existing feed dates were checked only for expiry bookkeeping, not reverified against PnP.

## 2A. Confirmed obsolete catalog retirement

- [x] Audit classification: `STALE_UNVERIFIED`; current promotional content is not verified.
- [x] No positive evidence that Pick n Pay or this catalog source was discontinued or obsolete.
- [x] No replacement URL, catalog removal, or highlight-reference change staged.
- [x] Existing catalog and dependent highlights remain unchanged; no orphan reference was introduced.

## 2B. Location relevance and expiry

- [x] Physical-store participation and item-level geography were not verified; no offer is claimed nationwide.
- [x] No product was staged into the country-wide feed.
- [x] Existing ZA feed offers show `valid_until: 2026-11-29`, later than the South African date `2026-11-23`; none was deleted based on this check.
- [x] No catalog expiry was inferred from the null date or the search-index lead.
- [x] No feed/index bytes or hashes changed.

## 3. Skip-or-update decision

- [x] `SKIPPED_BLOCKED` — the direct source attempt occurred outside the robots visit window, the page returned no catalog content, and terms/image reuse permission was not established. Stop without inspecting offers.

## 4. Checkpoint and context compact

- [x] Saved this checklist, separate evidence, compact handoff (under 400 words), and one-work-unit terminal receipt.
- [x] No accepted product IDs, expired deletions, or candidate feed.
- [x] Next manifest input: none; this is position 74/74.

## 5. Cycle completion and country closing gate

- [ ] Whole-manifest closing gate is not asserted here; parent orchestrator must reconcile all 74 receipts, bounded discovery, validation, and country targets.
