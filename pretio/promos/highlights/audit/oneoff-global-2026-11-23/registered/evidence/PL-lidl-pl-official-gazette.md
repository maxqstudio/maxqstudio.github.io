# Lidl Polska source-access evidence

Run: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PL:lidl-pl-official-gazette`  
Observed date: `2026-11-23` (request timestamps not retained by the web connector)

## Observations

1. Robots: <https://www.lidl.pl/robots.txt> — HTTP 200, `text/plain`. The `User-agent: *` rules disallow `/cc.js*`, `/cdn/assets/cwv/`, `/user-api/*`, `/cqe/*`, search-query paths and several query parameters. No rule matched `/c/nasze-gazetki/s10008614`.
2. Official home page: `https://www.lidl.pl` — web connector returned a fetch error (400). No catalog content was retained.
3. Bounded legal-terms discovery query: `site:lidl.pl "warunki korzystania" "Lidl" serwis`. It returned the first-party PDF <https://www.lidl.pl/static/assets/c2e4f1e0-a6f5-4c48-ad14-d0eabc8c5097.pdf>, `IV. Warunki korzystania z Usługi`.
4. The opened PDF states it applies exclusively to “Moje Konto Lidl” and not to separate online Group Lidl service agreements (sections I.6 and IV.14, rendered lines 13–14). It says commercial use of that account service is not allowed (IV.2, line 47). It identifies separate terms for individual online services, including the Lidl online shop terms at <https://www.lidl.pl/c/regulamin-sklepu-internetowego-lidl/s10000906>.
5. The web connector could not render that linked terms page (400). One direct standard HTTPS GET to the same URL returned HTTP 200 HTML. The capture summarized only the start of the HTML/JSON-LD and did not preserve the terms text; therefore the content reuse policy for the flyer/catalog remains unverified.

## Decision

No access bypass, TLS bypass, login, or alternate route was used. The exact catalog page was not opened after the terms check failed to establish permission. No product, price, image, date, or offer claims were retained. Status: `SKIPPED_UNVERIFIED`, catalog `STALE_UNVERIFIED`; no production change.
