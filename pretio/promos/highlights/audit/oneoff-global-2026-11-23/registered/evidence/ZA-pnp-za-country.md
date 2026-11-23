# Pick n Pay South Africa — source evidence

- Run: `pretio-oneoff-global-20261123T040625Z`
- Base/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`
- Work unit: `ZA:pnp-za-country` (74/74)
- Observed UTC: approximately `2026-11-23T10:55–10:56Z`
- Retrieval: one bounded source check; no product-level URLs, queries, APIs, listings, or images were opened.

## Official source and access policy

- Accepted catalog URL: <https://www.pnp.co.za/catalogues>.
- One direct page view returned only a JavaScript loading shell (“Loading” / “Please enable JavaScript to continue using this application”). It showed no catalog title/date range, offer or geography. No JavaScript rendering or retry was performed.
- Official robots file: <https://www.pnp.co.za/robots.txt>. One public GET returned `200 text/plain`. It says `Request-rate: 1/10`, `Crawl-delay: 10`, and `Visit-time: 0400-0845` UTC; disallowed paths include cart, checkout, account, search and lists. The requested path `/catalogues` is not among those path disallows.
- **Timing deviation:** the canonical page and two candidate terms URLs (`/terms-and-conditions`, `/terms`) were opened at approximately 10:55 UTC, before the robots window was known; the robots file was read at approximately 10:56 UTC. These attempts were outside its stated visit window. The direct page views for the candidate terms paths were reported inaccessible. No further PnP direct access was made after the schedule was discovered.
- No terms clause or license permitting Pretio's commercial extraction/reuse of offer data or product imagery was verified. The official <https://www.pnp.co.za/returns-policy> search result says that policy forms part of “Pick n Pay (PnP) Online and General Terms and Conditions,” but does not supply an applicable data/image reuse license. Permission is therefore **unverified**, not presumed.

## Catalogue period and area

- A search index surfaced this first-party PnP CDN PDF URL: <https://cdn-prd-02.pnp.co.za/media/2026/catalogues/week37/BLWCHS15872_09112026_29112026_Pinelands.pdf>. Its indexed title states “Prices Valid 9–29 Nov 2026” and its filename identifies `Pinelands`.
- This PDF was not opened directly; its link from the canonical catalog landing page was not verified. The search-index content is a discovery lead only, not accepted price or image evidence, and does not prove the full catalog is current or nationally applicable. No products or price pairs were copied from it.
- The accepted catalog record's summary says offers can vary by store and region. The Pinelands lead further prevents treating a local edition as nationwide; no official national participation proof was obtained.
- Canonical catalog `valid_until` and `last_verified_at` are both null. The URL's shape alone does not prove its content currently updates in place. No source expiry or obsolescence was established.

## Existing feed and verdict

- The local accepted ZA feed has two PnP offers with `valid_until: 2026-11-29`. On the South African market date `2026-11-23`, these dates are not past. This task did not reverify their prices, imagery, or source pages and did not change or delete them.
- Product listings inspected: 0. Prices/images inspected or reused: none. New verified discounts: none.
- Status: `SKIPPED_BLOCKED` for this bounded attempt. Catalog classification: `STALE_UNVERIFIED`, not proven obsolete. Keep catalog/feed unchanged and do not claim these offers were refreshed.
