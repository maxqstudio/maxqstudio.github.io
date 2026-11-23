# Carrefour România — Registered Catalog Checkpoint

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `RO` | Catalog ID: `carrefour-ro-catalogues` | Retailer: Carrefour  
Official registered URL: <https://carrefour.ro/corporate/cataloage/>  
Checked UTC: `2026-11-23T10:24Z` | Mode: `AUDIT / ONE_OFF_GLOBAL`  
Manifest ordinal: `59/74` | Attempt: `1`  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal result: **`SKIPPED_BLOCKED`**

## 1. Catalog Promo source

- [x] Loaded the active catalog record and frozen manifest unit. The record identifies `Carrefour` / `Carrefour România`, national coverage, location `RO`, and summary text describing city-selected nearby-store offers. The manifest URL matches the record. The registered hostname `carrefour.ro` is allowlisted.
- [x] Made one public GET each to the exact registered URL and its same-host `robots.txt`; both returned HTTP `403 Forbidden`, `text/html; charset=UTF-8`, with no redirect. The responses were Cloudflare `Attention Required!` pages. Full request timestamps and byte counts are in `../evidence/RO-carrefour-ro-catalogues.md`.
- [ ] Current official ownership was not reverified because the retailer page was blocked; stored merchant/publisher fields are baseline metadata only.
- [ ] Robots directives, terms of service, and any content-reuse permission could not be verified. No terms link was exposed by the blocked page. No Carrefour catalog or product content was used.
- [ ] Current canonical/evergreen behavior, page update freshness, validity dates, and current offers could not be inspected. The production catalog item has no `valid_from` or `valid_until`; the manifest's null expiry is not evidence of evergreen validity.
- [ ] The stored national label does not establish nationwide offer eligibility. The record describes city-selected nearby-store offers; current city/area scope could not be checked.
- [x] No production catalog or highlight data was changed; `last_verified_at` was not refreshed.

## 1B. Additional online-shop discovery

This assignment is the single registered physical-retail catalog work unit. No additional shop or marketplace discovery was attempted under this checkpoint.

## 2. Product Highlights candidates

- [x] The registered page was attempted, but no product or offer content was available.
- [ ] Same-item normal/promo prices, currency, variant, item image, offer dates, and item-level Romania geography could not be checked. No candidate was accepted or observed to reject; no product/image URLs were requested.
- [x] Local schema compatibility check: `RO` is absent from `pretio/data/currency.json`; `pretio/promos/highlights/RO.json` and an `RO` index entry are absent. No highlight JSON currently references this catalog ID. No candidate country feed was created.

## 2A. Obsolescence and disposition

- [x] Classify this attempt as `STALE_UNVERIFIED`; the access block does not prove obsolescence or expiry.
- [ ] Evergreen replacement, periodic validity, or successor catalog not verified. No alternate source search was made within the one-attempt source budget.
- [x] Preserve existing production catalog data; no expiry or deletion evidence was obtained.

## 2B. Location and expiry gate

- [ ] Physical-item participating locations and national price applicability could not be verified because no products were visible.
- [x] No dated offer or positive expiry evidence was obtained. No Product Highlights expiry deletion or catalog retirement was staged.

## 3. Skip-or-update decision

- [x] **`SKIPPED_BLOCKED`** — robots policy and exact registered page both returned 403 before any permitted retailer content could be checked.
- No accepted new product IDs; no rejected product candidates observed; no expired IDs deleted; no catalog URL migration or production JSON change.
- Romania's missing currency/feed support is a separate publication constraint, not the source-block reason.

## 4. Checkpoint and compaction

- [x] Source response evidence saved at `registered/evidence/RO-carrefour-ro-catalogues.md`.
- [x] Compact handoff saved at `registered/handoffs/RO-carrefour-ro-catalogues.md` (under 400 words).
- [x] Individual terminal receipt saved at `registered/receipts/RO-carrefour-ro-catalogues.json`.
- No shared progress or aggregate terminal-receipt file was changed. Cycle-level completion remains with the run orchestrator.

## 5. Cycle-level closing gate

Not evaluated by this per-catalog worker. This receipt closes only `RO:carrefour-ro-catalogues`; it does not assert global manifest completion or a Romania country target outcome.
