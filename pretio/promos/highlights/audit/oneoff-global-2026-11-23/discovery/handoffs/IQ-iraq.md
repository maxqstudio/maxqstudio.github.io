# Handoff — Iraq (IQ) discovery

- Run: pretio-oneoff-global-20261123T040625Z; rank 18/174; terminal: **SKIPPED_UNVERIFIED**.
- Search window: 2026-11-23 11:23–11:36 UTC (web tool did not expose per-query timestamps). Category query budget is consumed for this market; no automatic repeat.
- Catalog Promo lead: No current official flyer was opened from this query.
- Online shop lead: Taawon Hypermarket (https://store.taawon.iq/) was opened once
- No product data was retained in Product Highlights. Follow the checkpoint and any linked per-source note before any future candidate review.

## Post-audit compliance correction (no new crawl)

The registered Taawon checkpoint at approximately 09:42 UTC had already identified `User-agent: GPTBot; Disallow: /`. The later discovery-phase opening of `https://store.taawon.iq/` during 11:23–11:36 UTC was therefore **after the restriction was known** and constitutes an **access-policy deviation**. The earlier “opened once” wording describes one discovery-phase request, not permission to reopen it. Do not reuse content, crawl again, or count this as verified official catalog coverage. No offer prices/images were retained in the published feed. See `discovery/deviations.md` and `discovery/query-reconciliation-audit.md` for incident and source-count reconciliation. Independent auditor must keep compliance finding open; PR remains HOLD.
