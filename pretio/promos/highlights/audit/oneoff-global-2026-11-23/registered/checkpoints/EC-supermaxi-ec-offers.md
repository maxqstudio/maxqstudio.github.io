# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `EC:supermaxi-ec-offers` | manifest position: **not supplied** | Attempt: **1**  
Country: **EC** | Retailer: **Supermaxi** | Mode: **AUDIT**  
Source request window: **2026-11-23T05:01:31.1010213Z–05:01:43.5073413Z**  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded active entry `supermaxi-ec-offers`: `official_digital_channel`, country **EC**, national label **Ecuador**, `valid_until` absent, existing `last_verified_at: 2026-11-15T05:42:54.476Z`. The record's summary warns that prices and availability can vary by selected store.
- [x] Registered URL used exactly once: <https://www.supermaxi.com/mas-beneficios/>. `www.supermaxi.com` is in `catalog_app.json.allowed_hosts`.
- [x] Robots URL <https://www.supermaxi.com/robots.txt> returned HTTP `200`, `text/plain; charset=utf-8`, 395 UTF-8 bytes, requested at `2026-11-23T05:01:31.1010213Z`. It allows `/` and does not disallow `/mas-beneficios/`; it disallows `/api/`, `/buscar`, `/precios-local/`, `/login`, `/favoritos`, several query-filter paths, `/ui`, and `/design-system`. The local PowerShell response object did not expose its final URL.
- [ ] Terms were not verified. The retained single-page excerpt did not include the footer/legal links, and no second source-page request was made.
- [x] The exact registered URL returned HTTP `200`, `text/html; charset=utf-8`, 1,368,121 UTF-8 bytes; requested `2026-11-23T05:01:42.9009855Z`, completed `05:01:43.5073413Z`. The response body identified `lang="es-EC"`, publisher/author **Corporación Favorita**, and Ecuador in its site description. Its HTML canonical tag points to <https://www.supermaxi.com>; the final response URI/redirect chain was not available from the local response wrapper.
- [ ] The direct response excerpt retained only the first 6,000 characters of the HTML head. No promotion cards, product prices, validity dates, or item images were captured. The page request was not repeated after this capture limitation.
- [x] One robots request and one registered-URL request total; no retry, login, CAPTCHA, hidden API, cookie, proxy, or access-control bypass.
- [x] Source is **STALE_UNVERIFIED** for current offer claims. A `200` response and the national site description do not establish that individual offers are countrywide or provide current product evidence. No expiry or supersession was proven; no catalog field or `last_verified_at` was changed.

## 2. Product Highlights candidates

- [x] Ecuador has no entry in `pretio/data/currency.json`, and `pretio/promos/highlights/EC.json` does not exist. The registered source was still checked; Product Highlights publication is incompatible with the existing currency/feed baseline.
- [ ] No current product candidate could be recorded from the retained response. No same-product normal/promo pair, exact product identity, decodable image, offer validity, or product-level eligible area was verified.
- [x] The audit summary confirms store-level variation, so a national catalog label alone is insufficient for a countrywide highlight. No accepted/rejected offer IDs; no expired product or catalog was proven.
- [x] No production catalog, highlight feed, or index JSON changed. Existing retailer references in historical audit text are not active EC feed entries.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — the official route was reachable and permitted by the observed robots rules, but the captured HTML head did not retain offer content; canonical/final URL details and terms were not verified. Missing Ecuador currency/feed support separately blocks highlights.
- [x] No new item accepted, no expired ID deleted, no catalog obsolescence inferred, and no production data staged.

## Compact handoff (≤400 words)

- Work unit `EC:supermaxi-ec-offers`; terminal receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- The active `official_digital_channel` record is national-labeled Ecuador (`EC`), has no `valid_until`, and retains `last_verified_at: 2026-11-15T05:42:54.476Z`; its summary notes offer prices and availability can vary by selected store. The exact frozen URL <https://www.supermaxi.com/mas-beneficios/> was used once; its host is allowlisted.
- `robots.txt` returned HTTP 200 `text/plain; charset=utf-8`, 395 bytes, at `05:01:31.1010213Z`; it allows `/mas-beneficios/`. The registered URL returned HTTP 200 `text/html; charset=utf-8`, 1,368,121 bytes at `05:01:42.9009855Z–05:01:43.5073413Z`. The retained head identifies `es-EC` and Corporación Favorita, while its canonical tag points to the site root. Final URL/redirect chain was not captured. Only 6,000 head bytes were retained; no offer card or item evidence was recorded, and the successful request was not repeated.
- Terms were not verified. The store summary warns of selected-store variation, so national product eligibility is unproven. Ecuador lacks currency metadata and an `EC.json` highlights feed. No product, expiry, or obsolescence proof was obtained; no production JSON changed.
