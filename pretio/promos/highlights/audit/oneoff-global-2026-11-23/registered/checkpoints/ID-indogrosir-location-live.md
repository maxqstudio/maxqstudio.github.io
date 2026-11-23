# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `ID:indogrosir-location-live` | manifest position: **30/74** | attempt: **1**  
Country: **ID** | retailer: **Indogrosir** | mode: **AUDIT**  
Checked: **2026-11-23 UTC** (request-level timestamps not retained)  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded frozen manifest record `indogrosir-location-live`, ID, retailer, source URL, region list, active status, `valid_until: null`, existing `last_verified_at: 2026-08-22T01:00:00+08:00`.
- [x] Exact registered URL `https://indogrosir.co.id/promosi`; host is the already registered `indogrosir.co.id`. No URL or host change staged.
- [x] One robots check `https://indogrosir.co.id/robots.txt` returned HTTP 200, `text/plain`, 26 bytes; `User-agent: *` has an empty `Disallow:`.
- [x] Official homepage confirmed retailer identity (`PT. Inti Cakrawala Citra`) and linked `Syarat & Ketentuan`. Linked legal page returned 200, but rendered shared contact/privacy content and did not clearly grant or restrict automated access/reuse; Terms permission remains **unverified**.
- [x] One GET to exact registered Catalog Promo URL returned HTTP 200, `text/html; charset=UTF-8`, 37,480 bytes; title `Indogrosir`. No canonical meta value or redirect chain was captured. Page exposes a branch picker and an edition date range 16–30 November 2026.
- [x] The URL is a stable, undated branch-selectable landing page. Sixteen linked flyer JPEGs from `comprof-igr-prd.klikindogrosir.com` returned HTTP 200 `image/jpeg`; all 16 were visually reviewed. The linked host's robots response allows `/` and states `Content-Signal: search=yes,ai-train=no,use=reference`. No asset copies are retained in the repository.
- [x] Offer pages 3–14 explicitly say `Berlaku wilayah Ambon`; the flyer is regional. No national product-level applicability was inferred. Evidence and 22 exact price-pair observations are in `registered/evidence/ID-indogrosir-location-live.md`.
- [x] Landing page and edition are current as of 2026-11-23; selected flyer expires 2026-11-30. Do not mark the stable URL or the current edition stale/obsolete.
- [x] No catalog JSON, host allowlist, `last_verified_at`, highlight feed, or index was changed by this source worker.

## 2. Product Highlights

- [x] Currency `IDR` is configured and `pretio/promos/highlights/ID.json` exists with 4 entries; none references `indogrosir-location-live`.
- [x] Verified normal/promo price pairs exist in the official linked flyer and are recorded as audit-only facts.
- [ ] No product candidate is eligible for countrywide Product Highlights v1: the flyer says offers apply in Ambon, while this feed cannot represent region-only scope; Terms reuse permission also remains unclear.
- [x] No candidate added; no expired dependent offer or catalog reference exists, so no FK migration/deletion is required.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — current official Catalog Promo page and current regional flyer are accessible and contain verified price pairs, but region applicability cannot be represented in the countrywide highlight feed; Terms-based reuse permission is also unverified.
- [x] Catalog source remains as-is. Its stable page has no `valid_until`; the observed linked edition is current through 2026-11-30. No obsolescence or expiry is inferred.
- [x] No production JSON or schema changed.

## Compact handoff (≤400 words)

- `ID:indogrosir-location-live`, position 30/74; terminal receipt `SKIPPED_UNVERIFIED`; run `pretio-oneoff-global-20261123T040625Z`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Official source `https://indogrosir.co.id/promosi` returns 200 and displays a dated 16–30 Nov 2026 edition with branch selector. Landing URL is stable/permanent; current linked edition is not expired as of Nov 23. Main robots returns 200 with an empty `Disallow`.
- All 16 linked JPEGs were reviewed. Product flyer pages state `Berlaku wilayah Ambon`; 22 exact normal/promo pairs are documented in `registered/evidence/ID-indogrosir-location-live.md`. They remain audit-only because the existing ID feed cannot represent Ambon-only applicability. The active ID feed has four entries and zero references to this catalog.
- The linked Terms page rendered contact/privacy content but no clear automated-use grant/restriction. The linked image host allows reference use (`use=reference`) and prohibits model training; no asset copy is retained in repo. No production or schema change; no expired/obsolete record proven.
- Next manifest unit: `ID:indomaret-national-live`; continue in a fresh isolated context.
