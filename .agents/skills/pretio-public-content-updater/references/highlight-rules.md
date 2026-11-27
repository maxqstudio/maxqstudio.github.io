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
- Confirm price and availability for the actual eligible area, whether countrywide, provincial, city-specific or local pickup. Verify location evidence for the exact price; apply the compatibility gate for regional data.
- Newly discovered stores/marketplace sellers lacking an approved catalog ID remain **AUDIT_ONLY**, even if both prices are verified. New catalog registration and host additions need Owner review first. Store `platform`, `seller_id`, `discovery_source`, proof and approval decision in separate audit/checklist files; **NEVER** add these as production item fields.

See `online-shop-marketplace-rules.md` and `templates/ONLINE_SHOP_CHECKLIST.md`. Max 80 per country and 20 per retailer remain unchanged.

## Owner rule — location makes a highlight useful

## Owner correction — location-aware offers (27 November 2026)

**Nationwide coverage is NOT required.** A verified regional, province, city, or local-store promotion is legitimate. Record its exact eligible location(s), public price pair for that same area/channel, and official evidence. Do not extrapolate a location-selected price to the whole country. Genuine countrywide online/physical offers use country scope only.

- Research and retain regional candidates with canonical country/province/city codes and names from the existing location directory; record eligible branches/fulfillment restrictions and evidence in audit. Do not invent codes, widen an area, or assume all stores participate.
- **User-facing requirement:** filter by the location explicitly selected by the user; show a clear eligible-area label. Country selection shows countrywide offers; province selection additionally shows matching province offers; city selection additionally shows matching city offers. Unknown/invalid scope, unavailable required location, or nonmatching area fails closed. Never fall back to unrelated local prices. No GPS/address collection requirement.
- A regional promotion is NOT expired, obsolete, or invalid solely because of its geographic restriction. Preserve source evidence and regional candidates; do not delete an existing item solely for being regional. If its old countrywide presentation is misleading, flag for reviewed quarantine/migration rather than treating it as expiry or discarding evidence. Independently proven expiry, false price pairs, or source-rights violations remain separate correction grounds.
- **Compatibility gate:** current production Product Highlights v1 has no item-level locations; do not add unsupported fields or publish regional data to legacy clients as countrywide. Retain such candidates as LOCATION_AWARE_PENDING (audit-only, not a new terminal receipt enum) until the separately versioned location-aware feed, validator, Android reader/filter, visible labels and legacy-safe rollout are implemented and accepted. Catalog Promo v2 already supports explicit country/province/city location rules; use these as the geographical reference. Implementation: https://github.com/maxqstudio/pretio/issues/111. No production schema change in this skill-only revision.
- Regional scope alone is never a reason to skip discovery/extraction where access is permitted; if the precise scope cannot be established/represented, record the blocker, preserve evidence and continue. All access/rights, genuine price, image, expiry, currency, identity, and other acceptance requirements remain unchanged.

**Physical retailer catalog:** verify participating branches and exact offer geography. Regional scope is eligible; a national Catalog Promo link does not prove national product prices.

**Online store / marketplace:** verify actual order/fulfillment area and local currency; countrywide proof is sufficient for country-only scope, otherwise record the narrower verified locations. Regional offers are not disqualified.

**Auditor requirement:** retain `source_kind`, `market_code`, canonical eligible location rules, `verified_area`, `fulfillment_evidence`, `location_decision` and actual source URL in audit. Publish only using a compatible accepted schema; preserve regional candidates until rollout.

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
6. Location: verify the exact eligible area and price scope, not necessarily nationwide. Apply the Owner correction and compatibility gate above; do not widen a city/store offer to country scope.
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
