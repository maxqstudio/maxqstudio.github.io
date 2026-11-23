# TIP TOP — source evidence (audit only)

Run: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `ID:tiptop-location-live`  
Checked UTC: `2026-11-23T09:40:47Z`  
Outcome: the official catalog landing page is live and has a dated November issue; the visible offers do not expose normal/reference prices, so there is no qualifying Product Highlight price pair.

## Source and access

- Registered official URL: <https://www.tiptop.co.id/promo-products/katalog>
- The official page returned HTTP 200 and presented the title “Promo Katalog” with the period **16–30 November 2026** and a “Download” link.
- The permanent-looking parent page links to the dated official PDF: <https://www.tiptop.co.id/files/uploads/promoperiod/attachment/2026/Nov/16/6afaa3654dae8/16-30-november-2026-promo-katalog.pdf> (29 pages, PDF). The PDF was not text-readable through the available browser reader; no contents were inferred from its appearance or URL.
- `https://www.tiptop.co.id/robots.txt` returned HTTP 200 with `User-agent: *` and an empty `Disallow:` rule. The path was therefore not disallowed.
- The official homepage links <https://www.tiptop.co.id/terms-conditions>. The checked terms page contains store/consumer rules; no web-crawling or commercial reuse prohibition was found in the visible text. This is an absence-of-found-restriction observation, not an explicit permission grant.
- The catalog page links individual product image URLs, but no product image was decoded/validated for this audit.

## Visible promotion observations (promo-only, not accepted)

The current official landing page lists these four cards. All are within the stated 16–30 Nov period, but it does not show normal/reference prices or item-level participating geography.

| Product text shown | Promo evidence | Why not eligible |
|---|---|---|
| Molto/Rinso/Wipol assorted professional cleaning products, selected variants | “Promo Diskon 15%” | No source-backed normal price or resulting promo price pair; variant specifics not captured. |
| Karaboga all-purpose wheat flour, 1 kg | Rp 9.475 per bag | Promo price only; normal price absent. |
| Greenfields Fresh Milk Low Fat, 950 ml | Rp 31.175 per carton | Promo price only; normal price absent. |
| Milkow Actigrow children’s milk 1+ honey, 900 g jar | Rp 63.975 per jar | Promo price only; normal price absent. |

No normal price was inferred from the percentage or promo-price-only cards. There are **0 accepted highlight candidates**.

## Geography and lifecycle

- The active production entry for `tiptop-location-live` lists Indonesian provinces with codes **31 (DKI Jakarta), 32 (Jawa Barat), and 36 (Banten)**, despite its legacy `coverage_type: national` / `coverage_label: Nasional` wording. This source record does not establish countrywide item eligibility; these observations are not suitable for the countrywide ID feed.
- The catalog page itself is an evergreen-looking parent URL. Its linked dated flyer is current as of 23 Nov and ends 30 Nov 2026. No obsolete-catalog conclusion or URL migration is justified.
- `pretio/promos/highlights/ID.json` has 4 items, with **0** items referencing `tiptop-location-live`; no dependent product or orphan reference action is needed.
- No production catalog/feed/index or source verification timestamp was changed.
