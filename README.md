# Max-Q Studio Static Website

Static HTML/CSS/JS website. No React, no Next.js, no backend, no build step.

The studio homepage uses a monochrome dark theme inspired by the Sleek X showcase, with a dotted hero background, rounded navigation, and consistent icon-led project cards. Product pages retain their own branding. `images/project-icon-sources.json` records the source revisions for Pretio, SaldoSehat, and Max Q Tools icons. SaldoSehat's Android adaptive vector is translated to SVG with its original paths and colors.

The developer mark follows the supplied `icon_dev_2.svg` artwork. The header and footer use `images/icon-dev.svg` on a light backing in CSS; `images/icon-dev-favicon.svg` includes the same light backing for visibility in dark browser tabs.

Upload all files and folders to your hosting root.

Main pages:
- `/index.html`
- `/saldosehat/index.html`
- `/saldosehat/privacy.html`
- `/saldosehat/terms.html`
- `/saldosehat/support.html`


Added Pretio app pages: /pretio/, /pretio/privacy.html, /pretio/terms.html, /pretio/support.html

Updated Pretio card on Max-Q homepage to match SaldoSehat card style. Removed feature numbers on Pretio and SaldoSehat pages. Pretio screenshots now show 5 images only.

Added Max Cam Scanner app pages: /max-cam-scanner/ (index, privacy, terms, support, account-deletion, invite). `.well-known/assetlinks.json` lets workspace invite links open the Android app; `.nojekyll` makes GitHub Pages publish the `.well-known` folder.
