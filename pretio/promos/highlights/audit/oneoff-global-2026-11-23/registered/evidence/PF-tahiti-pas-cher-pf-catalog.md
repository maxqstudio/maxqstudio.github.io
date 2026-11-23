# Source evidence — Tahiti Pas Cher

Run: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PF:tahiti-pas-cher-pf-catalog` (50/74)  
Observed date: `2026-11-23`; source request timestamps were not returned by the clients. Evidence note recorded `2026-11-23T10:07:34Z`.

## Public access and ownership

- `https://www.tahitipascher.pf/robots.txt` — standard HTTPS request with `User-Agent: PretioCatalogAudit/1.0`; HTTP 200, `text/plain; charset=utf-8`. Wildcard disallows logs, WooCommerce transient/upload paths, cart query parameters and `/wp-admin/`; the registered catalog path is not disallowed.
- `https://www.tahitipascher.pf/` — HTTP 200, `text/html; charset=UTF-8`, final URL unchanged. The page title identifies Tahiti Pas Cher in French Polynesia. Its official links include the catalog and contact pages.
- `https://www.tahitipascher.pf/catalogue-du-moment/` — HTTP 200, final URL unchanged, `text/html; charset=UTF-8`, 191,557 bytes read by the bounded public request. Browser text view showed title “DÉCOUVREZ LE NOUVEAU CATALOGUE DU MOMENT”; page states the catalog is regularly updated and that featured products are available in five Tahiti stores, with shipping to French Polynesian islands. No dated flyer or `valid_until` appeared.
- `https://www.tahitipascher.pf/mentions-legales/` — official legal notice, opened from a bounded official-domain search. It identifies SARL SDE / Tahiti Pas Cher as site owner and describes information as indicative and subject to change. It says site selections concern products sold in the stores. No explicit automated-crawling or commercial-reuse license/prohibition was found in the checked text.
- `https://www.tahitipascher.pf/CGV/` — official sales conditions. It says there is no website sale/payment; visitors request a quote and the sales team provides availability and final pricing. It states island delivery is arranged across French Polynesia's archipelagos, with freight charged to the customer. No explicit crawler/reuse rule was found in the checked text.
- Official bounded search used to locate the legal page: `site:tahitipascher.pf ("conditions générales" OR "mentions légales" OR "politique de confidentialité")`. Search result was discovery only; the legal page itself was opened before using its details.

## Product, price and location evidence

- The catalog page exposed two generic newsletter graphics: `https://www.tahitipascher.pf/wp-content/uploads/post-Newsletter-TPC-072020-copie-3.jpg` and `https://www.tahitipascher.pf/wp-content/uploads/titre-newsletter-449px.png`. They do not identify a product variant or provide an individual product image plus a normal/promo price pair. The `072020` substring is only an asset filename; it is not treated as a validity date.
- No specific product price pair or offer expiry was captured. Final pricing requires a quote per the official CGV, so no public price was treated as verified.
- The page's general store/delivery statement is not item-level proof that an individual discount is available in every part of PF. PF has no currency mapping in the current highlights metadata and no country feed/index entry. Local scan found zero highlight references to this catalog ID.

## Outcome

Classify the source link `EVERGREEN_CURRENT`; terminal work-unit status is `SKIPPED_UNVERIFIED` because no publishable product evidence or price pair was verified and no explicit content-reuse authorization was found. Keep the registered entry active and unchanged. No expired product or obsolete catalog evidence; no production JSON changes.
