# Global Catalog Promo discovery checklist — 2026-11-27

- Run: `pretio-global-recovery-20261127T0434Z`; scope: `ONE_OFF_GLOBAL` manual continuation; base: `65bc23a54515c138d23e0e1465b9317a4bbc29d0`.
- Canonical skill Git blob at base: `2f46a28da390388eb34c316d5dbf45ad27ac264a`.
- Country universe: 249 entries in `pretio/location/v2/index.json`; selected 174 markets from the frozen GDP-ranked register at `pretio/promos/highlights/audit/oneoff-global-2026-11-23/country-discovery-register.json` (source commit `8b466c4994468b9ba3aa8b035a0c95706b80095e`, SHA-256 `93290def561f8b7c111bbdda8ca07d5f8b16bbfbdc566da601f47fa798b981ae`).
- The continuation addressed the prior 140 pending markets in 14 batches of 10. The previous 34 terminal dispositions remain attributed to the original run. Combined terminal decisions: 174/174; verified official new-market catalogs: 0. A terminal decision is not source verification or country coverage.
- The recovery register reports 280 discovery queries (one catalog-promo plus one online-shop search per market). Query-by-query receipts/timestamps are not retained uniformly in every batch, and some search outputs were clipped; treat the aggregate query count as operator-reported, not independently verified.
- One path mismatch was corrected during audit: batch 3 now points to `market-batch-3.md`. Two clipped outputs in batch 12 and other per-batch limitations remain recorded; no clipped result was retried or inferred.

## Aggregate dispositions

| Disposition | Markets |
|---|---:|
| `BLOCKED_COUNTRY_COMPATIBILITY` | 6 |
| `NEEDS_CATALOG_APPROVAL` | 29 |
| `NEW_ROTATING_CANDIDATE` | 1 |
| `SKIPPED_BLOCKED` | 31 |
| `SKIPPED_NO_VERIFIABLE_SOURCES` | 28 |
| `SKIPPED_UNAVAILABLE` | 17 |
| `SKIPPED_UNVERIFIED` | 62 |

- Origins: `34` prior-run decisions; `140` continuation decisions.
- Newly discovered candidates requiring separate Owner catalog approval: 29 markets (`PL, ZA, CZ, DZ, LT, LV, EE, ML, LB, AM, GN, GY, KG, MG, MK, PS, BN, TJ, GQ, MC, MR, ME, KY, FJ, SZ, LR, AW, DJ, AD`). One prior candidate is rotating and requires period/expiry review. None was registered.
- No market is marked `verified_official_catalog=true`; no new-market catalog was added; no product price/image from the market-discovery batch was accepted for production.

## Per-market checkpoint

