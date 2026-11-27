# Online shops, marketplaces & Google Shopping discovery — Pretio

**Scope:** Expand the existing official Catalog Promo + discounted Product Highlights research to authorized **online stores, direct-to-consumer shops, official marketplace stores and marketplace product offers** in every country included in the Owner's selected run. This reference is a *skill policy*, not an installed scraper or permission to schedule one. See `catalog-rules.md` and `highlight-rules.md` for the exact production schemas.

## 1. Three roles — never confuse them

1. **Discovery surface**: Google Shopping, a permitted shopping search API, or a marketplace search page. It MAY suggest a seller, brand, SKU, URL, or candidate discount. Search snippets, sponsored listings, Google Shopping price cards, search-engine summaries and LLM output are **NOT proof** of a normal/promo price pair; never write a discovery URL as a highlight `source_url`.
2. **Commerce platform**: a marketplace such as Shopee, Tokopedia, Lazada, Blibli, Amazon, eBay or another country-specific platform. It may host many independent sellers. **The platform is not automatically the seller**, nor does its domain alone prove a listing belongs to an official store.
3. **Actual merchant/store**: a merchant-owned online shop, the marketplace's own first-party retail listing, or a specific identifiable third-party seller/official-store storefront. Record the seller/store name and verifiable seller/storefront identity in the audit. Keep the same seller, variant, condition, location, purchase channel and session when proving a discount. Do not label a third-party seller as a platform-owned offer.

Examples are **discovery prompts, not preapproved hosts or catalog entries**. Sources must actually operate in that country at scan time.

## 2. Two-stage work plan and completion accounting

**Stage A — mandatory baseline:** Freeze and process EVERY existing active `(country_code, catalog_id)` in `pretio/promos/catalog_app.json`, exactly as the existing manifest/checkpoint rules require. Online shops already in that manifest count here and MUST NOT be skipped just because they are digital.

**Stage B — online-store discovery:** For each country within the exact Owner-specified scope, seek **additional local online stores/official marketplace storefronts** using authorized public sources. Save an audit-only `(country_code, platform, seller/store ID, canonical URL)` discovery register. Deduplicate by verified seller identity and URL. This register is **separate** from the frozen production catalog manifest and must never silently add to its terminal receipt denominator or claim the entire internet was crawled.

- Give EVERY discovered candidate considered for this run an audit outcome: `VERIFIED_STORE`, `ALREADY_REGISTERED`, `SKIPPED_NO_PROMO`, `SKIPPED_UNVERIFIED`, `SKIPPED_BLOCKED`, `SKIPPED_UNAVAILABLE`, `BLOCKED_CURRENCY_METADATA`, or `NEEDS_CATALOG_APPROVAL`.
- Discovery must be **bounded** by source terms, practical request/time budgets and finite pagination/retries, with a recorded boundary (pages/search queries/listings checked); do not claim exhaustive internet coverage. Check enough authorized sources to seek qualified offers, but no infinite crawl.
- A newly discovered merchant that is not in Catalog Promo may yield an **audit-only** verified offer candidate. It cannot enter production Product Highlights until a matching **approved active** `catalog_id` exists and the app/site schema+host+geography gates pass. Preserve the original baseline catalog IDs. New seller/catalog entries and host allowlist changes require **separate Owner review**; no automatic registration or publication from discovery alone.
- Do not treat unavailable currency metadata as an excuse to skip checking official shop sources. It blocks publishing that market's feed, not research.
- **One-off overrides remain absolute**: `ONE_OFF:ID` discovers only Indonesian shops and checks only Indonesia entries; `ONE_OFF_GLOBAL` covers all selected countries, runs once and stops; no cron, no extra countries or second cycle.

## 3. Source priority and permitted retrieval

1. **Seller's official public e-commerce web page** or documented, authorized retailer feed/API (stable catalog/offer page, structured `Product`/`Offer`, sale price + distinct source-proven crossed-out/list/reference price).
2. **Verified official marketplace storefront and its public product-detail pages**, after checking the platform's permitted access, true seller ID and listing context; differentiate marketplace seller from platform-owned listing.
3. **Official promotional catalogs** of the same online merchant and their directly linked item pages.
4. **Google Shopping / Google Search only as candidate discovery when an authorized access method exists**; confirm each offer on the **actual merchant's official page**. Do not automate scraping of Google Shopping/Search result pages, use hidden endpoints or imitate Googlebot in violation of terms or machine-readable restrictions. Do not assume that Merchant API provides general public Shopping-search extraction.

