# Pretio — per-catalog source checkpoint

Run ID: `pretio-oneoff-global-20261123T040625Z`
Work unit: `ZA:foodloversmarket-za-specials` | manifest position: **73/74** | attempt: **1**
Country: **ZA / South Africa** | retailer: **Food Lover's Market** | mode: **AUDIT** | scope: **ONE_OFF_GLOBAL**
Checked UTC: **2026-11-23 10:56:34 UTC**
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog source

- [x] Loaded the frozen manifest and current active record: `foodloversmarket-za-specials`; URL <https://foodloversmarket.co.za/specials/>; `valid_until: null`; `coverage_type: national`; `coverage_label: South Africa (weekly specials)`; location `ZA`; last verified `2026-11-15T05:42:54.476Z`.
- [x] Checked <https://foodloversmarket.co.za/robots.txt> once using a standard HTTPS request: HTTP 200; `User-agent: *` has an empty `Disallow`, so the registered path is not disallowed by robots.txt.
- [x] Checked the official same-host <https://foodloversmarket.co.za/terms-and-conditions/> page: HTTP 200. It is an index of individual competition/promotion terms (including a November 6, 2026 entry); it did not establish general crawler permission or a commercial content/image reuse license. The specials page footer states `© 2026 Food Lovers Market` and `All Rights Reserved`. No explicit reuse permission was found; this is unverified, not evidence that reuse is prohibited.
- [x] Opened the exact registered specials URL via one standard HTTP request and one normal browser render: both showed HTTP 200, unchanged URL, and title `Food Lover's Market | Specials`. Both stopped at `Specials loading` with a newsletter prompt; neither showed rendered specials, active promotion dates, dates of validity, or participating locations. The page URL is fixed; in-place update behavior was not verified.
- [x] Existing catalog metadata says offers are weekly, most run Monday–Sunday, and may vary by region. This is not current source evidence. The source page did not identify participating South African regions/stores or confirm national applicability for any item.
- [x] `ZAR` is configured and `ZA.json` exists. It currently has 2 items, with 0 references to `foodloversmarket-za-specials`.

## 2. Product evidence and integrity

- No product/card was visible or examined. Accepted/rejected candidates: **0 / 0 inspected**. No prices, product images, offer dates, or item-level geography were retained. No image assets were fetched.
- Current offer validity and geography remain unverified. No positive expiry or source retirement evidence was found; do not infer expiry from `valid_until: null` or the older verification timestamp. Keep the catalog active and mark it `STALE_UNVERIFIED` in audit; do not change `last_verified_at`.
- No production catalog, highlight feed, or index data changed.

## 3. Decision

`SKIPPED_UNVERIFIED`: the official page is reachable and robots permits access, but both HTTP and browser rendering expose only a loading placeholder. The terms page provides no general content-reuse permission, so no products, prices, or images were inspected or retained. Current promotion dates and item-level geography could not be verified. Next manifest unit is `ZA:pnp-za-country` (74/74); it is outside this source task.
