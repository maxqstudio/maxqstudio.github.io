# Max-Q Studio Static Website

Static HTML/CSS/JS website. No React, no Next.js, no backend, no build step.

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
