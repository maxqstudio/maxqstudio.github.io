# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PF:carrefour-pf-catalogue` | manifest position: **49/74** | attempt: **1**  
Country: **PF** | retailer: **Carrefour Polynésie** | mode: **AUDIT**  
Checked: **2026-11-23**; documentation checkpoint written **2026-11-23T10:02:13Z** (the HTTP client did not expose an exact response timestamp).  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_BLOCKED**

## 1. Catalog Promo source

- [x] Loaded the frozen manifest and active catalog entry: `carrefour-pf-catalogue`, Carrefour, publisher Carrefour Polynésie, French Polynesia (`PF`), `official_retailer`, country location, national label with record coverage note “French Polynesia (store-selected offers),” `valid_until: null`, and existing `last_verified_at: 2026-11-15T05:42:54.476Z`.
- [x] Registered URL: <https://carrefour.pf/catalogue-en-ligne>; host `carrefour.pf` is already in the production catalog allowlist.
- [x] One public `robots.txt` request to <https://www.carrefour.pf/robots.txt> returned HTTP 200, `text/plain; charset=utf-8`, no redirect. The file states `User-agent: *`, `Content-Signal: search=yes,ai-train=no,use=reference`, and `Allow: /`; it also explicitly disallows both `GPTBot` and `ChatGPT-User` at `/`.
- [x] This run is performed by ChatGPT. The explicit `ChatGPT-User: Disallow: /` rule means the registered catalog path must not be opened from this agent context. I stopped before requesting the catalog, legal page, or any promotional/product content. No alternate user-agent, browser, proxy, cookie, or other access workaround was used.
- [x] Before the robots response was checked, one bounded public search query looked for Carrefour Polynesia terms. Search results exposed official privacy/legal links, but no legal page was opened and no promotional content was retained. The explicit robots restriction, not a search snippet, determines this terminal decision.
- [ ] Current content, redirect/canonical URL, evergreen-vs-periodic status, promo validity, location applicability, terms for commercial reuse, prices, and images remain unverified. Do not infer expiry or obsolescence from the old verification timestamp or the block.
- [x] No catalog fields, source verification timestamp, host allowlist, highlight feed, currency metadata, or production schema was changed.

## 2. Product Highlights

- [x] No PF highlights feed or currency mapping exists in the baseline, so Product Highlights publication is unsupported for this country in this run.
- [x] A read-only scan of all existing highlight feeds found zero references to `carrefour-pf-catalogue`; no dependent item exists to remove or migrate.
- [x] The catalog page was not opened, so zero products were inspected and no price pairs, product images, dates, or geographic claims were accepted or rejected.

## 3. Skip decision

- [x] **SKIPPED_BLOCKED** — robots explicitly disallows `ChatGPT-User` across the host. The registered catalog page was not opened.
- [x] Preserve the current catalog record as `STALE_UNVERIFIED`; this access restriction does not establish that the catalog is expired or obsolete.
- [x] No highlight deletion, catalog retirement, migration, or production JSON change.

## Compact handoff (≤400 words)

Work unit `PF:carrefour-pf-catalogue`, position 49/74; receipt `SKIPPED_BLOCKED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; baseline and skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`. Registered URL is `https://carrefour.pf/catalogue-en-ligne`; the existing catalog record is active, has no `valid_until`, was last verified 2026-11-15, and describes offers as store-selected despite a national location label. The official robots file returned HTTP 200 and explicitly disallows `ChatGPT-User` at `/` (also `GPTBot`). I stopped before opening the catalog, legal page, or promo content; no alternate user-agent or access workaround was used. No current offer, price, image, validity, or item geography was checked. PF has no highlight feed/currency mapping and no existing highlight references this catalog. Keep its current record unchanged and stale-unverified; do not infer expiry. No production data changed. Next manifest source: `PF:tahiti-pas-cher-pf-catalog` (50/74).
