# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `ES:lidl-es-country` | manifest position: **27/74** | Attempt: **1**  
Country: **ES** | Retailer: **Lidl** | Mode: **AUDIT**  
Checked UTC: **2026-11-23** (exact request timestamps were not retained)  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_BLOCKED**

## 1. Catalog Promo source

- [x] Loaded frozen manifest record and active catalog `lidl-es-country`, Spain (`ES`), publisher Lidl España, `official_retailer`, national label. The exact registered URL is `https://www.lidl.es/c/descubre-nuevas-ofertas-cada-semana-folletos-lidl/s10087402`; `www.lidl.es` is allowlisted.
- [x] One public robots request to `https://www.lidl.es/robots.txt` returned HTTP `200 text/plain`. `User-agent: *` disallows `/cc.js*`, `/cdn/assets/cwv/`, `/user-api/*`, `/cqe/*`, search-query paths, and specified query parameters. The exact registered `/c/.../s10087402` path has no query and is not disallowed.
- [x] One request to the exact registered URL returned HTTP `200 text/html; charset=utf-8`, 191,528 UTF-8 bytes, no redirect reported; final URL and HTML canonical are the same registered URL. Page title: `Folletos Lidl: nuevas ofertas cada semana`. This supports a stable page URL, but the page's current flyer content was not inspected after the linked legal notice was found.
- [x] Followed the page's official `https://www.lidl.es/c/aviso-legal/s10075786` link. It returned HTTP `200 text/html; charset=utf-8`, 181,619 bytes. The notice states Lidl owns the site's intellectual-property rights, prohibits commercial reproduction/distribution/public communication of site content without authorization, and requires express consent for links to the portal from another website. No written consent is evidenced in this run.
- [x] **Stopped before examining flyer/product content** under those terms. No prices, products, images, offer cards, or replacement-period dates were collected. No guessed URL/API, alternate host, retry, login, CAPTCHA, proxy, or bypass was used.
- [x] No `last_verified_at`, catalog field, host allowlist, feed, or index was changed.

## 2. Expiry and Product Highlights

- [x] The existing active record is for `Folleto Alimentación 16/11`; its summary states it was valid **16–22 November 2026**. Its `valid_from` is `2026-11-16T07:00:00+08:00` and `valid_until` is `2026-11-23T07:00:00+08:00`, the midnight boundary after Nov 22 in Spain. The run date is Nov 23, so the *recorded period-specific flyer* has expired.
- [x] At the original attempt, the registered URL was self-canonical and its title described weekly flyers, but current in-place offers and an allowed successor were not verified under the linked terms. A later page-only audit confirmed that the hub now lists a 23–29 November flyer; see `deletion-audit.md`. Do not treat the URL's availability or title as proof that the expired flyer entry is current. The expired entry does not establish that Lidl's promotions page itself has been discontinued.
- [x] No ES highlight feed or ES entry exists in the highlights index; `currency.json` has EUR assigned to DE only, not ES. A product highlight is not publishable for ES under this baseline.
- [x] All seven existing country feeds were checked for `catalog_id: lidl-es-country`; **zero references** were found. No product IDs were expired/deleted, no product candidate was accepted, and no production JSON changed.

## 3. Skip decision and compact handoff (≤400 words)

- Work unit `ES:lidl-es-country`, manifest position 27/74; terminal receipt `SKIPPED_BLOCKED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; base/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- The robots file returned 200 and allows the exact registered path. That path returned 200 HTML, 191,528 bytes, self-canonical at `https://www.lidl.es/c/descubre-nuevas-ofertas-cada-semana-folletos-lidl/s10087402`, titled `Folletos Lidl: nuevas ofertas cada semana`.
- The directly linked legal notice `https://www.lidl.es/c/aviso-legal/s10075786` returned 200 HTML and restricts commercial reproduction/public communication of site content without authorization and linking to the portal from another website without express consent. No written consent is in this run, so I stopped before extracting or using flyer content. Exact request timestamps were not retained. No retry/bypass or product data was used.
- The active catalog record represents a dated flyer `16/11`, explicitly valid 16–22 Nov 2026. Its `valid_until` boundary is Nov 23 00:00 Spain local time. That period is expired as of the current Spain-local date. The original attempt did not verify current offers or a permitted successor; a later page-only audit confirmed the successor's listed period but did not inspect its offer content. Do not claim the page itself is obsolete solely from the expired record.
- No dependent highlights exist across the seven feeds, and ES has neither a highlight feed/index entry nor currency coverage. No catalog/feed/index JSON changed. Parent may resolve the expired active record in the final atomic candidate after policy/deletion review; there are no foreign-key dependents. Next manifest unit: `ID:alfamart-national-live`.
