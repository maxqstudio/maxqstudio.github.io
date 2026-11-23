# Agra Namibia — registered catalog checkpoint

Run: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `NA:agra-na-country` | manifest position: **44/74** | attempt: **1**  
Country: **NA** | retailer: **Agra** | mode: **AUDIT**  
Registered URL: <https://agra.com.na/index.php/retail-wholesale/specials-promotions>  
Recorded: **2026-11-23T09:59:59Z**; the shell client did not retain exact per-request timestamps.  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: **SKIPPED_UNVERIFIED**

## Catalog source checklist

- [x] Loaded the frozen manifest entry and existing active record: `agra-na-country`, Agra Namibia, `official_retailer`, national Namibia location, `valid_until: null`. No production field was changed.
- [x] Official homepage returned HTTP 200, identified the Agra site and linked its “Specials & Promotions” page. The registered URL is a permanent promotions landing path; no dated token is in the URL. Historical in-place updates were not compared in this one-off check.
- [x] `https://agra.com.na/robots.txt` returned HTTP 200 `text/plain`. Its disallows cover administrative/system paths; neither the registered promotions path nor `/images/` is disallowed. No robots bypass or alternate host was used.
- [x] The registered page returned HTTP 200 HTML and current campaign listings. The shell client did not expose a final response URI, so no redirect claim is made. The page title is “Specials & Promotions - Agra Namibia.”
- [x] The site footer exposes “Disclaimer | Terms and Conditions.” The linked `/index.php/comps-terms-and-conditions` page returned HTTP 200 but contains no articles; it is not evidence of a general content-reuse license or restriction. No general terms governing reuse were located during this bounded check. The public page and robots policy did not show an access block.
- [x] Source page stated these campaign names, date ranges and availability:
  - “Agra Safari Den - Camping & Outdoor Promotion 2026” — all Agra branches countrywide; 2026-11-19 through 2027-01-18.
  - “Month End Specials - November 2026” — all Agra stores nationwide; 2026-11-19 through 2026-12-14.
  - “Contractors - November 2026” — 2026-11-19 through 2026-12-14; no availability area was visible in the listing text.
  - “Month End Safari Den Specials - November 2026” — available at Agra Safari Den or orderable at any Agra branch; 2026-11-19 through 2026-12-14.
- [x] One linked detail page, “Month End Specials - November 2026,” returned HTTP 200. It displayed a flipbook prompt and a cover image whose response was `image/png`, 6,504,275 bytes, last-modified 2026-11-18. The cover contains no item price pairs; it was inspected only for this source check and is not stored in the repository.
- [ ] Item-level offers in the flipbook were not extracted. No individual product identity, same-item normal/promo pair, product image, SKU/variant or expiry was verified. The campaign dates above do not establish item-level discount eligibility.
- [x] No current successor, period-specific catalog URL or catalog-level expiry was inferred. Keep the registered evergreen landing record unchanged.

## Product Highlights and decision

- [x] Accepted products: **0**. The current page and inspected cover did not expose a verifiable item-level normal/promo price pair or individual product image. No price was inferred from campaign titles or cover art.
- [x] Namibia is not in the existing Product Highlights currency/feed mapping; no highlight can be published for NA under the current compatibility contract.
- [x] No active highlight reference was changed or deleted; no source/catalog retirement was proposed. No production catalog, feed, index, currency or location JSON was modified.
- [x] **SKIPPED_UNVERIFIED** — the official evergreen campaign landing page is current, but this bounded attempt did not verify any item-level offer suitable for Product Highlights. The catalog itself is not considered expired or obsolete.

## Compact handoff (≤400 words)

Work unit `NA:agra-na-country`, position 44/74; receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`. Agra Namibia’s registered URL `https://agra.com.na/index.php/retail-wholesale/specials-promotions` returned HTTP 200 and serves a permanent official specials landing page. The official homepage links to it. `robots.txt` returned 200; its system-path disallows do not cover the promotions path or `/images/`. A linked competition terms page returned 200 with no articles; no general reuse terms were located, and no access block was observed.

The listing showed four dated campaigns. Three included countrywide/all-store availability; the “Contractors” listing did not show an area. Current visible dates were Nov 19, 2026–Jan 18, 2027 for Camping & Outdoor and Nov 19–Dec 14, 2026 for the other campaigns. One Month End detail page exposed only a flipbook prompt and a cover image; no item-level price pair or individual product image was verified. Accepted products: 0. Namibia has no supported highlight currency/feed. No production data changed; keep the catalog active and do not mark it expired. Next source: `NA:food-lovers-market-na-country` (45/74), in a fresh context.
