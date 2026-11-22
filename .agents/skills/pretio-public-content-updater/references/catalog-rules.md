# Catalog Promo rules — exact production format

**File:** `pretio/promos/catalog_app.json` ONLY, with top-level keys:
`allowed_hosts`, `location_contract`, `schema`, `items`, `catalog_revision`, `schema_version`. No extra keys.

**Locked format:** `schema = pretio.catalog_app.v2`, `schema_version = 2`. Preserve `location_contract` verbatim except in a separately reviewed schema migration. All entries must remain parseable by the live Android `PromoCatalogItem.fromJson`; `content_type = webview`, `coverage_type = national`, `status = active`, `source_type = official_retailer` or `official_digital_channel`. Unusable/expired entries are removed from active presentation through verified dates or controlled deletion, **not** by inventing new status values.

**Existing catalog-item field allowlist (no additional fields):**

- Required: `id`, `merchant`, `publisher`, `title`, `summary`, `coverage_type`, `coverage_label`, `content_type`, `url`, `source_type`, `status`, `sort_order`, `locations`.
- Existing optional: `valid_from`, `valid_until`, `last_verified_at`, `logo_url`, `image_url`, `logo_revision`, `image_revision`. Only populate optional keys when verifiable; don't generate made-up revisions.
- Only recognized location-rule keys: `type`, `country`, `country_code`, `province`, `province_code`, `city`, `city_code`, `location_key` (when current Android parser supports/needs them). Read actual location rules from immutable accepted directory; don't create ad hoc codes.

## Catalog source priority

1. **PREFERRED — evergreen official landing URL:** e.g. retailer's permanent `/angebote`, `/weekly-ad`, `/prospekt` directory. Its visible catalog changes regularly while the canonical URL stays stable. Recheck canonical target, status, redirects, selected market, coverage, and updated content, not just HTTP 200. No invented `valid_until`.
2. **PERIODIC LINK — official URL changes each promotion period:** allowable only when that exact catalog's **real, sourced** `valid_until` is included (and `valid_from` if known), plus evidence for replacement. Do not substitute an arbitrary next Monday or "7-day default". If missing expiry, don't register the rotating link; find the permanent landing URL, else report `BLOCKED_MISSING_EXPIRY`.
3. **Unstable, blocked or unlicensed URLs:** do not replace with aggregator, guessed redirect, social repost, or bypassed session URL. Preserve known-good canonical registration if still valid, flag for review.

## Every catalog check (not just products)

- Match `country_code` and explicit regional scope in the accepted location rules. National catalog landing pages can expose store-specific prices; a nationwide entry does **not** establish a national product discount.
- Verify original host and redirect target on HTTPS and against `allowed_hosts`; new host additions require owner review and proof it belongs to the retailer. Do not automatically allow wildcard domains.
- Retain stable `id` and `sort_order` across updates. Preserve app deep links/foreign keys used by Product Highlights.
- Update `last_verified_at` **only** after actual successful source verification; `NO_CHANGE` need not churn the JSON.
- A dead periodic catalog (after its sourced `valid_until`) must not be silently extended; expire/remove or replace after independent confirmation, preserving transactional consistency with highlights referencing it.
- No unrestricted wildcard host allowlist. Logo/image must be HTTPS and from approved sources and rights-compatible; decodable MIME/image when published.
- Catalog reader must still accept and display the resulting entries and country filters in `/pretio/catalog/`.

## Write boundary and review

Catalog jobs may change only `catalog_app.json` plus separate controlled tooling/reports; highlight jobs have a separate writer for `highlights/**`. If a catalog is removed/rekeyed, either migrate/revalidate existing highlight foreign keys against the same final snapshot or block publication. Separate PR review for new retailer and location coverage.

Check each catalog independently and report `LINK_STABLE`, `LINK_PERIODIC_WITH_EXPIRY`, `LINK_CHANGED`, `BLOCKED_MISSING_EXPIRY`, `FETCH_FAILED`, `SOURCE_BLOCKED`, `LOCATION_RESTRICTED`, or `NO_CHANGE`. These statuses belong in **audit/checkpoint only**, not in production catalog item fields.
