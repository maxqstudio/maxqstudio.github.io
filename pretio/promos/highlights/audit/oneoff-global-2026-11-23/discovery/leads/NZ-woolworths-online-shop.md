# New Zealand online-shop source check — Woolworths NZ

- Run: `pretio-oneoff-global-20261123T040625Z`; country rank 58/174.
- Search lead: the one bounded online-shop query for New Zealand returned the official Woolworths NZ online-shopping page `https://www.woolworths.co.nz/services/online-shopping`.
- Robots check: `https://www.woolworths.co.nz/robots.txt` allows the service page, but disallows `/shop/search` and `/specials-offers/boosts`; account, checkout and saved-list paths are also disallowed.
- Opened source: `https://www.woolworths.co.nz/services/online-shopping` (Woolworths NZ; footer identifies Woolworths New Zealand Limited). It describes delivery, pickup, and savings offers. This is a service overview, not an item-level offer page. Delivery eligibility is address-dependent.
- Terms: the site's linked `https://www.woolworths.co.nz/help/terms-conditions/online-shopping-website-app`, section 6, says site information may be downloaded for personal use, but site content may not otherwise be “scraped, copied, altered, modified, reproduced, transmitted or distributed without our prior written consent.” Section 11 grants access solely for personal use. No prior written consent for this crawl was evidenced, so item and promotion pages were not opened and no product text was retained.
- Terms also say prices and product range vary by selected local store (section 1.1), and prices shown in NZ currency include taxes (section 1.6). This is consistent with NZ retail, but exact delivery/service coverage and current item discounts were not verified.
- No Product Highlight or catalog candidate accepted; no price pair, product image, offer date, or product availability evidence was retained. No production data changed.
- Disposition: `SKIPPED_BLOCKED` for the bounded New Zealand online-shop lead because the site's terms prohibit scraping/copying without prior written consent. This does not mean Woolworths NZ has no current products, delivery, or promotions.
- Evidence fetched 2026-11-23; web retrieval did not provide precise request timestamps. No additional search query, login, CAPTCHA, or access bypass was used.
