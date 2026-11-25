# Pretio Product Highlights Updater Contract

This document is the handoff contract for the external 12-hour highlights updater. Android remains a deterministic JSON/image consumer; it does not crawl retailer websites and contains no autonomous GPT worker.

## Write Boundary

The updater's only writable path is:

```text
pretio/promos/highlights/**
```

This includes `audit/**`. It must not edit `pretio/promos/catalog_app.json`, `pretio/promos/location.json`, `pretio/data/currency.json`, `pretio/localization/**`, legal pages, or application source. Catalog maintenance remains a separately governed workflow.

## Product name cleanup and audit-only structured extraction

The crawler MUST expand known catalog/receipt shorthand before writing new Product Highlights; examples: `MYK GRG`→`Minyak Goreng`, `KCP MNS`→`Kecap Manis`, `PCH`→`Pouch`, `BTL`→`Botol`, `KTG`→`Kaleng`, `SBN MND`→`Sabun Mandi`, `DTRGN`→`Deterjen`. Preserve `UHT`, `3in1`, `SPF` and standard units `ml`, `g`, `kg`, `L`, `pcs`. Normalize unit spacing and brand title case without changing SKU identity.

Each candidate must supply separate **intermediate/audit** `productName`, `brand`, `variant`, `packageSize`, `packCount`, with original source title and evidence. Existing production feed v1 recognizes **only** `product_name`, `brand`, `package_size` for these values; `variant`, `packCount` and raw/camelCase keys must NOT be written as new production JSON fields. Preserve distinct important variants in existing supported names or HOLD if exact identity cannot be safely represented. See the canonical skill `references/product-name-normalization.md` for examples and auditor gating. This improves local Watchlist/Saved Products matching without requiring a network AI operation.

## Feed Contract

The current index schema is **`pretio.product_highlights.index.v2` with `schema_version: 2`**, while country feeds use **`pretio.product_highlights.v1` with `schema_version: 1`**. Current country files are `ID.json`, `CL.json`, `RS.json`, `US.json`, `ZA.json`, `DE.json`, and `CH.json`; additional countries require approved currency metadata and Android compatibility. The v2 index country entries include `code`, `document_id`, `revision`, `sha256`, and `url`. The index binds each supported country to the canonical HTTPS URL, exact feed SHA-256, and feed revision. Each country feed declares country, currency, revision, UTC `generated_at`, and an `items` array (maximum 80 items; maximum 20 accepted items per retailer).

Every production item requires source evidence for retailer, product identity, normal/reference price, lower promo price, currency, official source URL, and a decodable product image. Preserve optional brand, package size, validity dates, and image metadata when verified. Store prices as canonical decimal strings, never floating point or localized display text. Do not infer normal prices from a percentage discount. Promo-only items are ineligible. `discount_percent` is not a price authority.

Optional `image_revision` and `logo_revision` are opaque tokens. Prefer SHA-256 of the fetched and validated bytes. A stable source asset version or reliable ETag may be used when the bytes cannot be measured. If there is no reliable version evidence, omit the field; do not invent a date or revision.

## Anti-Fabrication and Failure

Do not fabricate products, prices, source URLs, images, package sizes, or validity dates. Do not substitute an aggregator when an official source is blocked. Do not erase yesterday's valid feed because today's retailer fetch failed. Keep current valid feed bytes on `SOURCE_BLOCKED`, `EXTRACTION_FAILED`, or `FETCH_FAILED`; record the failure in audit evidence instead.

Useful audit states include `FETCH_OK`, `NO_CHANGE`, `NO_PROMO_FOUND`, `SOURCE_BLOCKED`, `EXTRACTION_FAILED`, `INVALID_PRICE`, and `EXPIRED`. If no items meet every eligibility rule, the feed may be empty only after a successful complete source check, not as a network-failure fallback.

## Image Metadata and App Cache

Try to record `image_url`, `image_revision`, `logo_url`, and `logo_revision` when reliably available. A new image revision must be emitted when source bytes change at the same URL. No artificial daily URL query parameter is allowed.

The app shares memory and persistent disk cache across product images, store logos, catalog thumbnails, and promo images. Current defaults: product/promo soft revalidation 24 hours and disk retention 60 days; store/catalog soft revalidation 7 days and disk retention 180 days; one 225 MiB / 300-object global LRU budget. The next 1–2 cards may be prefetched, not the entire feed.

`JSON REFRESH != IMAGE CACHE PURGE`. An unchanged URL and revision must not cause a full image download. `TTL DOES NOT OVERRIDE A NEW IMAGE REVISION`: a changed revision triggers immediate fetch before TTL. Without revision, the app uses ETag and/or Last-Modified conditional revalidation after soft TTL. It validates MIME and image decoding before atomically switching the cache pointer; failure retains the previous valid image. A bad image or HTML error page is never cached as an image.

## Mandatory confirmed-expiry / obsolete-source deletion

Every authorized staged release must **delete all provably expired items from active Product Highlights country feeds** and **retire or replace every proven-obsolete promotional Catalog Promo entry**. `valid_until < today` in the relevant market proves an item's expiry when date is source-backed. Catalog Promo period-specific URLs that have ended must be replaced with a verified official evergreen/current source (preserving `catalog_id` where appropriate) or removed from the live `items` list once all dependent highlights are resolved.

**Atomic integrity rule:** Removing a Catalog Promo entry must not strand any `CC.json.items[].catalog_id`. Delete proven-expired linked products, migrate independently verified current products only with an approved successor, or HOLD the pending removal for review. Update the exact SHA-256 hashes and revisions of changed country feeds and index. No old catalog/archive record should be kept in the active production list just for history.

