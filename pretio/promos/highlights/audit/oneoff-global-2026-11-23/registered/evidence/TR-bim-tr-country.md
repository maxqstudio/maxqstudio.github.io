# BİM registered source evidence

- Run: `pretio-oneoff-global-20261123T040625Z` (`ONE_OFF_GLOBAL`), unit `TR:bim-tr-country` (66/74), attempt 1; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Source from frozen manifest and active catalog: <https://www.bim.com.tr/Categories/254/aktuel-urunler.aspx>. Catalog ID `bim-tr-country`; allowed host `www.bim.com.tr`.

## Bounded requests

1. `2026-11-23T10:38:29Z` — one GET to <https://www.bim.com.tr/robots.txt>. HTTP 200, `text/plain`, 2,676 bytes. The response states `User-agent: *`, `Content-Signal: search=yes,ai-train=no,use=reference`, and `Allow: /`. It also has named training-crawler groups with `Disallow: /`; these do not change the general `User-agent: *` allowance for the registered path. The `use=reference` signal was not treated as commercial republication consent or an image license.
2. `2026-11-23T10:39:18Z` — one GET to the exact registered URL. HTTP 400 Bad Request; `Content-Type: text/html`; Cloudflare response; no redirect (`AllowAutoRedirect=false`, final request URI unchanged). The response headers gave a body length of 2,950 bytes. The page body was not inspected or retried.

No other BİM URL or host was requested. The 400 prevented inspection of the catalog page, current offers, its official footer/legal links, and any separate terms/reuse policy. The frozen catalog record identifies BİM as merchant/publisher, but this attempt did not independently verify current operator ownership. No current campaign period or exact validity date was observed. The record's `valid_until: null` and `last_verified_at: 2026-09-28T00:00:00Z` are baseline values, not currentness or expiry evidence.

## Product, date, and geography result

No product or leaflet page was opened; no prices, variants, photos, product availability, or item-level Turkish geography were inspected. Zero items were accepted or rejected. This is not evidence that BİM has no promotions. The record's national label cannot establish nationwide eligibility for individual offers. No offer expiry, catalog obsolescence, or currentness is asserted.

`TR` is absent from `pretio/data/currency.json`, and `pretio/promos/highlights/TR.json` is absent, so highlights could not be published for TR even if offers were verified. No production or shared progress file was modified.
