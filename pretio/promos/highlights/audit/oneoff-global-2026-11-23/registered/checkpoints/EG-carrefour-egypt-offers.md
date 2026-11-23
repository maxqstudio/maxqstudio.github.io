# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `EG:carrefour-egypt-offers` | manifest ordinal: **24/74** | Attempt: **1**  
Country: **EG** | Retailer: **Carrefour Egypt** | Mode: **AUDIT**  
Checked: **2026-11-23 UTC** (exact request timestamps were not retained)  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_BLOCKED**

## 1. Catalog Promo source

- [x] Loaded active catalog ID `carrefour-egypt-offers`; merchant `Carrefour Egypt`, publisher `Majid Al Futtaim Carrefour`, source type `official_retailer`, country/location `EG`, `coverage_type: national`, `coverage_label: Egypt`.
- [x] Frozen manifest and active record URL match exactly: <https://www.carrefouregypt.com/mafegy/en/n/c/clp_carrefour-deals>. Host `www.carrefouregypt.com` is in `catalog_app.json.allowed_hosts`.
- [x] Existing record has `valid_until: null`, `valid_from: null`, and `last_verified_at: 2026-11-12T09:33:19+08:00`. URL shape and descriptive text suggest a live deals landing page, but its evergreen/update-in-place behavior was **not verified** in this attempt.
- [ ] Robots request: `GET https://www.carrefouregypt.com/robots.txt` returned HTTP **403 Forbidden**. No usable directives/body were returned; content type, redirect chain and final URL were not captured. Permission for the Catalog Promo path could not be verified.
- [ ] Exact registered Catalog Promo URL was requested once over HTTPS; response was HTTP **403 Forbidden**. PowerShell did not retain a response body or content type; redirect chain/final URL are unknown. No catalog, current offers, linked terms page or product evidence was accessible.
- [ ] Terms of service were not verified because the source was blocked and exposed no links. No alternate path or host was guessed or requested.
- [x] One robots request and one exact registered-URL request; zero retries. No login, CAPTCHA, cookies, proxy, hidden endpoint, alternate host or access-control bypass. The access block is not proof of obsolescence; no catalog data or `last_verified_at` was changed.

## 2. Product Highlights candidates

- [x] Egypt is absent from `pretio/data/currency.json`; there is no `pretio/promos/highlights/EG.json` feed or EG entry in `pretio/promos/highlights/index.json`. The source was checked as required; Product Highlights cannot be added under current currency/feed compatibility.
- [x] No current product offer was accessible. No same-product normal/promo price pair, individual product image, validity date, or item-level Egypt-wide eligibility could be verified. No candidate was accepted; no product candidate was observed to reject.
- [x] A repository search of current country highlight JSON found no existing `catalog_id: carrefour-egypt-offers` reference. No item expiry or catalog obsolescence was proven. Existing production files remain unchanged.

## 3. Disposition

- [x] **SKIPPED_BLOCKED** — robots and the exact registered URL both returned HTTP 403, leaving permission directives and promotional content unavailable.
- [x] No new product, no expired product deletion, no catalog removal/replacement, and no production JSON changes. The source remains `STALE_UNVERIFIED` for this run; the old `last_verified_at` and 403 do not establish expiration.

## Compact handoff (≤400 words)

- Work unit `EG:carrefour-egypt-offers`, manifest ordinal 24/74. Receipt: `SKIPPED_BLOCKED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Exact frozen URL <https://www.carrefouregypt.com/mafegy/en/n/c/clp_carrefour-deals>; allowlisted host `www.carrefouregypt.com`. The active catalog record has national Egypt location, no `valid_until`, and `last_verified_at: 2026-11-12T09:33:19+08:00`.
- One public robots GET returned `403 Forbidden`; one GET of the exact registered URL also returned `403 Forbidden`. Response body, content type, final URL and redirects were not retained. Terms and robots directives remain unknown. No retry, guessed URL, alternate host, login, CAPTCHA, hidden endpoint, proxy or bypass was used.
- No offers were accessible. Egypt has no configured highlight currency, feed or index entry; current highlight JSON contains no reference to this catalog ID. No product pair/image/date/geography, expiry or obsolete-catalog proof was obtained. No catalog, highlight or index production JSON changed.
- Handoff: continue with the next frozen manifest work unit in a fresh context. Do not treat this access failure as proof of an obsolete catalog.
