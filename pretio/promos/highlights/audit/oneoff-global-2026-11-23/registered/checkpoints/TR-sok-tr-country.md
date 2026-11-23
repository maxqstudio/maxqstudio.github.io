# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `TR:sok-tr-country` | manifest position: `68/74` | attempt: `1`  
Country: `TR` | retailer: ŞOK | mode: `AUDIT`  
Registered URL: <https://kurumsal.sokmarket.com.tr/firsatlar/haftanin-firsatlari>  
Checked UTC: `2026-11-23T10:42:14Z`  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: `SKIPPED_UNVERIFIED`

Scope note: controller scope is `ONE_OFF_GLOBAL`; this checkpoint terminalizes only `TR:sok-tr-country` and does not close the run.

## 1. Catalog Promo source

- [x] Loaded active record: ŞOK / ŞOK Marketler; `official_retailer`; country location TR/Türkiye; national label; `valid_until: null`; `last_verified_at: 2026-09-28T00:00:00Z`; host allowlisted. TR has no currency metadata.
- [x] Official corporate host and the page title identify ŞOK Marketler. One robots request returned HTTP 200 and permits `/`; the registered path and observed canonical path are not disallowed.
- [x] One canonical-page request returned HTTP 200; registered URL resolved to `https://kurumsal.sokmarket.com.tr/tr/firsatlar`, which matched its HTML canonical URL. No Terms/use/content-reuse link appeared in page anchors; only privacy/KVKK and cookie-policy links appeared. Terms-based permission remains unverified; no legal link was fetched.
- [ ] Current dated promotion period or update-in-place history verified: **no**. The bounded page summary had no `DD.MM.YYYY` marker; do not infer current validity or expiry from “weekly offers,” URL shape, or `valid_until: null`.
- [ ] Individual offers' country-wide eligibility verified: **no**. Site metadata indicates a Türkiye-wide store footprint, not product-level offer geography.
- [x] Classify source `STALE_UNVERIFIED`; no positive evidence of obsolescence. No `last_verified_at` or production record changed.

## 2. Product Highlights and closeout

- [x] Terms/reuse permission not established; stop before product-level extraction. Prices, product pages, and images checked: `0`.
- [x] `SKIPPED_UNVERIFIED`; no accepted or rejected product IDs. This is not `NO_PROMO_FOUND`.
- [x] TR is absent from `pretio/data/currency.json`; `TR.json` does not exist. No candidate feed staged.
- [x] No production JSON, shared progress, or aggregate terminal-receipts file changed. No retry, alternate route, schedule, commit, or push.
- [x] Evidence: `registered/evidence/TR-sok-tr-country.md`. Handoff: `registered/handoffs/TR-sok-tr-country.md`. Receipt: `registered/receipts/TR-sok-tr-country.json`.
- [x] Next manifest input: `US:aldi-us-country` (`69/74`).

Final result: `SKIPPED_UNVERIFIED`  
Accepted NEW product IDs: none  
Expired deleted IDs: none  
Compact handoff artifact: `registered/handoffs/TR-sok-tr-country.md`
