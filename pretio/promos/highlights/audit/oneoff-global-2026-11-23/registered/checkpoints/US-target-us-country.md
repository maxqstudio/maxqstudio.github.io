# Pretio catalog checkpoint — Target weekly ad

- Manifest work unit: `US:target-us-country`, position **71 of 74**; terminal receipt: `SKIPPED_BLOCKED`.
- Counted as attempted: **yes**. One bounded official-source attempt; no retry.
- Owner scope: `ONE_OFF_GLOBAL`; this context handled only this manifest source. No schedule or second cycle.
- Run: `pretio-oneoff-global-20261123T040625Z`; checked `2026-11-23T10:48:42Z`.
- Base/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Completed: United States / `target-us-country` / Target.
- Source kind: retail weekly-ad landing page; location-selected offers may apply.
- Canonical link: <https://www.target.com/weekly-ad>. Route is stable, but current content/update period was not verified. Existing `valid_until: null` is not proof of evergreen validity.
- Result: `SOURCE_BLOCKED`; terminal receipt `SKIPPED_BLOCKED`.
- New discounted products accepted: none. Products inspected: zero; stopped before product prices/images because Target’s current terms disallow commercial use/collection of those assets/data absent permission. No expiry inferred.
- Evidence: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/evidence/US-target-us-country.md`.
- Candidate country feed: none; no production JSON or shared progress file edited.
- Source/market blockers: robots does not disallow `/weekly-ad`, but current terms restrict commercial extraction/use. The page notes price/promotion/availability variation by location; the returned page view did not show the current period or prove nationwide offer eligibility.
- Next input: `US:walmart-us-country` (72 of 74).

## Work-unit details

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `US` | Catalog ID: `target-us-country` | Retailer: Target  
Official URL: <https://www.target.com/weekly-ad> | Checked UTC: `2026-11-23T10:48:42Z`  
Mode: `AUDIT` | Manifest position: `71/74` | Attempt: `1`

## 1. Catalog Promo source

- [x] Loaded the frozen manifest row and exact active catalog record: US / Target / `target-us-country`; URL matches the manifest. Existing `last_verified_at` is `2026-09-22T00:00:00Z`; existing `valid_until` is null.
- [x] Verified official ownership from the official page footer and linked Target Terms. Terms apply to `www.target.com` and define Target as Target Corporation and its subsidiaries/affiliates.
- [x] Checked official `https://www.target.com/robots.txt`: no rule disallows `/weekly-ad`.
- [x] Checked linked Terms & Conditions, last updated September 10, 2026. They reserve content rights, grant a personal/noncommercial content license, and prohibit commercial use of product listings/descriptions/prices/images and data extraction/collection. No permission for commercial Pretio reuse was found.
- [x] Opened the canonical URL once in a public browser. The rendered page identified “Weekly Ad” but returned no current ad items, date range or promotional cycle.
- [x] URL path is a stable weekly-ad route; whether its catalog content currently updates in place remains unverified. Do not treat existing null `valid_until` as verified evergreen status.
- [x] Page footer notes pricing, promotions and availability may vary by location. Existing catalog coverage is store-selected when required; no item-level nationwide eligibility was proven.
- [x] `last_verified_at` unchanged because current promotional content was not positively verified.
- [x] Production catalog schema/JSON unchanged.

## Explicit scope / one-off validation

- [x] Mode: explicit `ONE_OFF_GLOBAL` run from the frozen 74-unit manifest, not a recurring scan.
- [x] This isolated task processed only `US:target-us-country`; no other country source was queried and no second cycle or schedule was created.
- [x] Per-source attempt is terminal. Whole-run completion remains with the parent orchestrator; this checkpoint does not assert all 74 receipts are complete.

## 1B. Online-store / marketplace discovery

- [x] No separate online-shop or marketplace discovery was performed in this catalog-only source context.
- [x] No product pages or sellers were reviewed; no unregistered seller was proposed or mapped.
- [x] Any separate one-off online discovery phase remains outside this source checkpoint.

## 2. Product Highlights — discounted items only

- [x] Product listings/prices/images were not inspected because commercial extraction/reuse permission was not established.
- [x] Accepted items: none. Rejected/assessed items: zero; offer assessment was not attempted.
- [x] No product name, price pair, image, validity date, product source URL or product-level geography was copied or inferred.
- [x] No US feed candidate was created or modified. Feed expiry cleanup was not attempted in this source task; no expiry was inferred.

## 2A. Confirmed obsolete catalog retirement

- [x] Audit classification: `STALE_UNVERIFIED` for current promotional content; the URL route is stable, but the current weekly ad could not be verified.
- [x] No positive evidence that the retailer or catalog was discontinued or obsolete.
- [x] No successor search, catalog URL migration, catalog deletion or highlight-reference change staged.
- [x] Existing catalog and any dependent feed records remain unchanged; no orphan reference was introduced.

## 2B. Location relevance and expiry

- [x] Physical-store participation/product scope was not verified; page-level location variation prevents a national product claim.
- [x] No online product/fulfillment claim was reviewed.
- [x] No regional product was staged into a national feed.
- [x] No known expiry was established; no product was deleted and no catalog expiry inferred.
- [x] No feed/index bytes or hashes changed.

## 3. Skip-or-update decision

- [x] `SKIPPED_BLOCKED` — official site terms do not provide the required commercial reuse/extraction permission. Stop after this bounded attempt and retain the catalog record unchanged for permission/Owner review.

## 4. Checkpoint and context compact

- [x] Saved this full checklist, separate source evidence, compact handoff (under 400 words), and one-work-unit terminal receipt.
- [x] No accepted product IDs, expired deletions or candidate feed file.
- [x] Next manifest input: `US:walmart-us-country`.

## 5. Cycle completion and country closing gate

- [ ] Whole-manifest closing gate not applicable to this isolated catalog task; parent orchestrator must reconcile all 74 work units and country-level targets.
