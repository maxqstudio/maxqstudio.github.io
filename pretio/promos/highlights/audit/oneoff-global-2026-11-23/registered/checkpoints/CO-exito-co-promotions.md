# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `CO:exito-co-promotions` | Position: `14 of 74` | Attempt: `1`  
Country: `CO` | Retailer: `Éxito` | Mode: `AUDIT`  
Checked UTC: `2026-11-23T04:47:10.2773881Z`–`2026-11-23T04:47:23.7433125Z` (robots and registered URL responses)  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: `SKIPPED_BLOCKED`

## 1. Catalog Promo source

- [x] Loaded active record `exito-co-promotions`: `official_digital_channel`, national / Colombia coverage, country location `CO`, `valid_until: null`, existing `last_verified_at: 2026-10-21T10:21:02+08:00`. The frozen manifest and catalog record both register <https://www.exito.com/mercado/descuentos-promociones-exito>.
- [x] Registered host `www.exito.com` is in `catalog_app.json.allowed_hosts`.
- [ ] Robots policy could not be read. <https://www.exito.com/robots.txt> returned HTTP `403`, `text/html; charset=UTF-8`, 4,905 body bytes, no redirect; requested `2026-11-23T04:47:10.2773881Z`, completed `04:47:10.8207846Z`. The body is a Cloudflare “Attention Required!” page saying access to `exito.com` is unavailable, not robots directives.
- [ ] Registered Catalog Promo URL returned HTTP `403`, `text/html; charset=UTF-8`, 6,019 body bytes, no redirect; requested `2026-11-23T04:47:23.3929953Z`, completed `04:47:23.7433125Z`. The response title is “Attention Required! | Cloudflare”; its body says “Sorry, you have been blocked” and “You are unable to access exito.com”. No catalog or product content was available.
- [ ] Terms were not independently verified because the page was blocked and exposed no retailer links. No legal URL was guessed and no additional URL was fetched.
- [x] Two GETs total (one robots URL and one exact registered URL), zero retries; finite request timeouts were 8 seconds and 22 seconds. Neither response redirected. No login, CAPTCHA, access-control bypass, hidden API, alternate host, or proxy was used.
- [x] Classify source as `STALE_UNVERIFIED`; the blocked attempt does not prove obsolescence. Current evergreen/periodic status and market-specific availability could not be assessed. No catalog field or `last_verified_at` was changed.

## 2. Product Highlights candidates

- [x] CO currency metadata is absent from `pretio/data/currency.json`; the registered source was still checked as required. A CO highlight cannot be staged under the current currency gate.
- [ ] No product content was inspected or accepted: same-item explicit normal/promo prices, individual image, dates, and Colombia-wide online ordering/fulfillment could not be assessed. No claim is made that Éxito has no promotions. Rejected candidates: none observed.
- [x] No product offer or expiry evidence was obtained. No feed, index, or catalog production JSON changed.

## 3. Disposition

- [x] **SKIPPED_BLOCKED** — robots and the exact registered public Catalog Promo URL returned Cloudflare `403` HTML. No offer proof or terms/robots policy was available; access was not bypassed.
- [x] No candidate accepted. The catalog remains `STALE_UNVERIFIED`; no expiry or permanent obsolescence is inferred. No production data changed.

## Compact handoff (≤400 words)

- Work unit `CO:exito-co-promotions`, position `14/74`; terminal receipt `SKIPPED_BLOCKED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, attempt `1`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- The active Éxito Catalog Promo record is `official_digital_channel`, national / Colombia (`CO`), with no `valid_until`; both the frozen manifest and catalog register <https://www.exito.com/mercado/descuentos-promociones-exito>. The host is allowlisted. Its recorded `last_verified_at` remains `2026-10-21T10:21:02+08:00`.
- At `2026-11-23T04:47:10.2773881Z`, <https://www.exito.com/robots.txt> returned `403 text/html; charset=UTF-8`, 4,905 bytes, no redirect; it was not a robots policy. At `04:47:23.3929953Z`, the exact registered Catalog Promo URL returned `403 text/html; charset=UTF-8`, 6,019 bytes, no redirect, completing at `04:47:23.7433125Z`. The Cloudflare body says “Sorry, you have been blocked.” Timeouts were 8s and 22s; two GETs total, zero retries.
- Terms remain unverified because the blocked response exposed no retailer links; no guessed URL or extra request was used. No product was inspectable, so price-pair, image, product-date, and Colombia-wide fulfillment evidence is unavailable. `CO` has no currency metadata in `pretio/data/currency.json`, but the source was still checked. No production JSON changed.
- No CAPTCHA, login, bypass, hidden API, alternate host, or proxy was used. Source classification: `STALE_UNVERIFIED`; one block is not obsolescence proof. Next manifest unit: `CO:olimpica-co-promotions`.
