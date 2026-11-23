# One-off country discovery checkpoint — France (FR)

- Run: `pretio-oneoff-global-20261123T040625Z`; market rank 29/174; no registered Catalog Promo sources.
- Search budget used: one Catalog Promo query (`France supermarché officiel promotions catalogue prospectus offres semaine 2026`) and one online-shop query (`France courses en ligne supermarché boutique officielle livraison courses`). Exact search timestamps were not retained; source checked 2026-11-23 UTC.
- Catalog query returned a third-party offers directory, not an official merchant catalog; it was not opened.
- Online lead: Carrefour France groceries <https://www.carrefour.fr/courses>. Robots returned HTTP 200 and did not disallow `/courses`; one request to the exact URL returned HTTP 403. No retry or alternate route. Terms, prices, images, promotions and delivery area remain unverified. Evidence: `../leads/FR-carrefour-online.md`.
- No verified promotion or online product data; no Product Highlight candidate accepted and no production data changed.
- Terminal bounded-market disposition: `SKIPPED_BLOCKED` for the only official lead opened. This is not evidence that France lacks online shops or promotions; both query budgets are spent.
