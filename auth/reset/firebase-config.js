// Firebase Web SDK configuration is public by design. DO NOT use the Android
// google-services.json key here: that key is restricted to Android app signatures.
// Before merging PR #40, register a Firebase Web app and insert its dedicated,
// HTTP-referrer-restricted web key below. Never put service account credentials here.
export const firebaseWebConfig = Object.freeze({
  apiKey: "",
  authDomain: "max-cam-scanner.firebaseapp.com",
  projectId: "max-cam-scanner",
});
