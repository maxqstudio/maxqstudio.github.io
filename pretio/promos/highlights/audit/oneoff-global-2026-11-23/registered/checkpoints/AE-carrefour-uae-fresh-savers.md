# Carrefour UAE Fresh Savers — Registered Catalog Checkpoint

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `AE` | Catalog ID: `carrefour-uae-fresh-savers` | Retailer: Carrefour  
Official registered URL: https://www.carrefouruae.com/mafuae/en/c/fresh-savers  
Checked UTC (response evidence recorded): `2026-11-23T04:17:33Z`  
Mode: `ONE_OFF_GLOBAL` | Manifest position: `1 of 74` | Attempt: `1` (no retry; HTTP 403 is an access block)  
Baseline commit supplied for this run: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`

## 1. Catalog Promo source

- [x] Loaded the active record for `carrefour-uae-fresh-savers`; country/location is AE / United Arab Emirates, labeled national. Existing summary says prices and availability depend on delivery location.
- [x] Registered hostname `www.carrefouruae.com` is present in `catalog_app.json.allowed_hosts`. No redirect was observed on either request.
- [x] Public access checks were attempted with a self-identifying `PretioCatalogAudit/1.0` client and a 30-second timeout; results are recorded below.
- [ ] Official source ownership and content could not be reverified because the registered page returned 403.
- [ ] Canonical/evergreen, in-place freshness, market scope, and any periodic validity dates could not be verified. The registered record has no `valid_until`; do not infer evergreen status from the URL shape.
- [ ] Terms could not be inspected: the page was denied and exposed no terms link. No robots directives could be read.
- [x] No production catalog fields or values were changed.

### Access evidence

1. Robots: requested/final URL `https://www.carrefouruae.com/robots.txt`; HTTP `403 Forbidden`; content type `text/html`; redirect: none; body/directives unavailable. Evidence URL: https://www.carrefouruae.com/robots.txt
2. Registered catalog: requested/final URL `https://www.carrefouruae.com/mafuae/en/c/fresh-savers`; HTTP `403 Forbidden`; content type `text/html`; redirect: none; short response excerpt: “Access Denied”. Evidence URL: https://www.carrefouruae.com/mafuae/en/c/fresh-savers
3. No retries were made because 403 is an access block, not a transient failure. No login, CAPTCHA, alternate user-agent, hidden endpoint, proxy, or other bypass was used.

## 1B. Online-shop discovery scope

This checkpoint covers only the assigned registered catalog URL. No additional seller/shop discovery sources were queried; the run’s separate discovery work is outside this work unit.

## 2. Product Highlights candidates

- [x] The catalog URL was attempted, but no product/listing content was available.
- [ ] No offer could be checked for same-item normal/promo prices, exact variant, currency, individual image, date, or market-wide eligibility.
- Rejected price candidates: none observed. No price pair or product candidate was visible in the 403 response.
- AE is absent from `pretio/data/currency.json` and has no country highlight feed in this checkout. Any otherwise qualifying UAE item would therefore also be blocked from highlight publication by currency metadata.

## 2A. Obsolescence and disposition

Classify as `STALE_UNVERIFIED` for this attempt. The 403 does not prove the catalog is obsolete or expired; no replacement search or dependent-record removal was attempted. Preserve the registered production record.

## 3. Terminal decision

**Final result: `SKIPPED_BLOCKED`** — direct access to the registered source was denied before content inspection. This is the primary terminal reason; currency metadata is an independent publication constraint, not a claim that a product was found.

## Compact handoff (≤400 words)

- Work unit `AE:carrefour-uae-fresh-savers`, position 1/74; terminal receipt `SKIPPED_BLOCKED`. Attempted: yes. Run: `pretio-oneoff-global-20261123T040625Z`; scope: `ONE_OFF_GLOBAL`. This worker checked only the assigned registered catalog URL.
- The robots URL and registered catalog URL were each requested once, sequentially, using a self-identifying public client with a 30-second timeout. Both returned `403 Forbidden`, `text/html`, no redirect. The catalog body begins “Access Denied.” No retry or access-control bypass was used.
- Robots directives were unavailable and terms could not be inspected because the page was blocked and no terms link was exposed. Source content, ownership, canonical stability, offer dates, geographic eligibility, prices, and images remain unverified.
- The registered host matches the local allowlist. The stored record has no `valid_until`, but this attempt cannot establish evergreen validity. Classify as `STALE_UNVERIFIED`; retain production data.
- No product or price candidates were observed. AE is missing from currency metadata, so highlight publication is also independently blocked.
- Next: continue with the next manifest work unit in its isolated context. No shared counters or other files were changed by this checkpoint.
