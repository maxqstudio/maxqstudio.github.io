# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `IT:conad-it-volantini` | manifest position: **38/74** | attempt: **1**  
Country: **IT** | retailer: **Conad** | mode: **AUDIT**  
Checked UTC: **2026-11-23T09:42Z**  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## Catalog source and permission

- [x] Loaded the frozen manifest and current catalog record: `conad-it-volantini`, Conad, Italy, `official_retailer`, active, national label “Italy (store-selected offers)”, `valid_until: null`, existing `last_verified_at: 2026-11-15T05:42:54.476Z`.
- [x] Official identity: `https://www.conad.it/` identifies Conad Società Cooperativa. The official homepage links to “Negozi e volantini”.
- [x] Robots: `https://www.conad.it/robots.txt` returned public rules (`User-agent: *`, `Allow: /`, except `/excel-volantini.xlsx`). The registered path is not disallowed.
- [x] Opened the exact registered page `https://www.conad.it/app-internal/home_leaflets`; it returned the official Conad page shell with a “select a store” control and no current leaflet/product offer content.
- [x] Followed the official “Negozi e volantini” link to `https://www.conad.it/ricerca-negozi`. The page says shoppers search/select a store to see that store’s flyers and active offers. No specific location was selected, so no local leaflet was inspected.
- [x] Official privacy and cookie policies are linked from the site. No crawler/reuse terms page or explicit commercial reuse authorization was found in the accessible navigation; no explicit prohibition was found either. Treat data-retention permission as unverified, not as an affirmative block.
- [ ] The registered URL is a permanent route, but current in-place catalog freshness, rotating flyer dates and a current flyer parent link were not verified. Classify content as `STALE_UNVERIFIED`; do not infer expiry from `last_verified_at` or the absent `valid_until`.

## Product, location, and lifecycle

- [x] The official flyer directory is store-selected. No item-level nationwide price applicability was proven; regional/local flyers cannot be represented as national highlights.
- [x] The page exposed no product offers or price pairs. Accepted/rejected product candidates: **0/0 inspected**. No image or validity interval was assessed; no Product Highlight is eligible.
- [x] Italy has no entry in the current Product Highlights currency map or index, so this run cannot publish an IT feed without a separately approved compatibility change.
- [x] No production highlight references `conad-it-volantini` (checked all country feeds); no dependency or expiry deletion is needed.
- [x] No evidence proves the catalog obsolete or expired. No production catalog/feed/index/location/currency data was changed; `last_verified_at` remains untouched.

## Decision and compact handoff

`SKIPPED_UNVERIFIED` — the official permanent route is reachable and robots permits it, but the current leaflet requires store selection and the page did not expose a current catalog without a location. Store-level geography and offer evidence remain unavailable in this bounded attempt; reuse permission was not explicitly established. Keep the existing catalog entry unchanged and do not claim current offers or obsolescence. No product candidates, deletions, or production changes. Next work unit: `IT:lidl-it-country` in a fresh source context.

Source references: <https://www.conad.it/robots.txt>; <https://www.conad.it/>; <https://www.conad.it/app-internal/home_leaflets>; <https://www.conad.it/ricerca-negozi>; <https://www.conad.it/informativa-privacy>; <https://www.conad.it/cookie-policy>.
