# Product Highlights rules — discounted products only

**Files:** `pretio/promos/highlights/{CC.json,index.json,audit/**}`. The country feed and index retain their currently shipped schemas. Never introduce new field names in production data.

## Source landing-page fallback and missing optional data

`source_url` is **mandatory** but it does NOT have to be a dedicated product-detail landing page. If no product-specific page exists, use the approved official **catalog promo landing URL** from the matching retailer (`catalog_app.json` `url`) or an official accessible leaflet page linked from it. For example, a discounted item shown in Indomaret's official promo catalog may use Indomaret's official general promo page as `source_url` when no individual product URL is provided. **The specific product, price pair, package and market must be verifiably shown in that actual page/leaflet** during the run; a generic retailer home page without this evidence is insufficient. Store the factual URL, screenshot/HTML excerpt and timestamp in the separate run evidence, not in new production fields. If no official page contains the evidence, skip the item.

If an existing optional item field is absent/unverifiable (`brand`, `package_size`, `valid_from`, `valid_until`, `logo_url`, image/logo revisions), **omit that optional key**, not an empty string, guessed value or newly invented substitute field. The required `image_url`, actual normal/promo prices, `source_url` and other required fields remain mandatory: if no valid official image exists, skip the product. Do not skip an otherwise qualified product merely because it lacks a dedicated product URL or optional metadata.

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
