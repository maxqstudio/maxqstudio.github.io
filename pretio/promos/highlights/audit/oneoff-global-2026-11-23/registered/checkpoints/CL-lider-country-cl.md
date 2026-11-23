# Pretio — per-catalog update checklist

Run ID: **pretio-oneoff-global-20261123T040625Z**  
Work unit: **CL:lider-country-cl** | frozen-manifest ordinal: not supplied | catalog array entry: 10/74 | Attempt: 1  
Country: **CL** | Retailer: **Lider** | Mode: **AUDIT**  
Checked UTC: **2026-11-23T04:31:41.527Z** (offers request start); linked terms checked at **2026-11-23T04:32:45.026Z**  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded active lider-country-cl: official retailer, national label Chile, country location CL, URL <https://super.lider.cl/v/ofertas>, no valid_until, last_verified_at 2026-09-14T00:00:00Z.
- [x] Registered host super.lider.cl is in catalog_app.json.allowed_hosts; www.lider.cl is not.
- [x] Robots checked first. <https://super.lider.cl/robots.txt> redirected 307 to <https://www.lider.cl/robots.txt>, which returned 200 text/plain, 639 bytes. The wildcard group does not disallow /v/ofertas; listed disallows cover cart, account, checkout, search, wallet, thank-you, reviews, selected catalog paths and /supermercado*.
- [x] Registered offer URL fetched once at 2026-11-23T04:31:41.527Z: 200 text/html; charset=utf-8, 294,408 bytes, no redirect; final URL stayed on super.lider.cl. Title: “Ofertas | Lider”; canonical metadata points to <https://www.lider.cl/v/ofertas>, an unapproved host. No host migration staged.
- [x] Linked terms page <https://www.lider.cl/ayuda/articulo/terminos-y-condiciones/94565deaa82842389a0665f0706f6b8f> fetched at 2026-11-23T04:32:45.026Z: 200 text/html; charset=utf-8, 431,281 bytes, no redirect. Reviewed text describes Lider Marketplace as a platform and says Marketplace offers are sold by the user seller. No explicit crawler restriction appeared in snippets reviewed; terms were not exhaustively interpreted.
- [x] No login, CAPTCHA, hidden API, proxy or access-control bypass. One robots URL (one redirect), one offers page and one linked terms page; no HTTP retries. Each request was time-bounded and completed in under five seconds.
- [ ] Historical in-place updates and all 211 offers were not verified. Page body: 294,408 bytes / 34,066 visible-text characters; reviewed metadata, location banner, offer count and first eight price-text matches only.

## 2. Product Highlights

- [x] CL currency is CLP. Existing CL feed has 24 items, four Lider; remaining capacity is 56 country-wide and 16 retailer slots under the 80/20 limits.
- [ ] No candidate accepted. First inspected offer-like card: “N-OFERTAS / N-ofertas - Ventilador Repelente De Moscas Portátil,” apparent promo $5.990, normal $6.990, “Ahorra $1.000.” Rejected because the actual seller is not positively identified as Lider; terms say Marketplace offers are sold by user sellers; no individual matching image was fetched or decoded; no offer validity period was verified; and the page location banner defaults to Santiago / Vitacura without proof of Chile-wide availability at that price.
- [x] No product page, image, pagination or other offer was opened. No claim is made that the other 210 offers are ineligible.
- [x] No expired offer or obsolete catalog was proven. Existing Lider items were not independently revalidated or pruned. No catalog_app.json, country feed, or index JSON changed; last_verified_at was not changed.
- [x] No accepted product IDs. Growth target missed because no candidate passed every gate.

## Compact handoff (≤400 words)

- Work unit CL:lider-country-cl; terminal receipt SKIPPED_UNVERIFIED. Run pretio-oneoff-global-20261123T040625Z, scope ONE_OFF_GLOBAL. Frozen-manifest ordinal was not supplied in the assignment.
- Robots: <https://super.lider.cl/robots.txt> returned 307 to <https://www.lider.cl/robots.txt>, then 200 text/plain (639 bytes); wildcard rules do not disallow /v/ofertas. Registered URL returned 200 text/html; charset=utf-8 (294,408 bytes), no redirect. Its canonical metadata is <https://www.lider.cl/v/ofertas>, which is not allowlisted; no host migration staged.
- Page says “Ofertas (211)” and defaults to “Santiago, • Vitacura”. One card appears to show $6.990 normal and $5.990 promo for “N-ofertas - Ventilador Repelente De Moscas Portátil,” tagged “N-OFERTAS.” Linked terms returned 200 text/html and describe Marketplace offers as sold by user sellers. Seller identity, nationwide eligibility, offer period and individual image were not established, so the candidate was rejected.
- CLP is supported; capacity remains 56 total and 16 for Lider. No accepted products, expiries or production changes. Four existing Lider items remain untouched and unverified by this attempt.
- Bounds: one offers page; first eight price-text matches only; one linked terms page and one robots fetch; no retries, product/image pages, pagination, hidden endpoints, login, CAPTCHA or proxy. Continue with the next unit from the immutable run manifest in a fresh isolated context.
