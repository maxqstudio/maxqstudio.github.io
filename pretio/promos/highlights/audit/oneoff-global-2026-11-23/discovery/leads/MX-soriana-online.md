# Mexico (MX) online-shop lead — audit only

- Run: `pretio-oneoff-global-20261123T040625Z`; source lead from the single Mexico online-shop query: <https://www.soriana.com/static-pages/static-page-faq.html>.
- Checked 2026-11-23 UTC. Search budget is spent; no additional search or alternate product/order page was requested.

## Access and permission

- Read <https://www.soriana.com/robots.txt> first. The public file was returned as `text/plain` with 40 lines. `User-agent: *` disallows checkout, account/cart, search-filter and other listed paths; it does not list `/static-pages/static-page-faq.html` as disallowed. The wrapper did not expose an HTTP status or final URL.
- The exact FAQ URL returned readable HTML (`text/html`, 299 lines; HTTP status and final URL were not exposed). It exposed the linked site terms URL <https://www.soriana.com/static-pages/terminos-y-condiciones.html>; that page returned readable HTML (`text/html`, 734 lines). The terms identify the site as operated by Tiendas Soriana S.A. de C.V. and govern use of the site. The terms page also states that Soriana intellectual-property elements require written authorization for use.
- Attempts to check the terms for automated access/robots/extraction language (`automatizado`, `robots`, `scraping`, `extraer`, `uso comercial`) all timed out in the web wrapper. Therefore automated-access permission is **unverified**. No inference of permission was made from the robots file alone.

## Qualification and handoff

- The FAQ is an official Soriana online-shopping information page, but this audit cannot qualify it for crawling or source reuse while applicable access terms remain unverified. Do not use its delivery/pricing statements or any site content as a Product Highlight source in this run.
- No product/order page, item, price, image, promotional period, or current offer was opened or retained. No delivery coverage claim is made; the FAQ lead is not counted as verified market coverage.
- Disposition: **`SKIPPED_UNVERIFIED`** due to unavailable confirmation of automated-access permission. This is not evidence that Soriana's online shop or promotions are absent. No registration, product data, or production file changed.
