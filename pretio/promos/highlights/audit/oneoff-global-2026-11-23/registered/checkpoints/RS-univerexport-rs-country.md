# RS:univerexport-rs-country — Univerexport

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `RS` | Catalog ID: `univerexport-rs-country` | Retailer: `Univerexport`  
Official URL: <https://www.univerexport.rs/sr/katalozi>  
Checked UTC: `2026-11-23T10:32:08Z`–`2026-11-23T10:32:43Z`  
Mode: `AUDIT` | Scope: `ONE_OFF_GLOBAL` | Manifest position: `64/74` | Attempt: `1`  
Baseline/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`

## Catalog source checklist

- [x] Loaded the active record: official retailer, national label “Serbia (location-selected offers),” country location `RS`, stable-looking catalog directory URL, `valid_until: null`; `www.univerexport.rs` is allowlisted. No production fields changed.
- [x] One public robots request returned `200 text/plain; charset=UTF-8`, no redirect, 178 bytes. `User-agent: *` disallows `/api/`, `/auth/`, `/admin/`, `/login`, `/*.pdf$`, `/kviz`, `/aplikacija`, and `/aplikacija/pravne-informacije`; it does not disallow `/sr/katalozi`. No crawl delay was stated.
- [x] One request to the exact registered page returned `200 text/html; charset=utf-8`, no redirect, 26,843 bytes; page title `Katalozi`. It displayed `Cene padalice od 16. 11.`, `Najnoviji katalog od 16. 11.`, and `Katalog vina i delikatesa`. The date has no year or end date, so the current issue/validity is unverified; no expiry was inferred.
- [x] Official brand identity is supported by the branded page and its contact footer (Sentandrejski put 165, 21000 Novi Sad; Univerexport contact details). The fetched page did not expose the legal corporate owner.
- [ ] Terms/reuse permission: the catalog page exposed no terms/legal link; the robots-disallowed `/aplikacija/pravne-informacije` path was not opened. No explicit commercial content-reuse permission or authorization was established.
- [x] The Serbian site and `RS` catalog location establish Serbia as the market context, but this page does not state nationwide item eligibility or participating stores. No product-specific geography was verified.

## Products and decision

No product/detail pages, PDF leaflets, prices, or product images were fetched because reuse permission remains unverified. Zero items were evaluated; this is not a no-promo finding. `RSD` exists in current currency metadata, but no highlight is eligible without authorized item-level price/image and geography evidence. Classify the catalog `STALE_UNVERIFIED`; retain its active registration and do not infer obsolescence.

**Terminal status: `SKIPPED_UNVERIFIED`.** No production JSON, highlight feed/index, or shared progress was changed. Next manifest input: `TR:a101-tr-country` (`65/74`).
