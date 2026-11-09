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
