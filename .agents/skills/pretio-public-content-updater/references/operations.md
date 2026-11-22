# Global 12-hour operations, per-catalog compaction, safety gates

## Scheduler target (not yet installed by this skill)

Intended GitHub Actions cron (UTC): \`17 1,13 * * *\` = 09:17 and 21:17 WITA. Also allow \`workflow_dispatch\` with country selection and \`dry_run=true\`. GitHub schedule is best-effort and may be delayed or disabled when a public repository has had no activity for 60 days; monitor missing runs. **A SKILL.md file is instructions, not an autonomous runner.** A dedicated scheduler, fetch adapters, publisher and credentials are separate deliverables.

Start with a manual AUDIT of 7 existing feed countries, then expand to remaining catalog countries **only after a supported currency mapping is approved**. Use country partitions; start at most 4 parallel country workers and <=1 in-flight request per retailer host, finite timeouts and randomized backoff. Avoid robots/ToS violations and HTML scraping when a source provides a permitted public feed.

## Deterministic pipeline

1. Build manifest from \`catalog_app.json\`: each unique \`(country_code, catalog_id)\`, canonical URL, merchant, known expiry, current existing highlight IDs and priority (\`evergreen\` first, \`periodic\` second).
2. Schedule each catalog as a separate bounded unit of work. Store \`CATALOG_CHECKLIST.md\` and evidence in an immutable run artifact directory e.g. \`artifacts/pretio-updater/<run-id>/<country>/<catalog-id>/\`. **Not in the production JSON.**
3. Start each isolated catalog agent only with its catalog entry, relevant existing highlight IDs, current timestamp, two reference rules and the previous **compact handoff**. Do not send complete country/crawl history.
4. Fetch official data deterministically where allowed. For uncertain presentation, optional AI extractor proposes candidate fields linked to exact source evidence (never directly published); rules engine verifies all prices/images/dates and rejects unsupported fields.
5. Complete the checklist for this catalog and write \`COMPACT_HANDOFF.md\` with at most ~400 words (catalog ID, status, accepted/rejected counts and reasons, candidate IDs, expired removals, next action). **After saving evidence, reset/compact the actual agent context** by launching the next catalog as a new job/session; the skill cannot force the runtime's built-in compaction command. Do not rely on ephemeral chat memory.
6. After each catalog completion, update the **candidate** country highlight feed, not production \`main\`; gather enough source evidence to justify each new item. Do not immediately publish a partial country feed with dangling index.
7. After all catalogs in that country, perform deterministic expiry cleanup, deduplication, 80/20 limits, currency and source checks. Count NEW unique verified products. If zero, fail the growth objective with \`TARGET_MISSED\`, not the security validator and never fabricate.
8. Reconcile all country changes with the final accepted catalog snapshot; stage feed(s) + index atomically and validate exact SHA. Publish via single reviewed PR or gated bot promotion, with rollback reference.
9. Emit report: country, catalogs attempted, links stable/rotating, sources failed, new verified products, expired removals, target met/missed, blockers, expected next run. Alert on missed runs, high source failure ratio, invalid schema or mass deletion.

## Safety / source economics

- Prefer canonical permanent retailer catalog pages; replace with a short-lived dated leaflet only when no stable source exists AND \`valid_until\` is proven.
- 200 OK alone does not prove content freshness or offer validity; test source page content/evidence and market coverage.
- No synthetic discounts, no guessing reference prices, no raw prices from an LLM without retailer proof.
- Deduplicate media fetch by source hash/ETag and share cache. Use HTML/OCR fallback selectively, not AI per HTTP request. Do not use residential proxy/CAPTCHA bypass to evade restrictions.
- Keep default schedule read-only/PR until Owner explicitly enables automatic publication with rollback.
- Race safety: GitHub workflow \`concurrency\` group per data publisher; never allow two schedules to overwrite the same \`main\` state. Recheck branch base SHA before merge, rerun validation on final snapshot.

## Status definitions

Per catalog: \`FETCH_OK\`, \`NO_CHANGE\`, \`NO_PROMO_FOUND\`, \`SOURCE_BLOCKED\`, \`FETCH_FAILED\`, \`EXTRACTION_FAILED\`, \`INVALID_PRICE\`, \`INVALID_IMAGE\`, \`LOCATION_RESTRICTED\`, \`LINK_STABLE\`, \`LINK_PERIODIC_WITH_EXPIRY\`, \`BLOCKED_MISSING_EXPIRY\`, \`EXPIRED\`, \`CATALOG_DONE\`.

Per country: \`TARGET_MET\` (≥1 NEW valid discounted product), \`TARGET_MISSED\` (no eligible new discounts), \`BLOCKED_CURRENCY_METADATA\`, \`VALIDATION_FAILED\`, \`READY_FOR_REVIEW\`, \`PUBLISHED\`. These are audit/checkpoint labels ONLY. Do not add them as keys to production feeds or catalog items.
