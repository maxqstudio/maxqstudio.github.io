# Continente Portugal — audit-only price evidence

Run: `pretio-oneoff-global-20261123T040625Z`  
Observed: `2026-11-23T10:19:12Z`  
Parent catalog: <https://www.continente.pt/folhetos/>  
Current leaflet inspected: <https://folhetos.continente.pt/2026/11/fim-de-semana-s47-lo74/>  
Access policy: <https://www.continente.pt/robots.txt> and <https://folhetos.continente.pt/robots.txt>  
Terms/price scope: <https://www.continente.pt/loja-online/politica-de-servicos/>

## Verified from the official leaflet text

One visible page was reviewed for each of the 11 current leaflet/campaign links listed on the parent page. The Weekend, general weekly, Continente Bom Dia, Madeira and Azores leaflets state current November validity; other items are dated Christmas campaigns. The rows below are **AUDIT_ONLY**, not Product Highlights. PVPR-only references and conditional member/multi-buy offers were excluded; only same-page public normal/promo pairs with clear product identity were retained. One Page 2 navigation returned duplicate text in the source viewer, so no unseen continuation was inferred.

| Product as shown / normalized for audit | Brand or variant | Normal price | Promo price | Currency / unit | Source date and limits |
|---|---|---:|---:|---|---|
| Bife Pá e Acém de Vitelão (Balcão de Atendimento) | butcher counter cut | 13.99 | 12.99 | EUR/kg | Page states “save €1”; 20–23 Nov 2026. Store/online selected location not established. |
| Pá de Porco com Osso Continente | Continente; bone-in cut | 4.49 | 3.99 | EUR/kg | Flyer shows direct discount; 20–23 Nov 2026. Store/online selected location not established. |
| Camarão 30/50 Cozido | 30/50 size grade; cooked | 14.99 | 9.99 | EUR/kg | Flyer shows direct discount; 20–23 Nov 2026. Store/online selected location not established. |
| Curgete Verde | green courgette | 1.69 | 1.19 | EUR/kg | Flyer shows direct discount; 20–23 Nov 2026. Store/online selected location not established. |
| Polvo 800 g a 1.5 kg Continente Congelado | Continente; frozen, size range on leaflet | 14.99 | 11.99 | EUR/kg | General weekly leaflet; direct discount; 17–23 Nov 2026. Location not selected. |
| Costeletas de Vitelão (Balcão de Atendimento) | butcher counter cut | 14.99 | 13.49 | EUR/kg | General weekly leaflet states €1.50 savings; 17–23 Nov 2026. Location not selected. |
| Bifanas de Porco Continente | Continente | 4.99 | 4.49 | EUR/kg | General weekly leaflet; same displayed price pair; 17–23 Nov 2026. Location not selected. |
| Couve Coração Inteira | whole cabbage | 1.69 | 1.29 | EUR/kg | General weekly leaflet; direct discount; 17–23 Nov 2026. Location not selected. |
| Abacaxi Super Sweet Inteiro | Super Sweet; whole | 1.99 | 1.69 | EUR/kg | General weekly leaflet; direct discount; 17–23 Nov 2026. Location not selected. |
| Aguardente Velha CR&F Reserva, 70 cl + copo balão | CR&F; gift pack | 19.99 | 18.49 | EUR/unit | Christmas decoration/gifts leaflet; states €1.50 savings; 10 Nov–24 Dec 2026. Location not selected. |
| Whisky Famous Grouse, 70 cl + caneca | Famous Grouse; gift pack | 20.29 | 15.29 | EUR/unit | Christmas dinner leaflet; direct discount shown; 17 Nov–24 Dec 2026. Location not selected. |
| Whisky Duck Tale, 70 cl | Duck Tale | 19.99 | 14.99 | EUR/unit | Christmas dinner leaflet; direct discount shown; 17 Nov–24 Dec 2026. Location not selected. |

These are short factual price observations from the retailer's public pages. The retailer's current Bom Dia, Madeira and Azores leaflets were also checked; where their displayed prices duplicated a general weekly row, or they only showed a single current price/PVPR/conditional offer, no duplicate pair was added. No product detail page or individual product image was opened or retained. The flyer pages contain physical-store/online references and region-specific leaflets; the official Services Policy says online prices may differ from physical-store prices and depend on delivery context. Do not treat these rows as nationwide physical-store deals.

## Permission, geography and publication gate

- Main-site robots permits the public `/folhetos/` page; the leaflet subdomain's wildcard rules did not disallow the opened HTML leaflet. Technical endpoints/extensions remain excluded.
- The official Services Policy identifies Modelo Continente Hipermercados, S.A. as owner of site content, and states its EUR prices apply to online orders and may differ from physical stores. The examined policy had no explicit general crawler prohibition and no affirmative blanket commercial-reuse license. No delivery address/store was selected.
- Portugal has no currency mapping in `pretio/data/currency.json`, no Product Highlights index entry, and no active feed references to `continente-pt-country`.
- Product images and nationwide item applicability are unverified. Keep all four rows audit-only; publish no highlight or new retailer schema fields.
