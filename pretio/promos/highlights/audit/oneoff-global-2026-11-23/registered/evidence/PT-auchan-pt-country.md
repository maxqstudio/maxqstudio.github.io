# Auchan Portugal — source and offer evidence

Run: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PT:auchan-pt-country` (frozen manifest position 53/74)  
Observed/checkpointed: `2026-11-23` / `2026-11-23T10:11:28Z` (UTC)  
Mode: audit only; no production catalog or highlight write

## Source and access

- Registered official URL: <https://www.auchan.pt/pt/folhetos/>. The public page title was “Folhetos Auchan - As melhores Promoções”; requested and rendered URL matched the manifest URL. It visibly lists multiple current dated campaigns, supporting a stable evergreen listing page. This does not establish that each item price is nationwide.
- Robots: <https://www.auchan.pt/robots.txt>. It returned text/plain rules for `User-Agent: *`, with query/filter, account, checkout and other disallows. No rule disallows `/pt/folhetos/`, `/pt/folheto-semanal-47-3/`, or the observed product-detail path. No alternate agent, session, private API, or bypass was used.
- Official terms found via bounded searches `site:auchan.pt/pt "Termos e Condições" Auchan Portugal` and `site:auchan.pt "política de utilização" Auchan Portugal`: <https://www.auchan.pt/pt/termos-condicoes/termos-e-condicoes.html>. The page is customer-account terms and discusses promotion eligibility, but no general crawler or commercial-content reuse permission/prohibition was found. Reuse permission therefore remains unverified; no page images or raw HTML were copied into production.
- The catalog landing page lists these periods (all current on 23 Nov 2026): Tecno Black Friday 23–30 Nov; Presentes 18 Nov–9 Dec; Semanal 19–25 Nov; Especial Nivea 13–29 Nov; Catálogo Brinquedos 10 Nov–9 Dec; Revista SBE Natal 4 Nov–26 Dec; Cabazes de Natal 1 Nov–31 Dec; Especial Eletrodomésticos and Especial Bosch 1–30 Nov; Puericultura 13 Jan–31 Dec; Pastelaria 1 Jan–31 Dec.
- Link discrepancy: the “Ver Folheto” link from the 19–25 Nov weekly listing resolved to an official smartviewer URL whose UTM text says `semanal_47_12_a_18_novembro`. The adjacent “Ver Produtos” link led to a weekly product listing and product detail that both explicitly show the 19–25 Nov period. The stable registered landing page remains current; the individual flyer viewer's period labeling was not relied on for price evidence.
- The official product listing says product selection and prices may change when delivery location changes; its visible notice also said the inspected postcode was outside the delivery area. No postcode/store was selected. Thus the single product price pair below cannot be claimed nationwide or tied to a user area.

## Bounded product observations

Official listing: <https://www.auchan.pt/pt/folheto-semanal-47-3/>. The page exposed 24 product cards before a “Ver mais produtos” control. No pagination or hidden endpoint was attempted. These rows are audit-only. `PVP Recomendado` is the displayed recommended retail price, not verified Auchan regular-price history, so it is **not** treated as `normal_price`.

| Product card | Current displayed amount | Other displayed value / claim | Evidence decision |
|---|---:|---|---|
| Whiskas Tasty Mix seleção do chef, 12×85 g | €5.99 | “-25% sobre PVPR”; PVP Recomendado €7.99 | No Auchan regular price pair; PVPR only |
| Ben & Jerry’s Dulce de-Lish Sundae, 427 ml | €6.99 | “Promoção” | No normal price |
| Compal 100% manga, 1 L | €1.69 | “Promoção” | No normal price |
| Actimel morango, 12×100 g | €5.39 | “-18% sobre PVPR”; PVP Recomendado €6.57 | No Auchan regular price pair; PVPR only |
| Rexona Tropical 72 h spray, 200 ml | €3.57 | “-35% sobre PVPR”; PVP Recomendado €5.49 | No Auchan regular price pair; PVPR only |
| Ravioli de trufa branca e queijo Rana, 250 g | **€3.14** | Explicit “Price reduced from €4.19 to €3.14”; promotion 19–25 Nov 2026; EAN 8001665700900 | **One explicit same-listing price pair**, audit-only; area, currency support and image decode gates still fail |
| TRESemmé Biotin Repair conditioner, 685 ml | €5.99 | “-25% sobre PVPR”; PVP Recomendado €7.99 | No Auchan regular price pair; PVPR only |
| Felix Fantastic carne, 24×85 g | €11.39 | “-25% sobre PVPR”; PVP Recomendado €15.19; marked unavailable online | No Auchan regular price pair; PVPR only |
| Old Spice Captain spray, 150 ml | €3.57 | “-35% sobre PVPR”; PVP Recomendado €5.49 | No Auchan regular price pair; PVPR only |
| Oliveira da Serra virgem PET, 750 ml | €4.99 | “-49% sobre PVPR”; PVP Recomendado €9.79 | No Auchan regular price pair; PVPR only |
| Domestos Power 5 Lime, 5 units | €5.39 | “-60% sobre PVPR”; PVP Recomendado €13.49; marked unavailable online | No Auchan regular price pair; PVPR only |
| TRESemmé Keratin Smooth conditioner, 400 ml | €3.83 | “-40% sobre PVPR”; PVP Recomendado €6.39 | No Auchan regular price pair; PVPR only |
| Super Pop OxyPower dishwasher tablets, 70 doses | €11.20 | “-60% sobre PVPR”; PVP Recomendado €27.99; marked unavailable online | No Auchan regular price pair; PVPR only |
| Sun All in One limão, 80 tablets | €11.99 | “-45% sobre PVPR”; PVP Recomendado €21.99 | No Auchan regular price pair; PVPR only |
| Glade Aromatherapy stick Energy, 80 ml | €7.49 | “-50% sobre PVPR”; PVP Recomendado €14.99; marked unavailable online | No Auchan regular price pair; PVPR only |
| Poca Terra Douro white wine, 0.75 L | €7.39 | “Promoção” | No normal price |
| Elode Deep Blue | €8.49 | “-15% sobre PVPR”; PVP Recomendado €9.99 | No Auchan regular price pair; PVPR only |
| Dum Dum electric insecticide, 45 nights | €4.99 | “-32% sobre PVPR”; PVP Recomendado €7.29; marked unavailable online | No Auchan regular price pair; PVPR only |
| Pork bifanas da perna, per kg | €4.99/kg | “Promoção”; 200 g minimum | No normal price |
| Rexona Men Invisible B+W stick, 50 ml | €3.24 | “-35% sobre PVPR”; PVP Recomendado €4.99 | No Auchan regular price pair; PVPR only |
| Pantene Liso e Sedoso, 800 ml | €8.99 | “-25% sobre PVPR”; PVP Recomendado €11.99; marked unavailable online | No Auchan regular price pair; PVPR only |
| Xau spring-flowers laundry liquid, 105 doses | €11.99 | “-60% sobre PVPR”; PVP Recomendado €29.98 | No Auchan regular price pair; PVPR only |
| Xau + Vanish Advanced, 118 doses | €13.99 | “-60% sobre PVPR”; PVP Recomendado €34.99 | No Auchan regular price pair; PVPR only |
| Purina One sterilized beef, 2.8 kg | €15.79 | “-35% sobre PVPR”; PVP Recomendado €24.29 | No Auchan regular price pair; PVPR only |

Direct product page for the one explicit pair: <https://www.auchan.pt/pt/produtos-frescos/gastronomia/massas-frescas/ravioli-de-trufa-branca-e-queijo-rana-250g/1146844.html>. It names the exact product/size, EAN, €4.19→€3.14 pair and 19–25 Nov validity. Its image alt names the same product, but the linked product image asset request timed out; the image was not decoded. A visible delivery notice says prices/catalog availability can change by delivery location and the inspected postcode was outside delivery zones.

## Eligibility and disposition

- One discount pair is source-verified, but **zero publishable Product Highlights**: PT has no supported currency mapping/feed/index; price/availability is delivery-location sensitive with no verified nationwide area; and the product image bytes could not be decoded.
- The 23 other visible cards either expose only a promo/current price or compare against PVP Recomendado, not an Auchan normal price. They are rejected as eligible highlights; no `normal_price` was inferred.
- No new catalog ID or host is proposed. Existing active Catalog Promo record and `last_verified_at` remain untouched. No item expiry or catalog obsolescence was proven. No production JSON changed.
