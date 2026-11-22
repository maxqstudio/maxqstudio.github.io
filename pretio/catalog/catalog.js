'use strict';
/* Public Pretio JSON viewer. No authentication, cookies, geolocation or analytics. */
(function () {
  const $ = (id) => document.getElementById(id);
  const state = {
    catalogs: [], index: null, highlights: [], highlightsByCountry: new Map(),
    country: 'DE', merchant: 'ALL', tab: 'catalogs', sort: 'featured',
    query: '', view: 'grid', loading: true, highlightLoading: false,
    error: '', highlightError: '', countries: [], selectedRequest: 0
  };
  const MAX_AGE_DAYS = 30;
  const nameByCountry = new Map();
  const dateFormatter = new Intl.DateTimeFormat('en', { day: 'numeric', month: 'short', year: 'numeric' });
  let displayNames;
  try { displayNames = new Intl.DisplayNames(['en'], { type: 'region' }); } catch (_) { displayNames = null; }

  function node(tag, className, value) {
    const n = document.createElement(tag);
    if (className) n.className = className;
    if (value !== undefined && value !== null) n.textContent = String(value);
    return n;
  }
  function append(parent) {
    for (let i = 1; i < arguments.length; i++) {
      const n = arguments[i];
      if (n !== null && n !== undefined) parent.append(n);
    }
    return parent;
  }
  function externalLink(url, title, className) {
    const u = secureUrl(url);
    if (!u) return node('span', (className || 'card-action') + ' disabled', 'Source unavailable');
    const a = node('a', className || 'card-action', title);
    a.href = u;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    a.referrerPolicy = 'no-referrer';
    a.setAttribute('aria-label', title + ' (opens external retailer site)');
    return a;
  }
  function secureUrl(value) {
    try {
      const u = new URL(value);
      if (u.protocol !== 'https:' || !u.hostname || u.username || u.password) return null;
      return u.toString();
    } catch (_) { return null; }
  }
  function logo(url, name) {
    const holder = node('span', 'merchant-logo');
    holder.textContent = initials(name);
    const src = secureUrl(url);
    if (src) {
      const img = document.createElement('img');
      img.alt = '';
      img.loading = 'lazy';
      img.decoding = 'async';
      img.referrerPolicy = 'no-referrer';
      img.addEventListener('load', function () { holder.textContent = ''; holder.append(img); }, { once: true });
      img.addEventListener('error', function () { img.remove(); }, { once: true });
      img.src = src;
    }
    return holder;
  }
  function initials(s) { return String(s || '?').split(/\s+/).filter(Boolean).slice(0, 2).map(x => x.slice(0, 1)).join('').toUpperCase(); }
  function day(value) {
    const d = value ? new Date(value) : null;
    return d && !isNaN(d.valueOf()) ? dateFormatter.format(d) : null;
  }
  function ageDays(value) {
    const time = value ? new Date(value).getTime() : NaN;
    return Number.isFinite(time) ? (Date.now() - time) / 86400000 : null;
  }
  function countryName(code) {
    if (code === 'ALL') return 'All countries';
    return nameByCountry.get(code) || (displayNames && displayNames.of(code)) || code;
  }
  function countryCodes(item) {
    const locs = Array.isArray(item.locations) ? item.locations : [];
    return [...new Set(locs.map(l => l && l.country_code).filter(Boolean))];
  }
  function appliesToCountry(item, code) {
    return code === 'ALL' || countryCodes(item).includes(code);
  }
  function normalized(text) {
    return String(text || '').normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('en');
  }
  function matchesText(item, type) {
    if (!state.query) return true;
    const fields = type === 'catalogs'
      ? [item.title, item.merchant, item.publisher, item.summary, item.coverage_label, item.id]
      : [item.product_name, item.retailer, item.brand, item.package_size, item.id];
    return normalized(fields.join(' ')).includes(normalized(state.query.trim()));
  }
  function catalogsInCountry() {
    return state.catalogs.filter(c => c && c.status === 'active' && appliesToCountry(c, state.country));
  }
  function visibleCatalogs() {
    const list = catalogsInCountry().filter(c => (state.merchant === 'ALL' || c.merchant === state.merchant) && matchesText(c, 'catalogs'));
    return list.sort((a, b) => {
      if (state.sort === 'name') return String(a.merchant).localeCompare(String(b.merchant), 'en');
      if (state.sort === 'recent') return String(b.last_verified_at || '').localeCompare(String(a.last_verified_at || ''));
      return (Number(a.sort_order) || 9999) - (Number(b.sort_order) || 9999) || String(a.merchant).localeCompare(String(b.merchant), 'en');
    });
  }
  function visibleHighlights() {
    const list = state.highlights.filter(h => (state.merchant === 'ALL' || h.retailer === state.merchant) && matchesText(h, 'highlights'));
    return list.sort((a, b) => {
      if (state.sort === 'name') return String(a.product_name).localeCompare(String(b.product_name), 'en');
      if (state.sort === 'recent') return String(b.observed_at || '').localeCompare(String(a.observed_at || ''));
      const aDiff = Number(a.normal_price) - Number(a.promo_price), bDiff = Number(b.normal_price) - Number(b.promo_price);
      return bDiff - aDiff || String(a.product_name).localeCompare(String(b.product_name), 'en');
    });
  }
  function marketMerchants() {
    const list = state.tab === 'catalogs' ? catalogsInCountry().map(c => c.merchant) : state.highlights.map(h => h.retailer);
    return [...new Set(list.filter(Boolean))].sort((a, b) => a.localeCompare(b, 'en'));
  }
  function syncMerchantSelect() {
    const select = $('merchant');
    const names = marketMerchants();
    if (state.merchant !== 'ALL' && !names.includes(state.merchant)) state.merchant = 'ALL';
    select.replaceChildren(new Option('All retailers', 'ALL'), ...names.map(x => new Option(x, x)));
    select.value = state.merchant;
  }
  function cardTop(item) {
    const top = node('div', 'card-top');
    const heading = node('div', 'card-heading');
    const tag = node('span', 'card-tag', item.source_type && item.source_type.startsWith('official') ? 'Official retailer' : 'Store catalog');
    const h = node('h3', '', item.title || item.merchant);
    append(heading, tag, h);
    return append(top, logo(item.logo_url, item.merchant), heading);
  }
  function catalogCard(item) {
    const card = node('article', 'catalog-card');
    const summary = node('p', '', item.summary || 'Browse the catalog on the retailer website.');
    const bottom = node('div', 'card-bottom');
    const meta = node('div', 'card-meta');
    const scope = item.coverage_label || (item.coverage_type === 'national' ? 'National coverage' : 'Regional coverage');
    append(meta, node('b', '', scope), node('small', '', item.last_verified_at ? 'Link checked ' + (day(item.last_verified_at) || 'previously') : 'Check latest offers at retailer'));
    append(bottom, meta, externalLink(item.url, 'Open catalog ↗'));
    return append(card, cardTop(item), summary, bottom);
  }
  function money(value, currency) {
    const n = Number(value);
    if (!Number.isFinite(n)) return String(value || '—');
    try { return new Intl.NumberFormat('en', { style: 'currency', currency: currency || 'EUR' }).format(n); }
    catch (_) { return n.toFixed(2) + ' ' + String(currency || ''); }
  }
  function highlightCard(item) {
    const card = node('article', 'highlight-card');
    const media = node('div', 'highlight-media');
    const fallback = node('span', 'media-placeholder', '▧');
    const imageSrc = secureUrl(item.image_url);
    append(media, fallback, node('span', 'card-tag old', 'Dated price highlight'));
    if (imageSrc) {
      const img = document.createElement('img');
      img.alt = String(item.product_name || 'Product photo');
      img.loading = 'lazy';
      img.decoding = 'async';
      img.referrerPolicy = 'no-referrer';
      img.addEventListener('load', function () { fallback.remove(); }, { once: true });
      img.addEventListener('error', function () { img.remove(); }, { once: true });
      img.src = imageSrc;
      media.append(img);
    }
    const body = node('div', 'highlight-body');
    append(body, node('p', 'highlight-brand', item.retailer || 'Retailer'), node('h3', '', item.product_name || 'Product'), node('p', 'highlight-size', [item.brand, item.package_size].filter(Boolean).join(' · ')));
    const prices = node('div', 'prices');
    const current = Number(item.promo_price), normal = Number(item.normal_price);
    append(prices, node('strong', 'price-now', money(item.promo_price, item.currency)), node('span', 'price-old', money(item.normal_price, item.currency)));
    if (Number.isFinite(current) && Number.isFinite(normal) && normal > current && normal > 0) {
      prices.append(node('span', 'saving', '-' + Math.round((normal - current) / normal * 100) + '% observed'));
    }
    body.append(prices);
    const seen = day(item.observed_at) || day(item.valid_from);
    body.append(node('p', 'highlight-disclaimer', 'Recorded' + (seen ? ' ' + seen : ' previously') + ' · This is not a confirmed current offer.'));
    const bottom = node('div', 'card-bottom');
    const meta = node('div', 'card-meta');
    append(meta, node('b', '', 'Source: ' + (item.retailer || 'Retailer')), node('small', '', (item.country_code ? countryName(item.country_code) + ' · ' : '') + 'Verify with retailer'));
    append(bottom, meta, externalLink(item.source_url, 'View source ↗', 'card-action ghost'));
    body.append(bottom);
    return append(card, media, body);
  }
  function buildCards(items) {
    const frag = document.createDocumentFragment();
    for (const item of items) frag.append(state.tab === 'catalogs' ? catalogCard(item) : highlightCard(item));
    $('results').replaceChildren(frag);
  }
  function noticeText() {
    if (state.error) return 'Unable to load public catalog data: ' + state.error + '. Try reloading the page.';
    if (state.tab === 'highlights') {
      if (state.highlightError) return 'Some highlight data could not be loaded: ' + state.highlightError;
      if (!state.index || !Array.isArray(state.index.countries) || (state.country !== 'ALL' && !state.index.countries.some(x => x.code === state.country))) return 'No product highlight feed is available for ' + countryName(state.country) + ' yet.';
      return 'Historical price observations only — verify offers with retailers before shopping.';
    }
    const stamps = catalogsInCountry().map(c => c.last_verified_at).filter(Boolean).sort();
    const last = stamps.at(-1);
    const age = ageDays(last);
    if (age !== null && age > MAX_AGE_DAYS) return 'Catalog links for this market were last checked ' + day(last) + '. Listings are not proof of offers available today.';
    return 'These cards link to third-party retailer catalogs. Promotions and availability may change.';
  }
  function reflectUrl() {
    const u = new URL(window.location.href);
    for (const k of ['country', 'tab', 'q', 'merchant', 'sort', 'view']) u.searchParams.delete(k);
    if (state.country !== 'ALL') u.searchParams.set('country', state.country);
    if (state.tab !== 'catalogs') u.searchParams.set('tab', state.tab);
    if (state.query.trim()) u.searchParams.set('q', state.query.trim());
    if (state.merchant !== 'ALL') u.searchParams.set('merchant', state.merchant);
    if (state.sort !== 'featured') u.searchParams.set('sort', state.sort);
    if (state.view !== 'grid') u.searchParams.set('view', state.view);
    window.history.replaceState(null, '', u.pathname + u.search + u.hash);
  }
  function paint() {
    $('stat-catalogs').textContent = String(state.catalogs.length || '—');
    $('stat-countries').textContent = String(state.countries.length || '—');
    $('stat-highlights').textContent = String(state.highlights.length);
    syncMerchantSelect();
    document.querySelectorAll('[data-tab]').forEach(t => {
      const selected = t.dataset.tab === state.tab;
      t.classList.toggle('active', selected);
      t.setAttribute('aria-selected', String(selected));
      t.tabIndex = selected ? 0 : -1;
    });
    $('results').setAttribute('aria-labelledby', state.tab === 'catalogs' ? 'tab-catalogs' : 'tab-highlights');
    $('results').classList.toggle('list', state.view === 'list');
    for (const view of ['grid', 'list']) {
      const el = $(view + '-view');
      el.classList.toggle('is-active', state.view === view);
      el.setAttribute('aria-pressed', String(state.view === view));
    }
    const baseCatalogs = catalogsInCountry();
    const list = state.tab === 'catalogs' ? visibleCatalogs() : visibleHighlights();
    $('catalog-count').textContent = String(baseCatalogs.length);
    $('highlight-count').textContent = String(state.highlights.length);
    $('clear-filters').hidden = !state.query && state.merchant === 'ALL' && state.sort === 'featured';
    $('notice').textContent = noticeText();
    $('notice').hidden = !noticeText();
    const waiting = state.loading || (state.tab === 'highlights' && state.highlightLoading);
    const failure = !!state.error;
    const showEmpty = !waiting && !failure && list.length === 0;
    $('empty').hidden = !showEmpty;
    $('result-summary').textContent = waiting ? 'Loading public data…' : failure ? 'Unable to load catalogs' :
      'Showing ' + list.length + ' ' + (state.tab === 'catalogs' ? 'catalog' : 'highlight') + (list.length === 1 ? '' : 's') +
      (state.country === 'ALL' ? ' across all countries' : ' in ' + countryName(state.country));
    if (waiting || failure) {
      $('results').replaceChildren(node('p', 'loading', waiting ? 'Loading entries…' : 'Please reload to retry.'));
    } else {
      buildCards(list);
    }
    reflectUrl();
  }
  async function readJson(path) {
    const res = await fetch(path, { cache: 'no-cache', credentials: 'omit' });
    if (!res.ok) throw new Error('HTTP ' + res.status);
    return res.json();
  }
  async function selectCountry(code) {
    state.country = state.countries.includes(code) || code === 'ALL' ? code : 'DE';
    state.merchant = 'ALL';
    const requestId = ++state.selectedRequest;
    state.highlights = [];
    state.highlightError = '';
    const entries = state.index && Array.isArray(state.index.countries) ? state.index.countries : [];
    const feedCountries = state.country === 'ALL'
      ? entries.map(e => e.code)
      : entries.filter(e => e.code === state.country).map(e => e.code);
    state.highlightLoading = feedCountries.length > 0;
    paint();
    if (!state.highlightLoading) return;
    const loads = await Promise.allSettled(feedCountries.map(async code => {
      let feed = state.highlightsByCountry.get(code);
      if (!feed) {
        feed = await readJson('../promos/highlights/' + code + '.json');
        if (!feed || feed.schema !== 'pretio.product_highlights.v1' || feed.country !== code || !Array.isArray(feed.items)) {
          throw new Error('Invalid highlight format (' + code + ')');
        }
        state.highlightsByCountry.set(code, feed);
      }
      return feed.items.map(item => Object.assign({}, item, { country_code: code }));
    }));
    if (requestId !== state.selectedRequest) return;
    const allowedCatalogs = new Set(catalogsInCountry().map(c => c.id));
    state.highlights = loads.flatMap(result => result.status === 'fulfilled'
      ? result.value.filter(item => item && allowedCatalogs.has(item.catalog_id))
      : []);
    const failures = loads.filter(r => r.status === 'rejected');
    if (failures.length) state.highlightError = failures.length + ' of ' + loads.length + ' feeds unavailable; retry later.';
    state.highlightLoading = false;
    paint();
  }
  function populateCountries() {
    const codes = new Set();
    for (const c of state.catalogs) for (const loc of c.locations || []) {
      if (loc.country_code) codes.add(loc.country_code);
      if (loc.country_code && loc.country) nameByCountry.set(loc.country_code, loc.country);
    }
    state.countries = [...codes].sort((a, b) => countryName(a).localeCompare(countryName(b), 'en'));
    const options = [new Option('All countries', 'ALL')].concat(state.countries.map(c => new Option(countryName(c) + ' (' + c + ')', c)));
    $('country').replaceChildren(...options);
  }
  function parseQuery() {
    const p = new URLSearchParams(window.location.search);
    const requested = String(p.get('country') || '').toUpperCase();
    const localeRegion = ((navigator.language || '').split('-')[1] || '').toUpperCase();
    state.country = requested || (state.countries.includes(localeRegion) ? localeRegion : 'ID');
    if (state.country !== 'ALL' && !state.countries.includes(state.country)) state.country = 'DE';
    state.tab = p.get('tab') === 'highlights' ? 'highlights' : 'catalogs';
    state.merchant = p.get('merchant') || 'ALL';
    state.sort = ['featured', 'name', 'recent'].includes(p.get('sort')) ? p.get('sort') : 'featured';
    state.view = p.get('view') === 'list' ? 'list' : 'grid';
    state.query = (p.get('q') || '').slice(0, 150);
    $('search').value = state.query;
    $('country').value = state.country;
    $('sort').value = state.sort;
  }
  function reset() {
    state.query = ''; state.merchant = 'ALL'; state.sort = 'featured';
    $('search').value = ''; $('sort').value = 'featured'; paint(); $('search').focus();
  }
  function bindControls() {
    $('search').addEventListener('input', e => { state.query = e.target.value.slice(0, 150); paint(); });
    $('country').addEventListener('change', e => { selectCountry(e.target.value); });
    $('merchant').addEventListener('change', e => { state.merchant = e.target.value; paint(); });
    $('sort').addEventListener('change', e => { state.sort = e.target.value; paint(); });
    document.querySelectorAll('[data-tab]').forEach(button => button.addEventListener('click', () => {
      state.tab = button.dataset.tab;
      state.merchant = 'ALL';
      paint();
    }));
    $('grid-view').addEventListener('click', () => { state.view = 'grid'; paint(); });
    $('list-view').addEventListener('click', () => { state.view = 'list'; paint(); });
    $('clear-filters').addEventListener('click', reset);
    $('empty-reset').addEventListener('click', reset);
    document.addEventListener('keydown', e => {
      if (e.key === '/' && !e.altKey && !e.ctrlKey && !e.metaKey && !['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) {
        e.preventDefault(); $('search').focus();
      }
    });
    window.addEventListener('popstate', () => { parseQuery(); selectCountry(state.country); });
  }
  async function init() {
    bindControls();
    try {
      const catalog = await readJson('../promos/catalog_app.json');
      if (!catalog || catalog.schema !== 'pretio.catalog_app.v2' || !Array.isArray(catalog.items)) throw new Error('Unexpected catalog format');
      state.catalogs = catalog.items;
      populateCountries();
      try {
        const index = await readJson('../promos/highlights/index.json');
        if (index && index.schema === 'pretio.product_highlights.index.v2' && Array.isArray(index.countries)) state.index = index;
      } catch (_) {
        state.index = null; // Keep the retailer catalog usable if highlights are unavailable.
      }
      parseQuery();
      state.loading = false;
      await selectCountry(state.country);
    } catch (error) {
      state.error = error instanceof Error ? error.message : 'Could not read catalog';
      state.loading = false; paint();
    }
  }
  init();
})();
