# Pretio - per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `CL:mayorista10-country-cl` | Position: `11 of 74` | Attempt: `1`  
Country: `CL` | Retailer: `Mayorista 10` | Mode: `AUDIT`  
Checkpoint UTC: `2026-11-23T04:38:01Z` (request timestamps were not surfaced by the capture wrapper)  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: `SKIPPED_UNVERIFIED`

## 1. Catalog Promo source

- [x] Loaded active record `mayorista10-country-cl`: `official_retailer`, national coverage label `Chile`, country location `CL`, `valid_until: null`, `last_verified_at: 2026-09-14T00:00:00Z`. Registered URL: <https://www.mayorista10.cl/>.
- [x] Registered host `www.mayorista10.cl` is in the current `catalog_app.json.allowed_hosts` list.
- [ ] Current redirect/canonical and official ownership are not verified in this attempt. The bounded collector requested the registered robots URL first and the registered home URL second (2 GETs, 5-second timeout per request, no retry; reported total 0.91 seconds), but its response-capture path did not surface HTTP status, content type, response bytes, `Location`, or response body for either request. Therefore there is no current-run HTTP or redirect-chain claim.
- [ ] The repository's inherited audit from prior PR #55 (base commit `0dfc9d9`) records the historical observation that `https://www.mayorista10.cl/` redirected to `https://www.super10.cl/` (Super 10 rebrand). This is historical baseline evidence only, not a response verified in this run. Current `allowed_hosts` contains `www.mayorista10.cl` but not `www.super10.cl`; no host change is authorized.
- [ ] Robots was requested first, but its status/body were not surfaced, so access permission is unverified. Terms were not inspected and no terms request was made. No redirect target or alternate URL was fetched after the capture failure.
- [x] No login, CAPTCHA, hidden API, proxy, alternate source, or access-control bypass was used. No retries, product pages, or category pages were requested.
- [x] No catalog field, URL, host allowlist, or `last_verified_at` was changed.

## 2. Product Highlights candidates

- [x] `CL` currency metadata supports `CLP`. `CL.json` contains 24 items and currently has 0 items referencing `mayorista10-country-cl`.
- [ ] Current offers could not be inspected because no response body was captured. No product candidate was observed; accepted: 0, rejected: 0. This does not establish that the retailer has no promotions.
- [ ] No same-product normal/promo pair, individual decodable image, source-host eligibility, Chile-wide product applicability, or source-backed validity dates were verified. The catalog-level `national` label is not product-level geographic proof. No product is eligible for addition.
- [x] No expired item was proved by this source attempt. No country feed, index, catalog JSON, or product record was modified.

## 3. Skip-or-update decision

- [x] `SKIPPED_UNVERIFIED` - fresh HTTP/robots/terms metadata was not observable from the bounded capture; no current catalog content or eligible product offer could be verified. Treat the source as `STALE_UNVERIFIED` for this attempt. Do not infer that the retailer has ceased operation or that its source is currently rebranded.
- [x] No production changes. Do not migrate to `www.super10.cl` without current official ownership verification and separate allowlist review.

## Compact handoff (under 400 words)

- Work unit `CL:mayorista10-country-cl`, position `11/74`; terminal receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`. Baseline/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Current registered record is `https://www.mayorista10.cl/`, host allowlisted; its `valid_until` is null and `last_verified_at` is `2026-09-14T00:00:00Z`. The bounded attempt requested `https://www.mayorista10.cl/robots.txt` before the registered home URL. Two GETs total, 5-second timeout each, 0 retries, reported total 0.91 seconds. The wrapper did not surface status, content type, bytes, redirect `Location`, or body; robots permission, terms, and the current redirect chain remain unverified. No product/category pages or alternatives were fetched.
- Historical baseline evidence only: the inherited prior PR #55 audit (base commit `0dfc9d9`) states that the registered URL redirected to `https://www.super10.cl/`. That is not a current-run observation. The current allowlist excludes `www.super10.cl`, so no host migration was made.
- `CLP` is configured; the CL feed has 24 items and no Mayorista 10 references. No current product pair, individual image, countrywide applicability, or dates were verified. Accepted 0, rejected 0; this does not mean no promotions exist. No catalog, feed, or index JSON changed.