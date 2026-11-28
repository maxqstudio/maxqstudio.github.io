# Max Cam Scanner password reset — web configuration

This page is an unreleased Firebase Authentication email-action fallback.
**Do not merge it while the Firebase Web key is blank.** It deliberately fails
closed with a localized message until configured.

1. In Firebase Console for project `max-cam-scanner`, register a **Web app**.
   Keep Android and Web Firebase app configurations separate.
2. In Google Cloud Credentials, use its dedicated Browser key with
   **Application restrictions: Websites**. Restrict referrers to the exact
   deployed HTTPS origin (`https://maxqstudio.dev/*` and only any additional
   origins actually used). Do not change the Android-restricted key.
3. Restrict allowed APIs to the ones needed for Firebase Auth, typically
   **Identity Toolkit API** and **Token Service API**. Check browser console
   for any service-blocked errors before releasing.
4. In Firebase Authentication authorized domains, verify `maxqstudio.dev`
   is listed. Use valid password-reset email action links pointing at
   `https://maxqstudio.dev/auth/reset/`.
5. Fill `auth/reset/firebase-config.js` with the PUBLIC Firebase Web
   `apiKey` for the same Firebase project, **never service account
   credentials, private keys, or admin tokens**.
6. Verify invalid, expired, and valid reset links in EN/ID on a real browser
   and inspect DevTools for referrer errors and network requests.
7. Keep this PR in Draft until end-to-end testing passes.

The `Referrer-Policy: origin` meta tag intentionally sends only the site
origin (not `oobCode`) so browser HTTP-referrer API restrictions can work.
`no-referrer` would hide the full referrer and may break API-key validation.
The code is also cleared from the address bar after script startup.

Note: Firebase Web API keys are public client identifiers; do not treat them
as administrator secrets. Firebase Security Rules, App Check (where supported),
Auth abuse controls, and quotas remain separate responsibilities.
