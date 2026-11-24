import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const read = (path) => readFileSync(new URL(`../${path}`, import.meta.url), 'utf8');

const landing = read('pretio/index.html');
const privacy = read('pretio/privacy.html');
const terms = read('pretio/terms.html');
const dataDeletion = read('pretio/data-deletion.html');
const support = read('pretio/support.html');

test('Pretio landing page reflects v1.5.0 features and multi-provider AI fallback', () => {
  assert.match(landing, /What's new in 1\.5\.0/);
  assert.doesNotMatch(landing, /What's new in 1\.4\.6/);
  assert.match(landing, /Home Best Deal/);
  assert.match(landing, /Product Highlights &amp; Watchlist/);
  assert.match(landing, /Multi-provider AI fallback/i);
  assert.match(landing, /Google Gemini/);
  assert.match(landing, /OpenAI/);
  assert.match(landing, /Anthropic/);
});

test('Pretio Privacy Policy discloses v1.5.0 multi-provider AI fallback, grounding cache rule, Remote Config, and security hardening', () => {
  assert.match(privacy, /November 24, 2026 \(Pretio 1\.5\.0\)/);
  assert.match(privacy, /Multi-Provider AI Fallback/);
  assert.match(privacy, /aiGenerate/);
  assert.match(privacy, /Google Gemini \(primary\)/);
  assert.match(privacy, /OpenAI \(fallback\)/);
  assert.match(privacy, /Anthropic \(fallback\)/);
  assert.match(privacy, /never persistently cached or stored/i);
  assert.match(privacy, /https:\/\/ai\.google\.dev\/gemini-api\/terms/);
  assert.match(privacy, /https:\/\/openai\.com\/policies\/privacy-policy\//);
  assert.match(privacy, /https:\/\/openai\.com\/business-data\//);
  assert.match(privacy, /https:\/\/www\.anthropic\.com\/legal\/privacy/);
  assert.match(privacy, /https:\/\/privacy\.anthropic\.com\/en\//);
  assert.match(privacy, /non-anonymous Google account/);
  assert.match(privacy, /rate-limited per account/);
  assert.match(privacy, /Firebase Remote Config/);
  assert.match(privacy, /app_latest_version/);
  assert.match(privacy, /app_force_update/);
  assert.match(privacy, /maxqstudio\.dev\/pretio\//);
  assert.match(privacy, /Product Watchlist/);
  assert.match(privacy, /anti-SSRF/);
});

test('Pretio Terms and Conditions disclose v1.5.0 AI fallback, Watchlist, Best Deal, and Remote Config update gate', () => {
  assert.match(terms, /November 24, 2026 \(Pretio 1\.5\.0\)/);
  assert.match(terms, /Home Best Deal/);
  assert.match(terms, /Multi-Provider AI Fallback/);
  assert.match(terms, /Google Gemini/);
  assert.match(terms, /OpenAI/);
  assert.match(terms, /Anthropic/);
  assert.match(terms, /https:\/\/ai\.google\.dev\/gemini-api\/terms/);
  assert.match(terms, /https:\/\/openai\.com\/business-data\//);
  assert.match(terms, /https:\/\/privacy\.anthropic\.com\/en\//);
  assert.match(terms, /never persistently cached/);
  assert.match(terms, /Product Watchlist/);
  assert.match(terms, /Firebase Remote Config/);
  assert.match(terms, /aiConsumeQuota/);
  assert.match(terms, /non-anonymous Google account/);
  assert.match(terms, /rate-limited per account/);
});

test('Pretio Data Deletion and Support pages reflect v1.5.0 AI fallback and cloud deletion', () => {
  assert.match(dataDeletion, /November 24, 2026 \(Pretio 1\.5\.0\)/);
  assert.match(dataDeletion, /Google Gemini/);
  assert.match(dataDeletion, /OpenAI/);
  assert.match(dataDeletion, /Anthropic/);
  assert.match(dataDeletion, /Product Watchlist/);
  assert.match(support, /Google Gemini/);
  assert.match(support, /OpenAI/);
  assert.match(support, /Anthropic/);
  assert.match(support, /Firebase Remote Config/);
  assert.match(support, /Delete Account|Account page/);
});
