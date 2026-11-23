# One-off country discovery checkpoint — Brazil (BR)

- Run: `pretio-oneoff-global-20261123T040625Z`; market rank 32/174; no registered Catalog Promo sources.
- Search budget used: one Catalog Promo query (`Brazil supermercado official ofertas folheto promoções encarte supermercado`) and one online-shop query (`Brazil online grocery ecommerce official supermarket delivery shop`). Exact search timestamps were not retained; sources were checked 2026-11-23 UTC.
- Catalog lead: <https://www.atacadao.com.br/folheto/14-sqA8x5KiIMas0y7gToN8VnkH8VdPOz>. Its robots request returned HTTP 403, so the flyer and Terms page were not opened. Evidence: `../leads/BR-atacadao-catalog.md`.
- Online-shop lead: <https://www.sondadelivery.com.br/>. Its robots request returned HTTP 403; homepage, terms, offers and delivery coverage were not opened. Evidence: `../leads/BR-sonda-online.md`.
- Both selected leads were stopped before offer retrieval. No current offer, geography, standard/discount pair, image, validity date, or catalog expiry was verified. No Product Highlight candidate accepted; no production data changed.
- Terminal bounded-market disposition: `SKIPPED_BLOCKED`. This is a source-access limitation, not evidence that Brazil lacks official retail promotions. Both search budgets are spent; no retry or alternate host was used.
