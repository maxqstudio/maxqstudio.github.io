# Pretio — per-catalog source checkpoint

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `NA:food-lovers-market-na-country` | manifest position: **45/74** | attempt: **1**  
Country: **NA / Namibia** | retailer: **Food Lover's Market** | mode: **AUDIT**  
Recorded UTC: **2026-11-23 09:55:45 UTC** (the browser connector did not expose request-level timestamps)  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## Catalog source and access

- [x] Loaded the frozen manifest and active record: `food-lovers-market-na-country`, publisher/merchant Food Lover's Market, country NA, national label `Namibia (store-selected offers)`, `valid_until: null`, existing `last_verified_at: 2026-09-28T00:00:00Z`.
- [x] Opened the exact registered HTTPS URL: <https://foodloversmarket.co.za/namibia/>. The page title identifies Food Lover's Market and Namibia, its footer says © 2026 Food Lovers Market, and it links a store finder. The page rendered only “Store information loading” and “Specials loading”; no catalog cards, dates, products or prices were visible in the captured page.
- [x] Requested <https://foodloversmarket.co.za/robots.txt> once with a standard HTTP client and 30-second timeout. Response: HTTP 200, `text/plain; charset=utf-8`; `User-agent: *` has an empty `Disallow:`, so no path is disallowed by that robots file.
- [x] Direct-opened the same-host <https://foodloversmarket.co.za/terms-and-conditions/> page after the official site displayed a “Terms and Conditions” footer link. It describes terms for competitions/promotions and lists individual promotion terms; it did not provide general automated-access or commercial-content-reuse permission. Following the footer link itself later timed out, so that exact navigation relationship was not independently verified. No explicit permission evidence was found; this is **unverified**, not a claim that commercial reuse is prohibited.
- [ ] Current promo data, a working stable canonical link, in-place update behavior, redirect chain, offer dates, and item-level Namibia store eligibility were not verified. The landing URL is fixed, but its evergreen freshness is unconfirmed.
- [x] The Namibia page's store-finder link and existing `store-selected offers` label mean a national product discount cannot be inferred from this page alone.
- [x] The standard currency registry does not support NA for Product Highlights and there is no `NA.json` feed.

## Product and integrity result

- No product page/card was visible or examined; accepted/rejected product candidates: **0 / 0 inspected**. No normal/promo pair, currency, individual product image, validity interval, or nationwide applicability was retained.
- A scan of all existing Product Highlights feeds found **zero** references to `food-lovers-market-na-country`.
- No expired/obsolete status is justified: `valid_until` is null and this check did not establish that the retailer's Namibia promo page ended. Production catalog/feed/index data was not changed.

## Decision and compact handoff

`SKIPPED_UNVERIFIED`: robots permits the path, but the country page exposes only loading placeholders and the official terms page does not establish automated commercial reuse permission. Do not copy offers or claim current discounts. Preserve the active catalog record as `STALE_UNVERIFIED`; do not infer expiry from missing content or its old verification date. The page is Namibia-specific and store-selected, so it cannot prove countrywide item eligibility. NA has no supported highlight currency/feed and no existing highlight references this catalog. No production data changed. Next manifest source: `PE:metro-pe-online-catalogs` (46/74), in a fresh isolated context.
