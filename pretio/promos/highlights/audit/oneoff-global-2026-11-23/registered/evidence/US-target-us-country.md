# Target weekly ad — source evidence

- Run: `pretio-oneoff-global-20261123T040625Z`
- Base/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`
- Work unit: `US:target-us-country` (71/74)
- Observed UTC: `2026-11-23T10:48:42Z`
- Retrieval: one bounded inspection of official public URLs in a browser; no product-level paths, searches, APIs, listings, or images opened.

## Official ownership

- Catalog page: <https://www.target.com/weekly-ad>
- The page identifies itself as “Weekly Ad”, links “Terms”, and displays a `TM & © 2026 Target Brands, Inc.` footer.
- Linked official Terms: <https://www.target.com/c/terms-conditions/-/N-4sr7l> (last updated September 10, 2026). They apply to `www.target.com` and define “Target” as Target Corporation and its subsidiaries/affiliates. The page was opened through the Terms link on the official weekly-ad page.

## Robots, terms and reuse permission

- Official robots file: <https://www.target.com/robots.txt>. The inspected rules contain no disallow rule matching `/weekly-ad`.
- Terms state that website content, including data, text and images, is owned or licensed by Target or suppliers/licensors and that Target reserves its intellectual-property rights. The granted access/copy license is for personal, noncommercial purposes only.
- The prohibited-use section expressly bars commercial use of product listings, descriptions, prices or images and bars data extraction/collection or systematically storing site content, except within the limited license. Therefore no commercial permission applicable to Pretio research or downstream reuse was located. No prices or images were inspected or copied.

## Current period and geography

- The public page view returned the heading “Weekly Ad” and a search field, but no current products, price pairs, date range or cycle period.
- Its footer states that pricing, promotions and availability may vary by location and at Target.com. This confirms location variation, not national eligibility for an individual offer. The existing catalog description also says a store may need to be selected.
- Current weekly period, exact participating area, and nationwide offer applicability remain unverified. No expiry date was inferred from “weekly” or the run date.

## Verdict

`SKIPPED_BLOCKED` for this one bounded catalog attempt. Official ownership and the robots path were checked, but the current terms block commercial extraction/reuse of the required offer data and image assets absent permission. Stop without inspecting products. Keep the existing catalog/feed records unchanged; this does not prove the catalog obsolete or its current ad expired.
