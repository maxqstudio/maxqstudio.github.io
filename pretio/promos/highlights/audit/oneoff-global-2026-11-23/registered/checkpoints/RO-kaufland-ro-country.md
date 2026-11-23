# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `RO:kaufland-ro-country` | manifest position: **60/74** | Attempt: **1**  
Country: **RO** | Retailer: **Kaufland** | Mode: **AUDIT** | Scope: **ONE_OFF_GLOBAL**  
Audit artifacts saved approximately **2026-11-23T10:26Z**; web tool did not expose exact response timestamps  
Baseline / skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal status: **BLOCKED_CURRENCY_METADATA**

## 1. Catalog Promo source

- [x] Loaded the frozen manifest and active record `kaufland-ro-country`: Kaufland / Kaufland România, RO country location, `official_retailer`, national label. Registered URL: <https://www.kaufland.ro/cataloage-cu-reduceri.html>, already on the `allowed_hosts` list. Record `valid_from` is 2026-11-18, `valid_until` is 2026-11-25T06:00:00+08:00, and `last_verified_at` is 2026-11-18T00:35:23Z; no catalog fields or `last_verified_at` changed.
- [x] One official `robots.txt` page check: <https://www.kaufland.ro/robots.txt>. It returns `User-agent: *`, disallows `/etc.clientlibs/`, and allows `/etc.clientlibs/kaufland`; it does not disallow the registered catalog path. The page links a sitemap. No robots restriction was observed for this path. No login, CAPTCHA, hidden endpoint, alternate user-agent, proxy or access bypass was used; no retries were made.
- [x] One bounded read of the exact registered landing URL. It identifies itself as the online catalog page and exposes current and next catalog links: current **18.11.2026–24.11.2026**, next **25.11.2026–01.12.2026**. Official catalog FAQ <https://www.kaufland.ro/utile/informatii-utile-contact/informatii-despre-catalogul-online-kaufland.html> says weekly catalogs run Wednesday through Tuesday. Thus the stored period matches the current flyer and has not expired on the run date.
- [x] Classification: **LINK_STABLE landing page with rotating weekly flyers**. The registered URL is a permanent catalog directory whose content lists current and upcoming weeks. Historical URL stability was not independently checked. The linked leaflet host is `leaflets.kaufland.com`, not present in this repo's current `allowed_hosts`; I did not follow that cross-host link.
- [x] Geography: landing page's selected store is **Kaufland Roman Soseaua de Centura**, with a store-change control; the record summary also warns that offer availability may vary by store/stock. A national record and one selected-store view do not prove a specific product's price/eligibility nationwide.
- [x] Limited official-site terms/reuse check found no general permission for commercial reuse of catalog prices or product imagery. Kaufland's press-media note at <https://despre.kaufland.ro/presa/newsroom/2024/septembrie/kaufland-aniverseaza-5-ani-de-kaufland-card-si-rasplateste-loialitatea-consumatorilor> restricts supplied images/text to editorial use and asks image credit © Kaufland; that media notice does not establish broader permission for flyer assets. No image was fetched or reused. Although the landing page displayed current recommendations and prices, I did not transcribe price pairs as candidate data without reuse terms/permission clarity.

## 2. Product Highlights / expiry

- [x] No `pretio/promos/highlights/RO.json` exists and `pretio/data/currency.json` has no RO currency mapping. RO Product Highlights cannot be published under the current schema; this catalog check still counts as attempted.
- [x] Read-only scan of existing country highlight feeds found no references to `kaufland-ro-country`. No item prices, product images or new candidate IDs were recorded; no feed or index changes were made.
- [x] Current official landing page proves the catalog is live and shows a future next-week period. Current catalog validity through 24 Nov is still ahead of the run date. No expiry/obsolescence was established; do not remove or extend the source.

## 3. Disposition

- [x] **BLOCKED_CURRENCY_METADATA** — registered catalog checked; RO has neither a highlight feed nor configured currency. Additional nationwide product eligibility and reuse permission are also unverified, so no product candidate is publishable from this attempt.
- [x] No catalog/feed/index/currency/host edits, no product price or image reuse, no expiry deletions. Preserve the active catalog record; lack of product evidence or reuse permission is not evidence of obsolescence.

## Compact handoff

Work unit `RO:kaufland-ro-country`, 60/74; terminal receipt `BLOCKED_CURRENCY_METADATA`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`. The exact registered page <https://www.kaufland.ro/cataloage-cu-reduceri.html> and its robots file were checked once. Robots does not block this path. The evergreen landing page lists the current flyer 18–24 Nov 2026 and next flyer 25 Nov–1 Dec; official FAQ says weeks run Wednesday–Tuesday. It is store-selected (Roman Soseaua de Centura) and says availability varies; item-level nationwide eligibility was not established. `leaflets.kaufland.com` is not an existing allowed host and was not followed. No general commercial reuse permission for price/image data was found; official press-media text limits those supplied assets to editorial use. No product prices were retained as candidates and no images were fetched. RO has no highlight feed/currency entry; the catalog remains live, valid, and unchanged. No production JSON changed. Next manifest unit: `RS:idea-rs-country` (61/74); continue in a fresh isolated context.