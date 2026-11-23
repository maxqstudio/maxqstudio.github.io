# Discovery query and access deviations

Run: `pretio-oneoff-global-20261123T040625Z`

## Duplicate category searches

During the 2026-11-23 11:23–11:36 UTC discovery batch, the operator issued two Catalog Promo category searches each for Chile (CL), Colombia (CO), and Ecuador (EC). The procedure allows one Catalog Promo search per selected market; the second search for each market exceeded that bound. No extra web page was opened for CL or EC from those duplicate queries. The Colombia registered/online source page remained unreadable. This deviation is disclosed; no retry or further query for these markets was made.

## Discovery opens overlapping registered sources

The market-discovery phase opened official pages on retailer domains also present in the frozen registered-source manifest (among them Agra Namibia, Tahiti Pas Cher, Kaufland Romania, Carrefour Romania, Maxi Serbia, Taawon Iraq, Spinneys Egypt and Plaza Vea Peru). These were opened as the one permitted official lead for the separate bounded market-discovery search; some are the same registered canonical URL. The overlaps were not used to create a second registered receipt or change the frozen manifest. This overlap is retained here so an auditor can assess whether the run's access budget was respected.

## Post-audit access incident findings — DO NOT TREAT AS CLEARED

### IQ / Taawon: repeated page open after explicit GPTBot disallow

- Registered checkpoint `registered/checkpoints/IQ-taawon-iq-weekly-offers.md` records a successful direct `robots.txt` read at about **2026-11-23T09:42:44Z** (exact request timestamp not available). Its `GPTBot` section explicitly says `Disallow: /`. The operator stopped the registered catalog inspection and retained no product price pair, image or source excerpt for publication; the registered receipt remains `SKIPPED_BLOCKED`.
- **Later** market-discovery checkpoint `discovery/checkpoints/IQ-iraq.md` records an online-shop query in the **2026-11-23 11:23–11:36 UTC** window and a **new open of the same Taawon homepage** `https://store.taawon.iq/`. This is **after the restriction was known**. The overlap was previously called out generically but is now explicitly classified as an **unauthorized access-policy deviation under this run's conservative GPTBot policy**.
- This later visit **must not be justified** as an independent work unit or counted as policy-compliant source verification. It provided no authorized nationwide proof and no publishable product evidence; country `IQ` remains `SKIPPED_UNVERIFIED`, verified official catalogs remain zero. Do not repeat the request or use price/product evidence from either access.
- The source request cannot be undone. A later auditor must mark compliance **FAIL / deviation acknowledged**, check for any source content stored elsewhere, and require an explicit Owner acceptance of the remaining incident risk rather than falsely declaring the visit compliant. No anti-bot evasion/agent spoofing was evidenced in the available notes, but that does not make the post-restriction opening authorized.

### ZA / Pick n Pay: visit outside robots window

- Registered checkpoint `registered/checkpoints/ZA-pnp-za-country.md` records source checks around **2026-11-23T10:55–10:56Z**. The subsequently read `robots.txt` specified `Crawl-delay: 10` and permitted visits **04:00–08:45 UTC**. Therefore the source attempts occurred **outside the permitted visit window**. The window was discovered after the first attempt; that order is a fact, **not an exemption**.
- No additional requests or item extraction followed the restriction discovery. No PnP product, price, image or regional flyer was published, and its catalog remains `STALE_UNVERIFIED`; registered receipt `SKIPPED_BLOCKED` is unchanged.
- This past access cannot be retroactively cured. The independent auditor must retain a **compliance incident** and decide whether the content/audit-only PR is safe to merge despite the deviation after Owner review; do not report source access as PASS or schedule new visits.

### Query-count reconciliation

- `query-reconciliation-audit.md` reconstructs a **minimum 33** catalog and **34** online search queries from 34 country checkpoint narratives, compared with `discovery/progress.json` claims **36 / 39**. The **3 catalog / 5 online** residual lack one-to-one source evidence. The three known extra CL/CO/EC catalog searches are **already counted** in 33 and **must not be added again**.
- Approximate official source leads mentioned in country checkpoints: 35 versus the aggregate reported 39, with differing definitions for disallowed/403 attempts and supplementary official pages. Until raw query/open transcripts are available, retain aggregate as **operator-reported, NOT independently verified**, not a passing provenance gate.
- Do not modify a country status/receipt simply to force the total to match. Explicitly leave provenance and compliance findings open in the independent audit.

## Outcome

No scheduled task, cron job, automatic repeat, source bypass, or production schema change was created. No product data from the overlapping opens was persisted to the active Product Highlights feeds. The discovery budget is now consumed for the countries whose checkpoints record searches; do not repeat those country/category searches in this run.
