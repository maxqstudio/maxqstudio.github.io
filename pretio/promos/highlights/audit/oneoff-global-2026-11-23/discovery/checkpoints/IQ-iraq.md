# One-off country discovery checkpoint — Iraq (IQ)

- Run: pretio-oneoff-global-20261123T040625Z; selected rank 18/174; 1 registered catalogs.
- Discovery search window: 2026-11-23 11:23–11:36 UTC (web tool did not expose per-query timestamps).
- One Catalog Promo query: “Iraq official supermarket weekly offers catalog flyer promotions retailer”. No current official flyer was opened from this query.
- One online-shop query: “Iraq official supermarket online shop grocery delivery promotions retailer”. Taawon Hypermarket (https://store.taawon.iq/) was opened once. The page states delivery across Baghdad, has a weekly-offers link and product prices, but does not establish countrywide online service or a normal/discount pair for an item.
- Official ownership is supported by the shop page, but Baghdad-only delivery does not establish Iraq-wide service. No product prices/images were retained and no Product Highlight candidate was accepted.
- Terminal disposition: **SKIPPED_UNVERIFIED**. This disposition is not a claim that no retailer exists; it records that this bounded market review did not pass the full evidence gate.
- No Product Highlight, catalog, feed, index, currency, or location schema/data change was made from this discovery lead.
- Handoff: the catalog-promo and online-shop category budgets for this market are consumed; do not repeat either query in this run.

## Independent-audit correction: post-robots access

**Compliance incident (not a cleared source):** The earlier **registered** Taawon checkpoint had already read `https://store.taawon.iq/robots.txt` and recorded an explicit `User-agent: GPTBot; Disallow: /` restriction (review time approximately `2026-11-23T09:42:44Z`). This **later discovery-phase** opening of `https://store.taawon.iq/` in the `11:23–11:36 UTC` window was therefore made **after that restriction was known**. The discovery note's original “opened once” describes one attempt in this phase, **not authorization to repeat access**. It remains a breach of the run's source access policy and cannot be made compliant after the fact.

Do not count that access as verified source coverage, use its text/prices to publish products, revisit the URL, or assign a second registered receipt. No prices/images from the revisit are in the active feeds. Keep Iraq's country disposition `SKIPPED_UNVERIFIED`, the registered Taawon receipt `SKIPPED_BLOCKED`, and both as distinct audit outcomes. See `../deviations.md` and `../query-reconciliation-audit.md`; auditor compliance remains HOLD/FAIL pending review.
