# Global 12-hour operations, per-catalog compaction, safety gates

## Highest-priority scope instruction: explicit one-off country

A command like **"kerjakan 1 kali saja untuk Indonesia"** means exactly **ONE manually triggered, non-recurring cycle limited to Indonesia (ID)**, then STOP. It must not open another country, exhaust all countries, or create/enable a schedule. For this task, the scoped checklist is all active official Indonesia catalogs, including failed/unchanged ones; no other countries. A one-off may not bypass product evidence/field, expiry, compact or completion gates. The global exhaustive 12-hour requirement applies **only** when the Owner asks for recurring/all-country operation or no explicit narrow scope is specified.

`python3 tooling/pretio_public_content/manifest.py --once --country ID` creates the locked Indonesia-only work manifest. For completion: `python3 tooling/pretio_public_content/manifest.py --once --country ID --receipts <run-receipts.json>`. The runner must pass the Owner-selected scope to fetchers, checkpoints and publisher; cross-country production changes must be refused. Do not modify existing schedules merely because a one-off run was requested. `--once` is manifest tooling, not a crawler or recurring workflow.

## Scheduler target (not yet installed by this skill)

Intended GitHub Actions cron (UTC): `17 1,13 * * *` = 09:17 and 21:17 WITA. Also allow `workflow_dispatch` with country selection and `dry_run=true`. GitHub schedule is best-effort and may be delayed or disabled when a public repository has had no activity for 60 days; monitor missing runs. **A SKILL.md file is instructions, not an autonomous runner.** A dedicated scheduler, fetch adapters, publisher and credentials are separate deliverables.

Start with a manual AUDIT, then every scheduled production cycle must **attempt all official catalogs in all countries in the catalog manifest**, not only the 7 highlight-feed countries. Unsupported currency blocks highlight publication for that country, **not** its catalog check. Use country partitions; start at most 4 parallel country workers and <=1 in-flight request per retailer host, finite timeouts and randomized backoff. Avoid robots/ToS violations and HTML scraping when a source provides a permitted public feed.

## Bounded online-shop / marketplace discovery after catalog coverage

**Mandatory research scope extension:** Catalog work units are still enumerated exactly from the frozen accepted catalog manifest. In the same Owner-authorized countries, add a **separate bounded discovery phase** for independent online shops and genuine marketplace seller storefronts (including online-only retailers). Do not assume that "retailer" only means a physical supermarket.

1. For each scoped country, search permitted public direct-store directories, authorized e-commerce product feeds/APIs and official marketplace store/offer pages. Google Shopping is only a **discovery lead** when permitted; do not automate scraping Google Search/Shopping pages against their rules or use Google Shopping pricing as source proof.
2. Verify the real seller identity, the official storefront, seller-specific item URL, market, explicit public normal/promo price pair, item photo, any promo dates, and access conditions. One platform can contain thousands of sellers; treat each discovered seller as a distinct audit identity rather than treating the whole platform as one retailer.
3. Use `templates/ONLINE_SHOP_CHECKLIST.md` and one compact handoff per new shop. Limit pagination, rate, time and retries, and record **search/query coverage bounds**; no claim of internet-wide completeness.
4. Map eligible offers to an **existing approved** seller/store `catalog_id` only. If none exists, stage the discovery and price evidence as AUDIT_ONLY, mark `NEEDS_CATALOG_APPROVAL`, and continue without changing the production catalog or feed. A new merchant/canonical marketplace host is never auto-allowlisted.
5. Keep two distinct sets of counters: registered `manifest_total/terminal_receipts/pending` and discovered `shops_found/checked/verified/awaiting_approval/blocked`. Do not use discovered shops as fake terminal receipts; do not declare research of all web stores "complete" when it was bounded.
6. On explicit `ONE_OFF:ID` or `ONE_OFF_GLOBAL`, perform **one** scoped research cycle only and STOP; no cron, polling loop, or ongoing scheduler is created by the skill update.

The country-feed v1 / index v2 exact-key and evidence requirements remain unchanged. See `online-shop-marketplace-rules.md` for the complete policy.

## Preflight / completeness tools

- Generate the **entire**, currency-independent manifest: `python3 tooling/pretio_public_content/manifest.py > /tmp/pretio-manifest.json`.
- At the end of a cycle, give the tool a JSON array of terminal receipts with existing audit-only keys `work_id` and `status`: `python3 tooling/pretio_public_content/manifest.py --receipts /tmp/receipts.json`.
- Exit code `0` means every manifest entry is terminal. Exit code `2` means `INCOMPLETE`; exit code `1` indicates invalid receipt / input. An incomplete run MUST NOT be declared done. These JSON audit objects are not production catalog or highlight records.

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

## Owner expiry cleanup — live list MUST NOT accumulate expired content

At EVERY candidate finalization (registered catalogs, expanded markets, shops), perform deterministic **expiry pruning on final staged snapshots**, including items from sources that were unavailable this run:

- Product Highlights with `valid_until` earlier than the relevant local-market date: DELETE them from their country `CC.json` active `items` list; preserve the exact identities/counts and supporting proof only in separate bounded audit evidence, **not** a historical feed. An official source's proof of earlier termination also justifies removal after human/verifier review. Recalculate exact country-feed bytes SHA and matching index revision together.
- Catalog Promo with proven-expired rotating URL: replace with a newly verified official evergreen/current link or remove/deactivate via the existing compatible schema under catalog-writer review; do not leave an expired leaflet listed as current or add unsupported `status` values. Revalidate product foreign-key references in the same snapshot.
- When source is blocked, undated or merely inaccessible, **do not conflate stale with expired**. Record `STALE_UNVERIFIED` in audit and prevent false "current promo" claims. Seek positive expiry evidence or flag manual review, not blind deletion.
- Confirm `expired_remaining == 0` for known-expired published items before preparing PR. Do not accumulate old batches in production as archive. Any long-term audit evidence retention needs separate bounded storage controls.

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