| Rank | Country | Decision source | Final disposition | Receipt/checkpoint |
|---:|---|---|---|---|
| 1 | `US` United States | `original_run` | `SKIPPED_BLOCKED` | `prior run: frozen register; source commit 8b466c4` |
| 2 | `DE` Germany | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 3 | `IT` Italy | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 4 | `ES` Spain | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 5 | `ID` Indonesia | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 6 | `TR` Turkey | `original_run` | `SKIPPED_BLOCKED` | `prior run: frozen register; source commit 8b466c4` |
| 7 | `CH` Switzerland | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 8 | `PL` Poland | `original_run` | `NEEDS_CATALOG_APPROVAL` | `prior run: frozen register; source commit 8b466c4` |
| 9 | `AE` United Arab Emirates | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 10 | `MY` Malaysia | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 11 | `CO` Colombia | `original_run` | `SKIPPED_UNAVAILABLE` | `prior run: frozen register; source commit 8b466c4` |
| 12 | `ZA` South Africa | `original_run` | `NEEDS_CATALOG_APPROVAL` | `prior run: frozen register; source commit 8b466c4` |
| 13 | `EG` Egypt | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 14 | `RO` Romania | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 15 | `CL` Chile | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 16 | `PT` Portugal | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 17 | `PE` Peru | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 18 | `IQ` Iraq | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 19 | `EC` Ecuador | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 20 | `RS` Serbia | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 21 | `MM` Myanmar | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 22 | `PY` Paraguay | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 23 | `NA` Namibia | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 24 | `PF` French Polynesia | `original_run` | `SKIPPED_UNVERIFIED` | `prior run: frozen register; source commit 8b466c4` |
| 25 | `CN` China | `original_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `prior run: frozen register; source commit 8b466c4` |
| 26 | `JP` Japan | `original_run` | `NEW_ROTATING_CANDIDATE` | `prior run: frozen register; source commit 8b466c4` |
| 27 | `IN` India | `original_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `prior run: frozen register; source commit 8b466c4` |
| 28 | `GB` United Kingdom | `original_run` | `SKIPPED_BLOCKED` | `prior run: frozen register; source commit 8b466c4` |
| 29 | `FR` France | `original_run` | `SKIPPED_BLOCKED` | `prior run: frozen register; source commit 8b466c4` |
| 30 | `CA` Canada | `original_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `prior run: frozen register; source commit 8b466c4` |
| 31 | `RU` Russia | `original_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `prior run: frozen register; source commit 8b466c4` |
| 32 | `BR` Brazil | `original_run` | `SKIPPED_BLOCKED` | `prior run: frozen register; source commit 8b466c4` |
| 33 | `KR` South Korea | `original_run` | `SKIPPED_BLOCKED` | `prior run: frozen register; source commit 8b466c4` |
| 34 | `MX` Mexico | `original_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `prior run: frozen register; source commit 8b466c4` |
| 35 | `AU` Australia | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-1.json` |
| 36 | `SA` Saudi Arabia | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-1.json` |
| 37 | `NL` The Netherlands | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-1.json` |
| 38 | `BE` Belgium | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-1.json` |
| 39 | `AR` Argentina | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-1.json` |
| 40 | `IE` Ireland | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-1.json` |
| 41 | `SE` Sweden | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-1.json` |
| 42 | `SG` Singapore | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-1.json` |
| 43 | `IL` Israel | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-1.json` |
| 44 | `AT` Austria | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-1.json` |
| 45 | `TH` Thailand | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-2.md` |
| 46 | `NO` Norway | `continuation_run` | `SKIPPED_UNVERIFIED` | `market-batch-3.md` |
| 47 | `VN` Vietnam | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-2.md` |
| 48 | `IR` Iran | `continuation_run` | `SKIPPED_UNVERIFIED` | `market-batch-3.md` |
| 49 | `PH` Philippines | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-2.md` |
| 50 | `BD` Bangladesh | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-2.md` |
| 51 | `DK` Denmark | `continuation_run` | `SKIPPED_UNVERIFIED` | `market-batch-3.md` |
| 52 | `HK` Hong Kong | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-2.md` |
| 53 | `PK` Pakistan | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-2.md` |
| 54 | `CZ` Czechia | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-2.md` |
| 55 | `FI` Finland | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-2.md` |
| 56 | `KZ` Kazakhstan | `continuation_run` | `SKIPPED_BLOCKED` | `market-batch-3.md` |
| 57 | `DZ` Algeria | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `market-batch-3.md` |
| 58 | `NZ` New Zealand | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-2.md` |
| 59 | `GR` Greece | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-2.md` |
| 60 | `NG` Nigeria | `continuation_run` | `SKIPPED_UNVERIFIED` | `market-batch-3.md` |
| 61 | `HU` Hungary | `continuation_run` | `SKIPPED_UNAVAILABLE` | `market-batch-3.md` |
| 62 | `QA` Qatar | `continuation_run` | `SKIPPED_UNAVAILABLE` | `market-batch-3.md` |
| 63 | `UA` Ukraine | `continuation_run` | `SKIPPED_UNVERIFIED` | `market-batch-3.md` |
| 64 | `KW` Kuwait | `continuation_run` | `SKIPPED_BLOCKED` | `market-batch-3.md` |
| 65 | `MA` Morocco | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-4.json` |
| 66 | `ET` Ethiopia | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-4.json` |
| 67 | `SK` Slovakia | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-4.json` |
| 68 | `PR` Puerto Rico | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-4.json` |
| 69 | `DO` Dominican Republic | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-4.json` |
| 70 | `UZ` Uzbekistan | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-4.json` |
| 71 | `VE` Venezuela | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-4.json` |
| 72 | `KE` Kenya | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-4.json` |
| 73 | `BG` Bulgaria | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-4.json` |
| 74 | `GT` Guatemala | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-4.json` |
| 75 | `OM` Oman | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-5.json` |
| 76 | `AO` Angola | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-5.json` |
| 77 | `LK` Sri Lanka | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-5.json` |
| 78 | `CR` Costa Rica | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-5.json` |
| 79 | `LU` Luxembourg | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-5.json` |
| 80 | `HR` Croatia | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-5.json` |
| 81 | `CI` Ivory Coast | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-5.json` |
| 82 | `PA` Panama | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-5.json` |
| 83 | `LT` Lithuania | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-5.json` |
| 84 | `GH` Ghana | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-5.json` |
| 85 | `UY` Uruguay | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-6.json` |
| 86 | `TZ` Tanzania | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-6.json` |
| 87 | `BY` Belarus | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-6.json` |
| 88 | `CD` Democratic Republic of the Congo | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-6.json` |
| 89 | `AZ` Azerbaijan | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-6.json` |
| 90 | `SI` Slovenia | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-6.json` |
| 91 | `JO` Jordan | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-6.json` |
| 92 | `BO` Bolivia | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-6.json` |
| 93 | `UG` Uganda | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-6.json` |
| 94 | `CM` Cameroon | `continuation_run` | `SKIPPED_UNVERIFIED` | `discovery-batch-6.json` |
| 95 | `TN` Tunisia | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-7.json` |
| 96 | `SD` Sudan | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-7.json` |
| 97 | `MO` Macao | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-7.json` |
| 98 | `LY` Libya | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-7.json` |
| 99 | `BH` Bahrain | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-7.json` |
| 100 | `KH` Cambodia | `continuation_run` | `BLOCKED_COUNTRY_COMPATIBILITY` | `discovery-batch-7.json` |
| 101 | `TM` Turkmenistan | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-7.json` |
| 102 | `LV` Latvia | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-7.json` |
| 103 | `NP` Nepal | `continuation_run` | `BLOCKED_COUNTRY_COMPATIBILITY` | `discovery-batch-7.json` |
| 104 | `EE` Estonia | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-7.json` |
| 105 | `ZW` Zimbabwe | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-8.json` |
| 106 | `CY` Cyprus | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-8.json` |
| 107 | `HN` Honduras | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-8.json` |
| 108 | `SV` El Salvador | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-8.json` |
| 109 | `GE` Georgia | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-8.json` |
| 110 | `IS` Iceland | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-8.json` |
| 111 | `SN` Senegal | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-8.json` |
| 112 | `PG` Papua New Guinea | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-8.json` |
| 113 | `BA` Bosnia and Herzegovina | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-8.json` |
| 114 | `AL` Albania | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-8.json` |
| 115 | `ML` Mali | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-9.json` |
| 116 | `LB` Lebanon | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-9.json` |
| 117 | `AM` Armenia | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-9.json` |
| 118 | `TT` Trinidad and Tobago | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-9.json` |
| 119 | `ZM` Zambia | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-9.json` |
| 120 | `MT` Malta | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-9.json` |
| 121 | `GN` Guinea | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-9.json` |
| 122 | `GY` Guyana | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-9.json` |
| 123 | `HT` Haiti | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-9.json` |
| 124 | `MN` Mongolia | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-9.json` |
| 125 | `BF` Burkina Faso | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-10.json` |
| 126 | `MZ` Mozambique | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-10.json` |
| 127 | `JM` Jamaica | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-10.json` |
| 128 | `BJ` Benin | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-10.json` |
| 129 | `GA` Gabon | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-10.json` |
| 130 | `TD` Chad | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-10.json` |
| 131 | `NE` Niger | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-10.json` |
| 132 | `NI` Nicaragua | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-10.json` |
| 133 | `BW` Botswana | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-10.json` |
| 134 | `MD` Moldova | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-10.json` |
| 135 | `KG` Kyrgyzstan | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-11.json` |
| 136 | `AF` Afghanistan | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-11.json` |
| 137 | `MG` Madagascar | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-11.json` |
| 138 | `MK` North Macedonia | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-11.json` |
| 139 | `LA` Laos | `continuation_run` | `BLOCKED_COUNTRY_COMPATIBILITY` | `discovery-batch-11.json` |
| 140 | `PS` Palestinian Territory | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-11.json` |
| 141 | `BS` Bahamas | `continuation_run` | `BLOCKED_COUNTRY_COMPATIBILITY` | `discovery-batch-11.json` |
| 142 | `CG` Republic of the Congo | `continuation_run` | `BLOCKED_COUNTRY_COMPATIBILITY` | `discovery-batch-11.json` |
| 143 | `BN` Brunei | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-11.json` |
| 144 | `RW` Rwanda | `continuation_run` | `BLOCKED_COUNTRY_COMPATIBILITY` | `discovery-batch-11.json` |
| 145 | `MU` Mauritius | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-14.json` |
| 146 | `TJ` Tajikistan | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-14.json` |
| 147 | `GQ` Equatorial Guinea | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-13.json` |
| 148 | `SO` Somalia | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-14.json` |
| 149 | `MW` Malawi | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-14.json` |
| 150 | `MC` Monaco | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-13.json` |
| 151 | `MR` Mauritania | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-13.json` |
| 152 | `TG` Togo | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-14.json` |
| 153 | `BM` Bermuda | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-12.json` |
| 154 | `LI` Liechtenstein | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-13.json` |
| 155 | `NC` New Caledonia | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-14.json` |
| 156 | `ME` Montenegro | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-13.json` |
| 157 | `KY` Cayman Islands | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-13.json` |
| 158 | `BB` Barbados | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-12.json` |
| 159 | `MV` Maldives | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-14.json` |
| 160 | `SL` Sierra Leone | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-14.json` |
| 161 | `FJ` Fiji | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-13.json` |
| 162 | `SZ` Eswatini | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-14.json` |
| 163 | `LR` Liberia | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-13.json` |
| 164 | `SR` Suriname | `continuation_run` | `SKIPPED_UNAVAILABLE` | `discovery-batch-14.json` |
| 165 | `AW` Aruba | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-12.json` |
| 166 | `DJ` Djibouti | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-13.json` |
| 167 | `FO` Faroe Islands | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-13.json` |
| 168 | `AD` Andorra | `continuation_run` | `NEEDS_CATALOG_APPROVAL` | `discovery-batch-12.json` |
| 169 | `CW` Curacao | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-12.json` |
| 170 | `BT` Bhutan | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-12.json` |
| 171 | `BZ` Belize | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-12.json` |
| 172 | `BI` Burundi | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-12.json` |
| 173 | `CF` Central African Republic | `continuation_run` | `SKIPPED_BLOCKED` | `discovery-batch-12.json` |
| 174 | `CV` Cabo Verde | `continuation_run` | `SKIPPED_NO_VERIFIABLE_SOURCES` | `discovery-batch-12.json` |

## Separate registered-catalog coverage

- Original run evidence lists 74 registered work units and 74 terminal rows at its original baseline. This is historical receipt coverage, not 74 successfully verified catalogs.
- Current `main` baseline has 71 active Catalog Promo records across 24 countries. This recovery did **not** rerun all 71 records; only `lidl-rs-country` was reverified and had `last_verified_at` refreshed. Do not claim the current manifest was fully crawled.
- Current one-off recovery did not create any retailer/country registration and did not change catalog URLs. The 29 candidates remain audit-only.

## Research and publication limits

- Six markets were blocked by country compatibility; 31 source/legal/access blocked; 28 had no verifiable source; 17 unavailable; 62 unverified; 29 await catalog registration review; one rotating candidate still needs a sourced period/expiry decision.
- The original run had separate recorded access/provenance incidents (including Pick n Pay outside its stated visit window and Taawon access after a disallow check); they remain for independent auditor review.
- The continuation is a user-directed resumption despite Issue #57 previously saying no second cycle. This scope change is disclosed for independent audit; no schedule, cron, automatic repeat, merge or deployment was authorized.
