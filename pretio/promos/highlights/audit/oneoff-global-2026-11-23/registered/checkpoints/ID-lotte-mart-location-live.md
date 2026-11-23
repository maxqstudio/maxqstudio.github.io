# Pretio — LOTTE MART catalog checkpoint

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `ID:lotte-mart-location-live` | manifest position: **33/74** | attempt: **1**  
Country: **ID** | retailer: **LOTTE MART** | mode: **AUDIT**  
Checked UTC: **2026-11-23T09:37:10Z**  
Base SHA / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_BLOCKED**

## Source and access

- Frozen manifest and current catalog record identify `https://www.lottemart.co.id/all-promo-mart`, `catalog_id=lotte-mart-location-live`, `source_type=official_retailer`, `valid_until=null`, and existing `last_verified_at=2026-08-22T01:00:00+08:00`. The host is already allowlisted.
- Fetched `https://www.lottemart.co.id/robots.txt` once at 2026-11-23T09:37:10Z. HTTP 200; `User-agent: *` disallows `/admin`, store-selection/account/helpdesk and subscription paths; no rule disallows `/all-promo-mart`.
- Read the official Terms at `https://www.lottemart.co.id/syarat-dan-ketentuan`. It identifies PT LOTTE Mart Indonesia and PT LOTTE Shopping Indonesia as site operators (sections 1; page lines 8–19). Clause 8.1 restricts saving, printing, or displaying site content to personal use, excluding business/commercial use; clause 8.3 describes consequences for prohibited copying/downloading (page lines 69–73). No separate authorization for commercial retention is evidenced in this run.
- Stopped before requesting the registered promo page or retaining promotional content. Requested/final URL, redirect chain, current offers, price pairs, source dates, freshness, and evergreen/rotating behavior are therefore **not verified**. Do not infer expiry or obsolescence from the blocked check or old verification timestamp.

## Catalog, geography, and dependencies

- Existing catalog location rules list seven Indonesian provinces (North Sumatra, DKI Jakarta, West Java, Central Java, East Java, Banten, South Sulawesi), although `coverage_type` is `national`. The complete market scope and whether any individual offer applies nationwide were not rechecked; flag this discrepancy for independent review.
- Current ID highlight feed contains four items referencing this catalog: `id-lotte-mart-pocari-sweat-pet-900ml-20261119`, `id-lotte-mart-buavita-juice-245ml-20261119`, `id-lotte-mart-vaseline-gluta-hya-330ml-20261119`, `id-lotte-mart-teh-kotak-300ml-20261119`. Their existing `valid_until` values are all `2026-12-02`, which is not before the market date `2026-11-23`; no expiry deletion is supported by dates in this check. Source content, price pairs, images, and offer geography were not revalidated because of the terms restriction.
- No catalog removal or URL migration proposed; no dependent highlights would be orphaned. No production catalog/feed/index or `last_verified_at` changed.

## Decision

**SKIPPED_BLOCKED** — the robots rules do not disallow the path, but the official site terms limit site-content retention to personal use and exclude business/commercial purposes. Catalog details and product observations were not accessed or copied. Keep the active source `STALE_UNVERIFIED` for current content; do not classify it as expired or obsolete. No new or rejected offers were inspected (0/0).

## Compact handoff

See `registered/handoffs/ID-lotte-mart-location-live.md` (150 words). Next manifest input: `ID:superindo-national-live`, using a fresh isolated source task.
