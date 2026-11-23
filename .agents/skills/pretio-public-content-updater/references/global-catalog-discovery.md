# Global Catalog Promo discovery — evergreen first, rotating second

**Mission:** Find and maintain official Catalog Promo directory entries worldwide, not only the existing 24 catalog countries. The Owner targets **approximately 174 commercially relevant countries** for discovery. This is a **research target**, NOT an assertion that 174 countries already have official catalogs or that the existing Android/browser data schemas support publication for all of them.

**Authoritative candidate-country universe:** `pretio/location/v2/index.json` currently contains **249** country/territory codes. `pretio/promos/catalog_app.json` currently has **74** registered catalogs covering **24** countries. Build the discovery country registry from location v2, not a hardcoded 174-country list and not the current 24-country feed. Each country/territory gets its own audit eligibility disposition. Do NOT silently pick the first 174 alphabetically or invent sources for the quota.

## Selection and measurement

- Attempt research in all **Owner-scoped** countries. For a global 174-market expansion, traverse the V2 candidate universe with documented market filters and country checkpoints; prioritize markets with registered sources, established online commerce, and verified official retail presence. Territories, tiny markets, disputed areas and locations without accessible commercial retail may be `SKIPPED_NO_VERIFIABLE_SOURCES` with proof; do not make unsupported blanket exclusions.
- Maintain separate counters `candidate_country_count`, `countries_researched`, `countries_with_verified_official_catalogs`, `countries_with_approved_active_catalogs`, `countries_no_source`, `countries_blocked`, and `country_target=174`. A country is "covered" **only after at least one source is actually opened and verified for official ownership, permitted access, geographical applicability and updated promotional content**. Mere HTTP 200 or search results are not catalog coverage.
- Reaching 174 does NOT authorize skipping requested manifest entries. If fewer than 174 qualify, report `TARGET_MISSED`; do not fabricate entries. A complete audit can still finish if every scoped country has a terminal disposition, including `SKIPPED_NO_VERIFIABLE_SOURCES`.
- Each country has a separate **discovery checkpoint** and handoff. The known 74-source manifest still has a separate immutable receipt count. Do not count "country discovery considered" as a retailer source successfully crawled.

## Catalog discovery order — mandatory

### Tier 1: evergreen canonical link (FIRST PRIORITY)

Search official retailer websites for permanent links where promotions change while the address stays stable, such as `/promotions`, `/offers`, `/weekly-ad`, `/catalogs`, `/prospekt`, `/flyers`, `/deals`, `/sale`, and localized equivalents. No URL-path shape alone proves validity.

- Verify merchant ownership, HTTPS host, stable canonical URL across historical/current cycles if evidence permits, actual current promo content/updates, correct country/site locale and geographical coverage.
- Prefer a **stable public storefront/category landing page** over a short-lived PDF/leaflet, even if the latter is easier to extract.
- An evergreen landing page **does not require an invented `valid_until`**. Individual item promos from that page still need evidence, and known product expiry dates must be preserved.
- Resolve redirects only to official merchant-controlled domains; any host change/allowlist addition needs Owner review. Keep existing catalog `id` when the merchant/source identity is unchanged.
- If this link works, it is the *preferred production Catalog Promo URL*. The most recent rotating PDF can be kept as **audit evidence**, not necessarily the production catalog URL.

### Tier 2: rotating period-specific link (SECOND PRIORITY)

If no stable official URL exposes the promotional content, locate retailer-published periodic PDF, flyer, image series, dated microsite or campaign URL.

- Capture the actual `valid_from` and **evidence-backed `valid_until`** for that exact catalog before publishing a rotating production URL. No assumed 7-day, Monday/Sunday, campaign-week or end-of-month dates.
- At each later run, follow its **official permanent parent landing page**, official catalog index, retailer-provided JSON feed or permitted page navigation to locate the next cycle's link; never guess file names, numeric IDs, hidden API endpoints or dates.
- While current period remains valid, do not rotate the URL unnecessarily. On known expiry, search the next published period, validate source and geography, then stage **one atomic replacement preserving catalog ID** and validating all highlights that reference it.
- If no next official URL is available, mark `SKIPPED_NO_NEW_CATALOG` or `BLOCKED_MISSING_EXPIRY`; retain the source as audit history but do not claim the expired flyer is current or extend dates.
- Changing from an expired rotating URL to a **verified evergreen URL** is a distinct reviewed migration; the current `validate_catalog_link_changes` baseline comparison requires `valid_until` for ANY changed URL, so it must **not** be bypassed. Stage `NEEDS_VALIDATOR_MIGRATION_REVIEW` and use a separate reviewed code/test change to support permanent migrations without fictional expiry.

### Tier 3: shop-only evergreen promotion page

For an online-only shop with no printed flyer, its official promotions/deals page is a legitimate Catalog Promo candidate **if it contains actual public offers** and publisher/store ownership, HTTPS, countrywide applicability and permitted access are verified. An arbitrary marketplace homepage, seller search result or generic shop home with no offers is not a promo catalog.

### Tier 4: no qualified source

If neither tier has a permitted official, current, geographically appropriate catalog, record `SKIPPED_NO_VERIFIABLE_SOURCES` in audit, do not create fake catalog entries. Recheck only upon a new Owner-instructed run or separately approved schedule (not automatically enabled).

## Verification and publication gates

1. Preserve **existing Catalog Promo v2 keys**; `content_type=webview`, `coverage_type=national`, only approved `source_type` values, valid location rules, official HTTPS `allowed_hosts`. Never invent extra fields for catalog type, platform, confidence, crawl date or discovery status.
2. **Brand-new country/retailer/catalog entries require review**, country compatibility and host allowlist verification before production. The location v2 registry makes a country discoverable, not necessarily supported by the old catalog or country highlights feed. `pretio/data/currency.json` currently supports seven highlight feed countries; missing currency does not block catalog research but blocks Product Highlights publication.
3. Prefer catalog source freshness evidence beyond HTTP 200: recently updated flyer/date range, visible current promo, stable redirect and market selection. For source failures, bounded retry, checkpoint reason and move on.
4. Record source proofs: ownership URL, requested/final URL, redirect chain, content type, stable/rotating evidence, official index/parent URL, market scope, last verified timestamp, dated flyer proof, exact changed fields, source access limits and permission state.
5. **One-off always stops** after the scoped registered-source manifest and the bounded global country discovery stage. This document does **not** install a crawler, GitHub Action schedule or automatic publication.

## Audit-only country discovery status

`REGISTERED_VERIFIED` | `NEW_EVERGREEN_CANDIDATE` | `NEW_ROTATING_CANDIDATE` | `NEEDS_CATALOG_APPROVAL` | `NEEDS_VALIDATOR_MIGRATION_REVIEW` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `SKIPPED_BLOCKED` | `SKIPPED_UNAVAILABLE` | `BLOCKED_COUNTRY_COMPATIBILITY`.

These statuses are NOT permitted production JSON fields.
