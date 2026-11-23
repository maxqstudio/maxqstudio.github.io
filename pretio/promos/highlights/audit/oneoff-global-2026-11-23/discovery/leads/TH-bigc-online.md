# Thailand online shop source check — Big C Online

- Run: `pretio-oneoff-global-20261123T040625Z`; country rank 45/174.
- Search lead: the one bounded online-shop query for Thailand returned the official Big C Online page `https://www.bigc.co.th/en/shop/we-are-fresh`.
- Robots check: `https://www.bigc.co.th/robots.txt` returned HTTP-readable rules; `User-agent: *` disallows cart, checkout, payment, customer, and selected service paths, but does not disallow `/en/shop/we-are-fresh`.
- Opened source: `https://www.bigc.co.th/en/shop/we-are-fresh` (Big C Online, page copyright identifies Big C Supercenter PLC). The landing page claims nationwide delivery and an official delivery-area checker; the checker and Terms say the service area is limited/address-dependent. Exact customer-eligible geography was not verified.
- Terms: linked `https://www.bigc.co.th/en/terms-conditions/register`, “Terms and Conditions of Shopping Online,” lines 49–56 says Big C owns the website's text, pictures and information, and users must not copy, download, or spread website text beyond normal use. The requested crawl would retain product/promotional page text at scale, so no offer or item data was retained for this audit and no continued item-level extraction was made after reviewing terms.
- The source landing page was reachable and presented merchandise/promotional sections, but there is no retained, auditable product evidence permitted for this run. No Product Highlight or catalog candidate accepted; no production data changed.
- Disposition: `SKIPPED_BLOCKED` for the bounded Thailand online-shop lead because the source terms prohibit the copying/retention needed for this crawl. This does not mean Big C has no current products, delivery, or promotions.
- Evidence fetched 2026-11-23; web retrieval did not provide a precise request timestamp. No additional search query, login, CAPTCHA, or access bypass was used.
