# PY:superseis-py-country — Superseis

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `PY` | Catalog ID: `superseis-py-country` | Retailer: `Superseis`  
Official URL on record: https://www.superseis.com.py/ofertas/es-es  
Checked UTC: `2026-11-23T10:23:13Z`  
Mode: `AUDIT` | Scope: `ONE_OFF_GLOBAL` | Manifest work unit: `58 of 74` | Attempt: `1`  
Frozen run baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: `SKIPPED_BLOCKED`

## 1. Catalog Promo source

- [x] Loaded the exact active `superseis-py-country` record from `pretio/promos/catalog_app.json`: merchant `Superseis`, publisher `Superseis Online`, source type `official_digital_channel`, national label `Paraguay`, country location `PY`, and `valid_until: null`. Existing `last_verified_at` is `2026-10-19T02:37:05.2093648+08:00`.
- [x] The registered host `www.superseis.com.py` is present in the current catalog `allowed_hosts` list. The record's prior classification does not independently establish current ownership, access permission, or freshness.
- [x] Made one bounded public-source check. The retrieval tool returned HTTP 403 for the registered offers page and the host root. The direct `robots.txt` URL was reported inaccessible via the same tool; no directives or permissions were available. One site-scoped search for terms/robots returned no applicable site terms or usable robots policy.
- [ ] Terms of use and commercial reuse permission verified: **no**. Neither an applicable site terms page nor a usable permission statement was found. The 403/access-policy uncertainty is treated as a block; no alternate host, browser workaround, retries, login, CAPTCHA handling, hidden endpoint or bypass was attempted.
- [ ] Canonical redirects, in-place updates, current catalog content and current promotion dates verified: **no**. The registered path is not established as current or obsolete.
- [x] No production `last_verified_at` or catalog data changed.

## 2. Product Highlights and geography

- [x] The source offers page was not inspected for items because access permission could not be established. Product candidates observed: `0`; this is **not** a no-promotion finding.
- [x] No normal/promo prices, product variants, validity dates, images or product-level geographic scope were collected or inferred. No offer/image fetch was made.
- [x] The catalog record is country-scoped to Paraguay (`PY`); `pretio/location/v2/PY.json` identifies Paraguay and has 18 provinces (revision `geonames-2026-09-23-py`). No product-level nationwide participation/availability was verified.
- [x] `pretio/data/currency.json` has no `PY` currency entry; Product Highlights publication is additionally blocked for this market.
- [x] No candidate feed, highlight feed, index, catalog JSON, or expiry/deletion list was changed.

## 3. Classification and terminal decision

- Catalog condition: `STALE_UNVERIFIED`; an inaccessible source is not evidence of retirement or expiry.
- Source evidence: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/evidence/PY-superseis-py-country.md`.
- [x] **SKIPPED_BLOCKED** — the registered pages could not be retrieved and robots/terms/commercial-use permission could not be established within the single bounded attempt.
- [ ] `NO_PROMO_FOUND`, `UPDATED`, or `VERIFIED_OBSOLETE` are not supported by the evidence.

## 4. Artifacts

- Checkpoint: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/checkpoints/PY-superseis-py-country.md`
- Compact handoff: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/handoffs/PY-superseis-py-country.md`
- Terminal receipt: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/receipts/PY-superseis-py-country.json`
- Production JSON and shared run progress remain untouched. This receipt terminalizes only this work unit; it does not claim global-run completion.
