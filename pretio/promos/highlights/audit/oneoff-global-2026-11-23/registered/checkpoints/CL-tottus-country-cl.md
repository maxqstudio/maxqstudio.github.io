# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `CL:tottus-country-cl` | Position: `13 of 74` | Attempt: `1`  
Country: `CL` | Retailer: `Tottus` | Mode: `AUDIT`  
Checked UTC: `2026-11-23T04:42:23.5428841Z`–`2026-11-23T04:43:19.1129962Z` (robots and registered URL responses)  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: `SKIPPED_BLOCKED`

## 1. Catalog Promo source

- [x] Loaded active record `tottus-country-cl`: `official_retailer`, coverage `national` / `Chile`, country location `CL`, `valid_until: null`, `last_verified_at: 2026-09-14T00:00:00Z`. Registered URL: <https://www.tottus.cl/tottus-cl/content/ofertas-tottus>.
- [x] Registered host `www.tottus.cl` is in `catalog_app.json.allowed_hosts`.
- [ ] Robots policy could not be read. <https://www.tottus.cl/robots.txt> returned HTTP `403`, `text/html; charset=UTF-8`, 4,544 bytes, no redirect; requested `2026-11-23T04:42:23.5428841Z`, completed `04:42:23.9136088Z`. The HTML response is not a robots policy, so permission for the catalog path remains unverified.
- [ ] The registered URL returned HTTP `403`, `text/html; charset=UTF-8`, 5,658 bytes, no redirect; requested `2026-11-23T04:43:18.8151032Z`, completed `04:43:19.1129962Z`. No canonical/product content could be verified. Evidence: <https://www.tottus.cl/tottus-cl/content/ofertas-tottus>.
- [ ] Terms were not independently verified; both the robots URL and catalog page returned forbidden HTML. No guessed terms URL or alternate page was requested.
- [x] Two GETs total (robots and registered URL), zero retries; finite per-request timeouts were 8 seconds and 22 seconds. Neither response redirected. No login, CAPTCHA, access-control bypass, hidden API, alternate host, or proxy was used.
- [x] Classify source `STALE_UNVERIFIED`; the single blocked observation does not prove obsolescence. No catalog field or `last_verified_at` was changed.

## 2. Product Highlights candidates

- [x] `CL` feed uses `CLP`, currently has 24 of 80 items; three existing items reference `tottus-country-cl`. Capacity remains for at most 56 additional country items and 17 additional Tottus items.
- [ ] No offer was inspected or accepted: the source returned `403` before product content was available. Product identity, explicit normal/promo pair, individual image and approved image host, offer dates, and country-wide eligibility could not be assessed. No claim is made that Tottus has no promotions.
- [x] Existing three Tottus items were not revalidated by this attempt. No expiry evidence was obtained, no product was deleted, and no feed/index/catalog JSON changed.

## 3. Disposition

- [x] **SKIPPED_BLOCKED** — both the robots request and registered public catalog request returned `403`; no access restriction was bypassed.
- [x] No candidate accepted. Catalog remains `STALE_UNVERIFIED`; no expiry or permanent obsolescence is inferred. No production data changed.

## Compact handoff (≤400 words)

- Work unit `CL:tottus-country-cl`, position `13/74`; terminal receipt `SKIPPED_BLOCKED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, attempt `1`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- The active Catalog Promo record identifies Tottus Chile, national CL coverage, and <https://www.tottus.cl/tottus-cl/content/ofertas-tottus>; registered host `www.tottus.cl` is allowlisted. It has no `valid_until`; `last_verified_at` remains `2026-09-14T00:00:00Z`.
- At `2026-11-23T04:42:23.5428841Z`, <https://www.tottus.cl/robots.txt> returned `403 text/html; charset=UTF-8`, 4,544 bytes, no redirect. At `04:43:18.8151032Z`, the registered offers URL returned `403 text/html; charset=UTF-8`, 5,658 bytes, no redirect, completing at `04:43:19.1129962Z`. Request timeouts were 8s and 22s; two GETs total, zero retries. Neither response provided robots rules or offer content. Terms remain unverified; no additional or guessed URL was fetched.
- No products were inspected, so no price/image/validity/nationwide evidence was available. CLP is configured; the feed has 24/80 items and three Tottus items, leaving 56 country and 17 retailer slots. Existing items were not revalidated; no expiry is inferred. No production JSON changed.
- No CAPTCHA, login, bypass, hidden API, alternate host or proxy was used. Source classification: `STALE_UNVERIFIED`; no obsolescence claim. Next manifest unit: `CL:unimarc-country-cl`.
