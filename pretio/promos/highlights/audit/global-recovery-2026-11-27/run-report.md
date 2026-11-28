# Superseded candidate delta — Owner location correction

The historical operator report below is preserved. Its 105→73 / 32 removals candidate is superseded by [owner-location-policy-reconciliation.json](owner-location-policy-reconciliation.json): 27 geographic-only removals withdrawn, 105→100 candidate, 5 remaining proposed non-geographic removals, 0 new products. No fresh source verification or legacy regional display fix is claimed. HOLD remains; see PR #74 and maxqstudio/pretio#111.

---

# Pretio global recovery report — 2026-11-27

**Run:** `pretio-global-recovery-20261127T0434Z`
**Scope:** `ONE_OFF_GLOBAL`, manually resumed after the Owner's later instruction to continue.
**Base SHA:** `65bc23a54515c138d23e0e1465b9317a4bbc29d0`
**Skill Git blob SHA:** `2f46a28da390388eb34c316d5dbf45ad27ac264a`
**Status:** `INCOMPLETE — no new Product Highlight qualified; independent audit required before any merge.`

## Scope and result

Issue #57 previously recorded `NO SECOND CYCLE`. This recovery continued the 140 pending market decisions after a later explicit Owner instruction. The scope conflict is disclosed for the independent auditor; this report does not reinterpret the original authorization silently. No scheduler, cron, automatic repeat or deployment was created. No merge was performed.

The 140 pending markets now have terminal dispositions in 14 bounded batches. Together with the original 34, the register has 174/174 **decisions**, not 174 verified sources. It records zero verified new-market official catalogs and zero verified new-market Product Highlights. The aggregate 280-search count is operator-reported; per-query receipts/timestamps are incomplete in some batches and clipped outputs are recorded as such. See [global-discovery-checklist.md](global-discovery-checklist.md).

The current-main catalog snapshot contains 71 active catalogs across 24 countries; this recovery did not re-crawl that entire 71-item manifest. The historical 23 Nov run had 74/74 terminal receipts at its then-current manifest. In this recovery, one existing catalog (`lidl-rs-country`) was reverified at its permanent official hub URL; its URL/period fields were not changed, and only `last_verified_at` plus the catalog revision were refreshed.

## Production data delta staged

| Dataset | Before | After | Delta |
|---|---:|---:|---:|
| Catalog Promo entries / countries | 71 / 24 | 71 / 24 | no add/remove; 1 existing source verification timestamp refreshed |
| Product Highlights | 105 / 7 countries | 73 / 7 countries | 32 removed; 0 added; 0 price updates |
| Confirmed expired products removed | — | 0 | No item was removed as expired |
| Orphan catalog references / duplicate IDs | — | 0 / 0 | Strict validator PASS on candidate snapshot |

Country counts after staging: ID `0` (−4), CL `21` (−3), DE `16` (−17), RS `17` (−8), US `12` (0), ZA `2` (0), CH `5` (0). Forty-six remaining highlights have no verified end date; they were not deleted as expired because undated or unreachable does not prove expiry. They must not be described as freshly verified.

The 32 removals are policy/scope corrections, not expiry pruning: CL Jumbo 3 (commune-limited online fulfillment not proven nationwide); DE ALDI Nord/Süd 16 (separate regional footprints cannot fit a nationwide feed) plus 1 Lidl Bosch item whose normal price was labeled UVP; ID LOTTE MART 4 (official terms do not authorize commercial reuse); RS Maxi 8 (delivery scope was city-limited). Exact IDs and source evidence are in `deletion-reconciliation.json` and per-country audit files. No catalog was removed; no Product Highlight references a removed catalog.

All seven supported highlight countries missed the target of one **new** verified discount: `0/1` in ID, CL, DE, RS, US, ZA and CH. Product Highlights remain discount-only. Jumbo Chile price observations are audit-only due geography; no CL item was published.

## Source-policy and access decisions

- Walmart US: official current Terms of Use prohibit commercial use and automated/manual-agent collection or incorporation of site materials without prior written consent. Earlier candidate discovery/product access occurred before the terms were recognized; access was stopped, no product/image payload was retained for production, and no further product or image requests were made. See `US-walmart-source-policy-block.json` and the [official terms](https://www.walmart.com/help/article/walmart-com-terms-of-use/3b75080af40340d6bbd596f116fae5a0/).
- Lidl Germany: the Slushie Maker page exposed EUR 179.00 “vorher” and EUR 129.00 Black Week price, with a matching decoded image and Germany-only order terms. The bounded official-site terms review found no explicit image/content reuse permission and also no express prohibition. The candidate remains audit-only; see `DE-lidl-slushie-policy-review.json`, the [product page](https://www.lidl.de/p/silvercrest-premium-slushie-maker-ssm-220-a1/p100412188), and [official online-shop terms](https://www.lidl.de/c/allgemeine-geschaeftsbedingungen-onlineshop/s10005181).
- Current ALDI Suisse item had no verified normal-price comparator; no highlight was created. Lidl Serbia's current rotating flyer was unreadable, so no period item was extracted; the permanent official hub itself was verified.
- The prior Pick n Pay and Taawon access-policy incidents and historical query-provenance gaps still need independent auditor classification. CI does not resolve those findings.

## Integrity, tests and release gate

- Production schema remains unchanged. Strict validator and catalog URL-change baseline check: **PASS** (`--as-of 2026-11-27 --strict-expiry --baseline-catalog`); 73 items, 0 expired, 0 warnings. Exact index hashes, catalog foreign keys, prices, dates and caps pass.
- Python unit tests: **PASS 27/27** on Python 3.12.10 using a temporary `tzdata` package outside the repo. Website security tests: **PASS 6/6**. `node --check pretio/catalog/catalog.js`: **PASS**. `git diff --check`: **PASS**.
- Local catalog browser smoke did not run because this Windows environment denied binding its test server to `127.0.0.1:8765` (`WinError 10013`). GitHub browser CI is required on the final Draft PR head.
- Existing GitHub main CI was successful at base `65bc23a54515c138d23e0e1465b9317a4bbc29d0` (security, Pretio skill/schema, catalog browser, Pages). This is baseline evidence only, not PR-head evidence. Draft PR checks are pending.
- `PR #60` is already merged at `2fbed8896cf175383c445439ebeacabb0c442055`. This recovery will use a separate Draft PR. It must remain Draft/HOLD until an independent auditor reviews its latest SHA and posts `PASS / READY FOR OWNER REVIEW`; Owner approval remains separate. No auto-merge.

## Handoff

1. Independently review the final Draft PR SHA and every deletion/product evidence record. Review all 46 undated items as stale/unverified; do not claim they are current or expired without evidence.
2. Reconcile the original 74 receipts and the current 71-record manifest as separate snapshots. Audit the corrected batch-3 pointer and the missing per-query receipts/timestamps/clipped outputs.
3. Review the disclosed authorization scope change and Walmart's prior access incident; do not revisit Walmart without written permission.
4. Confirm exact validators/CI and issue checkpoint before any Owner merge decision. No further crawl or scheduled work is implicit in this report.
