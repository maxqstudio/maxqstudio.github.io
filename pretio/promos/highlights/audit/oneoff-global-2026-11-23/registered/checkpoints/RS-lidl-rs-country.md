# RS:lidl-rs-country — Lidl Srbija

Run ID: pretio-oneoff-global-20261123T040625Z  
Country: RS | Catalog ID: lidl-rs-country | Retailer: Lidl Srbija  
Official URL on record: https://www.lidl.rs/c/online-letak/s10019338  
Checked UTC: 2026-11-23T10:31:04Z  
Mode: AUDIT | Scope: ONE_OFF_GLOBAL | Manifest work unit: 62 of 74 | Attempt: 1  
Frozen run baseline / skill SHA: 73fd02fe14c4935c3a95bca49bba3c1498a9cb54  
Terminal status: SKIPPED_BLOCKED

## 1. Catalog Promo source

- [x] Loaded the exact active catalog record: Lidl Srbija / Lidl Srbija, official_retailer, country RS, label “Serbia (location-selected offers),” stable official landing URL, valid_until: null. www.lidl.rs is in allowed_hosts.
- [x] One bounded public retrieval opened the registered landing page at the same official URL. The page lists “Pogledajte naše ponude 19.11. - 25.11.” and “26.11. - 2.12.”; neither label shows a year. Do not assign a year, infer product expiry, or convert these labels into a catalog valid_until.
- [x] Robots snapshot at https://www.lidl.rs/robots.txt did not disallow /c/online-letak/, but the retrieval reports its copy was crawled four weeks ago; current directives are therefore unverified. No retry or alternate access path was used.
- [x] Official General Information identifies Lidl Srbija KD as technical operator for lidl.rs and responsible for transmitting store offers. The retrieved official Lidl Plus terms describe private-use participation in Lidl Plus, but do not grant permission to commercially republish leaflet content or images. Content-reuse authorization remains unestablished.

## 2. Offers, location and feed

- [x] No leaflet, product page, price, image, or product link was opened. Zero items checked; this is not a NO_PROMO_FOUND result. Item extraction was withheld because permitted commercial reuse was not established and the robots copy was stale.
- [x] Official Serbian domain/operator establish the source market as Serbia. The registered catalog is location-selected; without item-level evidence, no nationwide or regional product coverage is asserted.
- [x] Existing RS.json has seven Lidl entries, all with valid_from: null and valid_until: null; their 2026-11-23 observation timestamps do not prove they remain on offer. No positive expiry evidence was obtained, and no feed or expiry data was changed.
- [x] No production catalog/feed/index or shared progress file was changed.

## 3. Terminal decision and artifacts

- Catalog link: LINK_STABLE evergreen landing page. Offer-date freshness: STALE_UNVERIFIED because the visible date labels omit the year. No obsolescence or expiry is inferred.
- SKIPPED_BLOCKED — do not reuse Lidl item prices or images until current access policy and commercial reuse permission are established.
- Evidence: pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/evidence/RS-lidl-rs-country.md
- Handoff: pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/handoffs/RS-lidl-rs-country.md
- Receipt: pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/receipts/RS-lidl-rs-country.json
- This terminalizes only RS:lidl-rs-country; it does not close the global run.