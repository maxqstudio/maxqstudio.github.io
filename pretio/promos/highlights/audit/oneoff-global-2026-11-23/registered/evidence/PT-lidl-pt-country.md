# Lidl Portugal — source and offer evidence

Run: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PT:lidl-pt-country` (frozen manifest position 56/74)  
Observed/checkpointed: `2026-11-23` / `2026-11-23T10:18:40Z` UTC  
Mode: audit only; no production catalog/highlight write

## Source ownership and catalog status

- Registered official URL: <https://www.lidl.pt/c/folhetos/s10020672>. The public page is titled “Folhetos - Promoções e Novidades”; requested and rendered URLs match. The stable `/c/folhetos/` directory lists multiple leaflets and is currently populated, supporting `LINK_STABLE` / `EVERGREEN_CURRENT` for this catalog. No date-specific URL migration was proposed.
- Lidl Portugal’s official [Ficha Técnica](https://www.lidl.pt/c/ficha-tecnica-site-lidl/s10027346) identifies Lidl & Companhia as the technical operator of lidl.pt, based in Sintra, Portugal, and responsible for promoting in-store benefits on that site.
- Official [robots.txt](https://www.lidl.pt/robots.txt) returns `User-agent: *`; it disallows search-query paths, `/cc.js*`, numeric-leading paths `/1*`–`/9*`, and `/cdn/assets/cwv/`. The registered `/c/folhetos/s10020672` and linked `/l/pt/folhetos/…` flyer paths do not match those rules. No restricted path, login, CAPTCHA, private endpoint, or access-control bypass was used.
- The registered path is an evergreen directory and its catalog record has `valid_until: null`; the directory's current content does not establish a period expiry for the Catalog Promo entry.

## Current content and geography

- The official [Folhetos directory](https://www.lidl.pt/c/folhetos/s10020672) lists “Promoções Semanais A partir de 23/11” and “Promoções Fim-de-Semana A partir de 27/11”, plus special leaflets for Christmas, toys, Feira do Mar, Cien and Parkside tools. The official [Lojas e Horários page](https://www.lidl.pt/c/lojas-e-horarios/) labels its leaflet section “National”. These observations verify current Portuguese catalog content, not exact item prices or dates of offer end.
- The catalog record is country PT and its label reads “Portugal (location-selected offers)”. No item-level offer was reviewed, so no specific product is represented as nationwide or available in every store. No end date was inferred from a flyer start date.

## Terms and image reuse review

- The official [Termos e Condições page](https://www.lidl.pt/c/termos-e-condicoes-lidl-plus/s10026008?pageId=10026539/10058201/10026008) found through the site footer governs Lidl Plus. It limits that app/service to personal use and excludes commercial use; it is not a general website term for the public leaflet directory.
- An official [Lidl corporate policy PDF](https://institucional.lidl.pt/content/download/61362/file/Pol%C3%ADtica%20de%20compras_Cadeias%20de%20Fornecimento%20Livres%20de%20Desfloresta%C3%A7%C3%A3o%20e%20Convers%C3%A3o.pdf) states that the PDF and its own text, images, photographs and logos are protected and cannot be reproduced without written Lidl consent. This notice is specific to that document, so it is not treated as a blanket prohibition on website content.
- Bounded official-site navigation/search found no explicit grant permitting reuse of leaflet product imagery. Result: `REUSE_PERMISSION_UNVERIFIED`. Since the task allowed item price/image evidence only if permitted, item-level inspection stopped at the leaflet headings. No product names, exact prices, item dates, image URLs or image assets were collected or copied.

## Disposition

- Source: official, current, stable and robots-allowed.
- Product findings: **none collected**; no candidate can pass the exact price/image gate.
- Status: **SKIPPED_UNVERIFIED**. Keep the active catalog record; do not claim any flyer item is current beyond the visible start-date headings. No expired catalog or highlight item was proven. No production JSON changed.
