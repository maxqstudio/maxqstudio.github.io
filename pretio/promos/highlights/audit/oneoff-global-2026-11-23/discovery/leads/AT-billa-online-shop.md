# Austria online-shop discovery — BILLA

- Run: `pretio-oneoff-global-20261123T040625Z`; country: `AT`; discovery type: online grocery shop.
- Discovery query: one bounded online-shop search for Austria, `Austria official online supermarket groceries delivery BILLA online INTERSPAR groceries` (2026-11-23). The result named the BILLA Online Shop at `https://shop.billa.at/`. Search output was used only to identify a lead, not as proof of ownership, service scope, product or offer.
- Frozen source lead: `https://shop.billa.at/`.
- Robots check: `GET https://shop.billa.at/robots.txt` returned HTTP 403 at `2026-11-23T09:24:25Z`. No robots policy could be read. To avoid accessing a shop/catalog page without an inspectable access policy, I did not request the storefront, product pages or Terms.
- Ownership, Terms, current product/offer prices, Austria-wide delivery eligibility, image rights and availability therefore remain unverified. No product candidate, normal/promo price pair, validity date or seller identifier was retained.
- Production checks: EUR currency metadata is not available for Austria (`pretio/data/currency.json` maps EUR only to DE); `shop.billa.at`/BILLA has no existing entry in `pretio/promos/catalog_app.json` or current highlight feeds. No catalog registration or highlight change was made.
- Bounded candidate disposition: `SKIPPED_BLOCKED` (robots endpoint access denied; terms/access permission unresolved). No bypass or retry was attempted. The source is not counted as a verified store. This does not assert BILLA lacks an online shop or promotions.
