# DE:aldi-nord-de-country — ALDI Nord

## Per-catalog checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Country: `DE` | Catalog ID: `aldi-nord-de-country` | Retailer: `ALDI Nord`  
Official URL: https://www.aldi-nord.de/angebote.html  
Checked UTC: `2026-11-23T04:55:12Z` (bounded collection window approx. 04:52–04:55Z)  
Mode: `AUDIT / ONE_OFF_GLOBAL` | Manifest work unit: `17 of 74` | Attempt: `1`  
Frozen base/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: `SKIPPED_UNVERIFIED`

### 1. Catalog Promo source

- [x] Loaded exact active record from `pretio/promos/catalog_app.json`: `official_retailer`, national catalog label, country `DE`, `valid_from: null`, `valid_until: null`, `last_verified_at: 2026-09-22T00:00:00Z`; `www.aldi-nord.de` is in `allowed_hosts`. Summary warns that offer availability can vary by location.
- [x] Official ownership is consistent with ALDI Nord's offers page and official imprint: https://www.aldi-nord.de/kundeninformationen/impressum.html. The registered frozen URL was used exactly.
- [x] Direct public GET of https://www.aldi-nord.de/angebote.html completed within the 30-second limit: HTTP `200`, `text/html; charset=utf-8`, 1,695,219 bytes. The page renderer returned the same URL; no redirect was reported. Current content includes “Highlights der aktuellen Woche”, “Aktion Mo. 23.11.” and links for the next “Aktion Do. 26.11.” period. This is an evergreen-style `/angebote.html` path with current changing content; historical in-place stability was not tested.
- [x] Robots checked at https://www.aldi-nord.de/robots.txt: HTTP `200`, `text/plain; charset=utf-8`, final URL unchanged. It begins `User-agent: *`; its listed disallows cover unrelated registration/bot paths and specified query patterns, not `/angebote.html`.
- [x] Terms check: official customer-information hub https://www.aldi-nord.de/kundeninformationen.html links to https://www.aldi-nord.de/kundeninformationen/teilnahmebedingungen-agb.html, titled “Teilnahmebedingungen für Gewinnspiele & Allgemeine Geschäftsbedingungen.” No general website-use/crawling terms were exposed in these official pages; this is not treated as affirmative scraping permission.
- [x] Source page positively verified current offer content. No catalog URL, `last_verified_at`, catalog JSON, feed, or index was changed.
- [ ] Nationwide applicability of product offers not established. The official catalog record itself says availability can vary by location; the viewed page did not establish that any selected item is offered in every German market/branch.

### 1B. Online shop / marketplace

- [x] Not applicable: this is a physical-retailer catalog; no online-store or marketplace discovery was performed.

### 2. Product Highlights — discounted items only

- [x] Checked the eight existing ALDI Nord items in `pretio/promos/highlights/DE.json` against the current-week cards. The page visibly repeats these pairs under “Aktion Mo. 23.11.”: Eisbergsalat `0.99/0.75 EUR`; Tafelbirnen `1.99/1.59`; Kulturchampignons braun `1.89/1.49`; Speisekartoffeln `1.99/1.79`; Orangen `2.49/2.22`; Clementinen `1.49/1.29`; Minutensteaks `2.99/2.29`; Hähnchenbrustfilet-Teilstücke XXL `9.99/8.49`. EUR matches `pretio/data/currency.json` for DE. Example source excerpt: `Eisbergsalat — -24%, 0.75, 0.99, Stück`; see https://www.aldi-nord.de/angebote.html.
- [ ] No item accepted or re-verified for feed use: the page gives a Monday start/current-week grouping but no source-backed end date for these items; no item-level nationwide participation evidence was visible; the card images were linked but not fetched/decoded in this bounded check. The DE feed's existing Scene7 image URLs were not revalidated. Other cards with one price only or a displayed `UVP` were not treated as a verified same-retailer normal-price pair.
- [x] Existing eight feed records were left byte-for-byte unchanged. Their missing/unknown expiry is not proof of expiry; no item was deleted or retimed. No new candidate IDs; no expired IDs pruned.

### 3. Close-out

- Catalog classification: `EVERGREEN_CURRENT` for the official evergreen-style page snapshot; source content is current as of the check, while item-level coverage/validity remains unverified.
- Catalog fetch result: `FETCH_OK`; highlight result: `SKIPPED_UNVERIFIED` because nationwide scope, source-backed end dates, and decoded individual images were not established.
- Inspected scope: the single registered ALDI Nord offers page and the eight matching current-week cards already present in the DE feed. No product-detail pages, hidden APIs, alternate routes, CAPTCHA/login, proxy, or bypass were used; no retry was made.
- No production JSON or shared progress/summary artifact was edited. This checkpoint and its per-unit receipt are the only outputs for this work unit.

## Compact handoff (≤400 words)

- Work unit `DE:aldi-nord-de-country`, position `17/74`; terminal receipt `SKIPPED_UNVERIFIED`. Counted as attempted. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, base/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`; no schedule or second cycle was started.
- The frozen official URL https://www.aldi-nord.de/angebote.html returned HTTP 200 `text/html; charset=utf-8` within 30 seconds; same final URL was reported. Robots returned HTTP 200 `text/plain; charset=utf-8` and did not disallow `/angebote.html`. Official terms pages inspected covered giveaway/general business terms; no general crawl terms were exposed and no permission is inferred.
- The page shows current week offers starting `Mo. 23.11.` and later offers `Do. 26.11.`. Eight existing DE feed products have visible matching EUR price pairs on the current-week cards (Eisbergsalat, Tafelbirnen, Kulturchampignons braun, Speisekartoffeln, Orangen, Clementinen, Minutensteaks, Hähnchenbrustfilet-Teilstücke XXL). No new item accepted: item-level Germany-wide applicability is unproven (registered summary warns availability may vary by location), no offer end date was visible, and image bytes were not decoded. Other single-price/UVP cards are insufficient.
- Existing feed, catalog, and index were not changed; no item was proved expired. Source evidence is in this checkpoint. Next manifest work unit: `DE:aldi-sued-de-country`.
