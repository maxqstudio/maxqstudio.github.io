# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `CH` | Catalog ID: `lidl-ch-country` | Retailer: `Lidl Schweiz`  
Official URL: https://sortiment.lidl.ch/de/aktuelle-aktionen  
Audit completed UTC: `2026-11-23T04:22:44Z`  
Mode: `AUDIT` | Manifest work unit: `6 of 74` | Attempt: `1`  
Terminal status: `SKIPPED_UNVERIFIED`

## 1. Catalog Promo source

- [x] Loaded the active record from `pretio/promos/catalog_app.json`: `official_retailer`, country `CH`, `coverage_type: national`, coverage label `Switzerland (location-selected offers)`, `valid_until: null`, `last_verified_at: 2026-09-22T00:00:00Z`.
- [x] Registered host `sortiment.lidl.ch` is in the catalog `allowed_hosts` list.
- [x] Robots checked before the catalog URL. `https://sortiment.lidl.ch/robots.txt` returned HTTP `200`, `text/plain;charset=UTF-8`, zero redirects, 461 bytes. `User-agent: *` does not disallow `/de/aktuelle-aktionen`; it disallows `/catalog/`, `/index.php/`, query-string paths and several other paths. No crawl-delay directive was present. `User-agent: Yandex` is disallowed site-wide and is not the audit user-agent.
- [x] Requested the exact registered catalog URL once with a 30-second timeout and a self-identifying public client; no retry or browser/API fallback. HTTP `200`, `text/html; charset=UTF-8`, 298,593 bytes, final URL identical to request, zero redirects.
- [ ] Terms of service not independently inspected. The page exposed a Lidl Plus terms link and privacy/imprint links; those linked pages were not fetched within the one-canonical-source bound. Robots permission is not treated as terms permission.
- [ ] A current promotions listing is visible at the registered evergreen-looking route. Page text shows pagination `1` through `5`; only the returned first page was inspected. No rotating URL, source-backed validity dates or proof of in-place update behavior was established in this bounded attempt.
- [ ] Item-level market-wide participation was not established. The catalog itself labels offers “Switzerland (location-selected offers)”; the page response did not show product-level national applicability.
- [x] No catalog record, `last_verified_at`, feed, currency file, or other production JSON was changed.

**Source evidence (requested/final URLs, redirects, content type, excerpts):**

1. Robots — requested/final <https://sortiment.lidl.ch/robots.txt>; HTTP `200`; `text/plain;charset=UTF-8`; no redirects. Excerpt: `User-agent: *` followed by path disallow rules; `/de/aktuelle-aktionen` is not disallowed. Evidence: <https://sortiment.lidl.ch/robots.txt>.
2. Catalog — requested <https://sortiment.lidl.ch/de/aktuelle-aktionen>; final same URL; HTTP `200`; `text/html; charset=UTF-8`; no redirects. Title: `Aktuelle Aktionen | Lidl Schweiz`. Excerpt: `Aktuelle Aktionen ... Seite 1 Seite 2 Seite 3 Seite 4 Seite 5 ... Angebote solange Vorrat.` Product examples in the returned page text: `Weichspüler Spa Moments Diverse Sorten — Aktion CHF 1.99 pro 750ml`; `duplo Lebkuchen 10er — Aktion CHF 3.59 pro 182g`; `Airwaves Menthol & Eucalyptus — Aktion CHF 9.75 pro 294g`. The page also says offers last while supplies last and that product depictions may differ. Evidence: <https://sortiment.lidl.ch/de/aktuelle-aktionen>.

## 2. Product Highlights — discounted items only

- [ ] No offer was accepted. A whole-response text/HTML scan found promo-price/“Aktion” evidence but no explicit normal/reference price labels or old-price markers; the listed examples show promo values only. This is insufficient to prove `normal_price > promo_price` for the same variant.
- [ ] Product images were not fetched or decoded, item-specific validity dates were not found in the inspected page excerpt, and product-level country-wide scope was not shown. These required gates remain unmet.
- [x] CHF is the configured currency for CH in `pretio/data/currency.json`; currency support does not cure the missing price, image, date and market-scope evidence.
- [x] Existing CH feed contains `0` items with `catalog_id: lidl-ch-country`; there is no Lidl item to revalidate or prune in this source attempt.
- [x] Rejected candidates: page-1 promo-only listings (including the three examples above), rejected from acceptance for missing same-product normal/promo price pair; all page-1 listings likewise remain unaccepted because image decoding, validity and market-wide participation were not established. Pages 2–5 and product/image/terms links were not fetched.

## 3. Catalog condition and close-out

- Catalog source outcome: `FETCH_OK`; canonical route is reachable. Offer qualification: `SKIPPED_UNVERIFIED`. No evidence of an obsolete/expired catalog or replacement was found.
- No current offers can be published from this bounded attempt. No production data or Issue #57 was changed.

## Compact handoff (≤400 words)

- Work unit `CH:lidl-ch-country`, manifest position `6/74`; terminal receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, audit completed `2026-11-23T04:22:44Z`.
- Robots <https://sortiment.lidl.ch/robots.txt> returned HTTP 200 `text/plain;charset=UTF-8`, no redirects; wildcard rules allow the registered `/de/aktuelle-aktionen` path. The single canonical URL request <https://sortiment.lidl.ch/de/aktuelle-aktionen> returned HTTP 200 `text/html; charset=UTF-8`, 298,593 bytes, final=requested, zero redirects. No retry or alternate route was used.
- The official page title is “Aktuelle Aktionen | Lidl Schweiz”; page 1 lists promo-only examples (Weichspüler CHF 1.99/750ml, duplo Lebkuchen CHF 3.59/182g, Airwaves CHF 9.75/294g). The response contains pagination for pages 1–5. The page text has promo prices but no explicit matching normal/reference price evidence, so no candidate qualifies. The listing also says “Angebote solange Vorrat.”
- Product images were not fetched/decoded; item validity dates and national applicability were not proven. The catalog coverage label says “Switzerland (location-selected offers).” CHF is supported, but that alone is insufficient. Existing CH feed has no Lidl entries. Terms pages were linked but not opened; terms remain unchecked.
- No production JSON, catalog record, feed, index, or Issue #57 was changed. Next: coordinator proceeds to the next manifest work unit; do not claim the uninspected pages 2–5 were checked.