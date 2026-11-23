# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `CL:santaisabel-country-cl` | Position: `12 of 74` | Attempt: `1`  
Country: `CL` | Retailer: `Santa Isabel` | Mode: `AUDIT`  
Checked UTC: `2026-11-23T04:35:01.2338244Z` (official offers-page response completed)  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: `SKIPPED_UNVERIFIED`

## 1. Catalog Promo source

- [x] Loaded active record `santaisabel-country-cl`: `official_retailer`, coverage `national` / `Chile`, location country `CL`, `valid_until: null`, `last_verified_at: 2026-09-14T00:00:00Z`. Registered URL: <https://www.santaisabel.cl/santas-ofertas>.
- [x] Registered host `www.santaisabel.cl` is in `catalog_app.json.allowed_hosts`.
- [x] Robots checked first. <https://www.santaisabel.cl/robots.txt> returned HTTP `200`, `text/plain`, 179 bytes, no redirect; requested `2026-11-23T04:34:42.2681487Z`–`04:34:43.6454402Z`. `User-agent: *` allows `/`; disallows `/admin/`, `/api/`, `/_next/`, `/private/`, and `/home-qa`; it does not disallow `/santas-ofertas`. `Crawl-delay: 1` was respected.
- [x] Registered offers URL returned HTTP `200`, `text/html; charset=utf-8`, 1,901,306 bytes, no redirect; request `2026-11-23T04:34:58.2622860Z`–`04:35:01.2338244Z`. Page title: `Santas ofertas | Santaisabel.cl | Santaisabel.cl`; canonical URL matches the registered path. The undated landing path is stable in form and displayed current campaign content on this visit. A single observation cannot prove historical in-place rotation.
- [ ] Terms / conditions were not independently verified or fetched in this single bounded source attempt. No further source request was made.
- [x] Two GETs total (robots + offers), zero retries; each request had an 8-second timeout. Elapsed from first request start through offers response: `18.97s`, under 30 seconds. No login, CAPTCHA, bot bypass, hidden API, proxy, or alternate source was used.
- [x] No catalog record or `last_verified_at` was changed.

## 2. Product Highlights candidates

- [x] `CL` feed uses `CLP`, has 24 items; 5 currently reference `santaisabel-country-cl`. Country (80-item) and retailer (20-item) caps leave room.
- [x] The single public page response included server-rendered Santa Isabel product/offer data (`soldBy: santa-isabel`, `isMarketplace: false`) with explicit price fields and campaign text. Examples observed in the response:
  - `Detergente en Polvo Omo Matic Ultra Power 800 g`: `listPrice` CLP `4490`, `price` CLP `1990`; promo text includes `27 OCT AL 23 NOV` and `27102026 AL 23112026`.
  - `Galletas McKay Mantequilla 140 g`: `listPrice` CLP `990`, `price` CLP `650`; promo text includes the same October–November campaign.
- [ ] No candidate accepted. Individual image URLs use `santaisabel.vteximg.com.br`, which is absent from the approved image-host list; image bytes were not fetched or decoded. The official page and national Catalog Promo label do not prove country-wide eligibility of these online prices, and terms / nationwide fulfillment were not verified. No hidden endpoint or unapproved image host was fetched.
- [x] Inspection was limited to product excerpts visible in the single 1.90 MB initial HTML response; no pagination, categories, product details, or other source pages were queried. Tool output truncated the full response, so this was not an exhaustive enumeration of every offer on the page.
- [x] Existing Santa Isabel highlights have null `valid_until`; this attempt did not establish their expiry. No new candidate IDs, expiry deletions, feed, or index changes were staged.

## 2A. Catalog disposition

The registered URL is undated and has a permanent landing-page form, with current offer content observed. Classify `EVERGREEN_CURRENT` for this check; one visit does not prove a recurring update schedule. No replacement or retirement is supported.

## 3. Skip-or-update decision

- [x] **SKIPPED_UNVERIFIED** — the public page showed explicit same-seller CLP list/current price pairs, but no candidate passed the approved image-host and country-wide eligibility gates; terms were not verified.
- [x] No production data changed. Next manifest unit: `CL:tottus-country-cl`.

## Compact handoff (≤400 words)

- Work unit `CL:santaisabel-country-cl`, position `12/74`; terminal receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; this covers only the assigned catalog. Baseline/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Checked `2026-11-23T04:34:42.2681487Z`–`04:35:01.2338244Z`. Robots returned `200 text/plain`, 179 bytes, no redirect; wildcard rules allow `/santas-ofertas`, with `Crawl-delay: 1`. Registered <https://www.santaisabel.cl/santas-ofertas> returned `200 text/html; charset=utf-8`, 1,901,306 bytes, no redirect, title `Santas ofertas | Santaisabel.cl | Santaisabel.cl`. Two GETs total, 0 retries, 8-second per-request timeout, 18.97 seconds elapsed.
- The initial public HTML included Santa Isabel offers. Example Omo Matic Ultra Power 800 g: CLP `4490` list / `1990` offer, campaign text `27 OCT AL 23 NOV` / `27102026 AL 23112026`; Galletas McKay Mantequilla 140 g: `990/650`. These are observed examples, not accepted products.
- No candidate passed: product images point to `santaisabel.vteximg.com.br`, absent from `allowed_hosts`, and nationwide online eligibility was not established from this response. Terms were not independently verified; no terms or additional page was fetched. Inspection was limited to visible excerpts from one page response; output truncation prevents an exhaustive offer count.
- CLP is supported and feed caps have room. No production JSON changed; existing undated items were not marked expired. Next: `CL:tottus-country-cl`.