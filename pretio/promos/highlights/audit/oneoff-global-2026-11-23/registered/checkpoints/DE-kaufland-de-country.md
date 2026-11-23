# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `DE:kaufland-de-country` | manifest position: **18/74** | Attempt: **1**  
Country: **DE** | Retailer: **Kaufland** | Mode: **AUDIT**  
Source capture completed around **2026-11-23T04:56Z**; exact request event times were not retained  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded active record `kaufland-de-country`: `official_retailer`, country DE, national location, `coverage_label: Germany (store-selected offers)`, and `valid_until: null`. Registered URL: <https://filiale.kaufland.de/angebote.html>. It is already on the source-host allowlist. Existing `last_verified_at` is `2026-09-22T00:00:00Z` and was not changed.
- [x] Robots check: <https://filiale.kaufland.de/robots.txt> returned HTTP `200`, `text/plain; charset=UTF-8`, 840 UTF-8 bytes. Its `User-agent: *` rules disallow several unrelated paths (including `/angebote/aktuell/uebersicht/detail`); the exact registered path `/angebote.html` is not disallowed. No robots crawl-delay was present in the captured text.
- [x] The exact registered URL returned HTTP `200`, `text/html; charset=UTF-8`, 433,654 UTF-8 bytes, `lang="de-DE"`, and title “Lebensmittel- und Non-Food-Angebote, Coupons, Rabatte | Kaufland”. The page showed “Aktuelle Angebote” and “Gültig vom 23.11.2026 bis 28.11.2026”, with 40 visible product tiles. The current offer dates and content show this page is live and currently updated in place. The URL is evergreen-looking; historical URL stability was not independently checked.
- [x] Four bounded GETs were made to the exact registered URL to inspect the page/card content after the initial response; each returned HTTP 200. These were successful reads, not retries. Timeouts were 20–25 seconds; no login, CAPTCHA, hidden API, alternate host, proxy, or access-control bypass was used. The PowerShell wrapper returned `BaseResponse.ResponseUri = null`; final URI/redirect chain cannot be asserted. No `Location` header was captured.
- [ ] Official retailer T&Cs were not independently fetched. The registered `coverage_label` says store-selected offers; the landing page did not establish nationwide eligibility for individual cards. No historical source snapshots were checked.
- [x] No catalog record or `last_verified_at` change is justified. The page is live; this attempt does not prove the source obsolete or its canonical URL changed.

## 2. Product Highlights candidates

- [x] `DE` uses `EUR`. The DE feed currently has 8 items referencing `kaufland-de-country`; all 8 have `valid_from: 2026-11-23` and `valid_until: 2026-11-28`, so none is expired on the run date. The live page showed matching current cards for Ehrmann Almighurt (`1.11` / `2.39`), Tassimo (`4.29` / `6.99`), Landliebe Landkäse/Quäse (`1.59` / `2.39`), Weihenstephan Butter (`1.29` / `2.99`), and Jägermeister (`11.99` / `14.99`). Existing feed items not visible among the 40 landing-page cards (Ferrero Stern, Dovgan Frischkäse-Flocken, White Birch Vodka) have future validity dates; absence from this one listing is not expiry proof, so they were left untouched.
- [x] Other visible same-card lower/higher price pairs were recorded as audit-only observations (EUR; every tile showed the current `23–28 Nov 2026` offer period): grapes 500 g `1.99/2.49`; mini tomatoes 250 g `0.99/1.49`; Landliebe milk 1 l `9.99/11.88`; Babybel Mini `2.89/4.79`; Bahlsen Comtess two-pack offer `1.50/3.00` (multi-buy text, not normalized); Melitta coffee `4.99/8.49` (limit 4); Mövenpick Caffè Crema `12.99/16.99` (limit 4); Ferrero Rocher 200 g `2.66/4.79`; Duplo `2.22/3.29`; Milka Weihnachtsmann `1.11/1.99`; Fürst von Metternich Sekt `1.99/3.29`; Rotkäppchen Sekt `2.75/4.99` (limit 3 cartons); Persil `15.99/17.95`; plus current-card variants of Ehrmann, Weihenstephan, Landliebe cheese, Tassimo and Jägermeister above. Some cards also showed Kaufland Card XTRA prices/conditions.
- [ ] No new product was accepted: although the landing page exposes exact offer pairs, dates and per-product image URLs, it does not prove each physical offer’s eligible geographic area across Germany. The catalog record itself says “store-selected offers”. Tile image URLs were observed on `kaufland.media.schwarz`, but image bytes were not fetched/decoded. These products fail the location/image gate for publication. This is not a claim that the offers are unavailable nationwide.
- [x] No product expiry was proven beyond the currently future `valid_until` dates. No highlight, catalog, or index production JSON was changed; no expired item was removed.

## 3. Disposition

- [x] **SKIPPED_UNVERIFIED** — official live source and current discount pairs were accessible, but product-level nationwide eligibility was unverified and image assets were not validated. Do not publish or count any new Product Highlight from this attempt.
- [x] No accepted product IDs and no deletions. Preserve the 8 existing linked items; their recorded validity ends 2026-11-28, after the run date.

## Compact handoff (≤400 words)

- `DE:kaufland-de-country`, position 18/74, terminal receipt `SKIPPED_UNVERIFIED`; run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Exact registered page <https://filiale.kaufland.de/angebote.html> and robots URL were checked. The page and robots both returned HTTP 200. Robots rules do not disallow `/angebote.html`. The page served German (`de-DE`) current offers valid 23–28 Nov 2026, with 40 cards. Four bounded page GETs (20–25s timeout) were used to inspect the response; zero retries or bypasses. The wrapper did not expose final URI/redirect metadata. T&Cs and historical URL stability were not independently checked.
- Multiple live explicit price pairs were seen, including 5 already represented in DE highlights and the additional audit-only observations above. However, store-selected physical offer geography was not proven nationally, and image URLs were not byte-validated. Publish none from this attempt.
- Existing DE feed contains 8 Kaufland items, all valid through 2026-11-28. Three were not visible in this 40-card landing-page response; no absence-based cleanup was performed. No expiry or catalog obsolescence was proven; no production JSON changed.
- Next manifest unit: `DE:lidl-de-country` at <https://www.lidl.de/c/online-prospekte/s10005610/>. Continue in a fresh isolated context.
