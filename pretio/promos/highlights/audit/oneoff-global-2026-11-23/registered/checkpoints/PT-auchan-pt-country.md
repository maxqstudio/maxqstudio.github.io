# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PT:auchan-pt-country` | manifest position: **53/74** | attempt: **1**  
Country: **PT** | retailer: **Auchan** | mode: **AUDIT**  
Registered URL: <https://www.auchan.pt/pt/folhetos/>  
Checkpoint time: **2026-11-23T10:11:28Z** (UTC; web connector did not retain request-level timestamps)  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded the frozen manifest and current catalog record `auchan-pt-country`, publisher `Auchan Retail Portugal`, `official_retailer`, `coverage_type: national`, country `PT`, `valid_until: null`, existing `last_verified_at: 2026-09-28T00:00:00Z`.
- [x] Requested the exact registered URL. The official page returned under the same URL with title “Folhetos Auchan - As melhores Promoções.” It exposes a stable `/pt/folhetos/` directory with multiple dated offers; no changed URL or migration was proposed.
- [x] Checked official robots rules at <https://www.auchan.pt/robots.txt>. `User-Agent: *` disallows certain query filters, account, checkout and other paths; it does **not** disallow the registered landing page, weekly promo product-list URL, or observed product-detail URL. No access-control bypass, login or private endpoint was used.
- [x] Verified official retailer context on the Auchan Portugal domain. The official terms page at <https://www.auchan.pt/pt/termos-condicoes/termos-e-condicoes.html> covers customer-account and promotion conditions but contains no general crawler/content-reuse permission or prohibition. Permission for commercial reuse is therefore **unverified**, not claimed as granted.
- [x] The official landing page listed current promotional periods as of 23 Nov 2026, including Tecno Black Friday 23–30 Nov and Folheto Semanal 19–25 Nov. Other listed campaigns and their dates are recorded in the source-evidence artifact.
- [x] Found a mismatch in one subordinate link: the visible weekly “Ver Folheto” viewer URL carries UTM text for 12–18 Nov, while the landing page and adjacent product-list/detail pages state 19–25 Nov. The registered evergreen landing page itself displays current campaigns; the viewer PDF contents were not relied on.
- [x] The catalog record labels offers location-selected. The product listing warns that available products/prices can change with delivery location, and the inspected page said the unspecified postcode was outside its delivery area. No national item-level geography was established.
- [x] The source page remains a useful current evergreen directory; no period-specific catalog record was proven expired. No URL, `valid_until`, host allowlist, `last_verified_at`, or other production field was changed.

## 2. Product Highlights — price and discount review

- [x] Inspected the visible first page of the official weekly product listing; 24 cards were visible before “Ver mais produtos.” No pagination, search API, cart, account or hidden data was accessed.
- [x] One item has an explicit same-listing normal-to-promo price pair: Rana Ravioli with white truffle and cheese, 250 g, EAN `8001665700900`, **€4.19 → €3.14**, with validity **19–25 Nov 2026**. Exact product page: <https://www.auchan.pt/pt/produtos-frescos/gastronomia/massas-frescas/ravioli-de-trufa-branca-e-queijo-rana-250g/1146844.html>.
- [x] The same product page has an individual-image alt label matching the product, but fetching the image asset timed out, so image decoding was not verified.
- [x] The other 23 visible cards expose a current price plus either a “Promoção” label or a `PVP Recomendado`/PVPR amount. A recommended price is not verified Auchan regular-price history; none was used as `normal_price`. Full card observations and rejection reasons are in `registered/evidence/PT-auchan-pt-country.md`.
- [x] **Accepted Product Highlights: 0.** The single explicit price pair remains audit-only because PT has no currency/feed/index support in this baseline, price/availability may vary by delivery location, nationwide applicability is unverified, and the product image did not decode. The other 23 lack a valid normal-price pair. No product was inserted into a feed.
- [x] No existing highlight references `auchan-pt-country`; no product expiry or deletion is associated with this source.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — current official catalog content and one explicit discount pair were observed, but commercial reuse permission was not explicit, product area/pricing is location-sensitive without a selected area, PT lacks highlight currency/feed support, and the product image decode was unavailable.
- [x] Keep the active Catalog Promo record. The evergreen directory shows current campaigns; the old `last_verified_at` alone is not used as expiry evidence.
- [x] No expired item deletion, catalog removal, URL migration, production JSON edit or schema change.

## Compact handoff (≤400 words)

`PT:auchan-pt-country`, position 53/74, terminal `SKIPPED_UNVERIFIED`; run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`. The official registered page `https://www.auchan.pt/pt/folhetos/` is an evergreen listing, allowed by the site's robots rules, and displays current campaign periods (including 19–25 Nov). A weekly flyer viewer link carries an older 12–18 Nov UTM label, but the adjacent products listing and product detail show 19–25 Nov. Official account terms did not establish commercial content-reuse permission. The listing warns that products/prices vary with delivery location; no postcode was selected and the displayed page reported the unspecified postcode outside its delivery area. One explicit pair was observed for Rana Ravioli 250 g, €4.19 to €3.14, 19–25 Nov, but the image asset timed out, PT lacks supported currency/feed/index, and nationwide applicability is unverified. The other 23 visible cards had only promo labels or recommended-price references, not verified normal prices. No product highlight or production change; no expiry inferred. See `registered/evidence/PT-auchan-pt-country.md`. Next manifest source: `PT:continente-pt-country` (54/74), in a fresh isolated context.