Do not use arbitrary aggregator/referral/shortened URLs as `source_url`; resolve to a canonical **official seller or permitted marketplace product page**, following only valid, approved redirects. An official catalog landing page can stand in for a missing item-detail URL only when that page/linked evidence clearly identifies the **same product and normal/promo pair**.

Respect `robots.txt`, website terms, CAPTCHA, authentication, platform API limits, copyright and image hotlink rules. Never bypass restrictions, scrape accounts, rotate IPs to evade blocks, or require user login/private cart data. Playwright or OCR may help on **permitted** pages only.

## 3B. Online-commerce extraction playbook (per approved merchant/store)

1. **Start at the canonical public storefront:** inspect the merchant's own `/promotions`, `/offers`, `/sale`, `/deals`, weekly listing, official catalog link, or permitted store-specific marketplace deal category. Prefer a retailer-published public structured feed/API over HTML automation when the site's terms explicitly allow it.
2. **Find product-detail links:** use merchant-official category navigation, `Product`/`Offer` JSON-LD, accessible item cards and public pagination. Preserve the seller identifier/variant/market observed on each candidate page. Do not assume "Sale" categories contain real discounts.
3. **Extract prices from the same rendered product context:** distinguish `price` versus genuine `listPrice` / `strikethroughPrice` / original regular price as explicitly labeled by that seller. If only a `price` field is present, no discount is proved. If the page price differs from JSON-LD, quarantine and review; do not fabricate a baseline. Ignore cross-seller comparison rows and personalization.
4. **Use browser rendering only as permitted:** inspect public JS-rendered listings when static HTML lacks prices. Wait for the actual seller/variant/locale price to stabilize and capture source evidence. Never log in, use hidden cart APIs, automate purchases, bypass bot checks or scrape Google Shopping results without authorization.
5. **Confirm the public final item context:** variant, stock, currency and exact eligible area, with no mandatory voucher, card, points, new-account or membership gate. If one city/postcode has a distinct price, retain the candidate at that verified area; never extrapolate nationally. Apply location-aware compatibility gate.
6. **Get the individual product image:** follow official seller image/media references and check decode + exact item/variant match. A full flyer image is supporting evidence, **not** the product `image_url`. Use source-approved CDN hosts and preserve original unmodified URLs.
7. **Record one seller/page verdict:** `ACCEPTED`, `SKIPPED_NO_PROMO`, `SKIPPED_UNVERIFIED`, `SKIPPED_BLOCKED`, `SKIPPED_UNAVAILABLE`, or `NEEDS_CATALOG_APPROVAL`. Keep the evidence, compact context and move on. Set limits on item pages/pagination per storefront and report what was not inspected.
8. **Reconcile** only registered sellers against catalog v2 + feed v1 + index v2. No direct-to-`main` writes. Run the existing deterministic validator, expiry pruning, and browser regression tests.

For marketplace results, check **seller identity on the product-detail page** as well as the storefront; the same SKU sold by two unrelated merchants must be treated as two independent offers, not a two-price discount. Deduplicate one merchant/SKU observed through multiple discovery paths.

## Physical retail versus online fulfillment location policy

**Physical promotion:** verify actual participating area and item-level price. National, province, city, and local-store offers are legitimate; retain narrower candidates with explicit scope and follow the location-aware compatibility gate in `highlight-rules.md`.

**Online store:** countrywide fulfillment and same public price justify country-only scope; otherwise verify and record the actual eligible province/city/local pickup or delivery area. Do not infer national price from a country domain or one postcode. No login/private checkout capture.

Record actual market, canonical location identifiers and source-supported fulfillment area in audit; the future compatible feed must filter and label the eligible area using the user's selected location. Do not collect users' addresses.

## Catalog/receipt abbreviation normalization also applies to online commerce

Normalize merchant labels as instructed in `product-name-normalization.md` BEFORE deduplication and matching across official storefronts, marketplaces and physical flyers. Produce intermediate `productName`, `brand`, `variant`, `packageSize`, `packCount` separately; retain raw listing title and seller/SKU proof in audit. Preserve genuine trademarks/standard unit abbreviations and never merge distinct pack sizes or sellers. Only supported `product_name`, `brand`, `package_size` may enter current production highlights; other extraction keys are audit-only.

