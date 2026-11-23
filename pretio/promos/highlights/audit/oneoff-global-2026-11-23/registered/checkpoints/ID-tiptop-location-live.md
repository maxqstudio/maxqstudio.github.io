# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `ID:tiptop-location-live` | manifest position: **35/74** | attempt: **1**  
Country: **ID** | retailer: **TIP TOP** | mode: **AUDIT**  
Checked UTC: **2026-11-23T09:40:47Z**  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded exact frozen manifest and production entry: `tiptop-location-live`, TIP TOP, Indonesia, official retailer, existing URL `https://www.tiptop.co.id/promo-products/katalog`, `valid_until: null`, active; current `last_verified_at` was left unchanged.
- [x] Exact registered URL returned HTTP 200 on the official TIP TOP domain. The page title is “Promo Katalog”.
- [x] Robots checked once: `https://www.tiptop.co.id/robots.txt` returned HTTP 200 with `User-agent: *` and blank `Disallow:`; the URL path is not disallowed.
- [x] Checked linked official terms page `https://www.tiptop.co.id/terms-conditions`; visible content contains store/consumer rules, with no web-crawling or commercial reuse restriction found. This is not an explicit permission grant.
- [x] Evergreen-first check: `/promo-products/katalog` is a stable-looking parent page and links the current dated catalog PDF. Current issue is **16–30 November 2026**. The official PDF link and source facts are captured in `registered/evidence/ID-tiptop-location-live.md`.
- [ ] A single page observation does not establish historical update-in-place behavior. The 29-page PDF exposed no text in the available browser reader; no PDF contents were inferred.
- [x] Scope is not proven national at item level. The production location record lists provinces 31 (DKI Jakarta), 32 (Jawa Barat), and 36 (Banten); do not treat it as nationwide just because legacy coverage label says “Nasional”.
- [x] No URL/domain/allowlist or production source verification timestamp was changed.

## 2. Product Highlights

- [x] IDR is supported. Existing ID feed contains 4 items and 0 references to this catalog ID.
- [x] The official page visibly listed 4 promo cards: selected Molto/Rinso/Wipol products at “Diskon 15%”; Karaboga wheat flour 1 kg at Rp 9.475/bag; Greenfields Low Fat milk 950 ml at Rp 31.175/carton; Milkow Actigrow 1+ honey 900 g at Rp 63.975/jar.
- [ ] None displayed a source-backed normal/reference price. No normal→promo pair was inferred; 0 items qualify for Product Highlights.
- [ ] Individual linked image URLs were not decoded/validated. The dated PDF could not be inspected as text by the available browser reader.
- [ ] Product-level applicable stores/areas and nationwide applicability were not proven. Regional observations remain audit-only.
- [x] No product or catalog was removed as expired/obsolete; the current flyer ends 30 Nov, after the run date. No orphan reference was introduced.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — current official evergreen-looking catalog parent and a dated current flyer are visible, but there is no same-item normal/promo price pair, product image validation, or item-level nationwide geography.
- [x] Four promo-only cards are documented as observations, not accepted product candidates. No product IDs accepted; no expired product IDs deleted; no catalog URL migration; no production JSON changes.

Evidence: `registered/evidence/ID-tiptop-location-live.md`  
Compact handoff: `registered/handoffs/ID-tiptop-location-live.md`  
Next manifest input: `ID:transmart-location-live`.
