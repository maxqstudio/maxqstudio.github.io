# Pretio catalog checkpoint — Intermarché Portugal

Run: `pretio-oneoff-global-20261123T040625Z` | Scope: `ONE_OFF_GLOBAL` | Mode: `AUDIT`  
Work unit: `PT:intermarche-pt-country`, **55/74**, attempt 1  
Checked: `2026-11-23T10:13Z` | Result: **SKIPPED_BLOCKED**  
Run base/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54` (the checked worktree skill matched this commit); observed workspace HEAD: `b65040f2bb18be6de1994b95424521aa4ce4a44d`.

## Source and permission

- Loaded the frozen manifest and active record: Intermarché, Portugal; `catalog_id: intermarche-pt-country`; `https://intermarche.pt/sign/brands/catalog-page`; `valid_until: null`; existing `last_verified_at: 2026-09-28T00:00:00Z`.
- The official page opened at the registered host and identifies itself as weekly brochures (`Folhetos Semanais`), with weekly and special brochure sections. It is directory-shaped and consistent with an evergreen catalog landing page, but no historical cycle or explicit validity dates were checked. The null expiry and prior verification date do not prove current offer dates or expiry.
- The official site terms at `https://intermarche.pt/politica-de-privacidade` identify ITMP Alimentar, S.A. and include terms of site access and intellectual property. They limit use to personal, noncommercial viewing/printing and prohibit copying, distribution, and exploitation absent an express license. No commercial reuse permission for Pretio was found; no brochure or product content was retained.
- A single direct GET of `https://intermarche.pt/robots.txt` returned HTTP 502 at `2026-11-23T10:12:19Z`; the web connector also could not open it. Robots permission is unresolved, not treated as allow or deny.
- The Portuguese site identifies Portugal-market weekly offers. Its own catalog record says “Portugal (location-selected offers)”; nationwide price applicability for any individual physical-store offer was not established. Keep the catalog `STALE_UNVERIFIED`; do not infer obsolescence or expiry.

## Product Highlights and disposition

- Search results incidentally surfaced retailer offer snippets with prices before the terms were reviewed. None were transcribed or used as candidates; product review stopped after the terms check. No product page or image was opened or downloaded. **Accepted products: 0; candidates retained: 0.**
- `pretio/promos/highlights/PT.json` is absent and the currency map has no PT entry (EUR is mapped only to DE). No highlight could be prepared for Portugal under the current schema in any case.
- Preserve production catalog, feeds, and index unchanged. No product expiry, catalog obsolescence, or nationwide offer was inferred. Next input: `PT:lidl-pt-country` (56/74).
