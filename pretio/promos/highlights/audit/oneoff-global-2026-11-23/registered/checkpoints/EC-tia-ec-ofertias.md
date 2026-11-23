# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `EC:tia-ec-ofertias` | manifest ordinal: **23/74** | catalog array position: **53/74** | Attempt: **1**  
Country: **EC** | Retailer: **Tía** | Mode: **AUDIT**  
Source request window: **2026-11-23T05:02:05.0942218Z–05:02:24.9099120Z**  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded active catalog `tia-ec-ofertias`: Tía / Tiendas Industriales Asociadas Tía, `official_digital_channel`, country EC / Ecuador, `coverage_type: national`, `valid_until: null`, `last_verified_at: 2026-10-21T10:21:02+08:00`. It is array position 53/74 in `catalog_app.json` and manifest unit 23/74.
- [x] Used only the frozen registered URL: <https://www.tia.com.ec/campa-as-marketing/ofertias>. Its HTTPS host `www.tia.com.ec` is present in `catalog_app.json.allowed_hosts`.
- [x] Robots request: <https://www.tia.com.ec/robots.txt> returned HTTP **200**, `text/plain; charset=UTF-8`, **541 bytes**, request `2026-11-23T05:02:05.0942218Z`, completed `05:02:05.5874507Z`. `User-agent: *` disallows `/catalog/`, checkout/customer/search and other paths; `/campa-as-marketing/ofertias` does not match a disallow rule. The final URI was not exposed by PowerShell, so redirect metadata is unknown.
- [x] One direct GET to the registered Catalog Promo URL returned HTTP **200**, `text/html; charset=UTF-8`, **351,463 UTF-8 bytes**, request `2026-11-23T05:02:23.9844803Z`, completed `05:02:24.9099120Z`. The response title was `Ofertías` and the HTML locale was `es`. Final URI/redirect metadata was not exposed.
- [ ] Terms of service were not verified. The retained response excerpt did not include a terms link, and no terms URL was guessed or fetched. This remains a source-qualification limitation.
- [ ] The landing path appears intended as a stable offers category, but this attempt did not compare historical cycles or establish that it updates in-place. No `valid_until` exists in the record; no periodic date was inferred.
- [x] Exactly one robots request and one catalog-page request were made; zero retries. No login, cookie session, CAPTCHA, hidden API, proxy, alternate host or access-control bypass was used. The full 351,463-byte HTML body was not saved as a run artifact; the tool output retained response metadata and its first 3,000 HTML characters, while this checkpoint preserves the metadata only.
- [x] No production catalog field or `last_verified_at` was changed.

## 2. Product Highlights

- [x] Ecuador is not supported in `pretio/data/currency.json`; USD is configured for US only. There is no EC highlights feed and no EC entry in `pretio/promos/highlights/index.json`.
- [ ] The retained page capture did not expose an inspectable product offer. No product candidate was accepted or rejected. No exact same-item normal/promo price pair, verified product image, validity, or country-wide delivery/price evidence was captured. The existing catalog summary says delivery, price and availability depend on coverage and address; the national catalog label alone cannot prove national item eligibility.
- [x] Repository-wide reference search found no Product Highlight `catalog_id` references to `tia-ec-ofertias` in active country feeds. There is no EC item to expire or remove in this run.
- [x] No product expiry or catalog obsolescence was proven. No feed, index or catalog production JSON was changed.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — the evergreen-looking page was reachable and permitted by the observed robots rules, but the retained capture lacks current offer evidence and official terms remain unchecked. The market-wide currency/feed compatibility gate also blocks EC Product Highlights. No claim is made that Tía has no current offers.
- [x] No accepted candidate IDs; no expired items deleted; no production JSON changes.

## Compact handoff (≤400 words)

- Work unit `EC:tia-ec-ofertias`, catalog array position 53/74 and frozen manifest ordinal 23/74; terminal receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- The exact frozen registered URL `https://www.tia.com.ec/campa-as-marketing/ofertias` returned HTTP 200, `text/html; charset=UTF-8`, 351,463 UTF-8 bytes, with title `Ofertías`. Request window: `2026-11-23T05:02:23.9844803Z–05:02:24.9099120Z`. The final URI/redirect chain was not captured. The full HTML was not saved, so offers cannot be reconstructed from this audit artifact.
- Robots returned HTTP 200, `text/plain; charset=UTF-8`, 541 bytes at `2026-11-23T05:02:05.0942218Z–05:02:05.5874507Z`; the frozen path is not disallowed by the published `User-agent: *` rules. Terms were not verified. No retry or bypass occurred.
- EC has no configured highlight currency/feed/index entry; the existing Tía catalog summary says delivery, prices and availability depend on address/coverage. No product price pair, image, validity or nationwide online fulfillment evidence was retained. No EC references or expired items were found; no production JSON changed.
- Next manifest unit: `EG:carrefour-egypt-offers`. Continue in a fresh isolated context.
