import assert from 'node:assert/strict';
import { test } from 'node:test';
import { mkdirSync } from 'node:fs';
import { chromium } from 'playwright';

const base = process.env.TEST_BASE_URL ?? 'http://127.0.0.1:8765';
mkdirSync('artifacts/screenshots', { recursive: true });
const browser = await chromium.launch({ headless: true });

const appearance = async (page) => page.evaluate(() => ({
  theme: document.documentElement.dataset.theme,
  background: getComputedStyle(document.body).backgroundColor,
  font: getComputedStyle(document.body).fontFamily,
  heroAlign: getComputedStyle(document.querySelector('.hero-inner')).textAlign,
  sheet: Array.from(document.querySelectorAll('link[data-theme-style]')).find(link => link.media === 'all' || link.media === '')?.getAttribute('href')?.split('?')[0],
  activeStylesheets: Array.from(document.querySelectorAll('link[data-theme-style]')).filter(link => link.media === 'all' || link.media === '').length,
  selectedStylesheetLoaded: Boolean(Array.from(document.querySelectorAll('link[data-theme-style]')).find(link => link.media === 'all' || link.media === '')?.sheet),
  meta: document.querySelector('meta[name="theme-color"]').content,
  overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
}));

try {
  for (const width of [320, 375, 768, 850, 1024, 1440]) {
    await test(`default dark, original Studio layout, light toggle + persistence at ${width}px`, async () => {
      const page = await browser.newPage({ viewport: { width, height: 900 }, colorScheme: 'light' });
      const failures = [];
      page.on('pageerror', error => failures.push(error.message));
      const res = await page.goto(base, { waitUntil: 'load' });
      assert.equal(res?.status(), 200);
      assert.equal(await page.locator('.hero-inner').count(), 1);
      assert.equal(await page.locator('.hero-grid, .hero-visual, .visual-frame').count(), 0);
      assert.equal(await page.locator('.product-tile').count(), 5);
      assert.match(await page.locator('h1').innerText(), /Small studio/);
      const logo = page.locator('img[src="images/maxq-tools-logo.svg"]').first();
      assert.ok(await logo.evaluate(img => img.complete && img.naturalWidth > 0), 'Official logo must load');
      const toggle = page.getByRole('button', { name: 'Switch to light mode' });
      assert.equal(await toggle.count(), 1);

      const dark = await appearance(page);
      assert.equal(dark.theme, 'dark');
      assert.equal(dark.sheet, 'style-dark.css');
      assert.equal(dark.activeStylesheets, 1);
      assert.equal(dark.selectedStylesheetLoaded, true);
      assert.equal(dark.background, 'rgb(9, 9, 9)');
      assert.equal(dark.meta.toLowerCase(), '#090909');
      assert.match(dark.font, /Inter/);
      assert.equal(dark.heroAlign, 'center');
      assert.equal(dark.overflow, false, 'no horizontal overflow in dark');
      await page.screenshot({ path: `artifacts/screenshots/dark-${width}.png`, fullPage: true });

      await toggle.click();
      await page.waitForFunction(() => getComputedStyle(document.body).backgroundColor === 'rgb(243, 238, 227)');
      const light = await appearance(page);
      assert.equal(light.theme, 'light');
      assert.equal(light.sheet, 'style.css');
      assert.equal(light.activeStylesheets, 1);
      assert.equal(light.selectedStylesheetLoaded, true);
      assert.equal(light.meta.toLowerCase(), '#f3eee3');
      assert.match(light.font, /DM Sans/);
      assert.equal(light.heroAlign, 'center');
      assert.equal(light.overflow, false, 'no horizontal overflow in light');
      assert.equal(await page.getByRole('button', { name: 'Switch to dark mode' }).count(), 1);
      assert.equal(await page.evaluate(() => localStorage.getItem('maxqstudio-theme')), 'light');
      await page.screenshot({ path: `artifacts/screenshots/light-${width}.png`, fullPage: true });

      await page.reload({ waitUntil: 'load' });
      const reloaded = await appearance(page);
      assert.equal(reloaded.theme, 'light', 'light selection persists');
      assert.equal(reloaded.background, 'rgb(243, 238, 227)');
      await page.getByRole('button', { name: 'Switch to dark mode' }).click();
      await page.waitForFunction(() => getComputedStyle(document.body).backgroundColor === 'rgb(9, 9, 9)');
      await page.reload({ waitUntil: 'load' });
      assert.equal((await appearance(page)).theme, 'dark', 'dark selection persists');

      const mobileMenu = page.getByRole('button', { name: 'Open menu' });
      if (width <= 800) {
        assert.equal(await mobileMenu.isVisible(), true);
        await mobileMenu.click();
        assert.equal(await mobileMenu.getAttribute('aria-expanded'), 'true');
        await page.getByRole('navigation', { name: 'Main navigation' }).getByRole('link', { name: 'Apps' }).click();
        assert.equal(await mobileMenu.getAttribute('aria-expanded'), 'false');
      } else {
        assert.equal(await mobileMenu.isVisible(), false);
        assert.equal(await page.getByRole('navigation', { name: 'Main navigation' }).isVisible(), true);
      }
      assert.deepEqual(failures, []);
      await page.close();
    });
  }

  await test('light preference is fully styled at DOMContentLoaded even with delayed CSS', async () => {
    const page = await browser.newPage({ viewport: { width: 375, height: 820 } });
    await page.addInitScript(() => {
      try { localStorage.setItem('maxqstudio-theme', 'light'); } catch (_) {}
    });
    await page.route('**/style.css?v=*', async (route) => {
      await new Promise(resolve => setTimeout(resolve, 600));
      await route.continue();
    });
    await page.goto(base, { waitUntil: 'domcontentloaded' });
    const state = await appearance(page);
    assert.equal(state.theme, 'light');
    assert.equal(state.background, 'rgb(243, 238, 227)');
    assert.equal(state.sheet, 'style.css');
    assert.equal(state.selectedStylesheetLoaded, true);
    assert.equal(state.overflow, false);
    await page.close();
  });

  await test('default dark remains fully styled under delayed CSS and blocked third-party fonts', async () => {
    const page = await browser.newPage({ viewport: { width: 850, height: 850 }, colorScheme: 'light' });
    await page.route('**/style-dark.css?v=*', async (route) => {
      await new Promise(resolve => setTimeout(resolve, 600));
      await route.continue();
    });
    await page.route('https://fonts.googleapis.com/**', route => route.abort());
    await page.route('https://fonts.gstatic.com/**', route => route.abort());
    await page.goto(base, { waitUntil: 'domcontentloaded' });
    const state = await appearance(page);
    assert.equal(state.theme, 'dark');
    assert.equal(state.background, 'rgb(9, 9, 9)');
    assert.equal(state.sheet, 'style-dark.css');
    assert.equal(state.selectedStylesheetLoaded, true);
    assert.equal(state.overflow, false);
    await page.close();
  });

  await test('failed inactive theme CSS does not remove current dark styling', async () => {
    const page = await browser.newPage();
    await page.route('**/style.css?v=*', route => route.abort());
    await page.goto(base, { waitUntil: 'load' });
    const toggle = page.getByRole('button', { name: 'Switch to light mode' });
    await toggle.click();
    await page.waitForFunction(() => document.querySelector('.theme-toggle').disabled === false);
    const state = await appearance(page);
    assert.equal(state.theme, 'dark');
    assert.equal(state.background, 'rgb(9, 9, 9)');
    assert.equal(state.sheet, 'style-dark.css');
    assert.equal(state.selectedStylesheetLoaded, true);
    await page.close();
  });

  await test('no-JavaScript fallback renders the original dark Studio', async () => {
    const context = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 375, height: 850 } });
    const page = await context.newPage();
    await page.goto(base, { waitUntil: 'load' });
    const state = await appearance(page);
    assert.equal(state.background, 'rgb(9, 9, 9)');
    assert.equal(state.sheet, 'style-dark.css');
    assert.equal(state.selectedStylesheetLoaded, true);
    await context.close();
  });

  await test('all product logos and original navigation anchors remain available', async () => {
    const page = await browser.newPage();
    await page.goto(base);
    for (const id of ['main','products','profile','projects','games','tools','contact']) {
      assert.equal(await page.locator('#'+id).count(), 1, `missing #${id}`);
    }
    const failedAssets = await page.evaluate(async () => {
      const paths = [...new Set([...document.querySelectorAll('img[src]')].map(el => el.getAttribute('src')))];
      const failed = [];
      for (const path of paths.filter(p => !p.startsWith('http'))) {
        const response = await fetch(path);
        if (!response.ok) failed.push(`${path}: ${response.status}`);
      }
      return failed;
    });
    assert.deepEqual(failedAssets, []);
    await page.close();
  });
} finally {
  await browser.close();
}
