# CH:coop-ch-country — Coop

## Per-catalog checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `CH` | Catalog ID: `coop-ch-country` | Retailer: `Coop`  
Official URL on record: https://www.coop.ch/de/aktionen/alle-aktionen/c/m_1111  
Checked UTC: `2026-11-23T04:19:56Z`  
Mode: `AUDIT` | Scope: `ONE_OFF_GLOBAL` | Manifest work unit: `4 of 74` | Attempt: `1`  
Terminal status: `SKIPPED_UNVERIFIED`

### 1. Catalog source

- [x] Loaded the exact active catalog record from `pretio/promos/catalog_app.json`: `official_retailer`, national listing, CH country location, `valid_until: null`, `last_verified_at: 2026-09-22T00:00:00Z`. Its summary says offers may depend on store and region.
- [x] Registered host `www.coop.ch` is in the existing `allowed_hosts` list.
- [x] Public robots and terms checks completed. Robots text allows the requested path (no matching disallow) and sets `Crawl-delay: 5`; a six-second gap was observed before opening the catalog page. No login, CAPTCHA, hidden endpoint, proxy, or retry was used.
- [x] The requested page opened as the official “Alle Aktionen” listing. The access tool displayed the requested URL as the final URL, with no redirect metadata. Its raw HTTP status code was not exposed; the tool reported `text/html`. The page says “Es stehen 4016 Produkte zur Auswahl” and has a `Filiale` filter, but its accessible text contains no individual product cards, names, prices, or image URLs. The route is an evergreen-style all-actions landing page; history of in-place updates was not independently compared.
- [ ] Country-wide eligibility for individual offers is not proven. The catalog summary warns of store/region variation, the page has a branch filter, and Coop AGB state assortment “kann auch regional je nach Lieferort abweichen.” No source-backed offer dates were visible.
- [x] No catalog or production data was edited; `last_verified_at` was not changed.

**Evidence links and access details (public page checks, each returned within 30 seconds):**

1. Robots: [https://www.coop.ch/robots.txt](https://www.coop.ch/robots.txt) — extracted as `text/plain`; HTTP status not exposed. Excerpt: `User-agent: *` / `Crawl-delay: 5`; disallows include `/catalog`, not the requested `/de/aktionen/alle-aktionen/c/m_1111` path.
2. Terms: [https://www.coop.ch/de/agb.html](https://www.coop.ch/de/agb.html) — extracted as `text/html`; HTTP status not exposed. Coop AGB, version 3.2 dated 2026-05-13, cover online orders and say the assortment can vary by delivery region. Searches of this page found no `automatis`, `Crawler`, or `Scraping` text. It states product descriptions, images, photos, and texts are solely used by Coop; no image was copied.
3. Catalog: [https://www.coop.ch/de/aktionen/alle-aktionen/c/m_1111](https://www.coop.ch/de/aktionen/alle-aktionen/c/m_1111) — extracted as `text/html`; HTTP status and redirect chain not exposed. Excerpts: `# Alle Aktionen`, `Es stehen 4016 Produkte zur Auswahl`, and `Filiale`. No item-level offer evidence was available in the rendered text.

### 1B. Online shop / marketplace

- [x] This was the registered Coop catalog source itself; no separate online-shop or marketplace discovery was run.

### 2. Highlight candidates

- [x] The existing CH feed contains no item tied to `coop-ch-country`.
- [ ] No offer was accepted. The page extraction exposed 4,016 results as a count, not inspectable offers. No exact product/variant, same-product normal and lower promo prices, individual image, offer dates, or market-wide eligibility could be verified. No candidate product IDs were visible to reject individually.
- [x] CHF is supported for CH in `pretio/data/currency.json`; supported currency alone does not qualify an offer.
- [x] No expiry evidence was found; no country feed item was added, removed, or refreshed.

### 3. Catalog condition and close-out

- Catalog condition: `STALE_UNVERIFIED` for item-level current offers; page classification `LINK_STABLE` (evergreen-style “Alle Aktionen” listing; update history not tested).
- [x] No source-backed reason to migrate or retire the catalog; no production JSON changes.
- [x] Terminal checkpoint and separate receipt recorded for this work unit only.

## Compact handoff (≤400 words)

- Work unit `CH:coop-ch-country`, position 4/74; terminal receipt `SKIPPED_UNVERIFIED`. Counted as attempted. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`.
- At `2026-11-23T04:19:56Z`, robots showed `Crawl-delay: 5` and no disallow matching the catalog path; the delay was observed. The official catalog page returned extracted HTML at the requested URL; raw HTTP status and redirect metadata were unavailable from the access tool. No retry or alternate route was used.
- Coop’s official AGB page (version 3.2, 2026-05-13) says assortment can vary by delivery region; searches found no crawler or scraping text. It also says product images/texts belong to Coop; none were copied.
- The current page identifies itself as “Alle Aktionen” and reports 4,016 products, but the accessible text has only filters and pagination, without item cards or price pairs. No candidate met the same-product price, image, dates, and market-wide gates. CHF is supported for CH; no existing CH highlight references this catalog.
- No production feed or catalog data changed. Next: coordinator selects the next manifest unit in a fresh isolated context.