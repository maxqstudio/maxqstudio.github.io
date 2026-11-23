# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `CL:jumbo-country-cl` | Position: `9 of 74` | Attempt: `1`  
Country: `CL` | Retailer: `Jumbo` | Mode: `AUDIT`  
Checked UTC: `2026-11-23T04:28:44.292Z` (official offers-page response)  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: `SKIPPED_UNVERIFIED`

## 1. Catalog Promo source

- [x] Loaded active record `jumbo-country-cl`: `official_retailer`, coverage label `Chile`, country location `CL`, `valid_until: null`, `last_verified_at: 2026-09-14T00:00:00Z`. Registered URL: <https://www.jumbo.cl/jumbo-ofertas>.
- [x] Registered host `www.jumbo.cl` is in `catalog_app.json.allowed_hosts`.
- [x] Robots checked first. [Robots file](https://www.jumbo.cl/robots.txt) returned HTTP `200`, `text/plain`, 1,450 bytes, no redirect; request started `2026-11-23T04:28:38.267Z`, completed `04:28:39.488Z`. It names `User-agent: *` and disallows parameterized paths such as `*?map=` and `*?PS=`; it does not disallow `/jumbo-ofertas`. The requested clean offers path was allowed.
- [x] Registered [offers URL](https://www.jumbo.cl/jumbo-ofertas) returned HTTP `200`, `text/html; charset=utf-8`, 4,978,532 bytes, no redirect; request started `04:28:39.557Z`, completed `04:28:44.292Z`. Page evidence includes `<title>Jumbo Ofertas | Jumbo.cl</title>` and public server-rendered product cards. The URL is undated and evergreen in form; current page content carries a November offer period. One observation cannot prove historical in-place rotation.
- [ ] Terms were not verified. A link-text match mistakenly selected <https://www.jumbo.cl/despensa/sopas-cremas-e-instantaneos/bases-y-salsas> because “bases” matched the search; that ordinary grocery category returned HTTP `200`, `text/html; charset=utf-8`, 1,650,499 bytes, no redirect (`04:28:44.553Z`–`04:28:47.355Z`) and is not a terms page. No guessed terms URL was fetched.
- [x] No login, CAPTCHA, bot bypass, hidden API, proxy, or alternate source was used. Three GETs total (robots, offers page, mistakenly matched category), zero retries; total elapsed time `9.32s` within a 25-second total budget. No further requests were made.
- [x] No catalog record, `last_verified_at`, production feed, or index was changed.

## 2. Product Highlights candidates

- [x] `CL` currency metadata supports `CLP`; `CL.json` has 24 items, including 8 linked to this catalog.
- [x] Public offer-card payload samples showed matching `listPrice` / `price`, Jumbo seller, and November validity text `27 OCT AL 23 NOV 2026` (observed on Nov 23 Chile time):
  - `Papel Higiénico Confort Súper Doble Hoja 40 m 8 un.` — CLP `8190` / `6790`.
  - `Papel Higiénico Favorita Acolchado Doble Hoja 23.5 m 24 un.` — CLP `11540` / `7690`.
  - `Papel Higiénico Elite Soft & Strong Triple Hoja 40 m 4 un.` — CLP `6650` / `5250`.
- [ ] No product was accepted. These source-page samples are rejected as `SKIPPED_UNVERIFIED`: the in-page individual-image URLs use `jumbocl.vtexassets.com`, which is absent from the approved `catalog_app.json.allowed_hosts`, and image bytes were not fetched/decoded. The Catalog Promo's `national` label alone does not establish these product prices' country-wide fulfillment/eligibility; no official nationwide terms were verified. Sample promo metadata names Jumbo's November monthly campaign and supplies the dates above, but cannot remedy the host and geographic gaps.
- [x] No new candidate IDs or expired IDs were staged. Existing Jumbo feed items have no `valid_until`; this bounded page check did not prove any existing item's expiry. No product/feed/index JSON was changed.

## 2A. Catalog disposition

The registered route is a stable, undated offers landing URL with current offer content, not a period-dated catalog URL. Keep classification as `EVERGREEN_CURRENT` for this check; repeated observations would be needed to establish in-place update behavior. No replacement or retirement is supported.

## 3. Skip-or-update decision

- [x] **SKIPPED_UNVERIFIED** — current price-pair/date samples exist, but no offer passed the approved image-host and country-wide eligibility gates; terms remain unverified.
- [x] No production data changed. Next manifest unit is `CL:lider-country-cl`.

## Compact handoff (≤400 words)

- Work unit `CL:jumbo-country-cl`, position `9/74`; terminal receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; this records only this assigned catalog. Baseline/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- At `2026-11-23T04:28:38.267Z`, <https://www.jumbo.cl/robots.txt> returned `200 text/plain`, 1,450 bytes, no redirect; its wildcard rules did not disallow `/jumbo-ofertas`. The registered <https://www.jumbo.cl/jumbo-ofertas> returned `200 text/html; charset=utf-8`, 4,978,532 bytes, no redirect, at `04:28:44.292Z`; title: `Jumbo Ofertas | Jumbo.cl`. Requests used one bounded 25-second budget: 9.32 seconds total, 3 GETs, 0 retries.
- The initial HTML included public Jumbo cards with CLP `listPrice`/`price` pairs and promotion text ending `27 OCT AL 23 NOV 2026`. Sample pairs: Confort 8 un. `8190/6790`; Favorita 24 un. `11540/7690`; Elite Soft & Strong 4 un. `6650/5250`. No candidate was accepted: image host `jumbocl.vtexassets.com` is not in the approved host list and image bytes were not decoded; the catalog-level Chile label does not prove product-wide nationwide eligibility.
- Terms remain unverified. One text-match follow-up landed on a linked “Bases y Salsas” grocery category (`200 text/html`), not legal terms; no guessed URL or further source request was made. No production JSON changed; existing undated Jumbo feed entries were not treated as expired.
- Next input: `CL:lider-country-cl`.
