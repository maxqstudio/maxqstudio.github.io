# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PE:plazavea-pe-national` | manifest position: **47/74** | attempt: **1**  
Country: **PE** | retailer: **Plaza Vea** | mode: **AUDIT**  
Checked UTC: **2026-11-23T09:59:32Z** (connector did not retain exact HTTP request time)  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded frozen work unit and active catalog record: `plazavea-pe-national`, Plaza Vea Perú, country PE, national label, source type `official_retailer`, `valid_until: null`, last verified `2026-11-12T09:19:33+08:00`.
- [x] Registered URL: <https://catalogos.plazavea.com.pe/volantes>. Its hostname `catalogos.plazavea.com.pe` is already in `catalog_app.json.allowed_hosts`.
- [x] Robots was requested once with `PretioCatalogAudit/1.0`: <https://catalogos.plazavea.com.pe/robots.txt> returned HTTP 200, `text/plain`, with `User-agent: *` and an empty `Disallow:`. No path restriction was present.
- [x] Official terms were found with one bounded query: `site:plazavea.com.pe Plaza Vea "Términos y Condiciones" uso sitio web`. The official <https://www.plazavea.com.pe/terminos-y-condiciones> identifies Compañía Food Retail S.A.C. as the operator of Plaza Vea's ecommerce site (lines 81–84) and states displayed prices/promotions remain valid while shown or for the stated period / until stock (lines 156–159). No explicit crawler/reuse permission or commercial copying restriction was found in the inspected terms; rights to reuse catalog content therefore remain **unverified**.
- [x] The registered Catalog Promo URL was requested once with the same self-identifying client: HTTP 200, `text/html; charset=utf-8`, 32,928 UTF-8 bytes. Page title: `Guia de compras | Plaza Vea`. The visible text contains sections `Especiales`, `Inserto`, `Volantes`, `Avisos` and banner labels `DESTACADO VOLANTE TIENDAS MINI N2` / `VOLANTE CANASTAS NAVIDAD PLUXEE`.
- [ ] Redirect/final URL was not captured by the HTTP response wrapper. The page path looks like a directory URL, but historical in-place update behavior was not checked. The page showed no flyer validity dates or individual current product price pairs in the visible text. Do not claim the November record is expired or that the current flyers are fully verified.
- [x] No catalog URL, date, `last_verified_at`, host allowlist, or production schema field was changed. Keep the current record; this attempt does not prove obsolescence or expiry.

## 2. Product Highlights

- [x] No individual product listing with both a normal price and lower public promo price was visible in the inspected landing-page text; accepted candidates: **0**; rejected price candidates: **0 inspected**.
- [x] Banner assets are not item-specific product images and were not used as highlight images. Promo dates and item-level geographic applicability were not verified.
- [x] Local scan found no Product Highlight references to `plazavea-pe-national`. PE has no currency mapping, country feed, or highlight-index entry, so publication would be unsupported even if a candidate were found.
- [x] No product expiry was established and no product/catalog dependency was removed.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — the official stable-looking flyer directory is accessible, but current flyer dates, item-level discounts, product images, and offer geography were not verified; catalog-content reuse permission was not explicit. No follow-on pages or retries were opened.
- [x] Retain the active catalog unchanged as `STALE_UNVERIFIED` for this run. Do not treat HTTP 200 or the existing November title as proof of current individual offers.
- [x] No production JSON changed.

## Compact handoff

Work unit `PE:plazavea-pe-national`, position 47/74, receipt `SKIPPED_UNVERIFIED`; run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, base/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`. The registered official URL <https://catalogos.plazavea.com.pe/volantes> returned HTTP 200 and its visible page showed flyer sections/banner labels, but no validity dates or item-level price pairs. Robots returned HTTP 200 and allows all paths. Plaza Vea’s official terms identify Compañía Food Retail S.A.C. and describe promotion periods, but give no explicit crawler/reuse permission; permission remains unverified. No product or item image was retained. The catalog path is stable-looking, but in-place update behavior and current flyer dates were not proved; keep the entry unchanged and do not infer expiry. PE lacks Product Highlights currency/feed support and no highlight references this catalog. Next source: `PF:carrefour-pf-catalogue`.
