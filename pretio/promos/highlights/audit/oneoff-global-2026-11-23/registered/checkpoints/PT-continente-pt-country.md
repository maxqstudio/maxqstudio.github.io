# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PT:continente-pt-country` | manifest position: **54/74** | attempt: **1**  
Country: **PT** | retailer: **Continente** | mode: **AUDIT**  
Checked UTC: **2026-11-23T10:19:12Z**  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal receipt: **BLOCKED_CURRENCY_METADATA**

## 1. Catalog Promo source

- [x] Loaded frozen-manifest work unit and original catalog record: `continente-pt-country`, Portugal, active, `official_retailer`, national label with `Portugal (location-selected offers)`, registered URL `https://www.continente.pt/folhetos/`, `valid_until: null`, existing `last_verified_at: 2026-09-28T00:00:00Z`.
- [x] Ownership: the official Services Policy identifies Modelo Continente Hipermercados, S.A. as owner of the site content and Continente Hipermercados, S.A. as seller/supplier (Policy of Services lines 3–7). The registered host is already allowlisted.
- [x] Main `https://www.continente.pt/robots.txt` was readable. `User-agent: *` disallows private/account, search, and technical paths, but not `/folhetos/`. AI-bot section leaves `GPTBot`, `Google-Extended`, `CCBot`, and `PerplexityBot` paths allowed.
- [x] Opened the official landing page at the exact registered URL. It returned the page titled “Folhetos Semanais | Continente Online”; the URL remained stable and the page showed current weekly promotions with dated content. This verifies an evergreen catalog directory, not a dated production link.
- [x] `https://folhetos.continente.pt/robots.txt` returned HTTP 200 `text/plain` through a standard HTTPS request. The wildcard policy blocks selected technical file extensions only; the linked HTML leaflet path is not disallowed. No alternate endpoint or bypass was used.
- [x] Reviewed the 11 flyer/campaign links currently displayed on the official parent page: Weekend, weekly, toys, Christmas decoration/gifts, Christmas dinner, holiday takeaway, Christmas baskets, Continente Magazine, Continente Bom Dia weekly, Madeira weekly, and Azores fortnightly. The page showed live intervals such as 20–23 Nov and 17–23 Nov, longer Christmas campaigns, and separate Madeira/Azores editions. One visible page per linked flyer was checked; opening the Weekend leaflet's Page 2 link returned the same text as Page 1 in the source viewer, so no further page range was inferred.
- [x] The official Services Policy (`https://www.continente.pt/loja-online/politica-de-servicos/`) says online prices are in EUR, apply to purchases through the online shop, and may differ from physical-store prices (lines 20–24). Prices can also change with the selected delivery address. The policy identifies the content owner but provides no affirmative commercial-reuse license or explicit general crawler prohibition in the inspected sections. No user address or delivery location was entered.
- [x] Classification: `LINK_STABLE` / `EVERGREEN_CURRENT`. The public directory updates in place; no catalog URL or `valid_until` change is needed. The record itself is not obsolete.
- [x] No production catalog/feed/index fields or timestamps were edited.

## 2. Product Highlights / audit observations

- [x] Twelve clear public normal/promo price pairs from the visible leaflet pages were transcribed to the separate audit evidence file `registered/evidence/PT-continente-pt-country.md`. PVPR-only references and conditional multi-buy/member offers were excluded. The leaflets show mixed online/physical channels, location-specific editions and/or selected locations; item-level nationwide applicability was not proved.
- [x] All twelve are **AUDIT_ONLY**. Portugal is absent from `pretio/data/currency.json` and from the Product Highlights v2 index; the current feeds have zero references to `continente-pt-country`. No Product Highlights entry can be published under the existing currency/schema baseline.
- [x] No standalone regular-price observation was added. Product-level photos/detail pages and exact fulfillment geography were not verified. Flyer artwork is not an individual product image.
- [x] No item was accepted for a Product Highlights feed; no expired item or highlight reference was found/deleted.

## 3. Skip decision and compact handoff (≤400 words)

- Work unit `PT:continente-pt-country`, position 54/74; receipt `BLOCKED_CURRENCY_METADATA`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; base/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Continente's registered `/folhetos/` URL is an official, stable, current evergreen directory. The page's 11 linked flyer/campaigns were checked at one visible page each; current weekly leaflets exposed dated prices through 23 Nov 2026, and the page distinguishes Madeira/Azores editions. Do not add a dated expiry to the evergreen directory.
- Main and leaflet-subdomain robots checks allowed the observed public HTML paths. The Services Policy identifies the site/content owner and warns that prices in the online shop may differ from physical-store prices; no delivery location was selected. No general crawler ban or commercial-reuse license was established, so all observed offers remain audit-only.
- Twelve clear normal/promo pairs are in `registered/evidence/PT-continente-pt-country.md`; other price text was excluded when it was PVPR-only, single-price, conditional or ambiguous. No individual product images or nationwide item coverage were verified. EUR is unsupported for Product Highlights in this baseline, PT is absent from the index, and there are zero active highlight references to this catalog.
- No production data changed. The catalog is `LINK_STABLE` / `EVERGREEN_CURRENT`, not expired or obsolete. No catalog removal/migration is proposed. Next manifest input: `PT:intermarche-pt-country` (55/74), in a fresh isolated source context.
