import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { test } from 'node:test';

const page = readFileSync(new URL('../auth/reset/index.html', import.meta.url), 'utf8');
const config = readFileSync(new URL('../auth/reset/firebase-config.js', import.meta.url), 'utf8');

test('reset page does not reuse an Android-restricted Firebase API key', () => {
  assert.doesNotMatch(page, /apiKey:\s*["']AIza[A-Za-z0-9_-]+/);
  assert.match(page, /firebase-config\.js/);
  assert.match(page, /isWebConfigured/);
  assert.match(page, /else if \(!auth\)/);
  assert.match(page, /L\.notConfigured/);
  assert.match(config, /apiKey:\s*""/);
  assert.match(config, /authDomain:\s*"max-cam-scanner\.firebaseapp\.com"/);
  assert.match(config, /projectId:\s*"max-cam-scanner"/);
});

test('HTTP referrers share only origin for restricted Web keys', () => {
  // no-referrer suppresses Referer and can break Website-restricted keys.
  // origin never sends the sensitive oobCode in the Referer header.
  assert.match(page, /<meta name="referrer" content="origin"\s*\/>/);
  assert.doesNotMatch(page, /<meta name="referrer" content="no-referrer"/);
});

test('reset link is private and action code is cleared after reading', () => {
  assert.match(page, /<meta name="robots" content="noindex, nofollow"/);
  assert.match(page, /const oobCode = params\.get\("oobCode"\)/);
  assert.match(page, /history\.replaceState/);
  assert.match(page, /verifyPasswordResetCode\(auth, oobCode\)/);
  assert.match(page, /confirmPasswordReset\(auth, oobCode, p1\)/);
  assert.doesNotMatch(page, /google-services\.json|firebase-admin|serviceAccountKey/);
});
