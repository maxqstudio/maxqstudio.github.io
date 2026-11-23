# DE:aldi-sued-de-country — ALDI Süd

## Per-catalog checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `DE` | Catalog ID: `aldi-sued-de-country` | Retailer: `ALDI Süd`  
Official URL on record: https://www.aldi-sued.de/angebote  
Checked UTC: `2026-11-23T04:51:36Z`  
Mode: `AUDIT` | Manifest work unit: `18 of 74` | Attempt: `1`  
Terminal status: `SKIPPED_BLOCKED`

### 1. Catalog source

- [x] Loaded exact active catalog record. It identifies ALDI Süd, the DE country location, national listing, `valid_until: null`, and notes that availability can vary by location.
- [x] The recorded host `www.aldi-sued.de` is present in the existing `allowed_hosts` list.
- [ ] Current canonical URL/content verified. Requested the exact frozen URL `https://www.aldi-sued.de/angebote`; response was HTTP `403`, `text/html`, with no redirect. Effective URL remained the requested URL.
- [ ] Evergreen update behavior, current promotion dates, and market-wide item eligibility could not be verified.
- [x] Robots check requested `https://www.aldi-sued.de/robots.txt`; HTTP `403`. PowerShell exposed no Content-Type or response body for this error, so the robots policy could not be read.
- [ ] Terms/access conditions not verified: the catalog response was denied and supplied no visible legal link. No guessed terms URL or alternate route was attempted.
- [x] No retry: both outcomes were explicit access denials, not transient failures. No login, CAPTCHA, alternate routing, hidden endpoint, proxy, or access-control bypass used.
- [x] No catalog data or `last_verified_at` changed.

**Access evidence and bounds:** One robots request and one canonical catalog request, sequentially; each had a maximum 30-second timeout and completed in under two seconds. Robots: [https://www.aldi-sued.de/robots.txt](https://www.aldi-sued.de/robots.txt), HTTP `403`; no redirect, policy text unavailable. Catalog: [https://www.aldi-sued.de/angebote](https://www.aldi-sued.de/angebote), HTTP `403`, `text/html`, no redirect. Short body excerpt: “Access Denied … You don't have permission to access … /angebote”. The page exposed no visible offers to inspect.

### 1B. Online shop / marketplace

- [x] Not applicable to this registered physical-retailer catalog unit; no separate shop discovery was performed.

### 2. Highlight candidates

- [x] No current offers were accessible; accepted new products: `0`. No candidate could be checked for dual price, exact individual image, currency, dates, or nationwide eligibility.
- [x] Existing DE feed has 33 items; 8 reference `aldi-sued-de-country`, below the per-country and per-retailer limits. Those existing items were not revalidated and were not changed.
- [x] No expiry evidence was obtained for existing records; none was pruned from this blocked attempt.
- [x] EUR is configured for DE, but currency support alone does not qualify an offer.

### 3. Catalog condition and close-out

- Catalog condition: `STALE_UNVERIFIED`; fetch outcome: `SOURCE_BLOCKED`.
- [x] No production catalog, highlight feed, index, or shared run summary changed.
- [x] Terminal checkpoint and separate receipt recorded for this work unit only.

## Compact handoff (≤400 words)

- Work unit `DE:aldi-sued-de-country`, position `18/74`; terminal receipt `SKIPPED_BLOCKED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`.
- Used the exact frozen URL `https://www.aldi-sued.de/angebote`. At `2026-11-23T04:51:36Z`, it returned HTTP `403`, `text/html`, no redirect; visible excerpt: “Access Denied … You don't have permission to access … /angebote”. The separate robots request to `https://www.aldi-sued.de/robots.txt` returned `403`; policy text and terms were not verified. No retries or alternate routes were used.
- The recorded host is allowlisted and the catalog identifies DE, but current content, promotion dates, location-specific scope, and offers remain unverified. No visible offer was available for inspection; accepted new items `0`.
- The DE feed contains 33 items, including 8 for ALDI Süd. They remain unchanged and were not revalidated. No item was removed because no expiry evidence was obtained. EUR is configured for DE.
- No production JSON or shared run summary was edited. Next step: coordinator proceeds to the next manifest unit in a fresh isolated context.