Do **not** mass-delete due to a lone 404, timeouts, CAPTCHA, stale `last_verified_at` or lack of observed discounts. These are `STALE_UNVERIFIED` and require evidence. Keep bounded deletion receipts in audit files and report removed product IDs, removed/relinked catalog IDs, evidence and blockers to Owner.

## Owner location and expiry policy

- **Physical store offers** require a proven eligible geographic area. Do not publish a regional leaflet's item as country-wide merely because the Catalog Promo URL is labeled national.
- **Online store offers** need a source-backed public price and ability to order/fulfill in the selected country; when country-wide available, **no province/city check is required**. If geographically restricted, do not treat as national.
- **Known-expired Product Highlights MUST be deleted from active country feeds** as part of staged release, with atomic feed/index SHA update. Known-expired rotating catalogs must be replaced with verified current/evergreen URL or safely retired under catalog-owner approval, without leaving expired content in active lists. Do not pile expired products in production. An inaccessible source or undated item alone is not expiry proof.
- **Regular-price products** may be collected as audit-only but may not be smuggled into discount-only country feed v1 using equal/guessed prices.

## Online shop / marketplace compatibility (no new fields)

The existing updater skill additionally researches official **online stores, direct-to-consumer shops, and verified marketplace seller storefronts**. Google Shopping may be used for candidate discovery through permitted methods, **but neither its snippet nor its pricing is a qualifying source**. For each accepted offer, verify the same merchant/seller, exact product variant, real normal price and lower public promo price, authorized individual image, country-wide eligibility, and source-backed expiry on the actual seller's official listing.

The `catalog_id` must already reference an approved active Catalog Promo store/source with matching official HTTPS host, using the unchanged `official_digital_channel` or `official_retailer` source type. An unregistered seller/platform/store or unapproved host requires separate Owner review and remains **audit-only** until approved. `seller_id`, `platform`, `discovery_source`, `coupon` and any other new fields are forbidden in production catalog/feed/index. Bounded online-store discovery is accounted **separately** from the frozen registered-catalog manifest; manifest receipts alone are not evidence of an internet-wide shop crawl.

An explicit ONE_OFF run remains exactly once for the selected countries; **no scheduler is installed or enabled** by these skill rules.

## Explicit one-off Owner requests (highest priority)

When Owner explicitly requests `kerjakan 1 kali saja untuk Indonesia`, the updater must **run exactly one Indonesia-only cycle**, check every Indonesia catalog, collect and stage valid discounted products, skip inaccessible/unchanged catalogs, prune only supported Indonesia expiries, then STOP. Do not enumerate/fetch/process other countries, create or enable a schedule, repeat the operation or mutate other-country feeds. The shared catalog directory may only change existing Indonesia entries. Global 12-hour exhaustive rules below apply to recurring runs and must **not** override an explicit narrower one-off command. Run manifest CLI: `python3 tooling/pretio_public_content/manifest.py --once --country ID`.

## Complete per-catalog coverage / skip semantics

Each 12-hour run snapshots all unique `(country_code, catalog_id)` pairs from every active Catalog Promo entry in all countries. Every catalog MUST be attempted and receive a completed checklist and compact handoff, even if the retailer has no updates or is inaccessible. When there are no qualifying discounts, source access fails, or country currency is unsupported, mark that catalog as skipped in the run checkpoint/audit **and continue with the next catalog**. Do NOT stop after finding the first new discounted product, after meeting any per-country quota, or after failing one source. Only finish once every catalog in the frozen manifest has a terminal receipt (including skipped/failed) and `pending=0`, then reconcile all valid updates and expiry deletions as a consistent batch. Do not endlessly poll after finishing. A canceled or timed-out run is `INCOMPLETE` and must resume outstanding units. These status/checkpoint fields are NOT to be added to production catalog or highlights JSON.

## Every 12-hour cycle

1. Read the accepted catalog and inspect active official sources.
2. Collect evidence and normalize decimal prices with source-locale rules.
3. Reject any candidate missing proof, a verified normal price, a lower promo price, or a valid image.
4. Deduplicate IDs and enforce per-retailer and per-country limits.
5. Validate feed schema and all URLs, currency, dates, prices, item counts, image metadata, and exact index hash.
6. Write only changed country feed/index/audit files within the allowed subtree.
7. **Only discounted products are eligible:** source-verified `promo_price < normal_price` for the same product, package, store and time. Product and feed fields MUST be exactly the existing app-recognized keys; never add `discount_percent`, `confidence` or invented metadata. See `.agents/skills/pretio-public-content-updater/references/highlight-rules.md`.
8. Check every catalog in every eligible country using its own checklist; write a compact handoff after each and process the next catalog in a new isolated context. See `.agents/skills/pretio-public-content-updater/templates/`.
9. Aim for **at least one NEW verified discounted product per country per 12-hour cycle**. If the target cannot be met, record `TARGET_MISSED` with evidence. NEVER fabricate products or prices to satisfy the target.
10. **Delete items whose verified `valid_until` date is before the market's current date**, or whose offer ending is positively established. Do this even if an unrelated source fetch fails; recompute index hashes. Do not delete undated or inaccessible items merely due to a fetch failure; treat them as stale, not confirmed current.
11. Keep production `items` empty when no verified product qualifies after complete success or deterministic expiry pruning. Never use test fixtures in production feeds.

## Separate Catalog Promo Updater (explicitly distinct writer)

The legacy `highlights/**` writer MUST NOT modify `catalog_app.json`. A separate catalog-maintenance agent may write `pretio/promos/catalog_app.json` under the skill's catalog rules and its own permission boundary. Prefer official **evergreen** catalog landing URLs that update their content in place. If a catalog link rotates by promotion period, a real source-supported `valid_until` is mandatory; no guessing. Catalog data retains `pretio.catalog_app.v2` and its existing field set only. Both workstreams reconcile against the **same final snapshot** before publication.
