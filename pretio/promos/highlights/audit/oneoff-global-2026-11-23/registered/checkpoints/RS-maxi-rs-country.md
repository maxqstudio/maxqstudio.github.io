# Pretio — per-catalog update checklist

Run ID: pretio-oneoff-global-20261123T040625Z  
Work unit: RS:maxi-rs-country | manifest position: 63/74 | attempt: 1  
Country: RS | retailer: Maxi | mode: AUDIT  
Registered URL: https://www.maxi.rs/maxi-nedeljna-akcija  
Checkpoint time: 2026-11-23T10:33:05Z (UTC)  
Baseline / skill SHA: 73fd02fe14c4935c3a95bca49bba3c1498a9cb54  
Terminal status: SKIPPED_UNVERIFIED

Scope note: controller scope is ONE_OFF_GLOBAL; the frozen manifest has 74 all-country units. This checkpoint terminalizes only RS:maxi-rs-country and does not close the run.

## 1. Catalog Promo source

- [x] Loaded the exact active entry: Maxi / Maxi, official_retailer, Serbia location code RS, national label “Serbia (location-selected offers),” URL above, valid_until null, last_verified_at null. The host www.maxi.rs is allowlisted. The record summary says users must select a city and address to see the offer valid for that location. RSD is supported.
- [x] Official ownership: the linked company-information page https://www.maxi.rs/delhaize-srbija identifies Delhaize Serbia društvo sa ograničenom odgovornošću and a Belgrade, Serbia address and company identifiers.
- [x] Robots: https://www.maxi.rs/robots.txt exposes User-agent: * and disallows account, checkout, registration, mobile and search paths; it does not disallow /maxi-nedeljna-akcija. No separate bot-specific group or Content-Signal directive was visible. The retrieval tool did not expose an HTTP status or request timestamp.
- [x] Query-budget deviation: two retrieval-tool calls were made to the same robots URL because the first call returned no displayable body; the second exposed the file. This was an accidental duplicate, not a source-page retry or access workaround. No alternate user-agent or bypass was used.
- [x] One attempt opened the registered catalog page. Its title was “Maxi nedeljna akcija,” and the rendered text contained navigation and a delivery-time prompt, but no current catalog items, flyer dates, or offer dates. A site banner referenced a delivery disruption on 22 Nov 2026; that is not promotional validity evidence. The URL shown by the tool remained the registered URL. HTTP status and redirect headers were not exposed.
- [x] Terms/reuse check: the official terms route https://www.maxi.rs/usloviposlovanja was reached from official-site links but the text extraction exposed only the page shell and breadcrumb, not the terms body. The “Uslovi kupovine” footer link resolved to that same route. Commercial reuse permission is therefore unverified, not claimed granted or prohibited.
- [x] Currentness and geography: the page contains no catalog period or date. Although the Serbian site and Serbian operator are verified, the catalog record requires city/address selection; countrywide applicability of any individual price is not established. Classify the catalog STALE_UNVERIFIED. The URL appears canonical, but in-place content updates were not proved.
- [x] No product, leaflet, or image page was opened because current offer evidence and commercial reuse permission were not established. No price, product name, variant, image, item validity date, or product-level coverage was collected. This is not a no-promotion finding.
- [x] Existing RS feed: 27 items total, 8 reference maxi-rs-country. Those 8 have no valid_until values; they were not revalidated against the source and are not asserted current or expired. No candidate feed was staged and no expiry was inferred.
- [x] No catalog URL, valid_until, last_verified_at, allowed host, highlight, or production JSON field was changed.

## 2. Skip decision and closeout

- [x] SKIPPED_UNVERIFIED — official identity is verified and the registered path is not disallowed by the observed robots rules, but the terms text/reuse permission, current catalog dates, product evidence, and item-level Serbia applicability remain unverified.
- [x] Accepted products: none. Product pages checked: 0. Expired IDs removed: none. Preserve the active catalog entry; missing source evidence is not proof of obsolescence.
- [x] Evidence: registered/evidence/RS-maxi-rs-country.md. Handoff: registered/handoffs/RS-maxi-rs-country.md. Receipt: registered/receipts/RS-maxi-rs-country.json.
- [x] No production JSON or shared progress/terminal-receipts file was changed; no catalog-page retry, commit, push, or schedule was made/created.
- [x] Next manifest input: RS:univerexport-rs-country, 64/74.

Final result: SKIPPED_UNVERIFIED  
Accepted NEW product IDs: none  
Expired deleted IDs: none  
Compact handoff artifact: registered/handoffs/RS-maxi-rs-country.md
