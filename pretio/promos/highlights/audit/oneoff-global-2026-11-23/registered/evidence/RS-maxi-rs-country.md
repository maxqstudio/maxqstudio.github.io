# Source evidence — RS:maxi-rs-country

Run: pretio-oneoff-global-20261123T040625Z | Observed: 2026-11-23 10:33 UTC

## Registered record and scope

The frozen manifest entry is Maxi, catalog ID maxi-rs-country, Serbia (RS), https://www.maxi.rs/maxi-nedeljna-akcija, valid_until null. The accepted catalog record is official_retailer and its host is allowlisted. Its coverage label is “Serbia (location-selected offers)”; its summary says to select a city and address to see the offer valid for that location. The RS highlight feed has 27 entries, 8 referencing this catalog ID; these 8 have no valid_until and were not source-verified in this bounded attempt. RSD is configured.

## Official source checks

- Robots file: https://www.maxi.rs/robots.txt. The retrieved 38-line text has User-agent: *; it disallows account, registration, mobile, checkout, error and search routes. It does not disallow the registered /maxi-nedeljna-akcija path. No separate crawler group or Content-Signal directive was present in the returned text. The web retrieval tool did not surface status or request-level timestamps.
- Run-budget deviation: the robots URL was opened twice by mistake. The first web-tool call returned no body in the wrapper; a second identical call was made to display it. The duplicate did not change the inspected source or enable another route. This exceeds the run metadata's one robots check per unique host and is recorded here for coordinator review. No alternate user-agent, retry on a failure, login, hidden endpoint, or access workaround was used.
- Registered page, opened once: https://www.maxi.rs/maxi-nedeljna-akcija. The tool returned the title “Maxi nedeljna akcija,” HTML text, and the same displayed URL. Extracted content included Serbian navigation, “Odaberite termin za dostavu” (choose a delivery time), and a header notice about a 22 Nov 2026 delivery disruption. It exposed no catalog item, flyer, product date, or current offer. The notice and 2026 copyright are site-level context, not campaign dates. The tool did not expose HTTP status or redirect headers.
- Official company page: https://www.maxi.rs/delhaize-srbija. It identifies Delhaize Serbia društvo sa ograničenom odgovornošću, its Belgrade address, and company registry/tax identifiers. This supports operator identity for the Maxi site.
- Terms route: https://www.maxi.rs/usloviposlovanja. It was opened via an official-site link; extraction showed the page shell and “Uslovi poslovanja” breadcrumb but not the terms body. A footer link labeled “Uslovi kupovine” resolved to the same URL. Neither explicit permission nor an explicit prohibition on commercial reuse was observable. Treat reuse permission as unverified.

## Result

The registered page appears to be a stable-looking weekly-action route, but this one observation does not prove it updates in place or show a dated current cycle. The official seller is Serbian, but offers require location selection and the page does not establish that individual items are available across Serbia. Product and image review stopped because the current catalog and applicable reuse permission were not established. Zero products were checked; this is not evidence that no offers exist. No item prices, images, dates, or candidate records were retained. Keep the active catalog unchanged and classify it STALE_UNVERIFIED; do not infer expiry or obsolescence.
