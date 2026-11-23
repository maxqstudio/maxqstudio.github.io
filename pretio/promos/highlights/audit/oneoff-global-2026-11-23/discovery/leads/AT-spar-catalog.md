# Austria — SPAR Catalog Promo lead (audit only)

- Run: `pretio-oneoff-global-20261123T040625Z`; selected market: Austria (AT), rank 44/174.
- Lead from the already-used single AT Catalog Promo search query `Austria supermarket Flugblatt Angebote Prospekt official 2026 grocery`: `https://www.spar.at/aktionen`. Search output identified it as SPAR Österreich's flyer/offers page; search-result text is discovery only and is not used as source evidence.
- Robots check: `GET https://www.spar.at/robots.txt` returned HTTP 200. The `User-agent: *` section has a blank `Disallow`, so no path restriction was found for this lead. It also lists `https://www.spar.at/index.sitemap-index.xml`.
- Exact source attempt: one time-bounded `GET https://www.spar.at/aktionen` at approximately `2026-11-23 09:23 UTC` returned HTTP **403 Forbidden**. The client did not expose a successful response body or final URL. No retry, alternate host, guessed Terms URL, login, CAPTCHA, proxy, or bypass was attempted.
- Since the page was blocked, ownership and Terms-based permission could not be independently checked from the source; current promo content, canonical stability/history, exact flyer validity, products/prices/images, and participating geography were not verified. The source was not treated as a qualified national catalog.
- Disposition for this source: **`SKIPPED_BLOCKED`**. The denial is not evidence that SPAR has no promotions or that an existing catalog is obsolete. No price evidence was retained, no Product Highlight candidate was accepted, and no production data changed.
