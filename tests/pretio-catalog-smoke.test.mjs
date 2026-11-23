import assert from 'node:assert/strict';
import { test } from 'node:test';
import { mkdirSync } from 'node:fs';
import { chromium } from 'playwright';

const base = process.env.TEST_BASE_URL || 'http://127.0.0.1:8765';
mkdirSync('artifacts/screenshots', { recursive: true });
const browser = await chromium.launch({ headless: true });

async function openCatalog(page, query = '?country=DE') {
  const errors = [];
  page.on('pageerror', err => errors.push(err.message));
  const res = await page.goto(base + '/pretio/catalog/' + query, { waitUntil: 'domcontentloaded' });
  assert.equal(res?.status(), 200);
  await page.waitForFunction(() => {
    const text = document.querySelector('#result-summary')?.textContent || '';
    return text.startsWith('Showing ') || text.startsWith('Unable');
  });
  assert.equal((await page.locator('#result-summary').innerText()).startsWith('Unable'), false);
  return errors;
}

try {
  await test('Germany has exactly five official catalog entries and one dated highlight', async () => {
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
    const errors = await openCatalog(page);
    assert.equal(await page.locator('#country').inputValue(), 'DE');
    assert.equal(await page.locator('.catalog-card').count(), 5);
    const titles = await page.locator('.catalog-card h3').allInnerTexts();
    for (const name of ['Lidl', 'ALDI Süd', 'ALDI Nord', 'REWE', 'Kaufland']) {
      assert.ok(titles.some(s => s.includes(name)), 'missing retailer ' + name);
    }
    assert.equal(await page.locator('#stat-countries').innerText(), '24');
    const links = await page.locator('.catalog-card a.card-action').evaluateAll(els => els.map(el => ({ href: el.href, rel: el.rel, target: el.target })));
    assert.equal(links.length, 5);
    assert.ok(links.every(x => x.href.startsWith('https://') && x.target === '_blank' && x.rel.includes('noopener')));
    await page.getByRole('tab', { name: /product highlights/i }).click();
    await page.waitForFunction(() => document.querySelectorAll('.highlight-card').length >= 1);
    const solevitaCard = page.locator('.highlight-card', { hasText: 'Solevita Orangensaft 100%' }).first();
    await solevitaCard.waitFor();
    const solevitaText = await solevitaCard.innerText();
    assert.match(solevitaText, /Solevita Orangensaft 100%/);
    assert.match(solevitaText, /€1\.39/);
    assert.match(solevitaText, /not a confirmed current offer/i);
    assert.deepEqual(errors, []);
    await page.screenshot({ path: 'artifacts/screenshots/pretio-catalog-germany-desktop.png', fullPage: true });
    await page.close();
  });

  await test('Search, retailer filter, reset, country switch and sharable query work', async () => {
    const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
    const errors = await openCatalog(page);
    await page.locator('#search').fill('Kaufland');
    assert.equal(await page.locator('.catalog-card').count(), 1);
    assert.match(await page.locator('.catalog-card').innerText(), /Kaufland/);
    assert.match(page.url(), /q=Kaufland/);
    await page.locator('#clear-filters').click();
    assert.equal(await page.locator('.catalog-card').count(), 5);
    await page.locator('#merchant').selectOption('Lidl');
    assert.equal(await page.locator('.catalog-card').count(), 1);
    await page.locator('#country').selectOption('ALL');
    assert.equal(await page.locator('.catalog-card').count(), 74);
    await page.locator('#search').fill('<img src=x onerror=alert(1)>');
    assert.equal(await page.locator('.catalog-card').count(), 0);
    assert.equal(await page.locator('#results img[src="x"]').count(), 0);
    assert.deepEqual(errors, []);
    await page.close();
  });

  await test('Product highlights across all countries can be searched', async () => {
    const page = await browser.newPage();
    const errors = await openCatalog(page, '?country=ALL&tab=highlights');
    await page.waitForFunction(() => {
      const summary = document.querySelector('#result-summary')?.textContent || '';
      return summary.startsWith('Showing ') && !document.querySelector('#results .loading');
    });
    assert.ok(await page.locator('.highlight-card').count() >= 1, 'expected global highlights');
    await page.locator('#search').fill('Solevita');
    assert.equal(await page.locator('.highlight-card').count(), 1);
    assert.deepEqual(errors, []);
    await page.close();
  });

  await test('IP country from same-origin Cloudflare trace is the initial market', async () => {
    const page = await browser.newPage();
    let externalLookupCount = 0;
    await page.route('**/cdn-cgi/trace', route => route.fulfill({
      status: 200, contentType: 'text/plain', body: 'h=localhost\\nloc=ID\\nip=203.0.113.50\\n'
    }));
    await page.route('https://get.geojs.io/**', route => {
      externalLookupCount++;
      return route.fulfill({ status: 200, contentType: 'application/json', body: '{"country":"US"}' });
    });
    await openCatalog(page, '');
    assert.equal(await page.locator('#country').inputValue(), 'ID');
    assert.equal(await page.locator('.catalog-card').count(), 9);
    assert.equal(externalLookupCount, 0);
    assert.match(page.url(), /country=ID/);
    await page.close();
  });

  await test('GeoJS country fallback works if own edge has no country', async () => {
    const page = await browser.newPage();
    await page.route('**/cdn-cgi/trace', route => route.fulfill({ status: 404, body: 'Not Found' }));
    await page.route('https://get.geojs.io/**', route => route.fulfill({
      status: 200, contentType: 'application/json', body: '{"country":"CL","ip":"203.0.113.7"}'
    }));
    await openCatalog(page, '');
    assert.equal(await page.locator('#country').inputValue(), 'CL');
    assert.equal(await page.locator('.catalog-card').count(), 7);
    await page.close();
  });

  await test('All countries is the fallback when IP detection fails or is unsupported', async () => {
    const page = await browser.newPage({ locale: 'en-US' });
    await page.route('**/cdn-cgi/trace', route => route.fulfill({ status: 404, body: 'No edge' }));
    await page.route('https://get.geojs.io/**', route => route.fulfill({ status: 503, body: 'No geo service' }));
    await openCatalog(page, '');
    assert.equal(await page.locator('#country').inputValue(), 'ALL');
    assert.equal(await page.locator('.catalog-card').count(), 74);
    assert.doesNotMatch(page.url(), /country=/);
    await page.close();

    const pageUnsupported = await browser.newPage();
    await pageUnsupported.route('**/cdn-cgi/trace', route => route.fulfill({
      status: 200, contentType: 'text/plain', body: 'loc=JP\\n'
    }));
    await openCatalog(pageUnsupported, '');
    assert.equal(await pageUnsupported.locator('#country').inputValue(), 'ALL');
    await pageUnsupported.close();
  });

  await test('Explicit country link and manually saved market override IP geolocation', async () => {
    const context = await browser.newContext();
    const page = await context.newPage();
    let ipLookupCount = 0;
    await page.route('**/cdn-cgi/trace', route => {
      ipLookupCount++;
      return route.fulfill({ status: 200, contentType: 'text/plain', body: 'loc=US\\n' });
    });
    await openCatalog(page, '?country=DE');
    assert.equal(await page.locator('#country').inputValue(), 'DE');
    assert.equal(ipLookupCount, 0, 'explicit link should never make an IP lookup');
    await page.locator('#country').selectOption('ID');
    assert.equal(await page.locator('.catalog-card').count(), 9);
    await page.goto(base + '/pretio/catalog/', { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => (document.querySelector('#result-summary')?.textContent || '').startsWith('Showing '));
    assert.equal(await page.locator('#country').inputValue(), 'ID', 'manually saved market should persist');
    assert.equal(ipLookupCount, 0, 'saved market should not make an IP lookup');
    await page.goto(base + '/pretio/catalog/?country=CH', { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => (document.querySelector('#result-summary')?.textContent || '').startsWith('Showing '));
    assert.equal(await page.locator('#country').inputValue(), 'CH', 'explicit link outranks stored selection');
    await context.close();
  });

  await test('Mobile layout fits screen and provides search, tabs and cards', async () => {
    const page = await browser.newPage({ viewport: { width: 360, height: 800 }, isMobile: true, hasTouch: true });
    const errors = await openCatalog(page);
    assert.equal(await page.locator('.catalog-card').count(), 5);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
    assert.equal(overflow, false, 'unexpected horizontal overflow at 360px');
    await page.locator('#search').fill('Lidl');
    assert.equal(await page.locator('.catalog-card').count(), 1);
    await page.locator('#list-view').click();
    assert.equal(await page.locator('#list-view').getAttribute('aria-pressed'), 'true');
    assert.deepEqual(errors, []);
    await page.screenshot({ path: 'artifacts/screenshots/pretio-catalog-germany-mobile.png', fullPage: true });
    await page.close();
  });
} finally {
  await browser.close();
}
