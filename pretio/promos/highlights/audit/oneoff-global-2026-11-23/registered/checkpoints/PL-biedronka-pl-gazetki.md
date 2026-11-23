# Pretio — per-catalog update checklist

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `PL:biedronka-pl-gazetki` | manifest position: **51/74** | attempt: **1**  
Country: **PL** | retailer: **Biedronka** | mode: **AUDIT**  
Registered promo URL: <https://www.biedronka.pl/pl/gazetki>  
Checked: **2026-11-23**; the web connector did not expose exact HTTP response timestamps. Checkpoint recorded at **2026-11-23T10:05:07Z**.  
Baseline / skill SHA: **73fd02fe14c4935c3a95bca49bba3c1498a9cb54**  
Terminal status: **SKIPPED_BLOCKED**

## 1. Catalog Promo source

- [x] Loaded frozen manifest record and active catalog: `biedronka-pl-gazetki`, Biedronka, Poland (`PL`), `source_type: official_retailer`, national directory location, active, `valid_until: null`, existing `last_verified_at: 2026-11-15T05:42:54.476Z`.
- [x] Registered URL is `https://www.biedronka.pl/pl/gazetki`; hostname `www.biedronka.pl` is already present in the allowed-host list.
- [x] Official homepage `https://www.biedronka.pl/` redirected to `https://www.biedronka.pl/pl`. It identifies Biedronka / Jeronimo Martins Polska S.A. and links to the `Gazetki` section. The registered promotional page itself was **not opened**.
- [x] `https://www.biedronka.pl/robots.txt` was readable. `User-agent: *` disallows `/front/search*` and `/pl/search*`; no rule disallows the registered `/pl/gazetki` path. This is only an access-rule observation, not permission to reuse site content.
- [x] Opened the official service terms at <https://www.biedronka.pl/pl/regulamin-serwisu>. Section 9.1 limits viewing/printing/saving site materials to personal use and says other use, including copying or distribution, requires prior permission from the administrator or rights holder. No such permission is evidenced for this commercial Pretio research and retention.
- [x] Stopped before opening the promo page or retaining offer content. No product names, price pairs, images, flyer dates, or item-level offer claims were copied.
- [ ] Current flyer content, canonical redirect of the registered path, update-in-place behavior, promotion dates, and official successor were not verified. Keep this catalog `STALE_UNVERIFIED`; do not infer obsolescence or expiry from the permission block or the prior verification timestamp.
- [x] The homepage workflow asks the visitor to select a store to see current offers, so item-level nationwide applicability was not established by the catalog record alone.
- [x] No production catalog field, URL, verification timestamp, highlight feed, index, location, or currency data was changed.

## 2. Product Highlights

- [x] No offer page or item was opened, so inspected products and accepted/rejected product candidates are **0/0**. There is no verified price pair, individual image, promo validity, or item-level geographic scope.
- [x] `PL` is absent from `pretio/data/currency.json`; no PL feed or index entry exists. This independently blocks Product Highlights publication for Poland under the current schema.
- [x] A local scan of every current country highlight feed found **zero** references to `biedronka-pl-gazetki`; no dependent highlight was deleted or migrated.

## 3. Terminal decision

**SKIPPED_BLOCKED** — robots does not disallow the path, but the official terms require prior consent for copying/reusing site materials beyond personal use. No permission was provided for this commercial retention. Source freshness and offers remain unverified; preserve the active catalog entry and do not treat the source as expired or obsolete.

## Compact handoff (≤400 words)

- Work unit `PL:biedronka-pl-gazetki`, position 51/74; terminal receipt `SKIPPED_BLOCKED`. Run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, base/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`.
- Registered URL: <https://www.biedronka.pl/pl/gazetki>. Official homepage redirected to `/pl`, identified the retailer, and linked a `Gazetki` section. Robots allows the exact route (only `/front/search*` and `/pl/search*` are disallowed). The registered promo page was not opened.
- Official service terms at <https://www.biedronka.pl/pl/regulamin-serwisu>, section 9.1, limit saving/printing/viewing materials to personal use and require prior permission for other use, including copying/distribution. No such permission is evidenced, so no offers or prices were retained.
- Catalog record is active and `valid_until` is null. The blocked attempt does not prove expiry, obsolescence, or current evergreen content; keep `STALE_UNVERIFIED` and preserve the record. Item-level geography is unverified because the source requires store selection.
- No products were inspected. PL has no supported highlight currency/feed, and no existing highlight references this catalog. No production data changed.
- Next source: `PL:lidl-pl-official-gazette` (52/74), in a fresh isolated context.
