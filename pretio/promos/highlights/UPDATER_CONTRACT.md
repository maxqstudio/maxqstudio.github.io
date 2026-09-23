# Pretio Product Highlights Updater Contract

This document is the handoff contract for the external daily catalog updater. Android remains a deterministic JSON/image consumer; it does not crawl retailer websites and contains no autonomous GPT worker.

## Write Boundary

The updater's only writable path is:

```text
pretio/promos/highlights/**
```

This includes `audit/**`. It must not edit `pretio/promos/catalog_app.json`, `pretio/promos/location.json`, `pretio/data/currency.json`, `pretio/localization/**`, legal pages, or application source. Catalog maintenance remains a separately governed workflow.

## Feed Contract

The index schema is `pretio.product_highlights.index.v1`; country feeds use `pretio.product_highlights.v1`; each has `schema_version: 1`. Country files are named `ID.json`, `CL.json`, `RS.json`, `US.json`, `ZA.json`, `DE.json`, and `CH.json`. The index binds each supported country to the canonical HTTPS URL, exact feed SHA-256, and feed revision. Each country feed declares country, currency, revision, UTC `generated_at`, and an `items` array (maximum 80 items; maximum 20 accepted items per retailer).

Every production item requires source evidence for retailer, product identity, normal/reference price, lower promo price, currency, official source URL, and a decodable product image. Preserve optional brand, package size, validity dates, and image metadata when verified. Store prices as canonical decimal strings, never floating point or localized display text. Do not infer normal prices from a percentage discount. Promo-only items are ineligible. `discount_percent` is not a price authority.

Optional `image_revision` and `logo_revision` are opaque tokens. Prefer SHA-256 of the fetched and validated bytes. A stable source asset version or reliable ETag may be used when the bytes cannot be measured. If there is no reliable version evidence, omit the field; do not invent a date or revision.

## Anti-Fabrication and Failure

Do not fabricate products, prices, source URLs, images, package sizes, or validity dates. Do not substitute an aggregator when an official source is blocked. Do not erase yesterday's valid feed because today's retailer fetch failed. Keep current valid feed bytes on `SOURCE_BLOCKED`, `EXTRACTION_FAILED`, or `FETCH_FAILED`; record the failure in audit evidence instead.

Useful audit states include `FETCH_OK`, `NO_CHANGE`, `NO_PROMO_FOUND`, `SOURCE_BLOCKED`, `EXTRACTION_FAILED`, `INVALID_PRICE`, and `EXPIRED`. If no items meet every eligibility rule, the feed may be empty only after a successful complete source check, not as a network-failure fallback.

## Image Metadata and App Cache

Try to record `image_url`, `image_revision`, `logo_url`, and `logo_revision` when reliably available. A new image revision must be emitted when source bytes change at the same URL. No artificial daily URL query parameter is allowed.

The app shares memory and persistent disk cache across product images, store logos, catalog thumbnails, and promo images. Current defaults: product/promo soft revalidation 24 hours and disk retention 60 days; store/catalog soft revalidation 7 days and disk retention 180 days; one 225 MiB / 300-object global LRU budget. The next 1–2 cards may be prefetched, not the entire feed.

`JSON REFRESH != IMAGE CACHE PURGE`. An unchanged URL and revision must not cause a full image download. `TTL DOES NOT OVERRIDE A NEW IMAGE REVISION`: a changed revision triggers immediate fetch before TTL. Without revision, the app uses ETag and/or Last-Modified conditional revalidation after soft TTL. It validates MIME and image decoding before atomically switching the cache pointer; failure retains the previous valid image. A bad image or HTML error page is never cached as an image.

## Daily Run

1. Read the accepted catalog and inspect active official sources.
2. Collect evidence and normalize decimal prices with source-locale rules.
3. Reject any candidate missing proof, a verified normal price, a lower promo price, or a valid image.
4. Deduplicate IDs and enforce per-retailer and per-country limits.
5. Validate feed schema and all URLs, currency, dates, prices, item counts, image metadata, and exact index hash.
6. Write only changed country feed/index/audit files within the allowed subtree.
7. Keep production `items` empty when no verified product qualifies. Never use test fixtures in production feeds.
