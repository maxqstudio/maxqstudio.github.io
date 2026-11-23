# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `MY:aeon-my-promotions` | manifest position: **42/74** | attempt: **1**  
Country: **MY** | retailer: **AEON** | mode: **AUDIT**  
Checked UTC: **2026-11-23**; the web connector did not expose exact request timestamps. Checkpoint recorded at **2026-11-23T09:51:17Z**.  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Candidate branch head at start of this source attempt: **4002a9b750ca11c321c02838c434be7362230fcb**  
Terminal status: **SKIPPED_UNVERIFIED**

## 1. Catalog Promo source

- [x] Loaded the frozen manifest work unit and current active record: catalog ID `aeon-my-promotions`, AEON Malaysia, official retailer, national label, Malaysia country location, registered URL <https://aeonretail.com.my/promotion/>, and `valid_until: null`. Existing `last_verified_at` is `2026-10-24T19:59:47+08:00`.
- [x] Official homepage <https://aeonretail.com.my/> identifies AEON Retail Malaysia, has a direct navigation link labeled `Promotion` to the same registered URL, and footer copyright identifies AEON CO. (M) BHD. The homepage was the only business page opened; the registered promotion page was not opened.
- [x] Attempted the official robots URL <https://aeonretail.com.my/robots.txt>. The web connector reported the URL was not accessible through its open tool. A normal `curl.exe` HTTPS request failed certificate-chain validation with Windows `SEC_E_UNTRUSTED_ROOT`; PowerShell's standard HTTPS request also failed TLS certificate validation. No certificate-validation bypass was used, and no robots rules could be verified.
- [x] Followed the homepage's `Terms & Conditions` navigation link. Its destination is <https://aeongroupmalaysia.com/personal-privacy-data-notice/> and the opened page is a personal-data privacy notice, not a site content license or crawler-use policy. No express permission for commercial retention/reuse of promotional content was found.
- [x] Because robots access rules and commercial content-reuse permission remain unverified, stopped before opening the registered promotion page or retaining promo/product information. No retry with weakened TLS, alternate identity, proxy, hidden endpoint, login, or other bypass was used.
- [ ] The registered promotion page's response, redirects, canonical behavior, actual in-place updates, current promo content, period dates, and countrywide item applicability were not verified. The path is a permanent-looking `/promotion/` URL, but URL shape alone does not prove evergreen freshness. Classify this attempt as `STALE_UNVERIFIED`; do not infer expiration or obsolescence from `valid_until: null` or the prior verification timestamp.
- [x] No production catalog fields, URLs, timestamps, highlights, index, currency, location registry, or schema were changed.

## 2. Product Highlights

- [x] The promotion page was not opened, so **0 products were inspected**, **0 offers accepted/rejected**, and no normal/promo price pair, item image, validity date, or geographic applicability was retained.
- [x] Malaysia (`MY`) has no currency mapping in `pretio/data/currency.json` and no country entry in `pretio/promos/highlights/index.json`; any new highlight would be blocked from publication under the current contract regardless.
- [x] A scan of all existing highlight feed files found **0** references to `catalog_id: aeon-my-promotions`; no dependent offer is present to remove or migrate.

## 3. Skip decision

- [x] **SKIPPED_UNVERIFIED** — homepage identity and navigation link were verified, but robots rules could not be fetched with a trusted TLS connection and the linked legal page provided only a privacy notice, not content-reuse permission. Stopped before the promo page.
- [x] No source evidence proves the catalog expired or became obsolete; keep the active catalog entry unchanged as stale/unverified for this attempt.
- [x] No product, price, or image evidence was collected; no highlight/catalog production data was changed.

## Compact handoff

Work unit `MY:aeon-my-promotions`, position 42/74; receipt `SKIPPED_UNVERIFIED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`. The frozen active record is AEON Malaysia at <https://aeonretail.com.my/promotion/> with `valid_until: null`. The official homepage identifies AEON Retail Malaysia, links to that promotion URL, and shows AEON CO. (M) BHD. copyright. The robots URL could not be opened by the web connector; normal HTTPS clients failed certificate validation, and no bypass was used. The homepage's `Terms & Conditions` link resolved to AEON Corporate's personal-data privacy notice, with no promotional-content reuse license or crawler permission. I stopped before opening the promotion page; no products/prices/images or current promo dates were inspected. Treat the source as `STALE_UNVERIFIED`, not expired; no production change or highlight reference exists. Malaysia has no highlight feed/currency mapping. Next source: `MY:lotuss-my-weekly` (43/74), in a fresh isolated context.
