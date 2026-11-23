# Brazil — Atacadão catalog lead (audit only)

- Run: `pretio-oneoff-global-20261123T040625Z`; scope: `ONE_OFF_GLOBAL`.
- Lead from the single Brazil Catalog Promo search: <https://www.atacadao.com.br/folheto/14-sqA8x5KiIMas0y7gToN8VnkH8VdPOz>. Search-result title identified an Atacadão promotional leaflet, but source ownership/content was not independently confirmed in this source attempt.
- Before requesting the flyer, sent one bounded public GET to <https://www.atacadao.com.br/robots.txt> (`2026-11-23`, about 06:07 UTC; 15-second timeout, maximum three redirects). It returned **HTTP 403 Forbidden**. The local wrapper retained only the status and generic error; response body, Content-Type, byte count, final URL and redirect chain were not captured.
- **Terminal disposition: `SKIPPED_BLOCKED`** — robots access was denied, so permitted access could not be established. Stopped without requesting the flyer or Terms page; no retry, login, alternate host, hidden endpoint, or bypass was used.
- No official offer content, catalog period, national/store coverage, product, price pair, image, or expiry was verified. The search-result excerpt is not used as product evidence. This does not establish catalog obsolescence or absence of current offers. No production data changed.
