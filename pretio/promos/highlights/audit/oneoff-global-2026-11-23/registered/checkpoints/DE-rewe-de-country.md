# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `DE:rewe-de-country` | Position: **21/74** | Attempt: **1**  
Country: **DE** | Retailer: **REWE** | Mode: **AUDIT**  
Checked UTC: **2026-11-23T05:02Z** (minute precision; individual request timestamps were not retained)  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: **SKIPPED_BLOCKED**

## 1. Catalog Promo source

- [x] Loaded frozen work unit `DE:rewe-de-country`, position 21/74, exact URL <https://www.rewe.de/angebote/nationale-angebote/>. Active catalog record is `rewe-de-country`, REWE / REWE, `official_retailer`, location Germany (`DE`), coverage label `Germany (location-selected offers)`, `valid_until: null`, existing `last_verified_at: 2026-09-22T00:00:00Z`.
- [x] Registered host `www.rewe.de` is already in `catalog_app.json.allowed_hosts`; no host or URL change was staged.
- [x] One public robots request to <https://www.rewe.de/robots.txt> returned HTTP `200`, `text/plain; charset=utf-8`, 2,029 UTF-8 bytes. `User-agent: *` does not disallow `/angebote/nationale-angebote/`; no query string was requested. The public content request used the exact frozen URL, 22-second timeout, maximum four redirects.
- [ ] The exact registered URL returned HTTP `403 Forbidden`. The response wrapper exposed no response body, headers/content type, final URL, redirect chain or response byte count. No offer page or terms link became available. Terms were not independently fetched.
- [x] One source-page GET after robots check; zero retries. No alternate URL/host, login, CAPTCHA, cookie, hidden endpoint, proxy or access-control bypass was attempted.
- [x] Source is **STALE_UNVERIFIED** for this run. A 403 does not prove the evergreen page was retired; the old `last_verified_at` and null expiry are not expiry evidence.

## 2. Product Highlights

- [x] DE highlight currency is configured as EUR. Scanned all country highlight JSON files: **0 items** reference `rewe-de-country`.
- [ ] No current offer content could be inspected. Accepted/rejected product candidates: **0/0 observed**; this does not mean REWE has no offers. No same-product normal/promo pair, product image, offer dates or item-level geographic scope were verifiable.
- [x] No published item expiry or catalog obsolescence was proven. No catalog, highlight, feed or index production JSON was changed; no item was added or removed.

## 3. Skip decision

- [x] **SKIPPED_BLOCKED** — the allowed public route returned HTTP 403 and no usable offer content. Preserve the existing catalog and any dependent data; suppress current-offer claims from this attempt.
- [x] Expired IDs deleted: **none**. No stale record was treated as expired or obsolete.

## Compact handoff (≤400 words)

- `DE:rewe-de-country`, position 21/74; terminal receipt `SKIPPED_BLOCKED`. Run `pretio-oneoff-global-20261123T040625Z`; baseline/skill `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Frozen URL: <https://www.rewe.de/angebote/nationale-angebote/>. Active entry `rewe-de-country` is REWE / REWE, national catalog but explicitly location-selected (`DE`), evergreen (`valid_until: null`); existing verification timestamp remains `2026-09-22T00:00:00Z`. Host is allowlisted.
- Robots returned `200 text/plain; charset=utf-8`, 2,029 bytes; wildcard rules do not disallow the frozen path. A single 22-second-bounded request to the exact URL returned `403 Forbidden`. The tool did not retain final URL, redirect chain, body, content type or bytes. No retry/bypass or alternate URL was used; terms were not checked because the page was blocked.
- EUR is supported, but no highlight in any country feed references this catalog. No products could be inspected. No expiry/obsolescence is proven and no production JSON changed.
- Next manifest input: `EC:supermaxi-ec-offers`; start in a fresh isolated context.
