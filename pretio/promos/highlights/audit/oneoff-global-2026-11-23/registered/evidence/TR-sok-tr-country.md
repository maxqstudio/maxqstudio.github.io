# Evidence — TR:sok-tr-country

- Run: `pretio-oneoff-global-20261123T040625Z`; scope `ONE_OFF_GLOBAL`; manifest position `68/74`; attempt `1`; baseline/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Registered record: ŞOK / ŞOK Marketler, `official_retailer`, country location `TR` / Türkiye, national label, `valid_until: null`, `last_verified_at: 2026-09-28T00:00:00Z`. Catalog ID `sok-tr-country`; host `kurumsal.sokmarket.com.tr` is allowlisted. No `TR` currency metadata or `TR.json` Product Highlights feed exists. The repository skill files match the supplied baseline commit.

## Bounded official-source check

- Robots request: `GET https://kurumsal.sokmarket.com.tr/robots.txt`, started `2026-11-23T10:41:28Z`; HTTP 200, `text/plain; charset=utf-8`, 231 bytes, final URL unchanged. `User-agent: *` has `Allow: /`; exclusions cover `/admin/`, `/api/`, search paths and search-query patterns. Neither the registered path nor observed canonical path matches an exclusion. Robots is not evidence of Terms permission.
- One registered-page request: `GET https://kurumsal.sokmarket.com.tr/firsatlar/haftanin-firsatlari`, started `2026-11-23T10:42:14Z`; HTTP 200, `text/html; charset=utf-8`, 109,711 bytes. Effective URL and HTML canonical URL were both `https://kurumsal.sokmarket.com.tr/tr/firsatlar`; title: “Haftanın Fırsatları - ŞOK Marketler.” Redirect count was not recorded. No retry, alternate endpoint, or bypass was used.
- Page anchors exposed KVKK/privacy and cookie-policy links, but no Terms-of-Service, use-conditions, or content-reuse permission link. No linked legal page was fetched; permission for automated product extraction or reuse of price/image content therefore remains unverified. The page metadata describes ŞOK's Türkiye-wide store footprint; that does not prove the geography of individual offers.
- The bounded page summary produced no `DD.MM.YYYY`-style promotion date. A current period, update-in-place history, and campaign validity were not established. The “weekly offers” title alone does not prove current dates or expiry.
- Product-level prices, product detail pages, and images inspected/fetched: **0**. No product evidence was retained or reused because terms/reuse permission was not established.

## Disposition

No product qualifies from this attempt. Terminal catalog result: `SKIPPED_UNVERIFIED`; audit classification: `STALE_UNVERIFIED` pending a permitted, dated verification. This is not a no-promo or obsolete-source finding. Do not infer evergreen status or expiry from `valid_until: null` or the page title. No candidate feed, production JSON, shared progress, or receipt aggregate was changed by this check.
