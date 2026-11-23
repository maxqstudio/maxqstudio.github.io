# Pretio one-off global catalog crawl — run report

- **Run ID:** `pretio-oneoff-global-20261123T040625Z`
- **Scope:** `ONE_OFF_GLOBAL`; one run only, no scheduler/cron/automatic repeat.
- **As-of:** 2026-11-23.
- **Frozen base and skill commit:** `73fd02fe14c4935c3a95bca49bba3c1498a9cb54` (`origin/main`, including merged PR #58).
- **Branch:** `codex/pretio-oneoff-global-crawl-20261123`.
- **Overall status:** **INCOMPLETE**. The registered source pass is terminal, but 140 of 174 selected market-discovery dispositions remain pending. No claim of global coverage is made.

## Work completed

- The frozen manifest contained **74 catalog work units across 24 registered countries**. All 74 have one terminal receipt, checkpoint and compact handoff: 30 `SKIPPED_BLOCKED`, 40 `SKIPPED_UNVERIFIED`, 2 `SKIPPED_UNAVAILABLE`, and 2 `BLOCKED_CURRENCY_METADATA`. No work unit remains pending.
- The market register contains 249 countries. All **24 countries with registered catalog sources** received terminal discovery dispositions. For the 174 selected markets, **34 are terminal and 140 remain pending**. The discovery pass used 36 Catalog Promo searches and 39 online-shop/marketplace searches, opened 39 official lead pages and recorded 34 country checkpoints/handoffs. Search results and exact limitations are in `discovery/`.
- One accidentally repeated Catalog Promo category search occurred for each of CL, CO and EC. This exceeded the one-search-per-market budget; it is documented in `discovery/deviations.md`, and those markets were not searched again.
- A few discovery-page opens overlapped official retailer sources already present in the registered manifest. The overlap is also documented in `discovery/deviations.md`; no second registered receipt was created.

## Active data changes

- Removed the expired period-specific Spain flyer record `lidl-es-country` from `pretio/promos/catalog_app.json`; this does **not** mean the registered landing-page URL is obsolete. The removed record described the 16–22 November flyer. A reference scan across all seven highlight feeds found **zero** dependent entries, so no highlight reference needed migration/deletion.
- No Product Highlights were added, edited or deleted. Final strict validation found **zero expired products** across all seven feeds.
- No product price, image or catalog entry was copied from audit-only leads whose reuse permission, service area, validity or catalog approval was unresolved. No schema, currency map or location schema was changed.
- The active catalog manifest now contains 73 entries. Comparing terminal receipts to those active entries yields 73 terminal dispositions, 0 pending and 0 failed. The frozen 74-entry registered run ledger remains unchanged by the separate expired-record retirement.

## Local validation

All checks below passed on the final local candidate before PR creation:

- `python -m py_compile tooling/pretio_public_content/validate.py tooling/pretio_public_content/manifest.py` — passed.
- `python -B -m unittest discover -s tooling/pretio_public_content -p 'test_*.py' -v` — **22 tests passed**. This Windows runtime needed the already-installed temporary `tzdata` package via `PYTHONPATH`.
- `python -B tooling/pretio_public_content/validate.py --as-of 2026-11-23 --strict-expiry` — `VALID`, no warnings, no expired products.
- The same strict validator with the `origin/main` catalog as baseline — `VALID`, no warnings.
- `python -B tooling/pretio_public_content/manifest.py --receipts <active-73-receipts.json>` — `COMPLETED`, 73/73 terminal, 0 pending, 0 failed. Its printed `SCHEDULED_GLOBAL` label is a legacy generator label; this run was manually scoped `ONE_OFF_GLOBAL`, and no schedule was created.
- `git diff --check` — passed.

### GitHub Actions

The first Draft PR run on `a072760` passed the public-content skill/schema gates, while the browser smoke failed because its test hard-coded 74 cards after the intentional expiry removal left 73 active catalog records. The assertion was corrected in `294b85e` to compare the UI count with `catalog_app.json`. No product or schema data changed in that fix.

All three workflows passed on the code/test commit `294b85e37508ab258a1aea239699bb4ab47e3140`:

- [Pretio public content skill & schema gates — run 18](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45168582334) — success.
- [Pretio public catalog browser — run 22](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45168582378) — success.
- [Website security regression — run 9](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45168582517) — success.

After the audit report was updated, all three workflows also passed on report-only head `d1e071b2ad59e816f530cc21a28daf517e0fd2b1`:

- [Pretio public content skill & schema gates — run 19](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45168957741) — success.
- [Pretio public catalog browser — run 23](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45168957776) — success.
- [Website security regression — run 10](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45168957738) — success.

All three workflows also passed on PR head `6f72bb8bd6cfb9d580eed94d7386db0949cdc474`:

- [Pretio public content skill & schema gates — run 20](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45170807349) — success.
- [Pretio public catalog browser — run 24](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45170807490) — success.
- [Website security regression — run 11](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45170807468) — success.

All three workflows passed again on the targeted Lidl audit-follow-up head `72f86a640f01ed688ecb79f3dee4c1f9506903dc`:

- [Pretio public content skill & schema gates — run 21](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45176763765) — success.
- [Pretio public catalog browser — run 25](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45176763792) — success.
- [Website security regression — run 12](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45176763982) — success.

The exact check status for later documentation-only handoff changes is shown on the current [Draft PR #60](https://github.com/maxqstudio/maxqstudio.github.io/pull/60).

## Post-run targeted review — Lidl Spain

- The audit follow-up correctly distinguished the stable official weekly-flyer hub from the expired period-specific record. On 2026-11-23, the same official hub URL displayed a successor flyer dated 23–29 November. The live page's title and date listing were checked; no flyer products, prices or images were extracted. Official hub URL (retained as non-clickable evidence text): `https://www.lidl.es/c/descubre-nuevas-ofertas-cada-semana-folletos-lidl/s10087402`.
- The official Lidl legal notice (`https://www.lidl.es/c/aviso-legal/s10075786`) states that links to the portal from another website require prior express consent, and that commercial reproduction, distribution or public communication of site content requires authorization. No such permission is recorded in this repository or run evidence. The PR therefore keeps the expired period-specific entry retired and does not publish a replacement link or copy current flyer content.
- The permission decision is tracked separately in [Issue #61](https://github.com/maxqstudio/maxqstudio.github.io/issues/61). If the Owner supplies written permission, a later audited change may restore the same ID with evergreen hub metadata and no invented validity dates. If not, keep the source out of active catalog data.
- This was a focused post-run source/terms review, not another crawl. It did not change catalog, Product Highlights or schema data.

## Post-audit operator reconciliation — partial scope accepted (23 November 2026)

This section is a **document-only correction** made after the original crawl and independent auditor HOLD. It is not an additional source visit, new run, independent audit PASS, authorization to merge, or new product evidence.

- **Owner's scope decision:** [Issue #57 acceptance](https://github.com/maxqstudio/maxqstudio.github.io/issues/57#issuecomment-7103122368) accepts the **partial run result only**. The 140 markets remain `PENDING_RESEARCH` in the original market register; none is upgraded to researched/verified. One-off research is stopped; no new cycle/cron is authorized. The register remains 249 candidates, 174 selected, 34 terminal, 140 pending, 75 unselected; **zero verified official catalogs** and **zero new Product Highlights**.
- **ZA status fixed in evidence:** Initial online-only country checkpoint said `SKIPPED_UNVERIFIED`; after a separate catalog-search supplement surfaced the **local Newton Park SPAR leaflet**, the final disposition changed to `NEEDS_CATALOG_APPROVAL`. The updated ZA checkpoint and handoff now explicitly mark the initial status as superseded. The register and progress already reflected the final status. New local catalog is **not approved as national**; no product data was accepted.
- **Search provenance:** New `discovery/query-reconciliation-audit.md` inventories 34 country checkpoint narratives: **33 explicitly documented Catalog Promo search queries and 34 online-shop queries**, versus operator progress claims **36 / 39**. The residual **3 / 5** are **NOT VERIFIED** by one-to-one source/query records; three known over-budget CL/CO/EC catalog searches are already included in the checkpoint subtotal. The reported 39 official lead opens similarly lack full individual-request provenance. Do not infer query timestamps, invent receipts, or treat aggregate counts as auditor PASS. Original counters remain unchanged as **operator-reported, not independently confirmed**.
- **IQ Taawon:** Registered checkpoint recorded `GPTBot Disallow: /` before the later Iraq market-discovery homepage visit. That later visit is a **post-robots access-policy deviation** and is now acknowledged in the IQ checkpoint and `discovery/deviations.md`. No usable offer data was retained; do not count that page as verified catalog coverage, claim compliance, revisit, or publish extracted source data.
- **ZA Pick n Pay:** Registered checkpoint records source attempts at about **10:55–10:56 UTC**, outside the robots-specified **04:00–08:45 UTC** visit window. That incident is explicitly classified as a **noncompliant access attempt** in `discovery/deviations.md`. It cannot be retroactively cured; no product data was published.
- **Lidl ES:** The old dated catalog entry remains removed pending written linking authorization and [Issue #61](https://github.com/maxqstudio/maxqstudio.github.io/issues/61). The official weekly landing page is evergreen and must **not** be described as an obsolete page; no current flyer data was extracted.
- **Release gate:** This operator evidence repair does **not** lift independent auditor `HOLD MERGE`. QA/CI checks cover code/schema/browser behavior, not missing provenance or robots/terms compliance. A separate re-audit must review this PR's latest SHA and decide if the documented residual risks can be accepted. **PR stays Draft, unmerged, without deployment or scheduling.**

## Owner decision — exclude noncompliant source access from accepted crawl output

The Owner instructed that the access incidents be removed from **this run's usable crawl results**. The operator therefore created `source-exclusions.json` with **IQ Taawon** (`taawon-iq-weekly-offers`) and **ZA Pick n Pay** (`pnp-za-country`).

- Both source visits and any content derived from them are **ineligible** for new/verified catalog coverage, source approval, product evidence and newly accepted Product Highlights in this one-off run. No products were accepted from either source during this run; no new public product fields or prices require deletion.
- **Historical receipts, actual visits, budget counters and access incident records remain** for audit transparency. Exclusion is not retroactive compliance, an auditor PASS, or a reason to falsify the frozen 74/74 receipt ledger.
- **Previously published ZA Pick n Pay highlight entries are baseline data, not products generated by this one-off run**, and remain unchanged. No retroactive withdrawal or deletion of pre-existing customer data is authorized here.
- The separate local Newton Park SPAR ZA lead remains audit-only `NEEDS_CATALOG_APPROVAL` (not promoted or verified).
- The 140 pending markets remain unresearched under the Owner-accepted partial scope. Lidl link permission in Issue #61, query provenance residuals and independent re-review remain outstanding.

**Status:** operator-filtered source evidence; original access deviations still recorded. **PR stays Draft / HOLD MERGE**, with no additional requests, schedule, merge or deployment.

## Review handoff

1. Independent auditor: start from the full instructions in [Issue #57](https://github.com/maxqstudio/maxqstudio.github.io/issues/57) and the merged crawling skill from [PR #58](https://github.com/maxqstudio/maxqstudio.github.io/pull/58). Review this run from a separate room and inspect every receipt, checkpoint, handoff, deletion reference scan, disclosed deviation, and the Lidl permission decision tracked in [Issue #61](https://github.com/maxqstudio/maxqstudio.github.io/issues/61).
2. Global discovery is incomplete until the remaining 140 selected markets are independently researched or explicitly dispositioned under the Issue #57 contract. Do not treat this candidate as complete global coverage.
3. Keep PR #60 in Draft and do not merge or deploy until the independent audit, Lidl permission decision, and Owner approval are complete.
