# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `TR:migros-tr-country` | Position: `67 of 74` | Attempt: `1`  
Country: `TR` | Catalog ID: `migros-tr-country` | Retailer: `Migros`  
Official URL: https://www.money.com.tr/migroskop-dijital  
Checked UTC: `2026-11-23T10:39:55Z`  
Mode: `AUDIT` | Scope: `ONE_OFF_GLOBAL`  
Baseline/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: `SKIPPED_BLOCKED`

## 1. Catalog Promo source

- [x] Loaded `pretio/promos/catalog_app.json`: active `official_retailer` entry; Migros/Migros; national label for Türkiye; null `valid_from`/`valid_until`; `last_verified_at: 2026-09-28T00:00:00Z`. `www.money.com.tr` is allowlisted.
- [x] The exact registered HTTPS path was opened once. The public web reader reported the same page URL and displayed official issue 911, 19 November–2 December 2026, and older issue dates on the same landing page. Its HTTP status and redirect chain were not exposed. This supports current page content and a stable evergreen landing URL; it is not product-price evidence.
- [x] Direct `https://www.money.com.tr/robots.txt` GET returned HTTP 200 `text/plain`; `User-agent: *` allows `/` and disallows `/profilim`, `*?id`, and `*?t=`. The registered path is not matched. Redirect metadata was unavailable.
- [x] The public Money Membership Agreement linked from the page identifies Migros Ticaret A.Ş. as Money Program owner and `www.money.com.tr` as the Money Site. Agreement §3.7 restricts use of automated programs/robots/crawlers/scraping and copying/publishing/using site content without Migros's prior written permission. It is framed as a membership contract, so anonymous-access applicability is not explicit. No separate public license or written permission was found. Robots allowance does not establish permission under the agreement.
- [x] Stopped after locating the use restriction. Did not open the viewer, product pages, image files, or other site paths. A search response unexpectedly surfaced a separate Migroskop viewer-host result with product/price text; it was not transcribed, retained, or analyzed as offer evidence. No images were opened/fetched. No bypass or retry.
- [x] No production catalog field, `last_verified_at`, or URL changed. The dated issue is current at page level, while the source's product-content use remains blocked/unresolved.

## 1B. Online-store / marketplace

- [x] This unit covers only its registered Migros catalog. No separate online-store or marketplace discovery was run.

## 2. Product Highlights candidates

- [x] Accepted products: `0`; observed product candidates rejected by ID: `0`; product pages/images opened: `0`. Incidental search-result product/price text was not evaluated or used.
- [x] Individual normal/promo price pairs, exact variants, item-level dates and item-level nationwide scope were not reviewed because permitted product-content use was not established. The registry's national label does not prove nationwide applicability of each item.
- [x] `TR` is absent from `pretio/data/currency.json`; no TR highlights feed exists. No production highlight references `migros-tr-country`.
- [x] No expiry or obsolete-catalog evidence. No catalog or highlight deletion/migration.

## 3. Skip-or-update decision

- [x] `SKIPPED_BLOCKED` — official ownership and a current landing-page issue were observed, but the linked agreement restricts automated content access/reuse without written permission and no such permission was found. This is not a no-promo result. Keep the catalog active and unchanged; classify product-content permission as unresolved.

## 4. Checkpoint and compact context

- [x] Source evidence: `registered/evidence/TR-migros-tr-country.md`.
- [x] Handoff: `registered/handoffs/TR-migros-tr-country.md` (under 400 words).
- [x] Terminal receipt: `registered/receipts/TR-migros-tr-country.json`.
- [x] No production JSON, shared progress file, or shared terminal-receipts file changed.
- [x] Next manifest input: `TR:sok-tr-country` (68/74), in a fresh isolated context.

Final result: `SKIPPED_BLOCKED`  
Accepted NEW product IDs: none  
Expired deleted IDs: none  
Compact handoff artifact: `registered/handoffs/TR-migros-tr-country.md`
