# Evidence — TR:a101-tr-country

- Run: `pretio-oneoff-global-20261123T040625Z`; scope `ONE_OFF_GLOBAL`; frozen manifest position `65/74`; attempt `1`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Checked: `2026-11-23T10:37:14Z` (UTC). Work was limited to this registered A101 unit.
- Registered source: https://www.a101.com.tr/liste/aldin-aldin (A101, official_retailer; catalog host is on the accepted allowlist; country rule `TR`/Türkiye; national catalog label; `valid_until: null`; last verification in source record `2026-09-28T00:00:00Z`). The same official host's membership agreement identifies Yeni Mağazacılık A.Ş. as A101 and describes the site/content (including text, pictures and catalog files); this supports official ownership of the domain/content, not permission to republish it.

## Bounded access / currentness

- A normal open of the registered page exposed only a page shell/iframe, without catalog items, source dates or coverage details. A bounded attempt to inspect the page body returned 403 Forbidden. No alternate user-agent, browser, endpoint, login, or access workaround was used; no further fetch was made.
- `https://www.a101.com.tr/robots.txt` did not expose readable directives: its first rendering showed only an ASCII-art header; follow-up reads/lookups returned 403. Robots permission for the registered path is therefore **unverified**, not assumed allowed.
- Official agreement: https://www.a101.com.tr/sozlesmeler/uyelik-sozlesmesi. The publicly visible agreement defines site content to include images/catalogs/data; §§4.11–4.12 reserve IP rights to A101 and prohibit copying/reproducing/distributing/sharing content; §4.18 prohibits automated devices/programs/processes for accessing, obtaining, copying, monitoring, querying or reproducing site content. No separate public license or permission for Pretio reuse was found. Because permission is absent and the terms state restrictions, no product-detail or image retrieval/reuse was attempted.
- Search-index snippets were discovery-only and stale/insufficient for current verification; third-party flyer pages are not A101 price/date evidence. No source-backed current start/end date, exact item prices, product variant, or product-level national participation was established as of the check time. The catalog's national location rule alone cannot prove individual offer coverage.

## Disposition

- No products accepted or rejected by item ID; zero item pages/images reviewed. This is not `NO_PROMO_FOUND`.
- TR has no currency entry in `pretio/data/currency.json`, independently blocking any Product Highlights publication. No `TR.json` feed exists and no feed referenced `a101-tr-country`.
- No production JSON, catalog URL, dates, image, feed, shared progress file, or terminal-receipts file changed. Inaccessibility and missing dates do not prove the catalog is obsolete; retain its active record as `STALE_UNVERIFIED` pending an authorized verification route.

