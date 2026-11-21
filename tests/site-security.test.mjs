import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { test } from 'node:test';
import vm from 'node:vm';

const read = (path) => readFileSync(new URL('../' + path, import.meta.url), 'utf8');

for (const path of ['max-cam-scanner/invite.html', 'max-cam-scanner/id/invite.html']) {
  const html = read(path);
  const match = html.match(/<script>\s*([\s\S]*?)<\/script>\s*<\/body>/);
  test(path + ': no invite-token egress or referrer leakage', () => {
    assert.match(html, /<meta name="referrer" content="no-referrer"\s*\/>/);
    assert.match(html, /<meta name="robots" content="noindex, nofollow, noarchive"\s*\/>/);
    assert.ok(match, 'inline invite handler must exist');
    assert.doesNotMatch(match[1], /fetch\s*\(|XMLHttpRequest|sendBeacon/);
    assert.doesNotMatch(html, /\/v1\/invites\/preview|api-staging\.maxq\.tools/);
    assert.match(match[1], /history\.replaceState/);
  });

  const openInvite = (search) => {
    const open = { href: '#', style: {} };
    const msg = { textContent: '' };
    let cleanUrl;
    const location = { pathname: '/max-cam-scanner/invite.html', search, hash: '#open' };
    const history = { state: { x: 1 }, replaceState(state, title, url) { cleanUrl = url; } };
    vm.runInNewContext(match[1], {
      URLSearchParams, encodeURIComponent, location, history,
      document: { getElementById: (id) => id === 'open' ? open : msg },
    }, { timeout: 1000 });
    return { open, msg, cleanUrl };
  };

  test(path + ': preserves the deep link but removes the token from address bar', () => {
    const token = 'abcdef0123456789'.repeat(4);
    const { open, cleanUrl } = openInvite('?token=' + token + '&lang=id');
    assert.equal(open.href, 'maxqscanner://invite?token=' + token);
    assert.equal(cleanUrl, '/max-cam-scanner/invite.html?lang=id#open');
    assert.notEqual(open.style.display, 'none');
  });

  test(path + ': invalid invite is not opened and is scrubbed', () => {
    const { open, cleanUrl, msg } = openInvite('?token=invalid');
    assert.equal(open.style.display, 'none');
    assert.equal(cleanUrl, '/max-cam-scanner/invite.html#open');
    assert.ok(msg.textContent.length > 10);
  });
}
