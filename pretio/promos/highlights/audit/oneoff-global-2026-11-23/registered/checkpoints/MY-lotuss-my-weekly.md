# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `MY:lotuss-my-weekly` | manifest position: **43/74** | attempt: **1**  
Country: **MY** | retailer: **Lotus's Malaysia** | mode: **AUDIT**  
Registered URL: <https://corp.lotuss.com.my/for-you/catalogue-promotions/weekly>  
Checked UTC: **2026-11-23T09:53:22Z** (robots response `Date` header; no offer page request was made)  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_BLOCKED**

## 1. Catalog Promo source

- [x] Loaded the exact frozen manifest record and local catalog record: `lotuss-my-weekly`, Lotus's Malaysia, active `official_retailer`, national label, URL above, `valid_until: null`, `last_verified_at: 2026-10-21T10:21:02+08:00`.
- [ ] Reverification of merchant page, redirect/canonical behavior, current catalogue, evergreen freshness, promotional period, and market applicability was not attempted after access policy was identified.
- [x] The web search/open connector could not access the exact robots URL. A single plain HTTPS request to `https://corp.lotuss.com.my/robots.txt` returned `200 OK`, `text/plain`, 542 bytes, server date `Mon, 23 Nov 2026 09:53:22 GMT`, `Last-Modified: Tue, 08 Sep 2026 07:48:12 GMT`.
- [x] The retrieved robots file explicitly says `User-agent: GPTBot` / `Disallow: /` and `User-agent: ChatGPT-User` / `Disallow: /`. It also disallows all paths for multiple other named AI crawlers. Because this task is performed by ChatGPT, the registered promo page and linked terms were not opened after this directive was found. No alternate user-agent, alternate endpoint, or access-control bypass was used.
- [ ] No terms page or promo content was opened; commercial reuse permission, page ownership, redirect chain, and current catalog state remain unverified for this attempt.
- [x] Existing `valid_until` is null; an old `last_verified_at` and a robots block are not proof of expiry or obsolescence. Keep the active entry unchanged and classify the current state `STALE_UNVERIFIED`.
- [x] No production catalog, source timestamp, highlight feed/index, currency metadata, or location file changed.

## 2. Product Highlights

- [x] The MY catalog page was not accessed; zero offers/products were inspected. No product, normal/promo price pair, image, offer period, or item-level geography was collected.
- [x] Local cross-feed reference scan found **zero** active highlight references to `lotuss-my-weekly`.
- [x] Malaysia has no Product Highlights currency mapping in `pretio/data/currency.json`; this independently prevents publication, but no products were found.
- [x] No offer expiry was evidenced; nothing was deleted and no catalog retirement/migration was proposed.

## 3. Skip decision and compact handoff (≤400 words)

Work unit `MY:lotuss-my-weekly`, position 43/74; terminal receipt `SKIPPED_BLOCKED`. The local active Catalog Promo record points to `https://corp.lotuss.com.my/for-you/catalogue-promotions/weekly`, is national-labeled and has no `valid_until`; its existing `last_verified_at` is `2026-10-21T10:21:02+08:00`. A single plain HTTPS request to the official host's robots file returned 200 text/plain at `2026-11-23T09:53:22Z`; it explicitly disallows `/` for both `GPTBot` and `ChatGPT-User`. After reading that restriction, I did not open the catalogue page, terms, or linked content and did not use another user-agent or route. Current promotion, expiry, ownership and permissions therefore remain unverified; retain the catalog and treat it as `STALE_UNVERIFIED`, not expired. No prices/products were inspected, no highlight references exist, and MY lacks currency metadata for highlight publication. No production data changed. Continue with the next source `NA:agra-na-country` in a fresh source context.
