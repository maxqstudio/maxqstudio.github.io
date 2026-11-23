# Agra Namibia source evidence

Run: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `NA:agra-na-country`  
Observed on: `2026-11-23`; exact request timestamps were not retained by the shell client.

## Official ownership, access and landing page

- Existing registered record URL: <https://agra.com.na/index.php/retail-wholesale/specials-promotions>
- Official homepage: <https://agra.com.na/> — HTTP 200; identified the Agra Namibia site and linked “Specials & Promotions.”
- Robots policy: <https://agra.com.na/robots.txt> — HTTP 200 `text/plain`; no disallow matched the registered promotions path or the public `/images/` folder. Disallows covered administrative/system paths such as `/administrator/`, `/cache/`, `/cli/`, `/includes/`, `/installation/`, `/language/`, `/libraries/`, `/logs/` and `/tmp/`.
- Registered page returned HTTP 200 HTML with title “Specials & Promotions - Agra Namibia.” The fetch wrapper did not expose the final response URI, so no redirect is asserted.
- Terms route found: <https://agra.com.na/index.php/comps-terms-and-conditions> — HTTP 200, page title “Terms and Conditions - Agra Namibia,” visible body says there are no articles in the category. This is not a general site reuse license. No general reuse restriction or permission clause was located in this bounded review.

## Current campaigns visible on the official landing page

| Campaign | Area text visible on page | Valid from | Valid until |
|---|---|---:|---:|
| Agra Safari Den - Camping & Outdoor Promotion 2026 | All Agra branches countrywide | 2026-11-19 | 2027-01-18 |
| Month End Specials - November 2026 | All Agra stores nationwide | 2026-11-19 | 2026-12-14 |
| Contractors - November 2026 | No availability area visible in listing text | 2026-11-19 | 2026-12-14 |
| Month End Safari Den Specials - November 2026 | At Agra Safari Den, or order at any Agra branch | 2026-11-19 | 2026-12-14 |

These are campaign-level facts from the listing, not item-level product discounts.

## Bounded detail-page inspection

- Official detail page opened: <https://agra.com.na/index.php/specials/1170-month-end-specials-november-2026> — HTTP 200; title “MONTH END SPECIALS - NOVEMBER 2026 - Agra Namibia.” Visible body prompts the reader to select the flipbook to view specials full-screen.
- Official image URL linked from page metadata: <https://www.agra.com.na/images/retail/specials/2026/MonthEnd/Nov2023_ME.png> — HTTP 200, `image/png`, `Content-Length: 6504275`, `Last-Modified: Wed, 18 Nov 2026 08:57:36 GMT`. Visual inspection showed a campaign cover, not item listings; no product name or price pair was extracted. The temporary inspection copy is not retained in this repository.
- No normal/promo pair, individual product image, SKU/variant or item-level validity was verified. No product candidate was accepted.

## Disposition

The stable official landing URL is active and the listed campaigns are current as of the check date. No change to catalog JSON is proposed. Namibia is absent from the current Product Highlights currency/feed mapping, so any future offers remain non-publishable until supported. This source attempt is terminal `SKIPPED_UNVERIFIED` for product research; the catalog is not expired or obsolete.
