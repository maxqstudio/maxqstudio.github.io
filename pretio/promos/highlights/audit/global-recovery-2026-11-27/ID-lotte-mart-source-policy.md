# Indonesia source policy checkpoint — LOTTE MART

- **Run:** `pretio-global-recovery-20261127T0434Z`
- **Observed:** 2026-11-27 04:44:48 UTC
- **Baseline:** `65bc23a54515c138d23e0e1465b9317a4bbc29d0`
- **Source:** [official LOTTE MART promotions landing page](https://www.lottemart.co.id/all-promo-mart)
- **Access check:** `robots.txt` was retrieved directly with HTTP 200. The recorded rules disallow account/store routes only; the promotion/media and terms paths were not disallowed.
- **Terms evidence:** [official LOTTE MART terms](https://www.lottemart.co.id/syarat-dan-ketentuan), sections 8.1 and 8.3, state that site content (including images, campaign titles and data compilations) may be saved/displayed only for personal use, not commercial business use, and prohibit copying/downloading contrary to those terms. Commercial reuse permission for campaign text/data was not found.
- **Decision:** `SKIPPED_BLOCKED` for offer extraction/reuse. Four active LOTTE MART highlights were removed from the ID feed because their source-derived campaign data lacks verified commercial-use permission. This is a source-policy cleanup, **not an expiry determination**.
- **Catalog lifecycle:** The official permanent promotions landing page remains live and advertises current promotions. The evidence does not establish that the catalog is obsolete. Its catalog entry was left unchanged; permission to link/webview it remains a separate review question.
- **Data integrity:** No replacements or new products were added. The ID feed and its index entry/hash were recalculated together. See the matching run JSON receipt for the affected IDs.
- **Limit:** The terms are retailer-authored policy, not legal advice. No written permission request was made.
