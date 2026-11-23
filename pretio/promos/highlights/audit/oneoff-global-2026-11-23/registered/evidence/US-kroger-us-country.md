# Source evidence — US:kroger-us-country

Run: `pretio-oneoff-global-20261123T040625Z` | Checked UTC: `2026-11-23T10:45:28Z` | Attempt: `1`
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`

Frozen manifest unit: `US:kroger-us-country`, ordinal `70/74`. Registered HTTPS URL: https://www.kroger.com/weeklyad. Baseline catalog item identifies Kroger / Kroger, `official_retailer`, country `US`, national label “United States (store-selected offers),” and says users browse the weekly ad after selecting a store. The URL host `www.kroger.com` is already in the catalog `allowed_hosts`. The separate weekly-ad page was **not requested**: the official terms prohibit automated access/collection/extraction/monitoring, so current page content, redirects and exact route ownership were not freshly checked.

## Robots policy

Public robots file: https://www.kroger.com/robots.txt (retrieved through the public web retrieval tool; text/plain, 92 lines; tool reports crawled today). Its opening comment names “The Kroger Co. Family of Stores” and says retrieval agents are welcome while training-only crawlers are blocked. In the `User-agent: *` group, listed path restrictions do not include `/weeklyad`; the file includes a separate set of user-agent-specific groups with `Disallow: /`. The retrieval tool did not expose its request user-agent. Robots text was read for the requested policy check; it does not override the following site terms.

## Terms and content reuse

Official terms URL: https://www.kroger.com/i/terms/website-and-app. The official site-scoped search result showed “Website & App Terms & Conditions of Use,” last updated September 9, 2026. It defines Kroger Sites as websites/apps of The Kroger Co. and its affiliates; says site content is owned by Kroger or licensors; limits its license to personal, non-commercial use; and §5.3 prohibits automated means (including bots, crawlers, scrapers and data-mining tools) used to access, collect, extract or monitor site information. Copying, distributing or otherwise exploiting content requires prior written consent unless an express exception applies. No written commercial reuse or product-image permission was located. Accordingly, the canonical weekly-ad page, its linked products, prices and images were not opened or copied. The official terms plus the already accepted catalog record support the registered Kroger domain/merchant identity, but do not independently verify the unrequested weekly-ad route.

## Offer, date and geography result

No current weekly-ad date range, participating stores, item-level US eligibility, public price pair, product image or current offer was inspected. This is a legal/access-based block, not evidence of no promotions or an expired catalog. No search-engine price snippet, third-party flyer, product page, image URL or alternate endpoint was used. Existing `pretio/promos/highlights/US.json` is configured for USD and has 12 items, zero referencing `kroger-us-country`; no Kroger product expiry/deletion was identified. No production or shared progress artifact was changed.

Disposition: `SKIPPED_BLOCKED`; catalog freshness and offer state remain `STALE_UNVERIFIED`.