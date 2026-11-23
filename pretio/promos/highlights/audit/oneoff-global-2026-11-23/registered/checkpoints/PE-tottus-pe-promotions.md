# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Scope: `ONE_OFF_GLOBAL`  
Work unit: `PE:tottus-pe-promotions` | manifest position: **48/74** | attempt: **1**  
Country: **PE** | retailer: **Tottus** | mode: **AUDIT**  
Official URL in frozen record: <https://www.tottus.com.pe/tottus-pe/lista/CATG23097/Promociones>  
Checked UTC: **2026-11-23T10:01:50Z**  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Working branch head at check: **d738c129473567167b0d2984926b232077268a99**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded the frozen record: `tottus-pe-promotions`, Tottus, Peru, `official_retailer`, active, national label, no recorded `valid_until`; existing `last_verified_at` is `2026-10-24T19:59:47+08:00`.
- [x] Checked the registered host's `https://www.tottus.com.pe/robots.txt`. The web open tool returned an internal inaccessible-page error; one standard HTTPS GET fallback with a self-identifying `PretioCatalogAudit/1.0` user agent and 30-second timeout returned **HTTP 403 Forbidden**. No body or directives were available; no further retry was made.
- [x] Because the access policy could not be read, did not open the registered promotions page, terms page, or linked item pages. No retry, alternate host, TLS bypass, hidden endpoint, login, CAPTCHA, proxy, or other bypass was attempted.
- [ ] Merchant ownership, redirect/canonical URL, current page content, evergreen/rotating status, official parent index, promo dates, prices, images, and geographic item applicability were not independently verified in this attempt. The local record alone is not proof of current content.
- [x] Keep the current production record unchanged and classify it `STALE_UNVERIFIED`; the old verification timestamp and inaccessible robots endpoint do not prove expiry or obsolescence.

## 2. Product Highlights

- [x] Peru has no supported Product Highlights currency mapping or indexed country feed in this baseline.
- [x] Scanned current country highlight JSON files for `catalog_id: tottus-pe-promotions`; zero references were found.
- [x] The promotions page was not opened, so **0** products were inspected; no price pair, product image, validity, or item-level geography was retained or accepted. No product was deleted.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — robots policy could not be retrieved (HTTP 403); stopped before opening catalog content because permitted access could not be established.
- [x] No catalog, feed, index, currency, or location data changed. No expiry or successor was inferred.

## Evidence

- `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/evidence/PE-tottus-pe-promotions.md`

## Compact handoff

`PE:tottus-pe-promotions`, position 48/74, terminal `SKIPPED_UNVERIFIED`. The frozen record is Tottus Peru at `https://www.tottus.com.pe/tottus-pe/lista/CATG23097/Promociones`, active with no `valid_until`. The web open tool could not open `https://www.tottus.com.pe/robots.txt`; one standard HTTPS fallback with a self-identifying user agent and 30-second timeout returned HTTP 403 with no readable directives. I stopped before opening the promotion, terms, or item pages because access permission remains unknown. No further retry or bypass was used. Current content, dates, geography, product prices, images and canonical behavior remain unverified; do not infer expiry from the old `last_verified_at`. Peru lacks Product Highlights currency/feed support, and no current feed references this catalog. No product candidate or production change. Next manifest source: `PF:carrefour-pf-catalogue` (49/74), in a fresh isolated context.
