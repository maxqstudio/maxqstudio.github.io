# Evidence — TR:migros-tr-country

- Run: `pretio-oneoff-global-20261123T040625Z`; scope `ONE_OFF_GLOBAL`; frozen manifest position `67/74`; attempt `1`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Checked: `2026-11-23T10:39:55Z`. This evidence is limited to the assigned registered Migros source.
- Registry snapshot: `migros-tr-country` is an active `official_retailer` catalog for Migros, publisher Migros, Türkiye country location, national label, and URL `https://www.money.com.tr/migroskop-dijital`. `www.money.com.tr` is in `allowed_hosts`. The record has null `valid_from`/`valid_until` and `last_verified_at: 2026-09-28T00:00:00Z`. No production field or date was changed.

## Identity, exact URL and currentness

- The registered HTTPS URL was opened once through the public web reader. Its reported page URL/title match the registered Migroskop page; the reader did not expose an HTTP status or redirect chain. It showed the official page section “Güncel Migroskop Dijital”, issue 911, dated 19 November–2 December 2026. The same page listed issue 910 for 5–18 November 2026 and earlier dated issues, consistent with an evergreen landing page whose catalog changes in place. This is page-level currentness only; it does not verify any item offer.
- The public page links its catalog viewer on `migroskop.migros.com.tr` and shopping on `www.migros.com.tr`. Neither was opened. A search response unexpectedly surfaced an unrequested result from the Migroskop viewer host containing product/price text. It was not opened, transcribed, retained as evidence, or analyzed for offers. No images were opened or fetched, and no hidden endpoints were used.
- One direct GET to `https://www.money.com.tr/robots.txt` returned HTTP 200, `text/plain`. It states `User-agent: *`, `Allow: /`, then disallows `/profilim`, paths containing `?id`, and paths containing `?t=`. `/migroskop-dijital` is not matched by those rules. Redirect metadata was not exposed for this robots response.

## Official identity and permitted use

- The page footer links the official [Money Membership Agreement](https://www.money.com.tr/mc/iletisim/money-uyelik-sozlesmesi/102). It names Migros Ticaret A.Ş. as owner of the Money Program and defines `www.money.com.tr` as the Money Site (sections 1–2, lines 46–67 in the public rendering). This supports Migros/Money ownership of the registered source.
- Section 3.7 says members must not use automated programs, robots, web crawlers, spiders, data-mining or screen-scraping systems to access/query/copy site content without Migros's prior written permission; it also restricts copying, publishing or using site content. The agreement is framed as a membership contract, so its application to anonymous public access is not explicit. No separate public crawl/content-reuse license or prior written permission was found. Robots allow the path, but that alone does not resolve the contractual restriction. After finding this restriction, no further site content was opened.

## Geography and disposition

- The registry describes the catalog as national in Türkiye, and the Money agreement limits member enrollment to people living in Türkiye with a Turkish phone number. Neither proves that individual leaflet offers participate nationwide. No item-level geography was established.
- No product candidate was accepted or rejected by item ID; zero item pages and zero product images were opened. The incidental search-result product/price text above was not used as offer evidence. `TR` is absent from `pretio/data/currency.json`; no `TR.json` feed exists and no production highlight references `migros-tr-country`.
- Catalog URL classification: `LINK_STABLE`; page-level current issue observed through 2 December 2026. Product/price/image reuse permission remains unresolved/restricted. Terminal disposition: `SKIPPED_BLOCKED` for product review. This is not `NO_PROMO_FOUND` and is not evidence of catalog obsolescence.
- No production JSON, shared `progress.json`, shared `terminal-receipts.json`, commit, push, retry, alternate endpoint, or schedule was changed or created.
