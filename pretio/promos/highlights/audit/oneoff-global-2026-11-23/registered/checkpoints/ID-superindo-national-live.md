# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `ID:superindo-national-live` | manifest position: **34/74** | attempt: **1**  
Country: **ID** | retailer: **Super Indo** | mode: **AUDIT**  
Checked UTC: **2026-11-23T09:38:22Z**  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded the frozen manifest entry and current record: `superindo-national-live`, Super Indo, Indonesia, `official_retailer`, active, URL `https://www.superindo.co.id/promosi/katalog-super-hemat`, `valid_until: null`, existing `last_verified_at: 2026-08-22T01:00:00+08:00`.
- [x] The official homepage response identifies Super Indo (`meta author=Superindo`, canonical URL `https://www.superindo.co.id/`). The registered catalog URL itself was not opened.
- [x] Requested <https://www.superindo.co.id/robots.txt>. It returned HTTP 200 but the response body was HTML for the Super Indo homepage (including its homepage title/canonical), not a machine-readable robots file. No applicable robots rule could be established; this is not evidence that the catalog path is permitted.
- [x] Opened the official <https://www.superindo.co.id/terms-and-conditions> page. Its visible terms discuss website membership, email promotions/catalogues and third-party links; they do not state a permission or license for automated commercial copying/retention of catalog contents. The page shows a 2017 copyright. No explicit reuse authorization was found.
- [x] Since robots policy and commercial reuse permission remain unverified, stopped before opening the registered promotion page or retaining product/promo content. No access restriction was affirmatively identified; the reason is insufficient permission evidence.
- [ ] Current catalog content, canonical redirect, evergreen/rotating behavior, official parent navigation, freshness, promo periods, and current item prices were not verified. Do not infer expiry or obsolescence from the existing verification timestamp or this access check; classify `STALE_UNVERIFIED`.
- [x] The record is labeled national but its locations list contains eight provinces: South Sumatra, Lampung, Jakarta, West Java, Central Java, Yogyakarta, East Java, and Banten. The catalog record alone does not establish item-level national promo applicability.
- [x] No production catalog or highlight data, source verification timestamp, currency, or location registry was changed.

## 2. Product Highlights

- [x] IDR is supported; the existing `ID.json` feed has 4 active items and none references `superindo-national-live` (0 dependencies observed).
- [x] The promo page was not opened, so zero products were inspected and no candidate was accepted or rejected. No normal/promo pair, individual image, offer expiry, or item-level geography was verified.
- [x] No highlight was tied to this catalog or deleted. No catalog removal/migration was proposed; no orphan reference was created.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — the requested robots URL returned homepage HTML rather than usable rules, and the official terms page did not verify commercial reuse permission. Stopped before catalog content extraction.
- [x] Existing catalog remains unchanged; the evidence does not prove it expired or became obsolete.
- [x] No Product Highlight accepted; no expiry deletion; no production JSON changed.

## Compact handoff

Work unit `ID:superindo-national-live`, position 34/74; receipt `SKIPPED_UNVERIFIED`. The registered record points to `https://www.superindo.co.id/promosi/katalog-super-hemat`, active with no `valid_until`; existing `last_verified_at` is `2026-08-22T01:00:00+08:00`. Official homepage identity was confirmed, but the registered promo URL was not opened. The requested `robots.txt` returned HTTP 200 HTML for the homepage instead of rules. Official terms at `https://www.superindo.co.id/terms-and-conditions` discuss membership and promotional communications but provide no explicit commercial reuse/crawler permission. Permission remains unverified, so no offer content was retained. The record is labeled national but lists eight provinces; item geography is unverified. IDR is supported, the ID feed has 4 items, and none references this catalog. No product candidate or production change. Keep `STALE_UNVERIFIED`; do not infer expiry. Next source: `ID:tiptop-location-live` (35/74), in a fresh context.
