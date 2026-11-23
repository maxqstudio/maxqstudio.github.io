# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `CL:unimarc-country-cl` | catalog array position: **13/74** | frozen-manifest ordinal: **not supplied** | Attempt: **1**  
Country: **CL** | Retailer: **Unimarc** | Mode: **AUDIT**  
Source request window: **2026-11-23T04:45:31Z–04:45:34Z**  
Catalog/feed snapshot read: **2026-11-23T04:47:06.037Z**  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_BLOCKED**

## 1. Catalog Promo source

- [x] Loaded active entry `unimarc-country-cl`: `official_retailer`, Chile / CL, national catalog label, `valid_until: null`, `last_verified_at: 2026-09-14T00:00:00Z`.
- [x] Registered URL: <https://www.unimarc.cl/page/catalogo>. Its exact host `www.unimarc.cl` is currently present in `catalog_app.json.allowed_hosts`; no host migration was staged.
- [ ] Robots permission could not be verified. A public HTTPS GET to <https://www.unimarc.cl/robots.txt> returned body text “Access Denied” and an Akamai error reference. The local capture output did not retain HTTP status, content type, byte count, Location, or final URL, so no robots directives or redirect chain can be asserted.
- [ ] The registered catalog URL was requested once over HTTPS. Its body also stated “Access Denied” and contained an errors.edgesuite.net reference. HTTP status, content type, byte count, Location, and final URL were not captured. This is an access block, not evidence of catalog obsolescence. The response did not expose a usable page or terms link; no terms page or parent fallback was requested. A parent fallback was not justified because a dead/404 response was not established.
- [x] No retry, login, CAPTCHA, hidden endpoint, cookie, proxy, or bypass was used. Requests were time-bounded; total script elapsed time was about 1.06 seconds. One robots request and one registered-URL request only.
- [x] No production catalog field, host allowlist, `last_verified_at`, country feed, or index was changed.

## 2. Product Highlights

- [x] CL metadata is `CLP`; `CL.json` has 24 existing items, including 4 referencing Unimarc (snapshot above).
- [ ] No current offer content was accessible. No product candidate was observed, accepted, or rejected; this does **not** establish that Unimarc has no promotions.
- [ ] No same-product public normal/promo pair, individual decodable image, product-level Chile-wide eligibility, or source-backed validity was verified. The national catalog label alone is insufficient for a country-wide product highlight.
- [x] No expiry or catalog obsolescence was proven. Existing four Unimarc highlights remain untouched and unverified by this attempt; no feed pruning or new item is staged. The growth target was unmet because the source was blocked, not because a complete catalog showed no promotions.

## 3. Skip decision

- [x] **SKIPPED_BLOCKED** — robots and registered-page bodies explicitly reported “Access Denied”; usable HTTP/header metadata and catalog content were unavailable. Treat the catalog as stale/unverified for this attempt, not obsolete.
- [x] No accepted product IDs; no expired IDs deleted; no production JSON changes.

## Compact handoff (≤400 words)

- Work unit `CL:unimarc-country-cl`, catalog array position 13/74; frozen-manifest ordinal was not supplied. Terminal receipt: `SKIPPED_BLOCKED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- One public robots request (<https://www.unimarc.cl/robots.txt>) and one registered URL request (<https://www.unimarc.cl/page/catalogo>) were made in the 04:45:31–04:45:34Z window. Both bodies said “Access Denied” and included an Akamai/error reference. The local response wrapper did not expose status, content type, byte count, Location, or final URL; redirects therefore remain unknown. Robots rules and terms were not verified. No terms, product, image, or parent page was requested; no retries or bypasses.
- The registered host `www.unimarc.cl` is allowlisted. CLP is configured; the CL feed contains 24 items, of which 4 reference Unimarc. No candidate price pair, matching individual image, country-wide product eligibility, or source-backed validity could be checked. Accepted/rejected: 0/0 observed; this does not imply no current offers.
- No expiry/obsolescence was proven. Existing feed items remain untouched and unverified. No catalog, feed, or index JSON changed.
- Next input: next unit from the immutable run manifest; its ordinal/order was not supplied here. Continue in a fresh isolated context.
