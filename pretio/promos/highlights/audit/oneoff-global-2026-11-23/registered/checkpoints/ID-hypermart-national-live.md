# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `ID:hypermart-national-live` | catalog array position: **3/74** | manifest ordinal: **29/74** | Attempt: **1**  
Country: **ID** | Retailer: **Hypermart** | Mode: **AUDIT**  
Checked: **2026-11-23 UTC** (wrapper did not retain exact request timestamps)  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded active catalog record `hypermart-national-live`: publisher/merchant Hypermart; `source_type: official_retailer`; ID / Indonesia; `coverage_type: national`; `valid_from: null`; `valid_until: null`; existing `last_verified_at: 2026-08-22T01:00:00+08:00`.
- [x] Frozen manifest URL and registered URL both equal <https://www.hypermart.co.id/promo-katalog-hypermart/>. Host `www.hypermart.co.id` is in `catalog_app.json.allowed_hosts`.
- [x] One request to <https://www.hypermart.co.id/robots.txt> returned HTTP 200, `text/plain`, 30 bytes. Body: `User-agent: *` and `Crawl-delay: 30`; no `Disallow` rule. I waited at least 30 seconds between each subsequent request to this host.
- [x] One GET to the public homepage `https://www.hypermart.co.id/` returned HTTP 200, `text/html; charset=UTF-8`, 409,270 UTF-8 bytes. A second homepage request (after the robots delay) used a local link scan to look for Terms/legal links; none was exposed in the returned HTML. No Terms URL was guessed.
- [x] One and only one GET to the exact frozen Catalog Promo URL returned HTTP 200, `text/html; charset=UTF-8`, 156,746 UTF-8 bytes. The page's canonical link is the exact registered URL. The local capture retained only status, content type, byte count and canonical URL while looking for legal links; no offer-card or product evidence was retained. The wrapper did not expose `ResponseUri` or redirect chain.
- [ ] Terms of use / automated collection permission were not independently verified: no Terms/legal link was exposed by the homepage or promo-page link scan. This is recorded as unknown, not as permission or a block.
- [ ] Current catalog content, updating-in-place behavior, period dates, product prices, images, and source-level geographic scope were not verified in this attempt. The national catalog label and its 29 province-location entries do not prove an individual offer is nationwide.
- [x] No retry, guessed URL, hidden endpoint, login, CAPTCHA, proxy, or bypass. No `last_verified_at`, catalog, feed or index data changed. Hypermart ID is configured for IDR. A scan of active non-audit highlight JSON found **0** references to `hypermart-national-live`.

## 2. Product Highlights

- [ ] No current product offer was inspected, accepted, or rejected. Same-item normal/promo pair, exact item image, offer validity, and item-level geography remain unknown. No claim is made that Hypermart has no promotions.
- [x] No active highlight reference was found for this `catalog_id`; no item expired/deleted. Neither catalog nor product expiry is proven by this attempt.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — public page access succeeded and canonical URL matched, but the offer content was not retained/verified and Terms permission remains unknown.
- [x] Source classification for current offer claims: **STALE_UNVERIFIED**. HTTP 200 and an old verification timestamp do not establish current promotional content or obsolescence.
- [x] Accepted product IDs: none. Expired IDs deleted: none. Production JSON changes: none.

## Compact handoff (≤400 words)

- Work unit `ID:hypermart-national-live`, catalog array position 3/74, frozen manifest ordinal 29/74. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`. Terminal receipt: `SKIPPED_UNVERIFIED`.
- Exact registered URL <https://www.hypermart.co.id/promo-katalog-hypermart/> was requested once: HTTP 200, HTML UTF-8, 156,746 bytes; canonical URL matched. Only response metadata and canonical link were retained, not promo cards or product data. Redirect/final `ResponseUri` was not exposed. The host robots file returned HTTP 200 / 30 bytes and sets `Crawl-delay: 30`; all follow-up requests were separated by at least 30 seconds.
- The active record has no `valid_until`, says national coverage, contains 29 province locations and retains `last_verified_at: 2026-08-22T01:00:00+08:00`. `www.hypermart.co.id` is allowlisted; IDR is configured. No active highlight JSON references this catalog ID. No price pair, image, current period, item geography, expiry or obsolescence was verified. No Terms link was found in homepage/promo link scans; automated-access permission remains unknown.
- No production JSON changed. Next manifest work unit is `ID:indogrosir-location-live` at <https://indogrosir.co.id/promosi>. Continue in a fresh isolated context.
