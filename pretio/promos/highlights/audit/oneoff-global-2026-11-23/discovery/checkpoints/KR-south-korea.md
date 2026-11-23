# One-off country discovery checkpoint — South Korea (KR)

- Run: `pretio-oneoff-global-20261123T040625Z`; market rank 33/174; no registered Catalog Promo sources.
- Search budget used: one Catalog Promo query (`South Korea official supermarket promotions sale leaflet mart deals`) and one online-shop query (`South Korea official online grocery supermarket store delivery shopping`). Exact search timestamps were not retained; checked 2026-11-23 UTC.
- Catalog lead: E-mart special flyer <https://emartapp.emart.com/leaflet/FlyerMainViewer.do?image_pop=true>. The lead's robots file returned HTTP 200 and `User-agent: *` disallows `/`; the flyer was not opened. Source note: `../leads/KR-emart-catalog.md`.
- The online query produced general consumer guidance and retailer video material, but no direct current online shop/storefront URL was opened. No URL was guessed from a video or search excerpt.
- No current offer, standard/discount pair, image, validity or nationwide eligibility was verified. No Product Highlight candidate accepted and no production data changed.
- Terminal bounded-market disposition: `SKIPPED_BLOCKED` because the chosen official flyer path is disallowed by robots. This does not establish that South Korea lacks promotions. Both query budgets are spent; no retry or bypass was made.
