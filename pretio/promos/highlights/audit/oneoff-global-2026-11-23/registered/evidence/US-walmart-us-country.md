# Walmart US — source evidence

Run: `pretio-oneoff-global-20261123T040625Z` (`ONE_OFF_GLOBAL`)  
Work unit: `US:walmart-us-country` (manifest position `72/74`)  
Catalog: `walmart-us-country`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Audit date: `2026-11-23 UTC`; exact HTTP request timestamps were not retained.

## Source identity and robots

- Frozen manifest and accepted record agree on `https://www.walmart.com/shop/deals/shop-advertised-deals`. The record lists `www.walmart.com` in `allowed_hosts`, country `US`, national label “United States (store-selected offers),” and `valid_until: null`.
- One GET to the official [`robots.txt`](https://www.walmart.com/robots.txt) returned HTTP 200 (`text/plain`). Under `User-agent: *`, the file does not disallow the registered `/shop/deals/shop-advertised-deals` path or the linked Help/Terms paths. Its listed exclusions (including `/search`, `/api/`, and selected store/API paths) were not used.
- One GET to the registered URL returned HTTP 200, final URL unchanged, `text/html; charset=utf-8`, title `deals shop advertised deals - Walmart.com`. This supports the page/domain identity, not item freshness or offer scope.

## Terms and permission

- The registered page linked to the official [Walmart.com Terms of Use](https://www.walmart.com/help/article/walmart-com-terms-of-use/3b75080af40340d6bbd596f116fae5a0) (HTTP 200; title `Walmart.com Terms of Use`). The Terms restrict automated retrieval/collection and prohibit collection/use of product listings, descriptions, or prices, along with reuse of site materials, without express permission. They limit the materials license to personal, non-commercial use and restrict commercial third-party availability.
- The page also exposed a Walmart+ terms link; that URL's title was `Walmart+ Terms of Use` and it was not treated as the applicable general site terms.
- Walmart's official [Agentic Access Terms](https://www.walmart.com/help/article/walmart-agentic-access-terms/d048fc229d7549738d7c05a4317e24d7) (October 21, 2026 version, surfaced by Walmart-domain search) limit Walmart Proprietary Data to an authorized customer's shopping purpose and prohibit systematic/bulk collection or storage, commercial analytics/reporting, and redistribution. This Pretio audit is not a customer-authorized shopping interaction. No written Walmart permission or applicable authorization for Pretio catalog collection/reuse was located.

## Bounded-attempt note

The registered page was fetched once before the linked general Terms were reviewed. After discovering the restriction, no further offer-page access or product-level extraction was performed. The only retained page facts are response metadata/title and terms links; no product names, offer dates, geographic claims, prices, or images were recorded in audit artifacts. No raw HTML or screenshot was saved. No retries, login, user-agent changes, CAPTCHA handling, hidden endpoint, proxy, or access bypass were used.

## Decision

`SKIPPED_BLOCKED`. Do not inspect or reuse Walmart listing, price, or image content in this run absent Walmart authorization. The catalog remains `STALE_UNVERIFIED`: the one response does not establish current offers, nationwide item availability, expiry, or obsolescence. Preserve the accepted catalog record and its `last_verified_at`; no production feed/index update or deletion is justified.
