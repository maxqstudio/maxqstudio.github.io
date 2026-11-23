# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `CL:alvi-country-cl` | Position: `8 of 74` | Attempt: `1`  
Country: `CL` | Retailer: `Alvi` | Mode: `AUDIT`  
Checked UTC: `2026-11-23T04:24:41.779Z` (catalog response observation)  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: `SKIPPED_UNVERIFIED`

## 1. Catalog Promo source

- [x] Loaded active record `alvi-country-cl`: `official_retailer`, national coverage label `Chile`, country location CL, no `valid_until`, `last_verified_at: 2026-09-14T00:00:00Z`. Registered URL: <https://fe-browse-alvi-gcp-alvi-prod.alvi.cl/>.
- [x] Registered host `fe-browse-alvi-gcp-alvi-prod.alvi.cl` is in `catalog_app.json.allowed_hosts`.
- [x] Robots checked before page access. Requested/final <https://fe-browse-alvi-gcp-alvi-prod.alvi.cl/robots.txt> returned HTTP `200`, `text/plain; charset=UTF-8`, no redirect, 109 bytes. Excerpt: `User-agent: *` and `Sitemap: https://www.alvi.cl/sitemap.xml`; no `Disallow` directive was present.
- [x] Registered URL requested once at `2026-11-23T04:24:41.779Z`, with a 30-second timeout: HTTP `200`, `text/html; charset=utf-8`, no redirect, 323,799 response bytes. Excerpt: `<title>Alvi</title>`, `og:site_name="Alvi.cl"`, corporation name `Alvi`, and a home banner asset named `ALVI_BANNER_HOME_INSUPERABLE_DESK_CECINAS.webp`.
- [ ] Canonical/evergreen promo source not verified. The fetched page declares `<link rel="canonical" href="https://www.alvi.cl">` and `og:url="https://www.alvi.cl"`, which differ from the registered host. `www.alvi.cl` is not in the current allowed-host list and was not requested under this unit's one-page bound.
- [ ] Terms were not independently verified: no terms link/text was captured in the reviewed initial HTML excerpt, and no separate terms request was made. Do not infer a crawling rule from the robots file alone.
- [x] No login, CAPTCHA, alternate host fetch, hidden endpoint, proxy, or access-control bypass was used. Request count: robots 1, registered URL 1, terms 0, product pages 0; retries 0.
- [x] No `catalog_app.json` fields or `last_verified_at` were changed.

## 2. Product Highlights candidates

- [x] `CL` currency metadata and current feed use `CLP`.
- [x] No existing CL highlight references `alvi-country-cl`.
- [ ] No product offer was accepted or rejected: the reviewed excerpt contained no product-specific price pair, individual image, offer dates, or market-wide product eligibility. No product page or alternate source was opened. The home banner alone is not offer evidence.
- [x] No Alvi-dependent feed item was modified or pruned; no production feed/index/catalog JSON changed.

## 3. Disposition

Classify the registered source `STALE_UNVERIFIED` for current catalog content: the retailer identity is supported, but the canonical host differs and no product-level offer proof was captured. Final result: `SKIPPED_UNVERIFIED`. No claim is made that Alvi has no promotions or that its offers are expired.

## Compact handoff (≤400 words)

- Work unit `CL:alvi-country-cl`, position 8/74; terminal receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; this checkpoint covers only the assigned registered catalog.
- At `2026-11-23T04:24:40.458Z`, robots returned `200 text/plain; charset=UTF-8`, 109 bytes, no redirect; it had `User-agent: *`, no `Disallow`, and a sitemap link to `https://www.alvi.cl/sitemap.xml`. At `04:24:41.779Z`, the registered URL returned `200 text/html; charset=utf-8`, 323,799 bytes, no redirect. Each request had a 30-second timeout; no retries were needed.
- The response identifies the site as Alvi (`<title>Alvi</title>`, `og:site_name="Alvi.cl"`) but declares canonical and `og:url` as `https://www.alvi.cl`, not the registered host. That host is not allowlisted and was not fetched. No terms link/text was captured in the reviewed initial HTML excerpt, so terms remain unverified.
- The excerpt showed a home banner asset but no product-specific price pair, item image, date, or nationwide offer evidence. No candidate was accepted; no product page or hidden endpoint was opened. `CLP` is supported and the CL feed has no Alvi references. No production JSON changed.
- Evidence: <https://fe-browse-alvi-gcp-alvi-prod.alvi.cl/robots.txt> and <https://fe-browse-alvi-gcp-alvi-prod.alvi.cl/>. Next: continue to the next manifest unit in an isolated context.
