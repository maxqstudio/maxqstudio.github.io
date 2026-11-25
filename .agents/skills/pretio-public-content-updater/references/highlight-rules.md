# Product Highlights rules — discounted products only

**Files:** `pretio/promos/highlights/{CC.json,index.json,audit/**}`. The country feed and index retain their currently shipped schemas. Never introduce new field names in production data.

## Source landing-page fallback and missing optional data

`source_url` is **mandatory** but it does NOT have to be a dedicated product-detail landing page. If no product-specific page exists, use the approved official **catalog promo landing URL** from the matching retailer (`catalog_app.json` `url`) or an official accessible leaflet page linked from it. For example, a discounted item shown in Indomaret's official promo catalog may use Indomaret's official general promo page as `source_url` when no individual product URL is provided. **The specific product, price pair, package and market must be verifiably shown in that actual page/leaflet** during the run; a generic retailer home page without this evidence is insufficient. Store the factual URL, screenshot/HTML excerpt and timestamp in the separate run evidence, not in new production fields. If no official page contains the evidence, skip the item.

If an existing optional item field is absent/unverifiable (`brand`, `package_size`, `valid_from`, `valid_until`, `logo_url`, image/logo revisions), **omit that optional key**, not an empty string, guessed value or newly invented substitute field. The required `image_url`, actual normal/promo prices, `source_url` and other required fields remain mandatory: if no valid official image exists, skip the product. Do not skip an otherwise qualified product merely because it lacks a dedicated product URL or optional metadata.

## Online-store / marketplace Product Highlights

- **Include online merchants, official e-commerce shops and permitted marketplace listings.** Google Shopping can suggest possible discounts through authorized discovery, but a Google snippet/search result or comparison card does **not** establish `normal_price`, `promo_price`, an official merchant URL or country availability. Verify the pair on the **actual seller's** listing.
- Confirm the **same seller**, product SKU/model/size, public purchase channel and country. Never compare the regular price from one seller with the discounted price from another, or a membership/coupon/credit-card/first-purchase price with a public regular price. RRP/MSRP alone is not proof that the item previously sold for that normal price.
- `catalog_id` must refer to an **approved existing active** seller/store Catalog Promo entry, not a generic unrelated marketplace category. `retailer` must identify the actual seller/store, not merely the marketplace brand for third-party listings. `source_url` must be the approved merchant/marketplace official HTTPS page (or verified permanent seller catalog) that displays the matching price evidence, with the exact catalog-source host relationship enforced by the current validator.
- Source may be a permitted dynamic product page, official retailer API or structured `Product`/`Offer` data **if the evidence agrees with what the public customer actually sees**. Do not use seller-private APIs, cart data, Google Shopping values or inferred original prices.
- Product `image_url` must represent the individual matching item/variant and decode successfully; marketplace thumbnails and official merchant CDN assets are permitted when rights and host checks pass. **Do not use the entire flyer/page image** as an individual product photo.
- Confirm the price/availability is valid **countrywide**. An IP-localized, postcode-restricted, store pickup only, region-only or other conditional price is not eligible for current country-wide feeds. Do not infer worldwide shipping or convert currencies across markets.
- Newly discovered stores/marketplace sellers lacking an approved catalog ID remain **AUDIT_ONLY**, even if both prices are verified. New catalog registration and host additions need Owner review first. Store `platform`, `seller_id`, `discovery_source`, proof and approval decision in separate audit/checklist files; **NEVER** add these as production item fields.

See `online-shop-marketplace-rules.md` and `templates/ONLINE_SHOP_CHECKLIST.md`. Max 80 per country and 20 per retailer remain unchanged.

## Owner rule — location makes a highlight useful

**Physical retailer catalog:** Audit the exact promotion's eligible branches, province/city, validity and published participation rules. The item must have confirmed **country-wide** offer eligibility to enter the current country-level Product Highlights v1. A catalog tagged `national` is insufficient proof: a leaflet for Jabodetabek must never be represented as available across all Indonesia.

**Online store / marketplace:** No province/city match is necessary **if** the product variant, publicly visible deal price and seller's ordering/fulfillment channel are verified as usable for the **entire selected country**. Confirm seller shipping/checkout coverage and country-local currency; do not require every postal code to be individually queried if the seller has credible official nationwide terms. An online platform localized to one region, local-pickup-only item, or country-specific restricted listing still fails the national-product gate.

**Auditor requirement:** Record audit-only `source_kind=PHYSICAL_RETAIL|ONLINE_STORE`, `market_code`, `verified_area`, `fulfillment_evidence`, `location_decision` and the actual source URL. If a physical retailer is regional or an online seller cannot establish target-market eligibility, keep that candidate OUT of published feed. No `area`, `shipping` or `source_kind` field may be added to existing production items.

## Product identity cleanup before publishing

Every source product from a receipt-like catalog, leaflet, online store, or marketplace must be normalized using `product-name-normalization.md` before comparing prices/deduplicating or writing candidate highlights. Expand known Indonesian shorthand such as `MYK GRG`, `KCP MNS`, `PCH`, `BTL`, `KTG`, `SBN MND`, `DTRGN`; preserve `UHT`, `3in1`, `SPF` and standardized measurement units. Keep source raw text, exact SKU/variant, and extraction proof in separate audit.

The extractor must produce separate audit/working fields `productName`, `brand`, `variant`, `packageSize`, `packCount`. Map only the currently supported `product_name`, `brand`, `package_size` into the strict v1 feed. A variant or pack count that changes product identity must not be silently lost during mapping; use existing `product_name` / `package_size` when faithful or HOLD the candidate. No new production keys.

