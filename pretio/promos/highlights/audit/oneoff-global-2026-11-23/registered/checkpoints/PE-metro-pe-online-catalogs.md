# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PE:metro-pe-online-catalogs` | manifest position: **46/74** | attempt: **1**  
Country: **PE** | retailer: **Metro** | mode: **AUDIT**  
Official URL: <https://www.metro.pe/catalogos>  
Checkpoint recorded: **2026-11-23T09:59:10Z**; exact page-request timestamps were not retained by the connectors.  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded frozen-manifest/catalog record: `metro-pe-online-catalogs`; Metro / Cencosud Retail Perú S.A.; active; national Peru label; stable URL; `valid_until: null`; existing `last_verified_at: 2026-10-24T19:59:47+08:00`.
- [x] The official registered route returned HTTP 200 and is self-canonical at the same URL. Page title: `Catálogo de Ofertas`. Metadata identifies Metro.pe, Peru (`PER`), Spanish Peru (`es-PE`), and PEN.
- [x] Robots returned HTTP 200 text/plain. `User-agent: *` does not disallow `/catalogos`; disallowed paths include images, account/login/checkout, quick-view, espiar and search pagination. No disallowed page was requested.
- [x] Opened Metro's official terms at <https://www.metro.pe/institucional/terminos-y-condiciones/>. The terms were updated 10/03/2026 and identify Cencosud Retail Perú S.A. as Metro. No explicit crawl/commercial-content-reuse permission or prohibition was found in the opened terms; permission is **unverified**, not an affirmative block.
- [x] The registered URL is a stable evergreen catalog landing page. Its server-rendered HTML contains an eight-slide `sliderCatalogo` carousel, but slide titles and image `src`/`alt` attributes were empty. Embedded static text includes an old 2023 “Aniversario 31 años Metro” promo dated 12 Oct–1 Nov 2023. This does not confirm current content or prove the landing URL obsolete.
- [ ] No current flyer title/date, current catalog successor, product-level location scope, or current promo content was verifiable. Do not mark the record `EVERGREEN_CURRENT`; classify its content `STALE_UNVERIFIED`.
- [x] No catalog fields, URL, host, `last_verified_at`, or production data were changed.

## 2. Product Highlights

- [x] No item-level product/variant or same-item normal-price/promo-price pair was verifiable; no prices or product images were retained. Accepted/rejected candidates: **0/0 inspected**.
- [x] The source response did not establish product-level geographic eligibility. A national catalog record alone is not item-level nationwide evidence.
- [x] PE is missing from currency metadata and has no PE highlight feed in this baseline. A full scan of existing highlight feeds found zero references to `metro-pe-online-catalogs`.
- [x] No Product Highlight was accepted, expired, deleted, or migrated; no orphan reference exists.

## 3. Terminal decision

**SKIPPED_UNVERIFIED** — the official evergreen landing URL and access policy were checked, but the current carousel content, dated catalog successor, individual offer prices/images, and product geography were not verifiable from the public response. The terms page did not establish explicit reuse permission either. No products are claimed and no expiry is inferred.

## Compact handoff (≤400 words)

Work unit `PE:metro-pe-online-catalogs`, position 46/74; receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; base/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`. Metro's official `https://www.metro.pe/catalogos` returned 200 HTML with title `Catálogo de Ofertas`, self-canonical URL, and Peru/Spanish/PEN metadata. Robots returned 200; `User-agent: *` does not disallow `/catalogos`. Official terms at `https://www.metro.pe/institucional/terminos-y-condiciones/` were updated 10/03/2026 and identify Cencosud Retail Perú S.A.; no explicit crawler/content-reuse permission or prohibition was established. The stable landing page server HTML contains 8 carousel slides, but titles/images are empty; embedded static text includes only a legacy Oct–Nov 2023 promotion. No current item offers, prices, individual images, catalog period, or product geography were verified. Keep the record `STALE_UNVERIFIED`; do not infer expiry/obsolescence. PE has no currency/feed support and no existing highlight references this ID. No production JSON changed. Next manifest item: `PE:plazavea-pe-national` (47/74), fresh isolated context.
