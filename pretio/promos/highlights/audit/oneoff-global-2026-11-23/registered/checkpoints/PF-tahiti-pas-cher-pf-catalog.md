# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PF:tahiti-pas-cher-pf-catalog` | manifest position: **50/74** | attempt: **1**  
Country: **PF** | retailer: **Tahiti Pas Cher** | mode: **AUDIT**  
Official URL: <https://www.tahitipascher.pf/catalogue-du-moment/>  
Checked date: **2026-11-23**; request-level UTC timestamps were not exposed by the HTTP/browser clients. This checkpoint was recorded at **2026-11-23T10:07:34Z**.  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded the frozen manifest and production record: `tahiti-pas-cher-pf-catalog`, active, `official_retailer`, country-level PF, `valid_from: null`, `valid_until: null`, existing `last_verified_at: 2026-11-12T09:33:19+08:00`.
- [x] The URL host `www.tahitipascher.pf` is already in `catalog_app.json.allowed_hosts`; the registered URL returned HTTP 200 at the same final URL, `text/html; charset=UTF-8`. The page title is “DÉCOUVREZ LE NOUVEAU CATALOGUE DU MOMENT | TAHITI PAS CHER.”
- [x] A self-identified public request to <https://www.tahitipascher.pf/robots.txt> returned HTTP 200 `text/plain`. The wildcard rules disallow logs, temporary WooCommerce paths, add-to-cart queries and `/wp-admin/`; they do not disallow `/catalogue-du-moment/` or the public sitemap.
- [x] Official legal page <https://www.tahitipascher.pf/mentions-legales/> names SARL SDE / Tahiti Pas Cher as owner and says the site is updated regularly. It describes selected products in the retailer's stores and says site information is indicative and may change. Official CGV <https://www.tahitipascher.pf/CGV/> says the website does not complete sales; customers request a quote and receive final availability/pricing through the sales team.
- [x] The registered page itself says its catalog is regularly updated and advertises products available in five Tahiti stores, with shipping to the islands of French Polynesia. It is an evergreen catalog landing page; no dated issue or source-backed `valid_until` is shown. The source page is not retired or marked obsolete.
- [x] The page exposes two generic newsletter graphics, not individual product images or a dated flyer. The images are not product/price evidence. No valid period or exact discounted item was found in the visible page text.
- [x] Robots permits this exact public page, and no explicit crawler or commercial-reuse prohibition was found in the checked legal/CGV pages. However, no explicit content-reuse authorization was found; no product price or promotional content was retained. A bounded official-site search used only to locate the legal page: `site:tahitipascher.pf ("conditions générales" OR "mentions légales" OR "politique de confidentialité")`.
- [x] The page's five-store/Tahiti availability and island shipping statements do not prove the same item-level promotion or price at every location. The CGV describes quote-based island delivery with freight paid by the customer; no item-level geographic offer was verified.
- [x] No production catalog fields, source-verification timestamp, location data, feeds or indexes were changed.

## 2. Product Highlights candidates

- [x] PF is absent from `pretio/data/currency.json`, has no PF highlight feed/index entry, and none of the existing feeds references `tahiti-pas-cher-pf-catalog`.
- [x] No exact product/variant with both a normal and lower public promo price, valid individual product image, and source-backed offer period was verified. Accepted/rejected item candidates: **0/0 inspected**.
- [x] No Product Highlight was created or deleted. No expired offer or dependent reference was found.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — the official permanent page is live and states it is regularly updated, but its visible current content does not provide verifiable item-level price pairs, individual product images, or offer validity. Final pricing is quote-based, and explicit commercial content-reuse permission was not found. PF also lacks Product Highlights currency support.
- [x] Keep the current catalog entry unchanged. Its evergreen landing page is not proven obsolete or expired. No URL migration or deletion is proposed.

## Compact handoff (≤400 words)

Work unit `PF:tahiti-pas-cher-pf-catalog`, position 50/74; terminal receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`; base and skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`. The registered official page <https://www.tahitipascher.pf/catalogue-du-moment/> and `robots.txt` returned 200; the exact path is not disallowed. Official legal disclosures identify SARL SDE / Tahiti Pas Cher, say the site is regularly updated, and describe products available in five Tahiti stores with shipping to French Polynesian islands. The page is an evergreen “catalogue du moment” landing page; no issue dates or expiry were shown. Its visible page has generic newsletter graphics, no exact item/price pair, no product photo evidence, and no validity dates. The legal notice says web information is indicative; the CGV says final pricing and availability are returned through a quote. No explicit crawler/content-reuse permission was found, so no price content was retained. PF has no highlight currency/feed and no existing highlight references this catalog. No production change or obsolescence claim. Next frozen manifest source is `PL:biedronka-pl-gazetki` (51/74).