**Auditor** checks raw-to-normalized names, preserved identity, original-source price/variant/pack size equality, no artificial brands or sizes and strict allowed feed keys.

## Exact schema contracts

- Top-level country-feed keys **only**: `schema`, `schema_version`, `country`, `currency`, `revision`, `generated_at`, `items`. Values `pretio.product_highlights.v1`, `1`, ISO country, configured ISO currency, opaque revision, real UTC generated time.
- Highlight item **required**: `id`, `catalog_id`, `retailer`, `product_name`, `normal_price`, `promo_price`, `currency`, `image_url`, `source_url`, `observed_at`.
- Item **optional already supported**: `brand`, `package_size`, `valid_from`, `valid_until`, `logo_url`, `image_revision`, `logo_revision`. Fill when supported by evidence; don't add `discount_percent`, `savings`, `confidence`, `is_active`, `source_status`, `country_code`, `store_id` or any unrecognized field.
- Highlight index top-level keys **only**: `schema`, `schema_version`, `revision`, `countries`. Index v2 (`pretio.product_highlights.index.v2`, version `2`) country-entry keys **only**: `code`, `document_id`, `revision`, `sha256`, `url`. Never downgrade index to v1.
- Use the **existing** catalog ID as foreign key and exact canonical retailer URL host relationship required by Android. Allowed image hosts must be validated independently as official/authorized media sources.

## Eligibility: all conditions mandatory

1. **A genuine discount.** Both `normal_price` and `promo_price` are explicit retailer-provided prices for the SAME product, unit/size, store/market, channel and discount period. `promo_price < normal_price` (Decimal, never float). `normal_price` must NOT be inferred from a percent-off or a guessed previous price. No full-price products, membership-only prices presented as public, cashback, bundles without comparable unit definitions or items with incomplete evidence.
2. `product_name`, retailer and catalog ID identify the real offer; `package_size` and `brand` are included if explicitly verifiable.
3. Official HTTPS `source_url` with the real price pair, associated with the accepted catalog retailer. A search result, model output, retailer logo alone, or an aggregator does not qualify.
4. Real, decodable product `image_url`, same product/variant as evidence; version metadata only from verified content bytes/ETag. No fake placeholder, unrelated stock image, or HTML error.
5. Currency exactly matches `pretio/data/currency.json` for the country. Locale-aware input normalization to canonical decimal strings (e.g. `"1.39"`, `"13200"`). No float rounding. **A new-country feed cannot be published unless currency metadata exists and Android compatibility is reviewed.**
6. Location: verify scope actually covered by that item. A `national` catalog card does not prove its pricing is nationwide. If only one location/store is proven and the feed has no supported location scope field, REJECT from country-wide highlights.
7. Time: `observed_at` is the real UTC observation time. `valid_from`/`valid_until` are source-backed only. For offers with an explicit end date, retain it; do not drop a known end date.
8. Deduplicate stable IDs; 80 accepted items max per country and 20 per retailer; no duplicates across catalog entries within the same country.

## Exhaustive catalog scan versus growth target

Every 12-hour cycle must try every `(country_code, catalog_id)` from the complete catalog manifest, **including countries without any existing highlights or recognized currency**. Reaching the one-product target is not a stop condition. A catalog with no eligible offer, no update, missing proof, or fetch failure is recorded as a terminal **skip**, and scanning continues through all remaining catalogs. Currency gaps prevent highlight publication for that market, not catalog source checking. A finished cycle requires one terminal receipt per manifest entry and `pending == 0`; interrupted cycles are `INCOMPLETE`.

## 12-hour coverage target

For each country, after checking **all applicable catalogs**, aim to add at least **one NEW, unique, verifiably discounted product per run** (two cycles/day). This is an objective, not an artificial minimum. If 0 qualify, report `TARGET_MISSED` with explicit reasons and retain or prune existing items according to evidence. Never publish synthetic discounts to meet a quota.

### Expired deletion and failed fetch distinction

- Remove an item from the **country feed** if `valid_until` < source-market current calendar day (inclusive validity on the end date), or official retailer evidence confirms the promotion has ended. Remove as part of the validated next candidate release; recompute exact index SHA-256.
- Do NOT delete only because the fetch failed, a site blocked the bot, or a 12-hour window elapsed. Such an item is `STALE_UNVERIFIED`; keep audit evidence and do not represent it as a confirmed current discount. Priority recheck next cycle. If it has explicit `valid_until`, delete on proven calendar expiry regardless of fetch errors.
- If all old items are expired, an empty feed is valid after deterministic expiry pruning; **do not confuse this with a failed empty crawl**. Record `EXPIRED` counts. An empty feed after no verified promotions also requires a complete successful source check.
- For undated items, stale `observed_at` is not itself expiry proof: stop claiming freshness, prioritize re-verification, seek official validity, and request policy review if sources remain inaccessible.
- No deleting data merely because an LLM failed; no changing observed dates when price cannot be re-confirmed.

## Safe output and index integrity

- Keep each unchanged feed byte-for-byte; a changed feed gets a new truthful `revision` and `generated_at`.
- Use atomic stage+validation of feed and index. Index SHA-256 is the lowercase digest of **exact feed bytes** published, not reserialized JSON in a different format.
- Never publish an index whose country entry points to missing/old bytes, wrong `revision`, incompatible `document_id`, or HTTP content type mismatch.
- Record sourcing, rejected candidates, expired removals, counts and checkpoints in per-run **audit artifacts** (not extra feed fields).
- The Android reader currently accepts country feed v1 and index v2; test both before publishing.
