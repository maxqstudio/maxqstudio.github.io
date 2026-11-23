# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `ES:aldi-es-weekly-offers` | manifest position: **26/74** | Attempt: **1**  
Country: **ES** | Retailer: **ALDI** | Mode: **AUDIT**  
Source checked: **2026-11-23 UTC**; exact robots-request time was not retained  
Catalog-page request: **2026-11-23T05:08:11.8787308Z–05:08:15.3667477Z**  
Legal-terms request: **2026-11-23T05:08:46.3690018Z–05:08:49.8718678Z**  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_BLOCKED**

## 1. Catalog Promo source

- [x] Loaded active catalog `aldi-es-weekly-offers`: publisher `ALDI España`; country `ES`; `coverage_type: national`; label `Spain (location-selected offers)`; URL `https://www.aldi.es/ofertas.html`; `valid_until` is null; `last_verified_at` remains `2026-11-15T05:42:54.476Z`.
- [x] Registered host `www.aldi.es` is in `catalog_app.json.allowed_hosts`.
- [x] Robots request `https://www.aldi.es/robots.txt` returned HTTP 200, `text/plain; charset=utf-8`, 332 bytes. Its rules disallow several region-specific paths, `/mds/`, `/*?*filters` and `/*?*jobId=`; the exact registered `/ofertas.html` path is not disallowed. Final URL was not exposed by the PowerShell wrapper.
- [x] One request to the exact registered Catalog Promo URL returned HTTP 200, `text/html; charset=utf-8`, 1,583,536 UTF-8 bytes. Response completed in 3.49 seconds; timeout was 20 seconds, maximum redirects 5. Wrapper did not expose `ResponseUri`, so final URL/redirect chain are unknown. The page's canonical metadata points to `https://www.aldi.es/ofertas.html` and declares locale `es_ES`.
- [x] The page linked its official “Condiciones de uso” at `https://www.aldi.es/nota-legal.html`. That page returned HTTP 200, `text/html; charset=utf-8`, 230,416 bytes, in 3.50 seconds (15-second timeout, maximum redirects 3). Its current terms restrict use to private purposes and prohibit commercial use/reproduction/exploitation of site content without prior written consent. No such consent is in this run. **No further offer extraction, image access, copying, or product reuse was performed after reading the restriction.**
- [ ] Although the URL is self-canonical and the response is current, update-in-place across offer cycles cannot be established under the terms restriction. Source remains `STALE_UNVERIFIED` for this attempt; this is not evidence of obsolescence.
- [x] No retry, login, CAPTCHA, hidden endpoint, proxy, alternate host, or access-control bypass. Exactly one robots request, one registered-page request and one directly linked legal-terms request.
- [x] No catalog field, host allowlist, `last_verified_at`, feed, or index was changed.

## Explicit scope / one-off validation

- [x] Run scope is the user-requested `ONE_OFF_GLOBAL` cycle. The frozen complete manifest has 74 work units; this checkpoint covers only `ES:aldi-es-weekly-offers`.
- [x] No schedule, cron, repeat cycle, or other retailer/catalog source was accessed in this isolated task. The overall one-off run remains in progress.

## 1B. Online-store / marketplace discovery alongside registered catalogs

- [x] Online-shop discovery is tracked separately under the run's global market-discovery stage. No marketplace/seller or other ALDI storefront was opened from this source context.
- [x] No unregistered seller or product offer was accepted or published.

## 2. Product Highlights — discounted items only

- [x] Spain is absent from the seven-country currency configuration; `ES.json` and an ES index entry do not exist. A Product Highlight cannot be published under the current contract.
- [ ] Product offers, regular/promo prices, images, validity dates and item-level store participation were not retained or verified for this audit because the linked terms restrict reuse without written consent. No candidate is accepted or individually assessed. No claim is made that ALDI Spain has no promotions.
- [x] The catalog's “location-selected offers” label does not prove item-level Spain-wide availability; no offer-level area was assessed.
- [x] No product expiry or catalog obsolescence was proven. No product/catalog deletions or production changes are justified.
- [x] No period-specific URL expiry was present in the active record (`valid_until: null`); missing expiry and a use restriction are not obsolescence evidence.

## 3. Skip decision

- [x] **SKIPPED_BLOCKED** — the official terms prohibit the requested public-data reuse absent prior written consent. Permission to publish product data/images is not established. The source remains active and unexpired in production; a terms restriction is not proof that its Catalog Promo is obsolete.
- [x] Accepted product IDs: none. Expired product IDs deleted: none. No production JSON changed.

## 5. Cycle completion gate

- [ ] Global registered manifest complete; 73 other units require their own terminal receipts.
- [ ] Global market-discovery stage complete; 174 selected-market checkpoints remain tracked separately.
- [x] This work unit is terminal; parent run remains **INCOMPLETE**.

## Compact handoff (≤400 words)

- Work unit `ES:aldi-es-weekly-offers`, position `26/74`; terminal receipt `SKIPPED_BLOCKED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- The registered URL `https://www.aldi.es/ofertas.html` is on the allowlist. Robots returned HTTP 200; the registered path is not disallowed. The page returned HTTP 200 with a self-canonical URL and Spanish locale. The PowerShell wrapper did not expose final URI/redirect chain.
- The retailer-linked legal page `https://www.aldi.es/nota-legal.html` returned HTTP 200 and states that site use is private and content cannot be commercially used/reproduced/exploited without prior written consent. No consent was provided. Stop further use of this source's catalog content, prices or images in this run.
- Spain has no Product Highlights currency/feed in the current schema. The active catalog has no `valid_until`; no expiry or obsolescence was proved. Preserve existing production data and `last_verified_at` unchanged. No product details or raw HTML are stored in this checkpoint.
- No retries or bypasses. Next input: `EG:carrefour-egypt-offers`; process in a fresh isolated context. The global run remains incomplete until all 74 source receipts and market-discovery checkpoints are terminal.
