# Walmart Advertised Deals — Registered Catalog Checkpoint

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `US` | Catalog ID: `walmart-us-country` | Retailer: Walmart  
Official registered URL: <https://www.walmart.com/shop/deals/shop-advertised-deals>  
Checked UTC: `2026-11-23` (exact request timestamps not retained) | Mode: `AUDIT / ONE_OFF_GLOBAL`  
Manifest ordinal: `72/74` | Attempt: `1`  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal result: **`SKIPPED_BLOCKED`**

## 1. Catalog Promo source

- [x] Loaded the exact frozen work unit and active catalog item. The URL matches; `www.walmart.com` is allowlisted. Record scope is country `US`, national label “United States (store-selected offers),” `valid_until: null`, `last_verified_at: 2026-09-22T00:00:00Z`.
- [x] One official robots request returned HTTP 200. The `User-agent: *` rules do not disallow the registered deals path or the linked Help/Terms path. Other listed exclusions were respected.
- [x] One request to the exact registered URL returned HTTP 200, unchanged final URL, and the Walmart.com page title `deals shop advertised deals - Walmart.com`. This confirms a response on the accepted official host, not offer freshness or geographic applicability.
- [x] The official [Walmart.com Terms of Use](https://www.walmart.com/help/article/walmart-com-terms-of-use/3b75080af40340d6bbd596f116fae5a0) prohibit automated collection and collection/use of product listings, descriptions, and prices without express permission; materials are limited to personal, non-commercial use. Walmart's official [Agentic Access Terms](https://www.walmart.com/help/article/walmart-agentic-access-terms/d048fc229d7549738d7c05a4317e24d7) further limit data use to authorized shopping purposes and prohibit systematic/bulk collection, commercial analytics/reporting, and redistribution. No Walmart authorization or written permission for this Pretio audit/reuse was found.
- [x] The registered page was fetched once before Terms review. After the restriction was identified, no product extraction or further registered-page access was performed. No written permission was obtained.
- [x] Current promotion dates/validity, canonical evergreen behavior, and participating-store geography remain unverified. No change to the catalog record or `last_verified_at`.

## 1B. Online-store / marketplace discovery

This task covers only the frozen Walmart registered catalog. No other store, seller, or marketplace was opened from this source context.

## 2. Product Highlights candidates

- [x] No product names, prices, images, or offer-validity details were inspected, retained, or evaluated for publication after the terms restriction was identified. No accepted or rejected item IDs; this is not `SKIPPED_NO_PROMO`.
- [x] The existing record labels US store-selected offers; that label does not establish item-level nationwide prices or availability. Product-level geographic scope remains unverified.
- [x] USD metadata exists. The current US feed has 12 items and no `walmart-us-country` references. No candidate feed was created and no expiry/deletion was established.

## 2A. Obsolescence and disposition

- [x] Audit disposition: `STALE_UNVERIFIED`. No source-backed expiry, obsolescence, or current replacement was established. Preserve the existing registration; no catalog retirement is justified.

## 3. Skip-or-update decision

- [x] **`SKIPPED_BLOCKED`** — official Terms prohibit the collection/use needed for this catalog audit absent express authorization; none was located. No offer/product evidence was retained.
- No accepted products, expiry deletions, or catalog migration. No production JSON, feed, index, or shared progress was changed.

## 4. Checkpoint and compaction

- [x] Source evidence: `registered/evidence/US-walmart-us-country.md`.
- [x] Compact handoff: `registered/handoffs/US-walmart-us-country.md` (under 400 words).
- [x] Terminal receipt: `registered/receipts/US-walmart-us-country.json`.
- Shared progress and aggregate terminal-receipt files were not changed. This closes only `US:walmart-us-country`; the global run remains with its orchestrator.

## 5. Cycle-level closing gate

Not evaluated by this per-catalog worker. This receipt does not assert full manifest completion or a US country target outcome.
