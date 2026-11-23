# One-off global market selection

- Run: `pretio-oneoff-global-20261123T040625Z`
- Baseline: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`
- Candidate universe: 249 codes from `pretio/location/v2/index.json`.
- Registered catalog baseline: 74 records across 24 countries from `pretio/promos/catalog_app.json`.
- Target: 174 markets, including every registered catalog country.

## Selection rule

The one-off sample includes all 24 countries that already have registered catalogs, then the 150 highest-ranking remaining registry countries by the World Bank's 2024 current-USD GDP indicator (`NY.GDP.MKTP.CD`). GDP is only a deterministic commercial-market prioritization proxy; it does not establish that a catalog, retailer, discount, or online shop exists. World Bank aggregate regions are excluded because their codes do not match a country/territory entry in Pretio's registry. Registered markets without a World Bank 2024 GDP observation remain included because their existing source IDs are in scope.

The raw API response is saved as `worldbank-gdp-2024.json`; the reproducible selection transform is `build-market-register.py`; the resulting 249-row selection and disposition file is `country-discovery-register.json`. The 75 unselected registry entries are `OUT_OF_SCOPE_BY_MARKET_RANK`, **not** `SKIPPED_NO_VERIFIABLE_SOURCES`; no claim is made that they lack commerce or official sources.

## Bounded research budget

For each selected market, the research budget is one query for official Catalog Promo/promotions sources and one separate query for online shops or marketplace seller storefronts. At most one official lead from each query is opened for initial qualification; deeper product checks are limited to offers visible on that official source. Search results are discovery leads only. A market is counted as researched after an official page is opened and source ownership, market applicability, permitted access, and current promo content are checked. A search result alone does not count as verified coverage.

All registered catalog work units are separately counted in `registered-manifest.json`; country research never changes that denominator. Requests use public pages only, finite timeouts, at most two transient retries, and no CAPTCHA, login, hidden API, proxy, or access-control bypass. New sellers and hosts remain audit-only pending separate Owner approval.

## Run accounting

The 174 selected market rows begin as `PENDING_RESEARCH`. The 75 unselected entries remain explicitly unresearched in this run. Each selected row will be changed only after the corresponding source research outcome is recorded in its country checkpoint. A verified official catalog requires an opened page with evidence of live promotional content; HTTP 200 or an official-looking search snippet is insufficient.
