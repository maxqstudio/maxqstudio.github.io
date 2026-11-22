# Global 12-hour operations, per-catalog compaction, safety gates

## Scheduler target (not yet installed by this skill)

Intended GitHub Actions cron (UTC): `17 1,13 * * *` = 09:17 and 21:17 WITA. Also allow `workflow_dispatch` with country selection and `dry_run=true`. GitHub schedule is best-effort and may be delayed or disabled when a public repository has had no activity for 60 days; monitor missing runs. **A SKILL.md file is instructions, not an autonomous runner.** A dedicated scheduler, fetch adapters, publisher and credentials are separate deliverables.

Start with a manual AUDIT, then every scheduled production cycle must **attempt all official catalogs in all countries in the catalog manifest**, not only the 7 highlight-feed countries. Unsupported currency blocks highlight publication for that country, **not** its catalog check. Use country partitions; start at most 4 parallel country workers and <=1 in-flight request per retailer host, finite timeouts and randomized backoff. Avoid robots/ToS violations and HTML scraping when a source provides a permitted public feed.

## Deterministic exhaustive 12-hour pipeline

**Completion invariant:** At the start of each cycle, freeze an immutable work manifest from **all** active official catalog entries and all their country codes in `catalog_app.json`. Every unique `(country_code, catalog_id)` must be attempted. **No stop after first product, first target-met country, first source failure, or first success.** The cycle ends only when every manifest entry has a durable terminal checklist/receipt and there are zero remaining entries.

1. **Manifest**: calculate `manifest_total`, work-unit IDs, last completed checkpoint, and market code. Country and catalog coverage must not be filtered by highlight feed existence or currency metadata. Prioritize stable evergreen links, then dated catalogs; every one must eventually be attempted.
2. **One task = one catalog**: initialize a fresh isolated context with the catalog entry, relevant existing highlights, source rules and the last COMPACT_HANDOFF only. Mark `PENDING → ATTEMPTED → UPDATED / SKIPPED_* / FAILED`. Do not carry full past contexts.
3. **Bounded collection**: use permitted official data access, finite timeouts (e.g. ≤30 s fetch) and at most 2 retries for transient failures with backoff. Do not retry CAPTCHA/legal blocks. Check changed URLs and expiry. Collect all qualifying discounted items possible with bounded per-host work; meeting ≥1 target does **not** stop catalog enumeration.
4. **Save or skip**: stage only verified changes to catalog candidate / highlight candidate. On `NO_CHANGE`, `NO_PROMO_FOUND`, inaccessible/blocked source, incomplete price/image/geo evidence or unsupported currency: write a `SKIPPED_*` receipt, retain prior valid records unless explicitly expired, and proceed immediately to next catalog. No infinite retry, no waiting for a retailer to recover.
5. **Checkpoint every catalog**: write the checklist/evidence and COMPACT_HANDOFF ≤400 words, then start a fresh agent task for the next manifest entry. A blocked/no-change catalog still counts as **attempted + finished with a reason**, never as successful extraction.
6. **Resume**: crash/cancel retries use durable checkpoint IDs and original manifest. Pending catalogs are picked up first; completed records are not repeated arbitrarily. If the runner is terminated with pending work, mark the cycle `INCOMPLETE`, not `COMPLETED`, and resume safely before declaring full coverage.
7. **Closing gate**: after `terminal_receipts == manifest_total` and `pending == 0`, reconcile all staged candidate changes; delete proven-expired highlights; enforce catalog v2 / index v2 / feed v1 exact-field allowlists, currency, geo, 80/20 caps, and exact SHA. Emit `TARGET_MET`/ `TARGET_MISSED` for each country without trying to fill a quota using guessed deals. A country with zero changes is a valid outcome. Publish a single consistent batch only under approved release policy.
8. **Stop**: finish the cycle and release runners. **Do not loop forever**, do not schedule continuous crawls after completion. The next clock event ~12 hours later starts a **new full manifest scan**.

**Coverage accounting:** `manifest_total = completed_updated + completed_skipped + completed_failed`; `pending = manifest_total - terminal_receipts`. Count source failures as terminal once they have an audit receipt. If `pending > 0`, result is `INCOMPLETE`. Per-cycle report lists checked and skipped catalogs by country with the reason, new confirmed discounts, expired deletions, and the next cycle target.

## Safety / source economics

- Prefer canonical permanent retailer catalog pages; replace with a short-lived dated leaflet only when no stable source exists AND `valid_until` is proven.
- 200 OK alone does not prove content freshness or offer validity; test source page content/evidence and market coverage.
- No synthetic discounts, no guessing reference prices, no raw prices from an LLM without retailer proof.
- Deduplicate media fetch by source hash/ETag and share cache. Use HTML/OCR fallback selectively, not AI per HTTP request. Do not use residential proxy/CAPTCHA bypass to evade restrictions.
- Keep default schedule read-only/PR until Owner explicitly enables automatic publication with rollback.
- Race safety: GitHub workflow `concurrency` group per data publisher; never allow two schedules to overwrite the same `main` state. Recheck branch base SHA before merge, rerun validation on final snapshot.

## Status definitions

Per catalog audit/evidence: `FETCH_OK`, `NO_CHANGE`, `NO_PROMO_FOUND`, `SOURCE_BLOCKED`, `FETCH_FAILED`, `EXTRACTION_FAILED`, `INVALID_PRICE`, `INVALID_IMAGE`, `LOCATION_RESTRICTED`, `LINK_STABLE`, `LINK_PERIODIC_WITH_EXPIRY`, `BLOCKED_MISSING_EXPIRY`, `EXPIRED`, `CATALOG_DONE`; scheduler terminal receipts: `UPDATED`, `SKIPPED_NO_CHANGE`, `SKIPPED_NO_PROMO`, `SKIPPED_UNAVAILABLE`, `SKIPPED_BLOCKED`, `SKIPPED_UNVERIFIED`, `BLOCKED_CURRENCY_METADATA`, `FAILED`.

Per country: `TARGET_MET` (≥1 NEW valid discounted product), `TARGET_MISSED` (no eligible new discounts), `BLOCKED_CURRENCY_METADATA`, `VALIDATION_FAILED`, `READY_FOR_REVIEW`, `PUBLISHED`, `INCOMPLETE` (some manifest entries not terminal). These are audit/checkpoint labels ONLY. Do not add them as keys to production feeds or catalog items.
