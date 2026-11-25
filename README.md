# Max-Q Studio Static Website

Static HTML/CSS/JS website deployed to https://maxqstudio.dev/ through GitHub Pages. No build step.

## Homepage visual theme

The original Max-Q Studio homepage structure remains unchanged: centered hero, project index, studio profile, web tools, game and app lists, and contact/footer. The November 2026 visual refresh changes **only** the palette and typography:
- Cream `#F3EEE3`, Ink Black `#111111`, Burnt Orange `#C64E1E`
- DM Sans for body/headings, Instrument Serif italic accents, with fallback fonts
- No extra background tiles behind project logos or photos. Container/cards reuse the page background.
- Max Q Tools uses the canonical branded asset `images/maxq-tools-logo.svg`, sourced from `maxqstudio/max-q-studio/public/brand/maxq-tools-logo.svg`. The SVG itself contains the brand's orange artwork; the site must not add a second cream or black rectangle behind it.

**Scope:** Homepage `index.html` and `style.css`; all product pages and legal/support pages keep their existing branding and behavior.

## CI

The `.github/workflows/homepage-ui.yml` GitHub Actions workflow runs headless Chromium at 320, 375, 768 and 1440px, checking the original centered layout, absence of mockup panel/backgrounds behind icons, correct logo, colors/fonts, mobile navigation, anchors/assets, errors and overflow. Screenshots are uploaded as workflow artifacts for inspection.

## Dark / Light toggle

- Dark (default, independent of operating-system preference): `style-dark.css`, restored directly from `b646fc04cdffd074b6cc469c1fd50f9d14510182:style.css` with only toggle control rules and an emphasis reset appended.
- Light (the approved November 9 cream/ink/orange theme): `style.css`.
- Header toggle switches stylesheets without changing the existing page layout and remembers the last selection using `localStorage['maxqstudio-theme']`. If storage is unavailable, the button still works during the session and defaults to dark on reload.
- The head selects the correct stylesheet before page content is parsed; JavaScript-disabled visitors receive dark CSS.
- Both desktop and mobile states are covered by `.github/workflows/homepage-ui.yml` smoke tests and screenshots.

## Stable homepage theme loading (2026-11-09)

- Two **static stylesheet links** in `index.html` replace JavaScript-injected CSS. The active CSS is declared before the body so slow connections do not briefly show an unstyled homepage.
- Dark remains the default and no-JavaScript fallback; Light retains its existing stylesheet and stored preference. Both stylesheet assets are unchanged.
- The header toggle waits for the target CSS to be available before switching; if an inactive stylesheet fails to load, the existing appearance is retained instead of showing unstyled content.
- Versioned asset references avoid stale cross-release `index.html` / `script.js` combinations.
- CI checks both appearances, storage persistence, navigation, asset loading, disabled JavaScript fallback, slow CSS loading, blocked external fonts and inactive stylesheet failure.


## Pretio public-content updater skill

The skill additionally covers **online shops, official marketplace seller storefronts, and public e-commerce discounted offers**; Google Shopping may be used as an authorized **discovery** source only, not as final price evidence. New seller/store IDs require Owner-reviewed catalog registration and app-compatible official domain validation before highlight publication. The workflow includes bounded online discovery per country and a seller/offer evidence checklist in `.agents/skills/pretio-public-content-updater/templates/ONLINE_SHOP_CHECKLIST.md`. This does **not** implement or schedule a crawler.



Agent instructions: [.agents/skills/pretio-public-content-updater/SKILL.md](.agents/skills/pretio-public-content-updater/SKILL.md). GitHub Copilot alias: [.github/skills/pretio-public-content-updater/SKILL.md](.github/skills/pretio-public-content-updater/SKILL.md).

This policy covers BOTH the official **Catalog Promo** directory and **discounted Product Highlights**. Each country/catalog gets an independent checklist and compact handoff; the next retailer is processed in a clean agent context. Only the existing app-compatible fields may be written. Rotating catalog links require source-backed expiry dates; verified-expired highlights are removed. The target of one new verified discounted product per country every 12 hours is aspirational, never a justification to fabricate a product.

Run read-only validation: `python3 tooling/pretio_public_content/validate.py`.
Preview expired cleanup in a disposable checkout, then use `--prune-expired` on a controlled branch (do not run it on production directly). Validation and regression tests run in GitHub Actions.

**The skill and CI do not themselves fetch retailer data or activate a 12-hour publisher.** A separate scheduler and retailer adapters are required; source authorization, approval gates, cross-country currency metadata and rollback must be solved first.
