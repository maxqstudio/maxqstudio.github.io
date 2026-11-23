# Audit-only online shop lead — Sonda Delivery (BR)

- Run: `pretio-oneoff-global-20261123T040625Z`; scope: `ONE_OFF_GLOBAL`; baseline/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Discovery lead from the already-spent Brazil online-shop query: <https://www.sondadelivery.com.br/>. Search output identified the result as Sonda Delivery; that is a discovery lead only, not direct ownership or product evidence.
- Checked UTC: `2026-11-23T06:10:54Z`.
- One direct request to `https://www.sondadelivery.com.br/robots.txt` returned HTTP **403 Forbidden** after a 12-second timeout setting; PowerShell reported the response after about 9.1 seconds. The wrapper retained no content type, final URL, or response body. No retry or bypass was used.
- Because the robots request was blocked, the homepage, offer page, terms page and any product listings were **not** requested. Robots permission, official seller ownership, current offer content, product prices/images/dates, and delivery geography remain unverified. Terms could not be checked without opening another site page.
- Search-result text about offers is not used as price or currentness proof. No product candidate was accepted; no source or seller was registered; no production data changed.
- Candidate status: **`SKIPPED_BLOCKED`** for this bounded source attempt. Handoff: do not retry or use an alternate host; a future Owner-authorized run can reassess only if the publisher provides an allowed public access route.
