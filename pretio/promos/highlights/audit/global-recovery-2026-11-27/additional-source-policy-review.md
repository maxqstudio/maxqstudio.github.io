# Additional Source Policy Review — 2026-11-27

**Observed at:** 2026-11-27 07:20 UTC

**Purpose:** Bounded, policy-first investigation after zero eligible Product Highlights.

**Owner instruction:** Continue the recovery work in this Codex turn. This review does not install a schedule or claim completion of another Catalog Promo cycle. Issue #57's prior no-second-cycle wording remains a scope conflict for the independent auditor to classify.

**Baseline:** `65bc23a54515c138d23e0e1465b9317a4bbc29d0`

**Prior PR head reviewed:** `024fc6e192c917518ddc9966a8f4ead294f96fa5`

## Result

No Product Highlight or Catalog Promo was added or changed by this review. No product listing, offer, image, cart, private endpoint, or logged-in area was requested from the retailers below. The review opened official terms/legal pages and stopped at the published commercial-use restrictions or missing permission grant. These findings are not product-price evidence and do not count as new-market verification.

| Country | Existing catalog ID / retailer | Official policy evidence | Decision |
|---|---|---|---|
| CH | `coop-ch-country` / Coop | [Online-shop terms](https://www.coop.ch/en/terms-condition.html), “Intellectual property” section: Coop states it has the exclusive right to use product descriptions, images, photographs, and texts. No external republication or image-use grant for Pretio was found. | `BLOCKED_PERMISSION_UNCONFIRMED`; no offer page accessed. |
| CH | `migros-ch-country` / Migros | [Migros legal information](https://jobs.migros.ch/de/rechtliche-informationen) says its usage rules apply to `migros.ch`; content belongs to Migros entities or contractors, and public/commercial use requires prior written consent. [Migros help](https://support.migros.ch/hc/de/articles/360014950740-Sind-die-Preise-der-Migros-Produkte-online-dieselben-wie-in-den-Migros-Superm%C3%A4rkten) also says offers vary by region. | `BLOCKED_WRITTEN_PERMISSION`; national price equivalence is unproven. No offer or image page accessed. |
| ID | `lotte-mart-location-live` / LOTTE MART | [Official terms](https://www.lottemart.co.id/en/syarat-dan-ketentuan), section 8: website materials may be used only personally, not for business or commercial purposes. | `BLOCKED_COMMERCIAL_REUSE`; no offer page accessed. |
| ID | `superindo-national-live` / Super Indo | [Official terms](https://www.superindo.co.id/syarat-dan-kondisi), sections 5–6: site/app materials are personal-use only; public or commercial distribution/reuse needs prior written consent; images are protected and cannot be used without rights-holder permission. | `BLOCKED_WRITTEN_PERMISSION`; no offer or image page accessed. |
| CL | `tottus-country-cl` / Tottus | [Official terms](https://www.tottus.cl/tottus-cl/content/terminos-y-condiciones), section 11: content and data are owned by Tottus/content providers; reproduction or exploitation requires prior written consent. | `BLOCKED_WRITTEN_PERMISSION`; no offer page accessed. |
| US | `aldi-us-country` / ALDI US | [Official terms](https://www.aldi.us/store/aldi/pages/terms-of-use), sections 3–4: the license is personal and noncommercial; other publication/distribution/use requires prior written consent. | `BLOCKED_WRITTEN_PERMISSION`; no offer or image page accessed. |
| US | `target-us-country` / Target | [Official terms](https://www.target.com/c/terms-conditions/-/N-4sr7l), sections “License and Access” and “Unlawful or Prohibited Uses”: commercial use of listings, prices, and images and automated extraction are prohibited; only specifically approved agents may conduct agentic access. | `BLOCKED_COMMERCIAL_AUTOMATION`; no listing or image page accessed. |
| US | `kroger-us-country` / Kroger | [Website and app terms](https://www.kroger.com/i/terms/website-and-app), section 5.4: automated bots, crawlers, scrapers, and data-mining tools may not access, collect, extract, or monitor site information. | `BLOCKED_AUTOMATED_ACCESS`; no offer page accessed. |
| ZA | `foodloversmarket-za-specials` / Food Lover's Market | [Official compliance and legal terms](https://foodloversmarket.co.za/compliance-and-legal/): site content is limited to personal, lawful, noncommercial use; commercial or other unauthorized use/republication is prohibited absent express permission. | `BLOCKED_WRITTEN_PERMISSION`; no offer or image page accessed. |

## Reconciliation and limits

- These are nine policy decisions across five already-supported highlight countries, not nine attempted catalog receipts and not nine verified retailers/offers.
- Existing run decisions remain unchanged: Walmart is already source-policy blocked; REWE Germany and Santa Isabel Chile remain audit-only for region/store selection and/or missing image authorization; Lidl Germany's current product candidate remains audit-only; the Pick n Pay/Taawon incidents remain excluded from eligible current-run evidence.
- No exact price pairs, current validity dates, market-wide availability, product-image bytes, or new seller identities were collected in this policy-only continuation.
- A publication-eligible source still requires an existing approved catalog ID, permission-compatible access and media use, exact product/variant, same-seller normal and lower promo prices, market eligibility, and a decodable individual image. None of those publication gates was satisfied by this review.
- This does **not** establish that every retailer or market in the 174-market target has been exhausted. It records only the named official-source policy checks. The 174-market coverage and the original registered-catalog completeness limitations in `run-report.md` remain unchanged.

## Next action

Keep the production delta at zero. Resume only against a retailer-provided written reuse authorization, an authorized/contracted data feed, or another approved source whose terms permit the required public commercial content and image use. Do not revisit sources blocked by the policies above without changed permission evidence.
