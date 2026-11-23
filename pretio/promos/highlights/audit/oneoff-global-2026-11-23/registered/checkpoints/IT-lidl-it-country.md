# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `IT:lidl-it-country` | manifest position: **39/74** | attempt: **1**  
Country: **IT** | retailer: **Lidl Italia** | mode: **AUDIT**  
Checked at: **2026-11-23 09:44 UTC** (browser tool did not expose individual request timestamps).  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded exact manifest entry and catalog record: `lidl-it-country`, Lidl Italia, URL `https://www.lidl.it/c/volantino-lidl/s10018048`, `coverage_type: national`, `locations: IT country`, `valid_from: 2026-11-19T07:00:00+08:00`, `valid_until: 2026-11-26T07:00:00+08:00`, `last_verified_at: 2026-11-18T03:09:34Z`.
- [x] Official ownership verified: Lidl Italia home page identifies `Lidl Italia S.r.l.` and the linked legal-information page names that company as technical website operator and responsible for promotions in stores: `https://www.lidl.it/c/informazioni-legali/s10018358`.
- [x] Robots check: `https://www.lidl.it/robots.txt` returned text rules; no matching disallow for `/c/volantino-lidl/s10018048`. It disallows unrelated search, numbered root paths and a CDN assets path.
- [x] The registered official page opened over HTTPS and retained the same canonical URL. It is an evergreen weekly-flyer landing page: the page lists current and future flyer periods, says the next week's flyer appears each Thursday, and links the selected shop's local offers.
- [x] Current source period: the page listed a weekly flyer valid **19/11–25/11** and a successor valid **26/11–02/12**. These dates support that the existing 19–25 Nov period is current on 23 Nov and ends at the stored valid-until boundary. The landing URL itself is stable; flyer content rotates.
- [x] Geography checked: page text says to select a reference Lidl store to see local promotions and flyers, and to select a store for offers in the user's area. Thus a country-level catalog landing page does not prove an individual item's nationwide price/applicability.
- [ ] No individual product, package, normal/promo price pair, product image, or item-level participating-area evidence was verified in the page text. Its current flyer art links were not treated as product-price proof; no store was selected and no product-specific record was collected.
- [ ] General public-site commercial reuse terms were not found in the opened legal-information page. Lidl Plus app terms found in search are service-specific and were not applied to the public flyer page. Robots permits the path; broader content-reuse permission remains **unverified**.
- [x] Classification: registered URL `LINK_STABLE`; current weekly flyer `LINK_PERIODIC_WITH_EXPIRY`; catalog `PERIODIC_CURRENT` behind a stable landing page. No source evidence supports obsolescence or an evergreen URL migration.
- [x] No production JSON, `last_verified_at`, schema, or allowed-host list was edited. No new catalog ID or field proposed.

## 2. Product Highlights and deletion

- [x] Existing `catalog_app.json` contains no unrelated catalog or price data changes; this record has no dependency in any existing highlight feed.
- [x] Italy has no country entry in `pretio/data/currency.json`; Product Highlights publication for IT is therefore unsupported. This does not block catalog verification.
- [x] Accepted product candidates: **0**. Normal and promo prices were not recorded; no discount is claimed.
- [x] Expired highlight IDs tied to this catalog: **0 observed**. Nothing was deleted or migrated; no orphan reference was created.
- [x] Existing catalog dates remain current as of 23 Nov Italy local time. No positive obsolescence evidence; do not remove the catalog.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — official evergreen landing page and flyer dates are verified, but the source presents offers as store-local; no exact item/price pair or national item-level applicability was verified. Italy also lacks highlight currency metadata. Catalog source remains active and unchanged.

## Compact handoff

Work unit `IT:lidl-it-country`, position 39/74; receipt `SKIPPED_UNVERIFIED`. The official stable page `https://www.lidl.it/c/volantino-lidl/s10018048` opened successfully; robots permits its path. Lidl Italia is identified as the page operator in `https://www.lidl.it/c/informazioni-legali/s10018358`. The page lists the current weekly flyer for 19–25 Nov and a successor for 26 Nov–2 Dec, with the next week published each Thursday. The registered `valid_until` (2026-11-26T07:00:00+08:00) matches the current flyer boundary; no catalog expiry/deletion is supported. The page requires selecting a reference store to see local offers, so country-level highlight geography cannot be inferred. No product/price/image pair was collected. General public-site reuse permission remains unverified; Lidl Plus terms were not treated as public-site terms. IT is absent from highlight currency metadata, and no IT feed or existing catalog dependency was found. No production data changed. Next manifest source: `MM:citymart-mm-promotions` (40/74), in a fresh context.