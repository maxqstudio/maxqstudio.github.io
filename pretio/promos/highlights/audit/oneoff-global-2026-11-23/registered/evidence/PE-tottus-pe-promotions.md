# Access evidence — PE:Tottus

- Run: `pretio-oneoff-global-20261123T040625Z`
- Checked UTC: `2026-11-23T10:01:50Z`
- Work unit: `PE:tottus-pe-promotions` (manifest 48/74)
- Registered URL: <https://www.tottus.com.pe/tottus-pe/lista/CATG23097/Promociones>
- Access-policy URL: <https://www.tottus.com.pe/robots.txt>

The web open tool returned an internal inaccessible-page error for the robots URL. One standard HTTPS GET fallback was then made using `PretioCatalogAudit/1.0` with a 30-second timeout; it returned HTTP `403 Forbidden`. No response body or robots directives were available. No further retry or alternate route was attempted. Since the source access policy could not be established, the registered promotions page, terms page and product pages were not opened. No product or price content was collected.

The local frozen record identifies Tottus as the Peru retailer and marks the entry active, but this attempt did not independently verify the source page or present-day catalog contents. The local `last_verified_at` is not expiry proof. Peru has no supported Product Highlights currency/feed entry, and a scan of existing highlight feeds found no references to `tottus-pe-promotions`.
