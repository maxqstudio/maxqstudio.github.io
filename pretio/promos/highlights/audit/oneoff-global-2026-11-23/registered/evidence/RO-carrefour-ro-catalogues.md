# Carrefour România source attempt evidence

- Run: `pretio-oneoff-global-20261123T040625Z`; scope: `ONE_OFF_GLOBAL`; baseline/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Frozen work unit: `RO:carrefour-ro-catalogues`, ordinal `59/74`, attempt `1`.
- Registered source: <https://carrefour.ro/corporate/cataloage/>. The active catalog record lists merchant `Carrefour`, publisher `Carrefour România`, country `RO`, national coverage label `Romania (store-selected offers)`, and `last_verified_at: 2026-11-15T05:42:54.476Z`. Its host `carrefour.ro` is in the local catalog allowlist. These are repository baseline facts, not current source verification.
- Requests were sequential, public HTTPS GETs with a 30-second client timeout, redirects disabled, and one request per exact URL. The self-identifying `PretioCatalogAudit/1.0 (+https://pretio.com/)` user agent was sent.

| Requested URL | Requested UTC | Completed UTC | Response | Redirect | Server Date |
| --- | --- | --- | --- | --- | --- |
| <https://carrefour.ro/robots.txt> | 2026-11-23T10:24:03.9191971Z | 2026-11-23T10:24:04.8498264Z | `403 Forbidden`, `text/html; charset=UTF-8`, 4,548 bytes | none | 2026-11-23T10:24:04Z |
| <https://carrefour.ro/corporate/cataloage/> | 2026-11-23T10:24:04.9529951Z | 2026-11-23T10:24:05.0904362Z | `403 Forbidden`, `text/html; charset=UTF-8`, 5,662 bytes | none | 2026-11-23T10:24:04Z |

Both bodies were Cloudflare `Attention Required!` interstitial HTML, not retailer content. No usable robots directives or catalog page were obtained. No retry, redirect follow, alternate URL/host, search, login, cookie, CAPTCHA attempt, hidden endpoint, proxy, or access-control bypass was used.

The blocked page exposed no terms link, so terms and any reuse permission were not verified. Current official ownership, canonical stability, campaign validity/freshness, selected-city behavior and item-level geography remain unverified. No retailer text, price, image, offer date, or catalog content was copied or used. No product page or image request was made after the catalog request was blocked.

Local compatibility check: Romania has no entry in `pretio/data/currency.json`, no `RO.json` highlight feed, and no `RO` entry in `pretio/promos/highlights/index.json`. A repository search found no current highlight JSON reference to `carrefour-ro-catalogues`. This only prevents current feed publication; it does not establish source expiry or obsolescence.
