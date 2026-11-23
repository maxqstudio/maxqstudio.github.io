# RS:idea-rs-country — IDEA

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `RS` | Catalog ID: `idea-rs-country` | Retailer: `IDEA`  
Official URL on record: https://www.idea.rs/Akcije/Katalozi  
Checked UTC: `2026-11-23T10:26:46Z`  
Mode: `AUDIT` | Scope: `ONE_OFF_GLOBAL` | Manifest work unit: `61 of 74` | Attempt: `1`  
Frozen run baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: `SKIPPED_BLOCKED`

## 1. Catalog Promo source

- [x] Loaded exact active record: IDEA / IDEA, `official_retailer`, national coverage label Serbia (location-selected offers), location `RS`, registered canonical page above, `valid_until: null`. `www.idea.rs` is in `allowed_hosts`.
- [x] One bounded public-source check opened the registered page. It displayed a catalog “Specijal ukrasa i poklona” with dates `09.11–05.12`, but no year; the page's current promotional freshness is therefore not fully verified. No production link or verification timestamp change is proposed.
- [x] Official ownership is supported by the IDEA page and its official terms identifying IDEA Marketi d.o.o. and its IDEA online store.
- [ ] Robots directives: **not verified**; the public retrieval tool could not open `https://www.idea.rs/robots.txt`.
- [ ] Commercial reuse permission: **not established**. Official `Uslovi i pravila` allow site/service use for private use and say commercial use of IDEA site content requires prior contact with IDEA Marketi d.o.o. No authorization was obtained. No alternate access route or retry was used.

## 2. Offers, location and feed

- [x] Catalog tile/date text observed; the year and current-cycle status remain unverified. Product pages/listings checked: `0`. No product prices, variants, offer dates, or images were fetched because commercial reuse permission was not established. This is not a `NO_PROMO_FOUND` result.
- [x] Serbian site/catalog scope and catalog `RS` country location are consistent. Item-level nationwide or store participation was not checked; the catalog landing page alone does not prove product geography.
- [x] Currency metadata includes `RS` / `RSD`. The existing `RS.json` feed has 12 IDEA items with `valid_until` dates from Nov 25 onward; none is expired on Nov 23. No feed or expiry data was changed.
- [x] No candidate offers accepted; no production JSON, feed, index, or shared progress changed.

## 3. Terminal decision and artifacts

- Catalog condition: `STALE_UNVERIFIED`; page displays a dated catalog, but no year is shown and no item-level offer evidence was inspected.
- **SKIPPED_BLOCKED** — commercial-use permission and robots policy were not established within this single bounded attempt; no product/image reuse was attempted.
- Evidence: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/evidence/RS-idea-rs-country.md`
- Handoff: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/handoffs/RS-idea-rs-country.md`
- Receipt: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/receipts/RS-idea-rs-country.json`
- This terminalizes only `RS:idea-rs-country`; it does not claim global-run completion.
