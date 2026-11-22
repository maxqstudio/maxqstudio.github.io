# Pretio — per-catalog update checklist

Create a **new copy for every (country, catalog_id) in every 12-hour run**. Save as a run artifact, NOT inside \`catalog_app.json\` or \`CC.json\`.

Run ID: \`<UTC run id>\`  
Country: \`<ISO2>\` | Catalog ID: \`<accepted catalog id>\` | Retailer: \`<accepted merchant>\`  
Official URL: \`<official HTTPS URL>\` | Checked UTC: \`<timestamp>\`  
Mode: \`AUDIT / PREPARE / PUBLISH\`

## 1. Catalog Promo source
- [ ] Exact \`catalog_id\`, country, location rules and current original record loaded
- [ ] Official retailer source verified; links, redirects, allowed host, ToS/robots checked
- [ ] **Permanent/canonical catalog URL** prioritized and verified as working and updating in-place
- [ ] If periodic/rotating URL, verified **real \`valid_until\`** from source before accepting (no guessed date)
- [ ] Confirm national vs city/store scope; no extrapolation from a single store
- [ ] \`last_verified_at\` only changed after actual positive verification
- [ ] No extra catalog JSON keys or schema changes

## 2. Product Highlights — discounted items ONLY
- [ ] All eligible discounted products on this catalog checked; candidates listed
- [ ] Each has same-product explicit **normal and promo prices** from original retailer; \`promo_price < normal_price\`
- [ ] Product name/size/brand and currency verified; no guessed fields
- [ ] Product image decodable, same exact item, official/authorized source
- [ ] Exact approved \`catalog_id\` and official item source URL verified
- [ ] Item's geographic offer applicability supported (not just a catalog marked national)
- [ ] \`observed_at\` factual; known \`valid_from\` and \`valid_until\` retained
- [ ] **Expired** items (\`valid_until\` before market today or explicit ending proof) removed from candidate country feed
- [ ] No item contains any field outside approved item allowlist
- [ ] Rejected items recorded separately with reasons; no fabricated filler for 12-hour quota

## 3. Checkpoint and context compact
- [ ] Accepted new product IDs and observed evidence recorded in run artifact
- [ ] Rejected candidates, source failures and location restrictions recorded
- [ ] Candidate country feed saved; unchanged good items retained
- [ ] Compact handoff written using \`COMPACT_HANDOFF.md\` (**max ~400 words**)
- [ ] Mark \`CATALOG_DONE\`, release raw evidence from next agent context
- [ ] Dispatch next catalog as NEW isolated task with compact handoff only

## 4. Country closing gate (after all catalogs)
- [ ] All catalogs processed or explicit failed/blocker receipts
- [ ] Target **≥1 NEW confirmed discounted product / country / run** checked; if missed report \`TARGET_MISSED\`
- [ ] 80/country, 20/retailer, unique ID, currency metadata and expiry validation PASS
- [ ] All feed fields match existing schema and all referenced \`catalog_id\` exist
- [ ] Index v2 entries/revisions and SHA-256 match exact staged bytes
- [ ] Diff confined to allowed writer paths; CI/approval/rollback ready

Final result: \`<CATALOG_DONE / source blocked>\`  
Accepted NEW product IDs: \`<ids or none>\`  
Expired deleted IDs: \`<ids or none>\`  
Compact handoff artifact: \`<artifact path>\`
