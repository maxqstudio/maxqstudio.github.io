# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `EG:spinneys-eg-weekly-deals` | Manifest position: **25/74**  
Country: **EG (Egypt)** | Retailer: **Spinneys** | Mode: **AUDIT**  
Checked: **2026-11-23 UTC** (the HTTP/browser tools did not retain exact request timestamps)  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded active record `spinneys-eg-weekly-deals`: `official_retailer`, Egypt / `EG`, `coverage_type: national`, `valid_until: null`, `last_verified_at: 2026-11-15T05:42:54.476Z`.
- [x] Exact registered URL: <https://spinneys-egypt.com/en/deals>. `spinneys-egypt.com` is present in the approved catalog `allowed_hosts`; no host migration was made.
- [x] Robots check: `GET https://spinneys-egypt.com/robots.txt` returned HTTP `200`, `text/plain`, 144 bytes. `User-agent: *` has an empty `Disallow` value; the registered `/en/deals` path is not disallowed. The local PowerShell response did not retain the final URI for this request.
- [x] Official page check: the exact registered URL returned HTTP `200`, `text/html; charset=utf-8`, 363,439 UTF-8 bytes, page title `Spinneys: Deals`; the HTTP client's request URI remained the exact registered URL. A browser-readable open of the same page also resolved to the same URL. These were successful reads for metadata/visible content capture, not retries after a failed request.
- [x] The source footer linked Terms and Conditions at `/en/terms`. One read returned HTTP `200`, `text/html; charset=utf-8`, 202,391 bytes, title `Terms & Conditions`. A targeted check for automated/robot/crawler/scraping/collection/reproduction terms found no matching text; the full legal text was not reviewed line by line. No access restriction was observed in that check.
- [ ] The page is a persistent `/en/deals` route, but this single snapshot does not prove how it is updated in place. Current individual deal content could not be verified.
- [ ] The page says `Delivering to Select Area` and requests a district because the selected delivery address is incomplete. It showed no usable offer cards or product prices. I did not choose an arbitrary district, access a hidden endpoint, or infer countrywide item eligibility from the catalog's national label.
- [x] The source is **`STALE_UNVERIFIED` for current offer claims**. No current catalog expiry, successor, or obsolescence was proven. Existing `last_verified_at` was not changed.

## 2. Product Highlights

- [x] `EG`/EGP is absent from `pretio/data/currency.json`; the highlight index has no `EG` entry and there is no `EG.json` feed.
- [ ] No product offer was observable without a selected delivery district. No exact product/variant, normal and lower promo price pair, official product image, item-level delivery area, or source-backed offer validity was verified. Accepted/rejected observed candidates: **0 / 0**.
- [x] No product was added or removed. No expired product or catalog was proven; no feed or index hash changed.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — the official evergreen-looking deals route and robots policy were accessible, but current deal cards were not available without completing a location-specific address. Countrywide item applicability and valid product discounts could not be verified. Missing EGP/feed metadata independently blocks highlight publication.
- [x] No CAPTCHA, login, arbitrary location selection, proxy, hidden API, alternate host, or access-control bypass was used. No production JSON changed.

## Compact handoff (≤400 words)

- Work unit `EG:spinneys-eg-weekly-deals`, manifest position `25/74`; terminal receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; base/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- The active Spinneys Egypt record points to `https://spinneys-egypt.com/en/deals`; its host is allowlisted. Its `valid_until` is null; `last_verified_at` remains `2026-11-15T05:42:54.476Z`.
- Robots returned `200 text/plain` (144 bytes), with an empty `Disallow` for `User-agent: *`; `/en/deals` is allowed. The registered page returned `200 text/html; charset=utf-8` (363,439 bytes), title `Spinneys: Deals`, same request URI. The footer-linked Terms page returned `200` and a targeted automated-access keyword check found no restriction; the whole legal text was not read line by line. Exact request timestamps/final robots URI were not retained.
- The visible page requires a delivery area and says the selected address lacks a district; no usable deal cards/prices appeared. No location was guessed, and no hidden API or retry was used. Current offer data, normal/promo price pairs, product images, item geography and validity remain unverified. No obsolescence/expiry is inferred.
- `EG`/EGP has no currency metadata, no `EG` index entry and no `EG.json` feed. No candidate accepted, no expired item removed and no production JSON changed. Continue with the next frozen manifest source in a fresh context.
