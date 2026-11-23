# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PT:lidl-pt-country` | manifest position: **56/74** | attempt: **1**  
Country: **PT** | retailer: **Lidl** | mode: **AUDIT**  
Registered URL: <https://www.lidl.pt/c/folhetos/s10020672>  
Checkpoint time: **2026-11-23T10:18:40Z** (UTC; web connector did not retain request-level timestamps)  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

Scope note: this source attempt is under controller scope `ONE_OFF_GLOBAL`. The frozen `registered-manifest.json` itself records `scope=ALL_COUNTRIES`, `execution=SCHEDULED_GLOBAL`, and 74 work units; this checkpoint closes only this Lidl source. No scheduler or additional source was run.

## 1. Catalog Promo source

- [x] Loaded manifest work unit `PT:lidl-pt-country` and current record: merchant Lidl; publisher Lidl Portugal; `official_retailer`; country PT; national coverage label “Portugal (location-selected offers)”; `valid_until: null`; `last_verified_at: 2026-09-28T00:00:00Z`.
- [x] Official ownership checked. Lidl Portugal’s technical-information page identifies Lidl & Companhia as operator of lidl.pt and says it is responsible for promoting in-store benefits on that website.
- [x] Checked official <https://www.lidl.pt/robots.txt>. `User-agent: *` disallows `/q/search?id=*`, `/cc.js*`, `/1*`–`/9*`, and `/cdn/assets/cwv/`; it does not disallow the registered `/c/folhetos/s10020672` page or the official `/l/pt/folhetos/…` weekly-flyer path. No restricted path, login, CAPTCHA or bypass was used.
- [x] The requested and rendered catalog URL match. This is a stable `/c/folhetos/` directory, not a date-specific catalog URL; the directory is current as of 23 Nov. `LINK_STABLE` / `EVERGREEN_CURRENT` (audit labels only). `valid_until: null` is retained; no expiry was inferred.
- [x] Official directory shows “Promoções Semanais A partir de 23/11” and “Promoções Fim-de-Semana A partir de 27/11”, plus special leaflets. These are start dates/headings, not evidence of offer end dates.
- [x] Geographic scope: the retailer site/operator and catalog are Portugal-specific; an official Lidl store page labels the leaflets “National”. The catalog record also warns “Portugal (location-selected offers)”; this does not prove every individual product price applies at every store.
- [x] Checked terms/reuse scope. The public “Termos e Condições” page found in the footer governs Lidl Plus, including personal-use-only/commercial-use-excluded provisions; it does not state terms for the public leaflet directory. An official corporate policy PDF says its own text/images/photos/logos cannot be reproduced without written Lidl consent; that notice is document-specific, not a general website license. No explicit permission to reuse leaflet product imagery was found. Reuse permission is therefore **UNVERIFIED**, not claimed prohibited or granted.
- [x] No general site content-reuse license was located in the bounded official-site navigation/search. Under the “only if permitted” gate, item-level price/image review stopped here; no exact product prices or item images were collected, downloaded or copied.
- [x] No URL, `valid_until`, host allowlist, `last_verified_at`, or other production field was changed.

## 2. Product Highlights — discounted items only

- [x] Current weekly/weekend leaflet headings were observed, but individual offers were not reviewed because image/data reuse permission was not established.
- [x] Accepted candidates: **none**. No product name, size, normal/promo price pair, image, item validity, or item-level national applicability is asserted.
- [x] No highlight was inserted, migrated, expired or deleted; no PT candidate feed was staged.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — the registered evergreen catalog source is official, robots-allowed and current, but the requested product/image evidence gate could not be satisfied because reuse permission is unverified. Do not treat the leaflet headings as item or expiry proof.
- [x] Keep the active Catalog Promo record. No obsolete catalog or expired product was proven.

## 4. Checkpoint and compact

- [x] Audit evidence: `registered/evidence/PT-lidl-pt-country.md`.
- [x] Compact handoff (≤400 words): `registered/handoffs/PT-lidl-pt-country.md`.
- [x] Terminal receipt: `registered/receipts/PT-lidl-pt-country.json`.

## 5. Cycle scope

- [x] This is one terminal receipt for manifest unit 56/74, not a full-run closing gate. No other catalog was processed in this source task.
- [x] New-product target from this source: **not met**; a country-level target decision belongs to the full scoped run.
- [x] No production JSON, shared progress file, commit, push, or schedule was changed/created.

Final result: **SKIPPED_UNVERIFIED**  
Accepted NEW product IDs: **none**  
Expired deleted IDs: **none**  
Compact handoff artifact: `registered/handoffs/PT-lidl-pt-country.md`