## 4. Offer qualification — all mandatory

- **Same listing, merchant and variant**: exact `product_name`, model/SKU, size/count, color/variant if price-relevant, condition and retailer/seller verified. Multiple sellers' prices are NOT normal/promo prices for one offer.
- **Same market and currency**: exact displayed normal price **strictly greater** than the advertised public promo price, not just Google Shopping "from" price, recommendation price, RRP/MSRP without genuine normal-price basis, coupon-only, cashback, loyalty/member subscription, first-purchase reward, coin redemption, flash price that cannot be verified, credit-card method, or conditional quantity discounts. If conditions are outside existing Pretio fields, **skip**.
- **Location eligibility**: verify public price/availability for its actual scope (country, province, city or local). Regional offers qualify for research and compatible location-aware display; do not broaden their scope. Shipping/tax differences must be documented; no unverified checkout total.
- **Evidence snapshot**: official seller/platform HTTPS URL, observed UTC time, merchant/store ID, exact pair of visible prices, currency, package/variant, market selection/locale, time period if published, separate image URL, screenshot/structured evidence and retrieval method. Record prices after dynamic rendering if prices were hidden before it; **do not infer from search snippets**.
- **Image**: real individual item photo of the matching product, decodable, with authorized source/CDN and usage. NO whole-catalog flyer image, unrelated product, placeholder, blocked media or guessed image.
- **Expiry**: source-backed `valid_from`/`valid_until` when available; missing optional dates can be omitted, but do not claim an undated historical price is currently on promotion. An offer known to be expired must not be published as active.
- **Deduplication**: stable per-seller/per-product identity; keep distinct sellers' genuinely independent offers separate (with separate approved catalog references). Do not duplicate the same merchant/SKU merely because it appeared in Google Shopping plus a retailer catalog.

When any mandatory proof is absent, mark the item `SKIPPED_UNVERIFIED` in **audit only**, then continue with the next item/shop. Meeting the "≥1 new product" target never ends the scan early.

## 5. Production mapping and gates — NO NEW JSON FIELDS

- Catalog Promo (v2): use only `id`, `merchant`, `publisher`, `title`, `summary`, `coverage_type`, `coverage_label`, `content_type`, `url`, `source_type`, `status`, `sort_order`, `locations`, and existing optional fields. `content_type=webview`, `coverage_type=national`, `source_type=official_digital_channel` or `official_retailer` **only when true**. New online stores require proof of ownership/store identity, geographic support, official domain/redirect and approved `allowed_hosts`. Prefer evergreen official store/catalog links; periodic links require sourced expiry.
- Highlights (country feed v1): only existing keys. `catalog_id` references **the exact approved seller/store catalog**; `retailer` identifies the genuine seller/store, `source_url` is its official permitted product/offer/catalog page, not a Google result or unrelated seller. The existing host relation validator requires `source_url` hostname to match the approved catalog host (or a subdomain): platform deep links are eligible only with compatible verified catalog registration. Missing optional keys are omitted; required image, price pair and URL are never invented.
- One country's feed may hold max **80** items, max **20 per retailer**. Preserve stable IDs/revisions; index v2 hash must match exact feed bytes. Run existing validator and Android/browser compatibility tests.
- If a valid shop is on an unapproved host or is a new unregistered seller, retain audit-only `NEEDS_CATALOG_APPROVAL`. For regional offers retain eligible area evidence as LOCATION_AWARE_PENDING until compatible rollout; do not weaken validators or invent production fields.

## 6. Suggested work-unit audit

For each researched shop/product page, use `../templates/ONLINE_SHOP_CHECKLIST.md`. Preserve separate evidence for `discovery_channel`, `platform`, `seller/storefront ID`, `seller URL`, `offer URL`, observed market, normal/promo price pair, photo, legality/robots, eligibility, rejection reason and relevant `catalog_id`. These are **audit metadata only**.

End-of-run reports distinguish:
1. **Registered catalog coverage**: `manifest_total`, terminal receipts, pending.
2. **Online discovery coverage**: markets queried, shops found, seller listings checked, new approved stores (after separate review), qualified but unpublished candidates, rejected/unavailable stores, blocked markets and source/pagination bounds.
3. **Published Product Highlights**: only approved, individually verified final items and expired removals.

A run may complete with zero new online offers; do not invent products or prolong a one-off request indefinitely.
