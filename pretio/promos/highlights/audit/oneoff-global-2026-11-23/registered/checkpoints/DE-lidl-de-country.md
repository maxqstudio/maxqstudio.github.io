# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `DE:lidl-de-country` | Position: **20/74** | Attempt: **1**  
Country: **DE** | Retailer: **Lidl Deutschland** | Mode: **AUDIT**  
Source request window (UTC): **2026-11-23T04:54:14.8728351Z–04:55:31.1280011Z**  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded frozen work unit `DE:lidl-de-country`: active `official_retailer`, Germany (`DE`), catalog ID `lidl-de-country`, `valid_until: null`; registered URL <https://www.lidl.de/c/online-prospekte/s10005610/>. Existing `last_verified_at` is `2026-09-22T00:00:00Z` and was not changed.
- [x] Registered host `www.lidl.de` is allowlisted in `catalog_app.json`.
- [x] Robots was checked first. <https://www.lidl.de/robots.txt> returned `200 text/plain`, 312 UTF-8 bytes, no `Location`, requested `2026-11-23T04:54:14.8728351Z`, completed `04:54:16.0979626Z`. `User-agent: *` disallows `/cc.js*`, `/cdn/assets/cwv/`, `/user-api/*`, `/cqe/*`, `*search?q=*`, and parameters `offset`, `idsOnly`, `productsOnly`, `id`, `pageId`, `advisor`, and `sort`; it does not disallow the frozen catalog path. No robots `Crawl-delay` was present.
- [x] The exact registered URL returned `200 text/html; charset=utf-8`, 207,450 UTF-8 bytes, title `Prospekte bei Lidl: Unsere Aktionsprospekte jetzt online- Lidl.de`, requested `2026-11-23T04:54:36.9073534Z`, completed `04:54:37.9660440Z`. It was fetched once more at `04:55:30.0470353Z`–`04:55:31.1280011Z` to retain the visible flyer links and page text omitted from the first console excerpt; response was again `200`, same content type and byte count. There was no `Location` header; the PowerShell wrapper returned a null `BaseResponse.ResponseUri`, so final URL/redirect chain could not be confirmed.
- [x] Current page text names official Lidl Germany weekly leaflets `Aktionsprospekt 23.11.2026–28.11.2026` (two variant links) and `Aktionsprospekt 30.11.2026–05.12.2026`. A current stable evergreen landing page is therefore available and actively lists dated leaflets. This one observation does not prove the URL's historical in-place rotation, but the registered URL itself is undated and unchanged. No new canonical URL or host migration is indicated.
- [x] Geographic note: the same page says `Wähle deine Filiale aus, um unsere speziellen Angebote und Prospekte für deine Region zu entdecken` (“choose your store to discover special offers and leaflets for your region”). Thus displayed physical-store offers depend on a selected region; this does not prove nationwide item-level eligibility.
- [ ] Terms page was not opened. The footer lists `AGB Onlineshop`, but its exact URL and terms were not captured. No terms URL was guessed.
- [x] Requests used the public exact registered URL and robots URL only; timeout was at most 25 seconds. No search query, retry after failure, product/image download, login, CAPTCHA, hidden endpoint, alternate host, proxy, or access-control bypass was used. The second successful HTML GET was an evidence-extraction pass, not a failed-request retry.
- [x] No production catalog field, `last_verified_at`, host allowlist, feed, or index was changed. The active evergreen source is not proven expired or obsolete and must remain active.

## 2. Product Highlights candidates and expiry

- [x] `DE` supports EUR. The existing `DE.json` has nine items linked to `lidl-de-country`; all nine carry `valid_until: 2026-11-28`, later than the Germany-local date 2026-11-23. No date-expired product was found for this work unit; no item was removed.
- [ ] The evergreen landing HTML did not expose individual product cards, matched normal/promo prices, product-level images, or price terms. It links to region-selected prospectuses; the visible image hosts are `imgproxy.leaflets.schwarz` cover thumbnails and were not in the approved catalog host list. No product page or image bytes were fetched.
- [ ] No new Product Highlight candidate could be individually verified for exact item identity, regular and lower promotional price, approved decodable product image, offer dates, and nationwide Germany eligibility. Candidate count: **0 observed**, which does not mean no promotions exist.
- [x] No expired published highlight or catalog URL was proven. No feed/index/catalog production data was changed.

## 3. Disposition

- [x] **SKIPPED_UNVERIFIED** — the official evergreen landing page is live and advertises current dated leaflets, but product-level offers were not exposed in the captured content and the page explicitly makes physical-store promotions regional. No new discount meets all publication gates.
- [x] No accepted/rejected product IDs, no expired IDs deleted, no schema changes, no production JSON changes. Keep registered evergreen URL active; do not infer obsolescence from region selection.

## Compact handoff (≤400 words)

Work unit `DE:lidl-de-country` (20/74), receipt `SKIPPED_UNVERIFIED`; run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`. The exact frozen URL `https://www.lidl.de/c/online-prospekte/s10005610/` is allowlisted and currently returns the Lidl Germany online prospectus landing page (`200 text/html`, 207,450 bytes, observed title `Prospekte bei Lidl: Unsere Aktionsprospekte jetzt online- Lidl.de`). The undated URL lists leaflets for 23–28 Nov and 30 Nov–5 Dec 2026. Robots was checked first (`200 text/plain`, 312 bytes); its wildcard rules do not disallow the registered route. A second successful request to the same page was made only because the first output excerpt omitted its visible links/text; this was not a failed-request retry. Final URI/redirect chain was not exposed by the PowerShell wrapper.

The page states to choose a Lidl store to see special offers and leaflets for that region. No item-level price, product image, validity, or nationwide eligibility was captured. No guessed endpoints, image fetches, or bypasses were used. The footer lists AGB but its exact URL/terms were not checked. Nine current DE highlight items reference this catalog and each is dated through `2026-11-28`, so none is expired on the run date; all remain untouched. No production JSON changed. Next manifest unit after this item: `DE:rewe-de-country`.