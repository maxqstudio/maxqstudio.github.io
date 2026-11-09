import assert from 'node:assert/strict';
import { test } from 'node:test';
import { mkdirSync } from 'node:fs';
import { chromium } from 'playwright';

const base = process.env.TEST_BASE_URL ?? 'http://127.0.0.1:8765';
mkdirSync('artifacts/screenshots', { recursive: true });
const browser = await chromium.launch({ headless: true });
try {
  for (const width of [320, 375, 768, 1440]) {
    await test(`homepage visual contract at ${width}px`, async () => {
      const page = await browser.newPage({ viewport: { width, height: 900 }, deviceScaleFactor: 1 });
      const failures = [];
      page.on('pageerror', error => failures.push(error.message));
      const response = await page.goto(base, { waitUntil: 'domcontentloaded' });
      assert.equal(response?.status(), 200);
      assert.equal(await page.locator('h1').count(), 1);
      assert.match(await page.locator('h1').innerText(), /Small studio/);
      assert.equal(await page.locator('.hero-inner').count(), 1, 'Restore original centered Studio hero');
      assert.equal(await page.locator('.hero-visual, .visual-frame, .hero-grid').count(), 0, 'No added mockup/visual panel');
      assert.equal(await page.locator('#products .product-tile').count(), 5);
      assert.ok(await page.locator('a[href="https://maxq.tools/"]').count() >= 2);
      const logo = page.locator('img[src="images/maxq-tools-logo.svg"]').first();
      await logo.waitFor({ state: 'visible' });
      assert.ok(await logo.evaluate(el => el.complete && el.naturalWidth > 0), 'Official Max Q Tools logo should load');
      const palette = await page.evaluate(() => ({
        background: getComputedStyle(document.body).backgroundColor,
        ink: getComputedStyle(document.documentElement).getPropertyValue('--ink').trim().toLowerCase(),
        orange: getComputedStyle(document.documentElement).getPropertyValue('--orange').trim().toLowerCase(),
        serif: getComputedStyle(document.querySelector('h1 em')).fontFamily,
        heroAlign: getComputedStyle(document.querySelector('.hero-inner')).textAlign,
        dockTileBackground: getComputedStyle(document.querySelector('.product-tile')).backgroundColor,
        dockIconBackground: getComputedStyle(document.querySelector('.product-tile img')).backgroundColor,
        featuredIconBackground: getComputedStyle(document.querySelector('.project-media img')).backgroundColor,
        scrollWidth: document.documentElement.scrollWidth
      }));
      assert.equal(palette.background, 'rgb(243, 238, 227)');
      assert.equal(palette.ink, '#111111');
      assert.equal(palette.orange, '#c64e1e');
      assert.match(palette.serif, /Instrument Serif/);
      assert.equal(palette.heroAlign, 'center');
      assert.equal(palette.dockTileBackground, 'rgba(0, 0, 0, 0)');
      assert.equal(palette.dockIconBackground, 'rgba(0, 0, 0, 0)');
      assert.equal(palette.featuredIconBackground, 'rgba(0, 0, 0, 0)');
      assert.ok(palette.scrollWidth <= width, `horizontal overflow: ${palette.scrollWidth}px at ${width}px`);
      const toggle = page.getByRole('button', { name: 'Open menu' });
      if (width <= 850) {
        assert.equal(await page.getByRole('navigation', { name: 'Main navigation' }).isVisible(), false);
        await toggle.click();
        assert.equal(await toggle.getAttribute('aria-expanded'), 'true');
        assert.equal(await page.getByRole('navigation', { name: 'Main navigation' }).isVisible(), true);
        await page.getByRole('navigation', { name: 'Main navigation' }).getByRole('link', { name: 'Apps' }).click();
        assert.equal(await toggle.getAttribute('aria-expanded'), 'false');
      } else {
        assert.equal(await toggle.isVisible(), false);
        assert.equal(await page.getByRole('navigation', { name: 'Main navigation' }).isVisible(), true);
      }
      assert.deepEqual(failures, []);
      await page.screenshot({ path: `artifacts/screenshots/homepage-${width}.png`, fullPage: true });
      await page.close();
    });
  }
  await test('main navigation, assets and accessible targets exist', async () => {
    const page = await browser.newPage();
    await page.goto(base, { waitUntil: 'domcontentloaded' });
    for (const id of ['main', 'products', 'profile', 'projects', 'games', 'tools', 'contact']) {
      assert.equal(await page.locator('#' + id).count(), 1, `missing anchor #${id}`);
    }
    const missing = await page.evaluate(async () => {
      const urls = Array.from(document.querySelectorAll('img[src]')).map(img => img.getAttribute('src'));
      const local = [...new Set(urls)].filter(url => !url.startsWith('http'));
      const failed = [];
      for (const url of local) {
        const res = await fetch(url);
        if (!res.ok) failed.push(`${url}: ${res.status}`);
      }
      return failed;
    });
    assert.deepEqual(missing, []);
    await page.close();
  });
} finally {
  await browser.close();
}
