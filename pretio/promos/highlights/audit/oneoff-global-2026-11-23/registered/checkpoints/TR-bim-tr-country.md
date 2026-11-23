# BİM — registered catalog checkpoint

Run ID: pretio-oneoff-global-20261123T040625Z  
Work unit: TR:bim-tr-country | manifest position: 66/74 | attempt: 1  
Country: TR (Türkiye) | Retailer: BİM | Mode: AUDIT  
Registered URL: https://www.bim.com.tr/Categories/254/aktuel-urunler.aspx  
Checked UTC: 2026-11-23T10:39:18Z (catalog request; robots checked 10:38:29Z)  
Scope: ONE_OFF_GLOBAL | Baseline / skill SHA: 73fd02fe14c4935c3a95bca49bba3c1498a9cb54  
Terminal status: SKIPPED_UNAVAILABLE

## 1. Catalog Promo source

- [x] Loaded the frozen manifest unit and active catalog record: BİM / BİM, catalog ID `bim-tr-country`, `official_retailer`, Türkiye country location, national coverage label, `valid_until: null`, and `last_verified_at: 2026-09-28T00:00:00Z`. The recorded URL matches the manifest; `www.bim.com.tr` is allowlisted. Baseline fields do not independently reverify current source ownership or freshness.
- [x] One live GET to `https://www.bim.com.tr/robots.txt` returned HTTP 200 (`text/plain`, 2,676 bytes). It states `User-agent: *`, `Allow: /`, and `Content-Signal: search=yes,ai-train=no,use=reference`; no general path disallow is present. The reference-use signal is not treated as a commercial republication or image license.
- [x] One live GET to the registered catalog URL returned HTTP 400 Bad Request from Cloudflare, with no redirect. No retry, alternate URL/host, browser impersonation, login, CAPTCHA, proxy, or bypass was used. The catalog page and its footer/legal links were unavailable.
- [ ] Current BİM ownership, terms of service, and commercial reuse/image permission were not independently verified in this attempt. Do not treat the robots reference-use signal as permission to republish campaign content or photos.
- [ ] Current campaign period/dates, evergreen versus rotating behavior, product content, and offer geography could not be inspected. The national catalog label does not prove any individual offer is nationally available. No expiry or obsolescence is inferred from the 400 or the null `valid_until`.

## 2. Products and feed

- [x] No product, leaflet, or image page was opened. Zero prices/images were inspected; this is not a `NO_PROMO_FOUND` result and no item was accepted or rejected.
- [x] `TR` has no configured currency entry in `pretio/data/currency.json` and no `TR.json` highlights feed. This separately blocks any future TR highlight publication; catalog source checking was still attempted.
- [x] No production catalog/feed/index or shared run progress/aggregate receipt was changed. No dated offer was positively proven expired.

## 3. Closeout

- Classify source freshness as `STALE_UNVERIFIED`; terminal result `SKIPPED_UNAVAILABLE` because the one registered-page attempt returned HTTP 400.
- Evidence: `registered/evidence/TR-bim-tr-country.md`; handoff: `registered/handoffs/TR-bim-tr-country.md`; receipt: `registered/receipts/TR-bim-tr-country.json`.
- This receipt terminalizes only `TR:bim-tr-country`; it does not close the global run.
