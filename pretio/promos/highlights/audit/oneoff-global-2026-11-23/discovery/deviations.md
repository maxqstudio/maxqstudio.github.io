# Discovery query and access deviations

Run: `pretio-oneoff-global-20261123T040625Z`

## Duplicate category searches

During the 2026-11-23 11:23–11:36 UTC discovery batch, the operator issued two Catalog Promo category searches each for Chile (CL), Colombia (CO), and Ecuador (EC). The procedure allows one Catalog Promo search per selected market; the second search for each market exceeded that bound. No extra web page was opened for CL or EC from those duplicate queries. The Colombia registered/online source page remained unreadable. This deviation is disclosed; no retry or further query for these markets was made.

## Discovery opens overlapping registered sources

The market-discovery phase opened official pages on retailer domains also present in the frozen registered-source manifest (among them Agra Namibia, Tahiti Pas Cher, Kaufland Romania, Carrefour Romania, Maxi Serbia, Taawon Iraq, Spinneys Egypt and Plaza Vea Peru). These were opened as the one permitted official lead for the separate bounded market-discovery search; some are the same registered canonical URL. The overlaps were not used to create a second registered receipt or change the frozen manifest. This overlap is retained here so an auditor can assess whether the run's access budget was respected.

## Outcome

No scheduled task, cron job, automatic repeat, source bypass, or production schema change was created. No product data from the overlapping opens was persisted to the active Product Highlights feeds. The discovery budget is now consumed for the countries whose checkpoints record searches; do not repeat those country/category searches in this run.
