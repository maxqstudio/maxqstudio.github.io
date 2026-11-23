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

## Online shops and marketplace catalog registration

- **Existing official online merchants are eligible Catalog Promo sources.** A direct-to-consumer shop or permitted marketplace official-store storefront is not excluded for lacking a physical shop or downloadable flyer. Check its offers on publicly accessible store pages and stable product/catalog links.
- A marketplace platform (e.g. Shopee, Tokopedia, Lazada, Amazon or a country-specific platform) is NOT automatically the seller of a third-party listing. A newly proposed catalog entry must document the verifiable **actual merchant/store** as `merchant` and the platform as `publisher` if appropriate, without adding `platform_id`, `seller_id`, `channel` or other new production keys. If the platform itself sells inventory directly, that is a distinct first-party merchant.
- Existing `source_type = official_digital_channel` may be used ONLY when it truthfully describes the approved store/channel. Keep `content_type = webview`, `coverage_type = national`, allowed country `locations`, HTTPS `url`, and only existing allowlisted keys. The canonical store/catalog URL should be a stable, public link; a seller-specific storefront is preferred over a generic marketplace homepage that does not identify a seller. Periodic URLs need source-backed `valid_until`.
- **New seller/store registration requires Owner review before any production edit**, including `id`, verified `merchant` identity, `publisher`, seller URL, country-wide coverage, selected market/currency compatibility, matching source host, and exact `allowed_hosts` addition. Do not add broad wildcard hosts or unrelated aggregators. Maintain stable IDs and foreign keys once approved.
- A merchant found through Google Shopping is **discovery only**; Google Shopping Search results and price cards are not official Catalog Promo entries or Product Highlights `source_url`. Confirm on the actual seller's official website or permitted marketplace listing.
- A marketplace product page may be the official evidence URL **only when** the page identifies the same registered seller/store, item variant, public price pair and supported country. If store identity or permissions cannot be verified, store the candidate in audit under `NEEDS_CATALOG_APPROVAL` or `SKIPPED_UNVERIFIED`, not the public directory.
- Deduplicate seller/store registrations: one merchant/store identity, stable URL, no duplicate `catalog_id` just because the merchant was seen in multiple search channels. Regional-only seller pricing cannot be represented as national price guarantees.

See `online-shop-marketplace-rules.md` for detailed research and evidence rules. Discovery-register fields live ONLY in run audit artifacts, never in this production schema.

## Write boundary and review

Catalog jobs may change only `catalog_app.json` plus separate controlled tooling/reports; highlight jobs have a separate writer for `highlights/**`. If a catalog is removed/rekeyed, either migrate/revalidate existing highlight foreign keys against the same final snapshot or block publication. Separate PR review for new retailer and location coverage.

Check each catalog independently and report `LINK_STABLE`, `LINK_PERIODIC_WITH_EXPIRY`, `LINK_CHANGED`, `BLOCKED_MISSING_EXPIRY`, `FETCH_FAILED`, `SOURCE_BLOCKED`, `LOCATION_RESTRICTED`, or `NO_CHANGE`. These statuses belong in **audit/checkpoint only**, not in production catalog item fields.
