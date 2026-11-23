# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `CH:migros-ch-country` | Position: `7 of 74` | Attempt: `1`  
Country: `CH` | Catalog ID: `migros-ch-country` | Retailer: `Migros`  
Official URL: https://www.migros.ch/de/offers/home  
Checked UTC: `2026-11-23T04:29:41Z`  
Mode: `AUDIT` | Scope: `ONE_OFF_GLOBAL`  
Terminal status: `SKIPPED_UNAVAILABLE`

## 1. Catalog Promo source

- [x] Loaded the active record from `pretio/promos/catalog_app.json`: `official_retailer`, CH country, national catalog label, `valid_from: null`, `valid_until: null`, `last_verified_at: 2026-09-22T00:00:00Z`. Its summary says offer availability may depend on region; the coverage label says “Switzerland (location-selected offers).”
- [x] `www.migros.ch` is an existing `allowed_hosts` entry. The requested URL uses HTTPS and that host.
- [x] Checked `https://www.migros.ch/robots.txt` once: HTTP 200, `text/plain`. The requested `/de/offers/home` path has no matching disallow; the file disallows specific `/offers/instore/`, `/offers/coupons/`, and `/promotion/` paths, which were not opened. No `Crawl-delay` directive was present in the returned text. The response object did not expose the final URL or redirect chain, so those are recorded as unknown.
- [x] Made one 30-second-bounded GET to the exact registered page, with no retry and no proxy. Requested URL: `https://www.migros.ch/de/offers/home`; final URL: same; redirects: none. HTTP 403, `text/html; charset=UTF-8`. The page text says Migros Online is temporarily closed for maintenance (in German, French, English and Italian). No offer cards or product/price/image content were visible. This is an unavailable response, not evidence that no promotions exist.
- [x] Terms check: official Migros Help center robots returned HTTP 200 `text/plain; charset=utf-8`; the AGB article path was not disallowed. The linked [Migros Online AGB](https://support.migros.ch/hc/de/articles/4407834469266-Allgemeine-Gesch%C3%A4ftsbedingungen) returned HTTP 403 `text/html; charset=UTF-8` with “Just a moment...” and no redirect; terms text could not be read. No retry or challenge bypass was attempted. A search preview identified this as “Allgemeine Geschäftsbedingungen – Migros Hilfe”; its cached date/version was not used as current terms evidence.
- [ ] Evergreen/current-in-place behavior and any current promotion period could not be checked. The null registry `valid_until` does not prove that the URL is evergreen. No source-backed offer dates were found.
- [x] Did not change the catalog record or `last_verified_at`; no production JSON was edited.

**Evidence links and access details:**

1. Robots: [Migros robots.txt](https://www.migros.ch/robots.txt) — requested directly, HTTP 200 `text/plain`; exact final URL/redirect metadata was not exposed by the response object.
2. Catalog: [Migros offers](https://www.migros.ch/de/offers/home) — requested and final URL match, no redirect; HTTP 403 `text/html; charset=UTF-8`; maintenance message described above.
3. Terms-site robots: [Migros Help robots.txt](https://support.migros.ch/robots.txt) — HTTP 200 `text/plain; charset=utf-8`; the AGB route was not disallowed.
4. Terms: [Migros Online AGB](https://support.migros.ch/hc/de/articles/4407834469266-Allgemeine-Gesch%C3%A4ftsbedingungen) — direct GET HTTP 403 `text/html; charset=UTF-8`, response text “Just a moment...”; terms unavailable for review.

## 1B. Online-store / marketplace

- This task checked only the registered Migros catalog source. No separate online-shop or marketplace discovery was run.

## 2. Product Highlights candidates

- [x] `pretio/promos/highlights/CH.json` has no existing item with `catalog_id: migros-ch-country`.
- [x] Accepted candidates: `0`. Individually rejected candidates: `0 observed`; the 403 response exposed no product candidates to assess. No claim is made that Migros has no current promotion.
- [x] CHF is supported for CH in `pretio/data/currency.json`.
- [x] Because no product evidence was accessible, no exact variant, same-seller normal/lower promo price pair, individual image, currency display, offer dates, or item-level countrywide applicability could be verified. The catalog’s location-selected label is not nationwide product proof.
- [x] No highlight was added, refreshed, or pruned; no expiry evidence was found.

## 2A. Catalog condition

- Catalog condition: `STALE_UNVERIFIED`; source result: `FETCH_FAILED` (HTTP 403 maintenance response). The URL was not verified current or obsolete, and the catalog is not a proven rotating period link. Do not migrate or retire it from this evidence.
- Expired IDs deleted: none. Catalog and Product Highlights production files were not changed.

## Compact handoff (≤400 words)

- Work unit `CH:migros-ch-country`, position `7/74`; terminal receipt `SKIPPED_UNAVAILABLE`. Counted as attempted. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`.
- At `2026-11-23T04:29:41Z`, one bounded request to the registered official URL returned HTTP 403 `text/html; charset=UTF-8`, with no redirect and a multilingual Migros Online maintenance message. No retry, alternate offer page, challenge bypass, or hidden endpoint was used; direct offers and terms requests used no proxy. Robots returned 200 and did not disallow `/de/offers/home`; `www.migros.ch` is allowed in the registered host list.
- The official Migros Help AGB route was not disallowed by its robots file, but a direct request returned HTTP 403 “Just a moment...”. Terms remain unverified; no search-preview text was relied on as current policy.
- No offer cards were exposed, so accepted products: `0`; observed individual candidates rejected: `0`. No product price pair, image, item-level geography, or validity dates could be verified. CH currency metadata supports CHF; the CH feed has no existing Migros-linked item.
- Catalog condition `STALE_UNVERIFIED`; its null `valid_until` does not establish an evergreen URL. No expiry or obsolescence evidence; no production JSON or `last_verified_at` changed. Checkpoint: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/checkpoints/CH-migros-ch-country.md`; receipt: `pretio/promos/highlights/audit/oneoff-global-2026-11-23/registered/receipts/CH-migros-ch-country.json`.
- Next: leave subsequent manifest work to the run coordinator; no other catalog was processed here.