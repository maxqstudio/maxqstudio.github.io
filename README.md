# Max-Q Studio Static Website

Static HTML/CSS/JS website deployed at https://maxqstudio.dev/ through GitHub Pages. No build step.

## Homepage design (November 2026)

The homepage uses the supplied editorial reference: Cream `#F3EEE3`, Ink Black `#111111`, and Burnt Orange `#C64E1E`. Type pairs DM Sans (heavy, tight headings) with Instrument Serif italic accents; local fallbacks are included. The homepage has a split editorial hero, an ink project index, and cream/orange content sections. Mobile navigation and reduced-motion behavior are preserved.

**Max Q Tools logo:** `images/maxq-tools-logo.svg` is copied unchanged from the canonical `maxqstudio/max-q-studio/public/brand/maxq-tools-logo.svg`. Do not substitute the Max-Q Studio developer mark or the legacy `maxq-tools-icon.png`.

**Scope:** The homepage (`index.html`, `style.css`) only. Product pages preserve their own branding; privacy, terms, support, and domain configuration remain unchanged.

## CI

`.github/workflows/homepage-ui.yml` runs Chromium smoke tests at 320, 375, 768, and 1440 px, checks mobile navigation, assets, links/anchors, type and palette, console errors, and horizontal overflow. Run locally with a static server and Playwright 1.56.1, then `node --test tests/homepage-smoke.test.mjs`.

Other pages:
- `/saldosehat/`
- `/pretio/`
- `/max-cam-scanner/`
- `/blendin/`
