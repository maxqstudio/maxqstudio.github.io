# PY:stock-py-online-offers — Supermercados Stock

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `PY` | Catalog ID: `stock-py-online-offers` | Retailer: `Supermercados Stock`  
Official URL on record: https://nuevo.stock.com.py/ofertas  
Checked UTC: `2026-11-23T10:17:11Z`  
Mode: `AUDIT` | Scope: `ONE_OFF_GLOBAL` | Manifest work unit: `55 of 74` | Attempt: `1`  
Designated run baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: `SKIPPED_BLOCKED`

## 1. Catalog Promo source

- [x] Loaded the exact active `stock-py-online-offers` record from `pretio/promos/catalog_app.json`: merchant/publisher `Supermercados Stock`, `official_retailer`, national label `Paraguay (online offers)`, explicit location `PY` / `Paraguay`, `valid_until: null`, and `last_verified_at: 2026-11-15T05:42:54.476Z`.
- [x] The registered host `nuevo.stock.com.py` is present in the existing `allowed_hosts` list. The existing record identifies the retailer and source; ownership was not independently reverified during this attempt.
- [x] Checked `https://nuevo.stock.com.py/robots.txt` first. At `2026-11-23T10:17:11Z`, it returned HTTP `403`, `text/html`, no redirect, with an nginx “403 Forbidden” body. No robots directives were exposed, so permission for `/ofertas` could not be established.
- [ ] Terms/access terms could not be checked: robots access failed and no terms page was accessed.
- [ ] Did not request the registered offer page because the source access policy could not be established. Current content, redirects, response status, validity dates, and whether the page updates in place are unverified.
- [x] No retries, alternate hosts, search, browser workaround, login, CAPTCHA handling, hidden endpoint, or bypass was used. `last_verified_at` and all production data remain unchanged.
- [ ] Current offer geography is unverified. The catalog record declares a national Paraguay online-offers scope, but it does not establish product-level countrywide ordering, price, or fulfillment.

## 1B. Online-store / marketplace discovery

- [x] No separate discovery was performed; this attempt was limited to the one registered Stock source.

## 2. Product Highlights — discounted items only

- [ ] No product content was observed. This is not evidence that Stock has no promotions.
- [x] No normal/promo pair, product variant, currency, validity period, public image, or item-level geography was collected or inferred.
- [x] `PY` has no currency entry in `pretio/data/currency.json`; this is an additional publication blocker for any later highlight.
- [x] No candidate or expired item was identified. No highlight feed or index was changed.

## 2A. Catalog condition and 2B. geography / expiry

- Catalog condition: `STALE_UNVERIFIED`; the inaccessible robots endpoint is not evidence that the retailer or catalog is obsolete.
- [x] No positive evidence of source retirement, replacement, current promotion validity, product geography, or expiry was found. No deletion or migration is proposed.

## 3. Skip-or-update decision

- [x] **SKIPPED_BLOCKED** — the robots endpoint returned HTTP 403 without policy directives, so access permission and terms could not be established. The canonical offer page was not requested.
- [ ] UPDATED / SKIPPED_NO_CHANGE / SKIPPED_NO_PROMO / SKIPPED_UNAVAILABLE / SKIPPED_UNVERIFIED / BLOCKED_CURRENCY_METADATA / FAILED.

## 4. Checkpoint and compact handoff

- Accepted products: `0`; observed product candidates: `0`; expired IDs deleted: `none`.
- Candidate feed: `none`; production catalog/feed/index: unchanged.
- Handoff: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/handoffs/PY-stock-py-online-offers.md`.
- Receipt: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/receipts/PY-stock-py-online-offers.json`.
- This source work unit is terminal; global run completion is not claimed.
