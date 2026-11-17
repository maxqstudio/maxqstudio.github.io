# Max Background Remover assets

The screenshot gallery is captured from the app's system-camera-test v1.2.0 build on Android emulator-5554 on November 17, 2026. The demo portrait was generated with the built-in imagegen tool and processed in the actual app; portrait-cutout.png is its gallery export. No astronaut or earlier v2 screenshot is used in the published product page.

app-icon.svg reproduces the application's camera/checkerboard vector. Manrope is the application's bundled OFL typeface; see Manrope-OFL.txt.

tooling/render-bg-remover-assets.mjs renders phone-frame promotional assets and the review board from these screenshots. It uses Playwright. Set BG_BROWSER_EXE if using a preinstalled Chromium executable. It writes the app repository's store-listing folder and copies website graphics back here.

Do not present this one sample as a general benchmark of segmentation quality or memory use.
