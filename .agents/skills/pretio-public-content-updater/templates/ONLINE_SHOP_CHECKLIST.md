# Pretio — online shop / marketplace offer checklist (audit ONLY)

Create one audit record per **seller/storefront** and append one evidence row per checked offer. This is NOT a production JSON structure and does NOT extend `catalog_app.json` or country feeds.

Run ID: `<UTC run id>`  
Owner scope: `<ONE_OFF:ID / ONE_OFF_GLOBAL / other explicit scope>`  
Country: `<ISO2>` | Currency supported: `<yes/no>`  
Discovery source: `<seller official directory / permitted marketplace search / Google Shopping authorized discovery / other>`  
Source access policy: `<robots, terms, permitted API/browser method>`  
Platform (if any): `<platform>`  
**Actual seller/store**: `<verifiable name>` | Seller/store ID: `<verified platform identity>`  
Canonical storefront: `<HTTPS URL>` | Catalog registration: `<existing catalog_id / NEEDS_CATALOG_APPROVAL>`  
Checked UTC: `<timestamp>`

## A. Seller/store approval
- [ ] Store operates in the scoped country, official seller identity verified
- [ ] Distinguish platform from seller and third-party from first-party offers
- [ ] Source permits access; no bot/CAPTCHA/login bypass or account scraping
- [ ] Link redirects, canonical host and allowed host checked
- [ ] If `catalog_id` is missing, candidate stays audit-only until separately approved
- [ ] **Online country-wide offer/delivery eligibility** verified through official shipping/market terms and offer context; **province/city checks not mandatory** for a genuine market-wide online deal
- [ ] Country-only storefront/domain does not itself prove eligible market, and pickup-only/regional pricing is not nationwide
- [ ] Price can be genuinely regular (AUDIT_ONLY) or discounted (eligible highlight if approved and verified)
- [ ] Expired published offers pruned from active feeds with matched index SHA; do not retain expired live records
- [ ] Currency metadata present for publishing; otherwise audit only
- [ ] All discovered seller/store candidates have terminal audit status

## B. Each product offer
| Audit-only field | Required recorded evidence |
|---|---|
| Product / SKU / variant | Exact matched identifier, size, pack, model/condition |
| Seller and URL | Actual same seller/store + official permitted product link |
| Discovery URL | Where found (including Google Shopping if authorized); never production `source_url` |
| Price evidence | Explicit public normal and discounted prices from same seller/listing, same market/currency |
| Restrictions | Public, unconditional, no member/cart/credit-card/coupon-only/cashback ambiguity |
| Geo & period | Country-wide offer evidence, source-provided validity if known |
| Image | Decodable real individual product image, authorized host, screenshot/MIME proof |
| Catalog mapping | Existing validated `catalog_id` and matching `source_url` host |
| Decision | `ACCEPTED` / `SKIPPED_UNVERIFIED` / `SKIPPED_BLOCKED` / `NEEDS_CATALOG_APPROVAL` / etc |
| Source snapshot | HTML excerpt / JSON-LD Offer / screenshot path + observed UTC time |

- [ ] Never infer normal price from the Google Shopping price, another seller, percent, MSRP or subscription/coupon price
- [ ] Never reuse a flyer-page image as the individual product photo
- [ ] Never write new production keys like `seller_id`, `platform`, `discovery_source`, `seller_rating`
- [ ] Deduplicate within seller/SKU across discovery sources; other sellers need independent approved catalog IDs
- [ ] Save accepted/rejected candidates and evidence, compact handoff (≤400 words), proceed to next storefront

## C. Bounded discovery and close-out
- Sources searched: `<authorized domains/APIs>`
- Search terms/pages/listings visited: `<counts and bounds>`
- Storefronts found: `<count>`; storefronts checked: `<count>`
- Eligible candidate offers: `<count>`; approved/publishable: `<count>`
- Awaiting catalog owner approval: `<count>`; rejected/blocked: `<count>`
- Status: `<VERIFIED_STORE / ALREADY_REGISTERED / SKIPPED_* / BLOCKED_CURRENCY_METADATA / NEEDS_CATALOG_APPROVAL>`
- Next storefront / country: `<id or STOP>`

The frozen **registered catalog manifest** is counted separately. Closing that manifest does not make discovery infinite, and discovery findings never fake a registered-catalog receipt.
