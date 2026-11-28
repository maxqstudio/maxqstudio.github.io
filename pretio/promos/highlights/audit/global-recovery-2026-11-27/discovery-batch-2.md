# Discovery batch 2 — bounded market research

- **Run ID:** `pretio-global-recovery-20261127T0434Z`
- **Observed:** 2026-11-27 04:45 UTC (agent-reported)
- **Scope:** TH, VN, PH, BD, HK, PK, CZ, FI, NZ, GR. Each market received bounded catalog and online-shop discovery. Search-result snippets were leads only, not offer or price evidence.
- **Page policy:** No offer/product page was opened where robots, access, seller identity, or geography remained unclear.

| Market | Disposition | Source evidence and reason |
|---|---|---|
| TH — Thailand | `SKIPPED_UNVERIFIED` | Bounded Catalog Promo and online-shop searches returned no direct official source lead. No retailer page opened. |
| VN — Vietnam | `SKIPPED_UNVERIFIED` | Bounded Catalog Promo and online-shop searches returned no direct official source lead. No retailer page opened. |
| PH — Philippines | `SKIPPED_UNVERIFIED` | Search surfaced [Robinsons Supermarket promos](https://www.robinsonssupermarket.com.ph/promos); its robots endpoint was inaccessible to the permitted reader. The offer page was not opened. |
| BD — Bangladesh | `SKIPPED_UNVERIFIED` | Leads: [AshBazar](https://www.ashbazarbd.com/en), [The Grocer](https://grocer.com.bd/page/extra-discount), and [SNGmart](https://sngmart.com/). Robots checks were inaccessible; no offer pages or prices were opened. |
| HK — Hong Kong | `SKIPPED_UNVERIFIED` | [foodpanda groceries](https://www.foodpanda.hk/groceries) is a platform, not an identified seller; ordering requires an address. No seller-specific, countrywide offer was verified. |
| PK — Pakistan | `SKIPPED_UNVERIFIED` | Leads: [SPAR Pakistan discounts FAQ](https://www.spar.pk/faqs/do-you-have-any-discounts/) and [Carrefour Pakistan deals](https://www.carrefour.pk/mafpak/en/c/deals). Robots checks were inaccessible; no offers opened. |
| CZ — Czechia | `NEEDS_CATALOG_APPROVAL` | [BILLA’s official stable leaflet page](https://www.billa.cz/akcni-letaky) showed a current leaflet for 25 Nov–1 Dec 2026 and robots allowed the path. [Terms](https://www.billa.cz/obchodni-podminky) identify BILLA but did not establish commercial reuse or image permission. The page also has regional specials. Candidate remains audit-only; no catalog ID or product was added. [Robots](https://www.billa.cz/robots.txt). A separate [GlobusOnline](https://globusonline.cz/cs) lead was not opened because robots was inaccessible. |
| FI — Finland | `SKIPPED_UNVERIFIED` | Bounded searches surfaced no direct official source. No page opened. |
| NZ — New Zealand | `SKIPPED_UNVERIFIED` | [Woolworths NZ FAQ](https://www.woolworths.co.nz/help/faqs) says shoppers select a local store and some offers are localised; its FAQ path was allowed by [robots.txt](https://www.woolworths.co.nz/robots.txt). Countrywide offer scope was not established. [PAK’nSAVE](https://www.paknsave.co.nz/) was not opened because its robots endpoint was inaccessible. |
| GR — Greece | `SKIPPED_UNVERIFIED` | Search surfaced [Mourgis](https://mourgis.gr/) with outlets in Kalamata/Messini, indicating regional scope; robots was inaccessible, so the page was not opened. No national source was verified. |

**Results:** 10 markets; 9 `SKIPPED_UNVERIFIED`, 1 `NEEDS_CATALOG_APPROVAL`; 0 verified catalogs, 0 prices, 0 images, 0 Product Highlights, and no repository production data changed by this batch. Exact per-query timestamps and full search-provider receipts were not retained by the agent; this is a research-summary checkpoint, not a claim of stronger provenance.
