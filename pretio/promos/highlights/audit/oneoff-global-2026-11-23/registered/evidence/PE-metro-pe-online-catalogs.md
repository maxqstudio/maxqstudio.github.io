# Metro Perú Catalogos — source evidence

- Run: `pretio-oneoff-global-20261123T040625Z`
- Work unit: `PE:metro-pe-online-catalogs` (46/74)
- Checked date: 2026-11-23. Exact HTTP/web request times were not exposed by the connectors; checkpoint recorded at 2026-11-23T09:59:10Z.
- Baseline and skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`

## Official ownership and access

- Registered promo URL: <https://www.metro.pe/catalogos>
- One direct public GET returned HTTP 200, `text/html; charset=utf-8`, 1,966,264 bytes. The page title and Open Graph title were `Catálogo de Ofertas`; canonical/Open Graph URL was the same `https://www.metro.pe/catalogos`.
- The page's metadata identifies Metro.pe, author Metro.pe, country `PER`, language `es-PE`, currency `PEN`. The frozen catalog record identifies publisher `Cencosud Retail Perú S.A.` and national Peru coverage.
- `GET https://www.metro.pe/robots.txt` returned HTTP 200 `text/plain`. `User-agent: *` disallows `/img/*`, `/account/*`, `/login/*`, `/checkout/*`, `/quick-view/*`, `/espiar/*`, and `/buscapagina/*`; it does not disallow `/catalogos`. The file allows `/colecciones/*` and lists the official sitemap URLs. No blocked route was accessed.
- Official terms: <https://www.metro.pe/institucional/terminos-y-condiciones/>. The public page was opened and states access/use are governed by its terms and Peruvian law, naming Cencosud Retail Perú S.A. as Metro. It was last updated 10/03/2026. Searches within the opened terms for `propiedad intelectual`, `reproducción`, and `robots` had no matching text. No explicit crawler/commercial-reuse permission or prohibition was established; mark permission as **unverified**, not as a confirmed block.

## Current promo content and limits

- The registered route is a stable, official catalog landing URL; the source record has `valid_until: null`. The direct page response included an eight-slide `sliderCatalogo` carousel, but its server-rendered slide titles and image `src`/`alt` values were empty. Embedded content contained a legacy “Aniversario 31 años Metro” title dated 12 Oct–1 Nov 2023. That old embedded string does not establish a current promo or prove the evergreen landing route is obsolete.
- No current flyer title/date, item-specific normal/promo price pair, product identity, individual image, or current offer geography could be verified from the permitted page content. No product evidence was accepted or retained; the search result snippet was not used as offer proof.
- No PE Product Highlights feed or currency mapping exists in this baseline, and a full scan of existing highlight feeds found zero references to `metro-pe-online-catalogs`.

No production catalog, highlight, index, currency, or location data was changed. Preserve the catalog as `STALE_UNVERIFIED`; do not infer expiry from its old `last_verified_at` or the legacy 2023 embedded carousel content.
