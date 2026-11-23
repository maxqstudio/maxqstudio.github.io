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

- Removed the positively expired dated Spain catalog record `lidl-es-country` from `pretio/promos/catalog_app.json`. Its dated flyer expired on 2026-11-22 in Spain. A reference scan across all seven highlight feeds found **zero** dependent entries, so no highlight reference needed migration/deletion.
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

All three workflows passed on `294b85e37508ab258a1aea239699bb4ab47e3140`:

- [Pretio public content skill & schema gates — run 18](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45168582334) — success.
- [Pretio public catalog browser — run 22](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45168582378) — success.
- [Website security regression — run 9](https://github.com/maxqstudio/maxqstudio.github.io/actions/runs/45168582517) — success.

A documentation-only follow-up to record these results will trigger a fresh PR workflow. The PR and Issue #57 handoff will carry the latest head SHA and final check status.

## Review handoff

1. Independent auditor: start from the full instructions in [Issue #57](https://github.com/maxqstudio/maxqstudio.github.io/issues/57) and the merged crawling skill from [PR #58](https://github.com/maxqstudio/maxqstudio.github.io/pull/58). Review this run from a separate room and inspect every receipt, checkpoint, handoff, deletion reference scan, and disclosed deviation.
2. Global discovery is incomplete until the remaining 140 selected markets are independently researched or explicitly dispositioned under the Issue #57 contract. Do not treat this candidate as complete global coverage.
3. No merge or deployment has been performed. Owner approval must wait for the independent auditor's report as required by Issue #57.
