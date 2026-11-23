# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `CH:denner-ch-country` | Position: `5 of 74` | Attempt: `1`  
Country: `CH` | Retailer: `Denner` | Mode: `AUDIT`  
Checked UTC: `2026-11-23T04:20:41Z` (latest source observation)
Terminal status: `SKIPPED_UNVERIFIED`

## 1. Catalog Promo source

- [x] Loaded active record: `official_retailer`, coverage `national`, CH country location, `valid_until: null`, `last_verified_at: 2026-09-22T00:00:00Z`; coverage label says `Switzerland (location-selected offers)`. Registered URL: <https://www.denner.ch/de/aktionen/aktuelle-aktionen>.
- [x] Registered host `www.denner.ch` is in `catalog_app.json.allowed_hosts`.
- [x] Robots checked before page access: <https://www.denner.ch/robots.txt> returned HTTP `200 OK`, `text/plain; charset=utf-8`, no redirect. Excerpt: `User-agent: *` / `Allow: /`; it disallows checkout, shopping-list, preview and a specific auth query path; no crawl-delay is stated. The catalog path is not disallowed.
- [x] Terms link observed on official page and checked: <https://www.denner.ch/de/agb> returned HTTP `200 OK`, `text/html; charset=utf-8`, no redirect. Excerpt: `Diese Allgemeinen Geschäftsbedingungen gelten ... für Bestellungen ... via ... Weinshop`; this document describes the online wine shop and did not expose a crawling-specific rule for the promotions page. No login or gated page was used.
- [x] Registered catalog page requested once: HTTP `200 OK`, `text/html; charset=utf-8`, no redirect; final URL equals requested URL. `<title>`: `Aktuelle Aktionen - Aktuelle Preise und Aktionen`; canonical URL matches registered URL. It exposes 33 unique product-action links. This confirms the official page was accessible and canonical at observation time, but does not establish long-term update-in-place behavior.
- [ ] Offer applicability is not verified countrywide. The registered coverage label explicitly notes location-selected offers; no product-level all-Switzerland participation evidence was captured.
- [x] No `catalog_app.json` fields or `last_verified_at` were changed.
- [x] No alternate domains, hidden endpoints, proxy, login, CAPTCHA, or access-control workaround used; no retry was needed.

**Requests and evidence (all public HTTPS; each request used a 30-second timeout):**

1. Robots — requested/final <https://www.denner.ch/robots.txt>; `200`, `text/plain`, redirect: none; excerpt above.
2. Catalog — requested/final <https://www.denner.ch/de/aktionen/aktuelle-aktionen>; `200`, `text/html`, redirect: none; title/canonical and 33 unique action-product links captured.
3. Terms — requested/final <https://www.denner.ch/de/agb>; `200`, `text/html`, redirect: none; wine-shop AGB excerpt above.
4. One public product detail page from the catalog — requested <https://www.denner.ch/de/aktionen/ancora-alaska-wildlachs~p1009058?variant=958940a9-0779-4b74-bbdb-bbff43d64190>; `200`, `text/html`; product title `Ancora Alaska Wildlachs - Aktuelle Preise und Aktionen | Denner`; effective URL remained on `www.denner.ch`. Excerpt: `geschnitten, Alaska, 2 x 100 g 20% 7.20 statt 9.–`. It references an individual image at <https://denner.imgix.net/assets/83be51ae-a9de-4ab8-b61c-2f6ddae5336e/web/904525_25_07_04.png>.

## 1B. Online shop / marketplace

- [x] Not applicable; this was the assigned physical-retailer catalog source. No separate discovery was performed.

## 2. Highlight candidates

- [x] Currency metadata supports `CHF` for `CH`; the existing CH feed currency is `CHF`.
- [ ] No offer accepted. The one inspected product, Ancora Alaska Wildlachs (2 × 100 g), has an explicit same-item pair of CHF `9.00` normal and CHF `7.20` promo and an official page-linked product image. It is rejected as `SKIPPED_UNVERIFIED`: product-level nationwide applicability is not established, the offer's validity dates were not captured, and the image bytes were not downloaded/decoded. The CDN host `denner.imgix.net` is referenced by Denner's page but is not in the catalog host allowlist; no host-policy change was attempted.
- [ ] The other 32 linked offers were enumerated from the registered landing page but their detail pages were not opened; their prices, images, dates, and geographic applicability remain unchecked. Do not infer a full current-offer set from the 33 links alone.
- [x] Existing feed items were not revalidated or pruned. No expiry claim and no production feed/index/catalog change.

## 3. Catalog condition and close-out

- Catalog condition: `STALE_UNVERIFIED` for offer-level national scope and dates; the canonical official page itself was reachable.
- [x] Terminal checkpoint and receipt recorded for this work unit only.

## Compact handoff (≤400 words)

- Work unit `CH:denner-ch-country`, position 5/74; terminal receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; this is one isolated registered-catalog check.
- At `2026-11-23T04:18:38Z`, robots returned `200 text/plain`, no redirect, and allowed the catalog path. At `04:19:07Z`, the registered catalog URL returned `200 text/html`, no redirect, with matching canonical URL and 33 unique product-action links. At `04:19:57Z`, the linked AGB returned `200 text/html`; its text is scoped to the Denner Weinshop and contained no page-crawl rule. At `04:20:41Z`, one linked product detail returned `200 text/html` and showed Ancora Alaska Wildlachs 2 × 100 g, `7.20 statt 9.–` (CHF inferred from CH-local currency metadata and the official market context; the detail excerpt itself showed bare amounts), plus a Denner-page-referenced product image URL. Each request had a 30-second timeout; no retries or bypasses.
- Denner's registered record says `Switzerland (location-selected offers)`. Neither the checked product page nor the captured listing established countrywide participation or offer validity dates. The image bytes were not decoded. Ancora is rejected from acceptance for those missing gates; the other 32 offer links were not opened and remain unchecked. No offer is claimed absent or current.
- CHF is supported for CH. No production JSON or feed/index bytes changed. Source evidence: robots, catalog, AGB, and Ancora links recorded above.
- Next: coordinator selects the next manifest unit in a fresh isolated context.
