# Durable crawler checkpoint (audit only)

Use a distinct ledger for Catalog Promo and Product Highlights, one writer per run. Before research, freeze the actual catalog bytes from the recorded main SHA and a reviewed discovery market list. For Catalog Promo the list includes the registered markets plus justified global discovery markets; for Product Highlights it is the registered markets. A one-off country is restricted to that country. Do not derive the frozen manifest again from a newer main during resume.

```sh
git show "$BASE_SHA:pretio/promos/catalog_app.json" > "$AUDIT_DIR/catalog-snapshot.json"
python tooling/pretio_public_content/checkpoint.py --ledger "$AUDIT_DIR/run.json" init --kind catalog --run-id "$RUN_ID" --base-sha "$BASE_SHA" --catalog "$AUDIT_DIR/catalog-snapshot.json" --markets "$AUDIT_DIR/markets.json"
python tooling/pretio_public_content/checkpoint.py --ledger "$AUDIT_DIR/run.json" record --phase catalog --work-id 'ID:example' --status SKIPPED_UNVERIFIED --reason 'Reason backed by checklist' --evidence 'durable checklist reference'
python tooling/pretio_public_content/checkpoint.py --ledger "$AUDIT_DIR/run.json" status
```

The example ID is illustrative, not a source to crawl. For each real catalog, write its actual evidence/checklist first, then record one terminal receipt. After every receipt, save the ledger and evidence to durable cross-run audit storage, not merely a temporary filesystem or chat transcript. Record its stable retrieval reference in the run handoff. Do not put receipts or raw evidence in published GitHub Pages files. No parallel writers for one ledger; workers may send results to a single writer. Exact repeated receipts are idempotent; conflicting receipts require review.

When a scheduled run resumes, retrieve the previous ledger and evidence and use status/next_catalog; do not initialize a replacement run while work remains. The baseline SHA is historical provenance; recheck current main and open PRs separately before staging any candidate. If a durable ledger is unavailable, report the missing checkpoint honestly rather than invent terminal receipts.

After all registered work is terminal, use record --phase discovery with the market code and a documented bounded-search outcome (CHECKED, SKIPPED_BLOCKED, SKIPPED_UNAVAILABLE, SKIPPED_UNVERIFIED, FAILED). Registered completion does not establish global discovery completion. RESEARCH_TERMINAL means all recorded work units have terminal outcomes, not that the sources or offers are verified and not that publication is approved. Only the existing closing evidence, expiry, candidate/CI and Owner gates can authorize a completed cycle or publication.

This tool provides local atomic checkpoint storage and accounting only. It does not fetch retailer sites, implement a scheduler, upload artifacts, validate evidence truth, or publish data. The executing operator must persist the audit state to an available durable service and resume it on subsequent runs.
