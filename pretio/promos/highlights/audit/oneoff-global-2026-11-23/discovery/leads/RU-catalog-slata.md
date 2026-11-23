# Russia (RU) Catalog Promo lead — source-only evidence

- Run: `pretio-oneoff-global-20261123T040625Z`; baseline/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Single market-search lead supplied to this isolated source check: <https://slata.ru/promotions/>. It was not requested.
- Checked 2026-11-23 UTC; exact per-request timestamps were not retained by the terminal wrapper.

## Access and ownership checks

- One GET to <https://slata.ru/robots.txt> returned HTTP **404 Not Found**. The response did not provide robots directives; absence of the file is not treated as permission.
- One GET to the official-looking homepage <https://slata.ru/> returned HTTP **200**, `text/html; charset=utf-8`, 136,989 UTF-8 bytes. The title was `Слата — сеть супермаркетов`, supporting that Slata presents itself as a supermarket chain. The final response URL was not captured by the wrapper.
- The homepage link scan exposed a PDF named “Personal Data Processing Policy”; it did not expose a promotions/use-terms link. That policy was not fetched, and no terms page was identified or verified. No specific permission for automated retrieval could be established.
- Following the source-only task instruction, the promo page was not opened. No URL, file ID, hidden API, alternate host or query parameter was guessed. No retry, CAPTCHA, login or bypass was used.

## Qualification and handoff

- No Catalog Promo content, current campaign dates, product prices, normal-price comparisons, product images, terms, or offer geography were inspected. The market search snippet is not used as product evidence.
- Disposition: **`SKIPPED_UNVERIFIED`** because robots directives and applicable automated-access terms could not be established before opening the promotions page. This is not evidence that the page is blocked, stale, or expired, and it is not evidence that Russia lacks official promotions.
- This lead cannot support a verified country-coverage count or Product Highlight. No source registration, feed/catalog change or production-data write occurred. The market's one Catalog Promo query budget is spent for this run.
