# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `ID:indomaret-national-live` | manifest position: **31/74** | attempt: **1**  
Country: **ID** | retailer: **Indomaret** | mode: **AUDIT**  
Checked UTC: **2026-11-23 (approximately 09:33–09:35 UTC; web tool did not expose exact request timestamps)**  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded exact frozen-manifest record and production entry: `indomaret-national-live`, merchant/publisher Indomaret, Indonesia (`ID`), `official_retailer`, active, national label, `valid_from: null`, `valid_until: null`, existing `last_verified_at: 2026-08-22T01:00:00+08:00`.
- [x] Registered URL <https://www.indomaret.co.id/promosi/> is HTTPS, on the already allowlisted host `www.indomaret.co.id`, and resolves to an official Indomaret-branded Promotions page. Footer identifies PT Indomarco Prismatama and a Jakarta head office. No redirect/final-response URI was exposed by the HTTP wrapper.
- [x] The canonical page was opened once on 2026-11-23. It is a permanent-looking `/promosi/` landing path and visibly contains current campaign periods: Super Hemat (12–25 Nov 2026), Paling Murah (19–25 Nov), Hemat Minggu Ini (19–25 Nov), Tebus Heboh (12–25 Nov), Promosi Berhadiah (12–25 Nov), Promo Susu & Perlengkapan Balita (12–25 Nov), Harga Khusus Member (19–25 Nov). This supports current campaign activity but does not prove historical in-place updating behavior.
- [x] The same page lists Promo 4 Hari (19–22 Nov 2026), which had ended by the market date 23 Nov. This is one expired campaign card inside an otherwise currently populated evergreen landing page; it does **not** prove the registered catalog URL itself is obsolete.
- [x] One request to <https://www.indomaret.co.id/robots.txt> returned HTTP 200, but no visible rule lines were returned by the PowerShell response and the web reader could not open the robots resource. Therefore no specific allow/disallow rule was verified.
- [ ] No generally applicable website use/crawling terms were found in the page's visible links or the bounded `site:indomaret.co.id` terms search. This is not proof that none exist; permission beyond the public page's accessibility remains **unverified**.
- [x] The page's “Katalog Promosi Indomaret” / campaign image link inspected for Paling Murah resolved to <https://www.indomaret.co.id/wp-content/uploads/2025/08/Thumbnail-Promosi-Website_PalingMurah-1.png>; visual content was a generic campaign logo, not a product/price flyer. No attempt was made to access private, authenticated, or hidden endpoints.
- [ ] No exact product prices, regular/promo price pairs, product-specific images, item validity conditions, or offer-level nationwide applicability were visible in retained page text or the inspected generic thumbnail. Other campaign artwork was not opened.
- [x] Catalog is not classified `VERIFIED_OBSOLETE`; no active-list removal or URL migration is proposed. The existing `last_verified_at` remains unchanged.
- [x] No production catalog, host allowlist, country feed, or index was changed.

## 2. Product Highlights

- [x] IDR is supported by existing currency metadata; current `pretio/promos/highlights/ID.json` contains **0** items referencing `indomaret-national-live`.
- [ ] Accepted candidates: **0**. No rejected product candidates were individually assessed; the page's campaign-level copy is not evidence of any item-specific normal/promo price pair or required product image.
- [ ] Physical-store nationwide item applicability and online fulfillment coverage were not verified at product level.
- [x] No expired highlight was linked to this catalog ID, no catalog removal is proposed, and no foreign-key migration is needed for this source check.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — the official evergreen-looking promotions landing page is accessible and displays live campaign date windows, but item-specific price pairs, image proof, geography, and reuse/access permission were not established. Do not report “no promo”; offer extraction was incomplete.
- [x] Campaign-level observation: Promo 4 Hari is dated 19–22 Nov 2026 and is ended as of 23 Nov. The page also contains multiple campaign windows ending 25 Nov. No campaign listing was removed from production because this is an audit finding and the catalog page itself remains active.
- [x] No accepted product IDs; no expired product IDs deleted; no catalog URL migration; no production JSON changes.

## Compact handoff (≤400 words)

- Work unit `ID:indomaret-national-live`, manifest position 31/74; receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Exact registered URL <https://www.indomaret.co.id/promosi/> is official, HTTPS, and already host-allowlisted. Its stable-looking landing path returned current campaign windows, including Paling Murah and Hemat Minggu Ini through 25 Nov 2026. One listed Promo 4 Hari window ended 22 Nov 2026; that card does not establish that the evergreen catalog page is obsolete. Update-in-place behavior was not established from a single observation.
- Robots returned HTTP 200 but no readable rule lines; the official site's general crawling/reuse terms were not located by bounded page-link inspection and site-scoped terms search. Permission therefore remains unverified. A linked Paling Murah image was a generic logo thumbnail, not a product flyer. The current page text contains no item-level normal/promo pairs; no price, product image, or national item eligibility was verified.
- IDR is supported and ID feed has zero references to this catalog. No product accepted, no product/catalog retired, and no production JSON changed. Next manifest work unit: `ID:lotte-grosir-location-live`.
