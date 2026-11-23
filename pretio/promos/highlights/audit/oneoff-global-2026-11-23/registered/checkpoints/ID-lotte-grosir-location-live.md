# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `ID:lotte-grosir-location-live` | manifest position: **32/74** | attempt: **1**  
Country: **ID** | retailer: **LOTTE Grosir** | mode: **AUDIT**  
Checked: **2026-11-23**; exact web-check timestamps were not retained by the browser/search connector; checkpoint recorded by **2026-11-23T09:33:49Z**.  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_BLOCKED**

## 1. Catalog Promo source

- [x] Loaded frozen-manifest and current catalog entry: `lotte-grosir-location-live`, LOTTE Grosir, Indonesia, `source_type: official_retailer`, `coverage_type: national`, active, `valid_until: null`, existing `last_verified_at: 2026-08-22T01:00:00+08:00`.
- [x] Registered URL and host: <https://www.lottemart.co.id/all-promo-grosir> (`www.lottemart.co.id`, already an approved record host); no redirect or canonical URL was checked because source terms require personal use only.
- [x] Robots policy fetched once from <https://www.lottemart.co.id/robots.txt>, HTTP 200. `User-agent: *` disallows several account/helpdesk paths; no matching rule disallows `/all-promo-grosir`.
- [x] Reviewed official Terms at <https://www.lottemart.co.id/syarat-dan-ketentuan>. The page identifies PT LOTTE Mart Indonesia and PT LOTTE Shopping Indonesia as the site operators (lines 8–19). Clause 8.1 states site content may be saved, printed, or displayed only for personal use, not business/commercial use; clause 8.3 addresses copying/downloading in breach (lines 69–73).
- [x] This run would retain promotion and pricing content for the Pretio catalog/product research use, which is commercial. No separate authorization for that use was provided. Stopped before opening the registered catalog URL or copying any offer content.
- [ ] Evergreen/rotating behavior, current catalog content, actual promo dates, official parent navigation, source redirect, and link freshness were not verified. Classify as `STALE_UNVERIFIED`; do not infer expiry or obsolescence from the blocked attempt or old `last_verified_at`.
- [x] No production catalog, feed, index, location, currency, or source verification timestamp was changed.

## 2. Product Highlights

- [x] `IDR` is supported; `pretio/promos/highlights/ID.json` has 4 active items.
- [x] No active ID highlight references `lotte-grosir-location-live` (0 dependencies observed).
- [x] No offer content was opened or retained. Accepted/rejected product candidates: **0/0 inspected**. No price pair, product image, offer validity, or product-level geographic applicability was verified.
- [x] No expired Product Highlight was tied to this catalog; none deleted. No catalog removal/migration was proposed, so no orphan was created.

## 3. Skip decision

- [x] **SKIPPED_BLOCKED** — robots permits the path, but official terms restrict copying/display of site content to personal use and exclude commercial use. No separate permission is evidenced for this run.
- [x] Existing Catalog Promo remains active and unchanged because the evidence does not prove it is expired or obsolete. `valid_until: null` and the historical `last_verified_at` alone are not expiry evidence.
- [x] No Product Highlight accepted; no active item deleted; no production JSON changed.

## Compact handoff (≤400 words)

- Work unit `ID:lotte-grosir-location-live`, position 32/74; receipt `SKIPPED_BLOCKED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Frozen record is LOTTE Grosir, Indonesia, `https://www.lottemart.co.id/all-promo-grosir`, active with `valid_until: null`; existing `last_verified_at` is `2026-08-22T01:00:00+08:00`. The registered catalog page itself was not opened.
- `https://www.lottemart.co.id/robots.txt` returned HTTP 200 and has no matching disallow for `/all-promo-grosir`. Official terms at `https://www.lottemart.co.id/syarat-dan-ketentuan` identify the operators and limit saving/printing/displaying site content to personal use, excluding business/commercial use (clause 8.1); clause 8.3 addresses unauthorized copying/downloading. With no separate permission, price/catalog retention was stopped.
- Current content, dates, evergreen status, and item prices remain unverified. Keep catalog `STALE_UNVERIFIED`; do not mark expired or obsolete. IDR is supported; the ID feed has 4 items and none references this catalog. No product candidate, expiry deletion, or production JSON change.
- Next manifest input: `ID:lotte-mart-location-live`, in a fresh isolated source context.
