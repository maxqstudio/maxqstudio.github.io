# Kroger Weekly Ad — Registered Catalog Checkpoint

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `US` | Catalog ID: `kroger-us-country` | Retailer: Kroger  
Official registered URL: <https://www.kroger.com/weeklyad>  
Checked UTC: `2026-11-23T10:45:28Z` | Mode: `AUDIT / ONE_OFF_GLOBAL`  
Manifest ordinal: `70/74` | Attempt: `1`  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal result: **`SKIPPED_BLOCKED`**

## 1. Catalog Promo source

- [x] Loaded exact active item and frozen unit. Baseline is Kroger / Kroger, `official_retailer`, `US`, national label “United States (store-selected offers),” location US, `valid_until: null`; its summary says users select a store. Manifest URL matches, and `www.kroger.com` is allowlisted.
- [x] Official Kroger robots file checked at `https://www.kroger.com/robots.txt`. It names The Kroger Co. Family of Stores; its `User-agent: *` path list does not disallow `/weeklyad`, while it has separate user-agent-specific `Disallow: /` groups. The retrieval user-agent was not exposed.
- [x] Official Website & App Terms checked at `https://www.kroger.com/i/terms/website-and-app` via official site-scoped search result (last updated September 9, 2026). The terms identify Kroger Sites as The Kroger Co. and affiliate sites, limit the content license to personal/non-commercial use, reserve content rights to Kroger/licensors, and §5.3 prohibits automated access, collection, extraction or monitoring. Copy/reuse absent express permission requires prior written consent. No written commercial reuse or image permission was located.
- [x] The exact registered `/weeklyad` page was **not requested** once terms disclosed the automated-access restriction. Therefore its current response/redirect, canonical or evergreen behavior, current weekly-ad dates, update status and participating-store geography remain unverified. Baseline `valid_until: null` does not prove currentness or evergreen behavior.
- [x] Registered retailer/domain identity is supported by the accepted catalog record and official Kroger terms; ownership of this specific unrequested page was not freshly reverified. No alternate domain, third-party flyer, restricted endpoint or bypass was used.
- [x] `last_verified_at` remains at the baseline value; no production catalog edit or extra field was made.

## 1B. Online-store / marketplace discovery

This is one registered physical-retail Catalog Promo task. No additional shop or marketplace discovery was attempted.

## 2. Product Highlights candidates

- [x] No weekly-ad, product, price, image, date or participating-store content was accessed because automated collection is prohibited by the official terms. Zero candidates were inspected; zero were accepted or rejected. This is not `SKIPPED_NO_PROMO`.
- [x] Item-level nationwide price applicability could not be checked; the baseline country location and store-selected weekly-ad summary do not establish national eligibility for any item.
- [x] US currency metadata is USD. The existing `US.json` has 12 items and no references to `kroger-us-country`; no Kroger item expiry/deletion was identified. No candidate feed was created.

## 2A. Obsolescence and disposition

- [x] Catalog condition: `STALE_UNVERIFIED`. The prohibited page was not checked; no official evidence proves expiry, obsolescence or a successor.
- [x] Preserve existing registration. No `last_verified_at`, URL, expiry or highlight data was changed.

## 2B. Location and expiry gate

- [x] No product-level participation, price geography, dated offer or positive expiry evidence was obtained. No Product Highlights deletion or catalog retirement was staged.

## 3. Skip-or-update decision

- [x] **`SKIPPED_BLOCKED`** — official §5.3 prohibits automated access/collection/extraction/monitoring of Kroger-site information; no written permission was found. Robots' general retrieval language does not supersede the terms.
- No accepted or rejected product IDs; no expiry deletions; no catalog URL migration; no production JSON or shared progress change.

## 4. Checkpoint and compaction

- [x] Source evidence: `registered/evidence/US-kroger-us-country.md`.
- [x] Compact handoff: `registered/handoffs/US-kroger-us-country.md` (under 400 words).
- [x] Terminal receipt: `registered/receipts/US-kroger-us-country.json`.
- Shared progress and aggregate terminal-receipt files were not changed. This closes only `US:kroger-us-country`; global completion remains with the run orchestrator.

## 5. Cycle-level closing gate

Not evaluated by this per-catalog worker. This receipt does not assert full manifest completion or a US country target outcome.