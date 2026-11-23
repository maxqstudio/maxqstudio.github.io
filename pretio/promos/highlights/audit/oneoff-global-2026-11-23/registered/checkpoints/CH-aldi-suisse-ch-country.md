# CH:aldi-suisse-ch-country — ALDI Suisse

## Per-catalog checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `CH` | Catalog ID: `aldi-suisse-ch-country` | Retailer: `ALDI Suisse`  
Official URL on record: https://www.aldi-suisse.ch/de/aktionen-und-angebote  
Checked UTC: `2026-11-23T04:15:20Z`  
Mode: `AUDIT` | Manifest work unit: `3 of 74` | Attempt: `1`  
Terminal status: `SKIPPED_BLOCKED`

### 1. Catalog source

- [x] Loaded the exact active catalog record from `pretio/promos/catalog_app.json`: `official_retailer`, national listing, CH country location, `valid_until: null`, `last_verified_at: 2026-09-22T00:00:00Z`. Its summary says offers may depend on region.
- [x] Recorded host `www.aldi-suisse.ch` is in the existing catalog `allowed_hosts` list.
- [ ] Current canonical URL/content verified. The official URL was requested and returned HTTP 403; no `Location` redirect was supplied. Effective response URL is therefore the requested URL: https://www.aldi-suisse.ch/de/aktionen-und-angebote.
- [ ] Evergreen versus rotating status, current promotion period, and source-backed expiry could not be determined. The registry's null `valid_until` does not prove the page is evergreen.
- [ ] Market-wide product coverage could not be checked; the catalog itself warns of location-selected offers.
- [x] Did not change `last_verified_at` or any catalog data.
- [x] Access check made without login, CAPTCHA, alternate routing, hidden endpoints, or retries.

**Access evidence (one request at a time, 30-second timeout):**

1. Robots: requested https://www.aldi-suisse.ch/robots.txt — HTTP `403`, `text/html`, no redirect. Excerpt: `Access Denied` / `You don't have permission to access ... /robots.txt`. Robots policy could not be read.
2. Terms: not verified. The catalog page was denied and no official terms link was available from its response; no alternate route was attempted.
3. Catalog: requested https://www.aldi-suisse.ch/de/aktionen-und-angebote — HTTP `403`, `text/html`, no redirect. Excerpt: `Access Denied` / `You don't have permission to access ... /de/aktionen-und-angebote`.

403 is an access denial, not a transient failure, so no retries were made. Source content and any currently visible offers were unavailable. The official URL and host are from the existing catalog record; no current source URL was positively verified.

### 1B. Online shop / marketplace

- [x] Not applicable to this physical retailer catalog task; no separate shop discovery or seller claim was made.

### 2. Highlight candidates

- [ ] Could not inspect current official offers, so no offer was accepted and the complete set of current discounts was not established.
- [x] Logged the one existing local-feed candidate as not revalidated for this attempt: Hansaplast Wundspray, 50 ml, CHF `4.99` normal / `4.89` promo; existing source URL https://www.aldi-suisse.ch/de/produkt/hansaplast-wundspray-000000000000304228; existing image URL https://dm.emea.cms.aldi.cx/is/image/aldiprodeu/product/jpg/scaleWidth/500/26f9ade8-b04a-4a81-82c2-3534a415752f/Wundspray. The source URL, exact variant, price pair, individual image, market eligibility, and current dates could not be rechecked because the catalog host returned 403. Rejected from new acceptance as `SKIPPED_UNVERIFIED`; this does not establish that the offer is false or expired.
- [x] Existing CH feed currency is CHF and `pretio/data/currency.json` supports CHF for CH. Currency alone does not qualify the unverified candidate.
- [x] No expiry proof was obtained; existing highlight/feed bytes were not changed or pruned.

### 3. Catalog condition and close-out

- Catalog condition: `STALE_UNVERIFIED` for current content; fetch outcome `SOURCE_BLOCKED`.
- [x] No source-backed reason to migrate or retire the registered catalog; no production JSON changes.
- [x] Terminal checkpoint and separate receipt recorded for this work unit only.

## Compact handoff (≤400 words)

- Work unit `CH:aldi-suisse-ch-country`, position 3/74; terminal receipt `SKIPPED_BLOCKED`. Counted as attempted. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; this is one isolated registered-catalog check.
- At `2026-11-23T04:15:20Z`, the robots URL and official catalog URL each returned HTTP 403 `text/html` with an Access Denied body and no redirect. The robots policy could not be read; terms were not verified. No retry or alternate route was used.
- Registered URL/host match the existing catalog entry and the host is already allowlisted, but current page content, evergreen status, offer dates, locality and product evidence remain unverified. CHF is supported for CH.
- Existing Hansaplast Wundspray (50 ml; CHF 4.99 / CHF 4.89) is not revalidated and is excluded from this attempt’s accepted candidates. Its prior source and image URLs are preserved in the checklist. No new product was accepted, and no production feed/catalog/counter was changed.
- Next: run coordinator selects the next manifest unit in a fresh isolated context.
