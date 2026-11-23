# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PL:lidl-pl-official-gazette` | manifest position: **52/74** | attempt: **1**  
Country: **PL** | retailer: **Lidl Polska** | mode: **AUDIT**  
Checked: **2026-11-23**; this web connector did not return request timestamps. Audit finalized by **2026-11-23T10:08:58Z**.  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded the frozen manifest and active production record: `lidl-pl-official-gazette`, Lidl Polska, Poland; `source_type: official_retailer`, `coverage_type: national`, `valid_until: null`, existing `last_verified_at: 2026-11-18T03:09:34Z`.
- [x] Registered URL: <https://www.lidl.pl/c/nasze-gazetki/s10008614>; hostname `www.lidl.pl` is already in the catalog allowlist.
- [x] One robots request to <https://www.lidl.pl/robots.txt> returned HTTP 200, `text/plain`. Its `User-agent: *` rules disallow `/cc.js*`, `/cdn/assets/cwv/`, `/user-api/*`, `/cqe/*`, search-query paths and several query parameters. No rule matches the exact registered path, which has no query.
- [x] A public web-connector attempt to the official home page returned a fetch error (400). The registered Catalog Promo URL itself was **not opened**.
- [x] One bounded search for Lidl Poland usage terms found the official PDF <https://www.lidl.pl/static/assets/c2e4f1e0-a6f5-4c48-ad14-d0eabc8c5097.pdf>, titled `Warunki korzystania z Usługi`. The document says it regulates only “Moje Konto Lidl” and does not govern separate Group Lidl online-service agreements (sections I.6 and IV.14, rendered lines 13–14); it prohibits commercial use of that account service (IV.2, line 47). It points to separate online-service terms, including <https://www.lidl.pl/c/regulamin-sklepu-internetowego-lidl/s10000906>.
- [x] The web connector could not render the separate online-shop terms URL (400). A single standard HTTPS GET to that exact terms URL returned HTTP 200 HTML; the response summary did not expose the actual terms text. No TLS bypass or access-control workaround was used.
- [x] Result: access to the registered path is not disallowed by the observed robots rules, but the website/catalog content reuse permission remains **unverified**. The account-service prohibition is not generalized to the public flyer page. Stopped before opening the flyer or retaining any offer content.
- [ ] Current catalog contents, official parent navigation, evergreen-vs-periodic behavior, current dates, redirect/canonical status, and national/store-specific offer scope were not verified. `valid_until: null` and an existing verification timestamp do not prove the catalog is current or evergreen. Classify as `STALE_UNVERIFIED`; do not infer expiry or obsolescence.
- [x] No production catalog fields, URL, host allowlist, `last_verified_at`, feed, or index were changed.

## 2. Product Highlights

- [x] No promotional/product page was opened and zero products were inspected. No price pair, image, validity interval, or nationwide applicability was retained; accepted/rejected product candidates: **0/0 inspected**.
- [x] Poland has no Product Highlights currency mapping or country feed in the current schema baseline. A local scan found zero existing highlight references to `lidl-pl-official-gazette`.
- [x] No product deletion or catalog removal is supported by this attempt; zero orphan references created.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — robots permits the exact path, but the available terms only govern the account service, and the separate relevant terms page could not be reviewed. Commercial reuse permission and current offer evidence therefore remain unverified.
- [x] Preserve the active catalog unchanged; do not claim current/evergreen status or expiry.
- [x] No Product Highlight accepted; no production data changed.

## Compact handoff

Work unit `PL:lidl-pl-official-gazette`, position 52/74; receipt `SKIPPED_UNVERIFIED`. The active record points to `https://www.lidl.pl/c/nasze-gazetki/s10008614`, has `valid_until:null`, and last verified timestamp `2026-11-18T03:09:34Z`. `https://www.lidl.pl/robots.txt` returned HTTP 200 text/plain; wildcard rules do not disallow the exact registered path. The official `Warunki korzystania z Usługi` PDF regulates only “Moje Konto Lidl”, explicitly excludes separate online-service agreements, and prohibits commercial use of that account service; do not extend that clause to the public flyer page. The PDF links to separate shop terms; the web connector failed to render that page, while a single standard HTTPS request returned 200 without the legal text being captured. The registered catalog page was not opened, so current flyers, dates, prices, images, and geographic offer scope remain unverified. Keep `STALE_UNVERIFIED`; do not infer expiry. PL has no highlight currency/feed and no existing references to this catalog. No production changes. Next manifest input: `PT:auchan-pt-country`.
