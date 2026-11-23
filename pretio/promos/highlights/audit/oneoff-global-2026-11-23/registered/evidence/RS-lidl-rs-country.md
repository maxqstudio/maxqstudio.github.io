# Source evidence — RS:lidl-rs-country

Run: pretio-oneoff-global-20261123T040625Z | Checked: 2026-11-23T10:31:04Z

Frozen manifest source: https://www.lidl.rs/c/online-letak/s10019338

## Bounded check

A single official landing-page retrieval, one robots retrieval, and a limited official-site legal/terms lookup were used. No retry, item-link navigation, PDF access, image request, alternate route, login, or bypass was used.

- The registered page was returned from the same https://www.lidl.rs/c/online-letak/s10019338 URL. The public page lists weekly offer links labeled 19.11. - 25.11. and 26.11. - 2.12. on the Online letak page. No year is included in either label. The extraction metadata said “Crawled: today,” but the date text itself does not prove a year or product-specific validity period.
- Robots: https://www.lidl.rs/robots.txt. The retrieved text is User-agent: * and disallows /q/search?id=*, /cc.js*, root paths /1* through /9*, and /cdn/assets/cwv/; it names https://www.lidl.rs/static/sitemap.xml. There is no disallow line matching /c/online-letak/. The public retrieval metadata says the robots copy was crawled four weeks ago, so this single check cannot establish the current directives. No second robots request was made.
- Official General Information: https://www.lidl.rs/c/opste-informacije/s10018393. It names Lidl Srbija KD in Nova Pazova, Serbia, as the technical operator for lidl.rs and responsible for transmitting store offers.
- Official Lidl Plus terms: https://www.lidl.rs/c/uslovi-koriscenja/s10019528. The retrieved page identifies the terms as status November 2026 and says Lidl Plus participation is for private purposes. Those terms concern Lidl Plus; they do not expressly license commercial republication of online-leaflet content or product images. No affirmative commercial content/image reuse permission was found. The separate general terms result did not expose a reuse grant either.

## Result

The registered evergreen landing URL and Serbian market are supported. The listed weekly date ranges omit the year, so no catalog expiry or current product dates are inferred. The official source does not itself establish nationwide item-level participation; no product geography was checked. Because commercial reuse permission was not established and the available robots copy is stale, no leaflet, product listing, price, or image was opened or copied. Zero products were examined; this is not evidence that the catalog has no promotions.

The existing RS.json feed contains seven Lidl highlights, each with null valid_from and valid_until and observation time 2026-11-23T02:49:37Z. This source attempt does not prove those offers current or expired. No production catalog, feed, index, receipt aggregate, or shared run progress file was changed.