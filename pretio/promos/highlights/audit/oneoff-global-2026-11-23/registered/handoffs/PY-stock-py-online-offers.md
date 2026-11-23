# Compact handoff — PY:stock-py-online-offers

- Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; work unit `55/74`, attempt `1`, terminal status `SKIPPED_BLOCKED`.
- The active catalog record identifies Supermercados Stock, `official_retailer`, URL `https://nuevo.stock.com.py/ofertas`, and national Paraguay (`PY`) coverage. Its host is already in `allowed_hosts`; the record’s last verification was `2026-11-15T05:42:54.476Z`.
- At `2026-11-23T10:17:11Z`, the only request was to `https://nuevo.stock.com.py/robots.txt`. It returned HTTP 403 `text/html`, no redirect, with nginx “403 Forbidden”; it provided no directives. Access permission for the catalog path and terms therefore remain unverified. I did not request the offers page or use retries, an alternate route, browser workaround, or search.
- Current promotions, period, ownership, item prices/images, and product-level Paraguay fulfillment/geography were not verified. No product was observed, so this is not a no-promotion finding. `PY` also has no currency entry in `pretio/data/currency.json`.
- No production JSON, feed/index, shared progress, or aggregate was changed. Checkpoint and terminal receipt are in this run’s `registered` folders. Next action: coordinator proceeds to the next assigned manifest unit.
