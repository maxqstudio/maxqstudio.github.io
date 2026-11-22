# Pretio catalog checkpoint (≤400 words, separate run artifact)

- Manifest work unit: `<country>:<catalog_id>`, position `<N of manifest_total>`; terminal receipt status `<UPDATED / SKIPPED_* / BLOCKED_CURRENCY_METADATA / FAILED>`.
- Counted as attempted: `yes`. This catalog must not hold up later entries if no verified new data is available.
- Run: `<UTC run ID>`, cycle: `<09:17/21:17 WITA>`.
- Completed: `<country>` / `<catalog_id>` / `<retailer>`.
- Canonical link: `<source URL>`. Classification: `LINK_STABLE / LINK_PERIODIC_WITH_EXPIRY / BLOCKED_MISSING_EXPIRY`. Known `valid_until`: `<verified date or null for evergreen>`.
- Result: `<CATALOG_DONE / FETCH_FAILED / SOURCE_BLOCKED / ...>`.
- New discounted products accepted: `<count and stable IDs only>`.
- Products rejected: `<count, short reasons; no raw HTML>`.
- Expired IDs pruned from country candidate: `<ids>`.
- Evidence artifact path(s): `<paths in run artifacts>`.
- Candidate country feed path: `<temp or branch artifact>`.
- Source/market blockers: `<facts only>`.
- **Next input:** `<next country/catalog_id>`. Load only this checkpoint, next catalog entry, and relevant matching highlight IDs. Start a **new isolated context**; never rely on carrying a long previous conversation.

No extra field is to be added to a production catalog or highlight entry. These checkpoint keys exist **only** in the markdown audit artifact.
