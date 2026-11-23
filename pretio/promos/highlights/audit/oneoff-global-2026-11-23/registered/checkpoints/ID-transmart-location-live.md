# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `ID:transmart-location-live` | manifest position: **36/74** | attempt: **1**  
Country: **ID** | retailer: **Transmart** | mode: **AUDIT**  
Checked: **2026-11-23**; exact HTTP request timestamps were not returned by the source tooling; checkpoint recorded by **2026-11-23T09:39:36Z**.  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded frozen-manifest entry and active catalog record: `transmart-location-live`, Indonesia, registered URL `https://transmart.co.id/katalog`, `official_retailer`, `coverage_type: national`, `valid_until: null`, last verified `2026-08-22T01:00:00+08:00`.
- [x] Robots checked first at `https://transmart.co.id/robots.txt`: HTTP 200, body `User-agent: *` with an empty `Disallow:` value; the registered path is not disallowed.
- [x] Official home page `https://transmart.co.id/` returned HTTP 200 and identified as “Transmart - Temukan kebutuhan sehari-hari Anda di Transmart.co.id!”; no terms/privacy/syarat link was present in the retained static HTML.
- [x] Registered catalog URL returned HTTP 200, title `Transmart - Katalog`, canonical URL `https://transmart.co.id/katalog` (same as the registered URL). The response included generic catalog-page markers but exposed no verifiable item-level current offer, date, or price pair in the retained static content.
- [x] A bounded search for official terms/catalog references did not locate an official terms page. Access permission is therefore **unverified**, not confirmed prohibited. No separate reuse permission was found.
- [ ] Update-in-place history and current catalog validity were not established. Treat the canonical path as stable in form only; do not classify the catalog as verified evergreen/current. No dated successor or official parent index was verified.
- [x] Existing record lists 18 province locations while labeling coverage national. The catalog response did not establish item-level/nationwide geography; flag location-scope review, but do not change the catalog without evidence/review.
- [x] No product price, image, or offer content was copied into audit evidence because current offer and permission evidence were insufficient.

## 2. Product Highlights and dependency review

- [x] IDR is supported; the existing Indonesia feed has 4 items.
- [x] No active ID highlight references `transmart-location-live` (0 dependencies observed).
- [x] No product candidate was inspected/accepted; no valid price pair, image, offer period, or item-level geography was verified.
- [x] No expired product or catalog period was proven. No production records were deleted or changed; no orphan risk created.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — robots permits access and official pages respond, but current item-level promotional content/freshness and terms permission were not verified. The response does not substantiate a current discount or nationwide product applicability.
- [x] Keep the existing Catalog Promo active and unchanged; a null `valid_until`, old `last_verified_at`, or missing page content is not expiry/obsolescence proof.
- [x] No production catalog/feed/index, schema, location or currency file changed.

## Compact handoff (≤400 words)

Work unit `ID:transmart-location-live`, position 36/74; terminal receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`. The registered URL `https://transmart.co.id/katalog` returned HTTP 200 with canonical URL unchanged and title “Transmart - Katalog.” `robots.txt` returned HTTP 200 with `User-agent: *` and empty `Disallow:`, so the registered path is not disallowed. The official homepage also returned HTTP 200. Neither retained HTML nor bounded official search revealed a terms/privacy page; reuse permission remains unverified. The catalog response contained generic page markers but no verifiable current item-level promotion, price pair, date, or geography. The record lists 18 province locations under national coverage; the source page did not resolve whether offers are national, so flag scope review. IDR is supported and the ID feed has 4 items, none referencing this catalog. No candidate, expiry deletion, catalog migration, or production JSON change is supported. Do not infer expiry/obsolescence. Next manifest item after this source is `IQ:taawon-iq-weekly-offers`.
