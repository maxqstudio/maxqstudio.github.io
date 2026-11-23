# Operator remediation — query provenance reconstruction (NO additional crawl)

**Run:** `pretio-oneoff-global-20261123T040625Z`  
**Evidence baseline:** PR #60 head `41161e0e27d8ba7cd6a14ece12ec7b05ea61dedb`.  
**Method:** Read only the existing 34 country discovery checkpoint narratives; counted explicit country-level search queries and official lead **attempt/open statements** per checkpoint. This is a **documentary lower-bound reconstruction, not raw search tool telemetry**. Exact per-query timestamps, provider request IDs and full unfiltered query logs were not preserved by the operator, so **nothing below independently authenticates the reported aggregate totals**.

## Checkpoint-level count ledger

| ISO | Catalog searches explicitly documented | Online searches explicitly documented | Official lead attempts/opens mentioned (approx., not authenticated) | Source country checkpoint |
|---|---:|---:|---:|---|
| AE | 1 | 1 | 1 | `checkpoints/AE-united-arab-emirates.md` |
| BR | 1 | 1 | 0 | `checkpoints/BR-brazil.md` |
| CA | 1 | 1 | 0 | `checkpoints/CA-canada.md` |
| CH | 0 | 1 | 1 | `checkpoints/CH-switzerland.md` |
| CL | 2 | 1 | 0 | `checkpoints/CL-chile.md` |
| CN | 1 | 1 | 1 | `checkpoints/CN-china.md` |
| CO | 2 | 1 | 1 | `checkpoints/CO-colombia.md` |
| DE | 1 | 1 | 1 | `checkpoints/DE-germany.md` |
| EC | 2 | 1 | 0 | `checkpoints/EC-ecuador.md` |
| EG | 1 | 1 | 1 | `checkpoints/EG-egypt.md` |
| ES | 1 | 1 | 2 | `checkpoints/ES-spain.md` |
| FR | 1 | 1 | 1 | `checkpoints/FR-france.md` |
| GB | 1 | 1 | 2 | `checkpoints/GB-united-kingdom.md` |
| ID | 0 | 1 | 0 | `checkpoints/ID-indonesia.md` |
| IN | 1 | 1 | 2 | `checkpoints/IN-india.md` |
| IQ | 1 | 1 | 1 | `checkpoints/IQ-iraq.md` |
| IT | 1 | 1 | 2 | `checkpoints/IT-italy.md` |
| JP | 1 | 1 | 2 | `checkpoints/JP-japan.md` |
| KR | 1 | 1 | 0 | `checkpoints/KR-south-korea.md` |
| MM | 1 | 1 | 1 | `checkpoints/MM-myanmar.md` |
| MX | 1 | 1 | 1 | `checkpoints/MX-mexico.md` |
| MY | 1 | 1 | 2 | `checkpoints/MY-malaysia.md` |
| NA | 1 | 1 | 1 | `checkpoints/NA-namibia.md` |
| PE | 1 | 1 | 1 | `checkpoints/PE-peru.md` |
| PF | 1 | 1 | 2 | `checkpoints/PF-french-polynesia.md` |
| PL | 0 | 1 | 1 | `checkpoints/PL-poland.md` |
| PT | 1 | 1 | 1 | `checkpoints/PT-portugal.md` |
| PY | 1 | 1 | 1 | `checkpoints/PY-paraguay.md` |
| RO | 1 | 1 | 2 | `checkpoints/RO-romania.md` |
| RS | 1 | 1 | 2 | `checkpoints/RS-serbia.md` |
| RU | 1 | 1 | 1 | `checkpoints/RU-russia.md` |
| TR | 0 | 1 | 0 | `checkpoints/TR-turkiye.md` |
| US | 1 | 1 | 0 | `checkpoints/US-united-states.md` |
| ZA | 1 | 1 | 1 | `checkpoints/ZA-south-africa.md` |
| **Narrative-subtotal** | **33** | **34** | **35** | 34 checkpoint files |
| **Run progress claims** | **36** | **39** | **39** | `progress.json` |
| **Not attributable from country checkpoint narratives alone** | **3** | **5** | **4** | **NOT VERIFIED** |

**Interpretation:** 34 terminal markets are accounted for, but the number of checkpoint-documented queries is lower than the aggregate fields. This does **not prove 8 searches did not occur**: supplemental notes, earlier stages or search-result records may exist outside the 34 checkpoint summaries. Conversely, those aggregate-only searches must NOT be upgraded to a verified ledger without matching evidence (query text, date/rough window, market/category, tool source or lead record, and deduplication).

### Known budget exceptions

- Chile (CL), Colombia (CO) and Ecuador (EC) each explicitly contain **two Catalog Promo queries instead of one**; these six searches (three over-budget) are already counted in the **33** narrative-subtotal, not added again.
- **CH, ID, PL, TR** record only an online-shop query in their discovery checkpoint. They may have had other searches outside those notes, but an auditor cannot infer one automatically just because the rule budget permitted it.
- The official lead attempt/open count is inherently ambiguous: some checkpoints describe a 403/disallowed source as an attempted open, and others omit ancillary/supplementary official pages. The separate run progress explanation for 39 opened leads is an **operator aggregate**, not a independently checked per-request log. At least four lead appearances lack one-to-one mapping in this reconstruction.
- Openings overlapping registered sources (Agra NA, Taawon IQ, etc.) must NOT be treated as new distinct retail sources or a second registered receipt. The Taawon post-robots re-open is an access deviation, **not a valid source-verification lead**.

### Required audit disposition

- **Registered manifest receipts:** remain 74/74, unchanged and unaffected by the above discovery ledger.
- **Country discovery:** remain 34/174 terminal, 140 pending, **zero verified catalogs**.
- **Search query provenance:** `NOT VERIFIED`; do **not** replace the declared `36/39/39` fields with guesses or silently assert these counts are audited.
- **Compliance:** CL/CO/EC exceeded query budget; Taawon and Pick n Pay require explicit incident decisions. No source or price data from disallowed access may be reused.
- **Resolution options without further website requests:** retrieve original saved tool/search transcripts if available and produce a linkable per-query log, or explicitly retain the residual difference as an unresolved evidence gap. The latter **cannot be described as PASS**.
- This note contains **no source re-crawl, no post hoc fabricated timestamps, and no change to any canonical registered receipt, country disposition, or production dataset**. Require independent auditor re-review on the eventual final SHA; existing `HOLD MERGE` stays in force.

## ZA status clarification

`ZA` country register and progress show final `NEEDS_CATALOG_APPROVAL` because the later official Newton Park SPAR **local** promo-leaflet lead was discovered. The earlier online-query `SKIPPED_UNVERIFIED` status shown in the checkpoint/handoff is **provisional/superseded**; neither implies a nationwide approved catalog or an eligible Product Highlight. See updated ZA checkpoint and handoff.

## Iraq Taawon + Pick n Pay access

Details are in `deviations.md`. The IQ discovery opening after a registered-source robot restriction cannot be considered policy-compliant merely because no products were retained. PnP direct source request outside its robot-specified window likewise remains a real access violation. Both are documented for independent review, not retroactively excused.
