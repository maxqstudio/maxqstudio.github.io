const menuToggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav');

if (menuToggle && nav) {
  menuToggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', String(isOpen));
  });

  nav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      nav.classList.remove('open');
      menuToggle.setAttribute('aria-expanded', 'false');
    });
  });
}


const themeToggle = document.querySelector('.theme-toggle');
const darkStylesheet = document.querySelector('#theme-dark-stylesheet');
const lightStylesheet = document.querySelector('#theme-light-stylesheet');
const themeColor = document.querySelector('meta[name="theme-color"]');

if (themeToggle && darkStylesheet && lightStylesheet) {
  const updateThemeToggle = () => {
    const switchTo = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
    const label = `Switch to ${switchTo} mode`;
    themeToggle.setAttribute('aria-label', label);
    themeToggle.title = label;
    themeToggle.querySelector('.theme-toggle-symbol').textContent = switchTo === 'light' ? '☀' : '☾';
    themeToggle.querySelector('.theme-toggle-label').textContent = switchTo === 'light' ? 'Light' : 'Dark';
  };

  // Keep the current theme visible until the target CSS has actually loaded.
  const waitForStylesheet = (link) => {
    if (link.sheet) return Promise.resolve(true);
    if (link.dataset.failed === 'true') return Promise.resolve(false);
    return new Promise((resolve) => {
      const cleanup = () => {
        clearTimeout(timeout);
        link.removeEventListener('load', onLoad);
        link.removeEventListener('error', onError);
      };
      const finish = (loaded) => { cleanup(); resolve(loaded); };
      const onLoad = () => finish(Boolean(link.sheet));
      const onError = () => finish(false);
      const timeout = setTimeout(() => finish(false), 6000);
      link.addEventListener('load', onLoad);
      link.addEventListener('error', onError);
      if (link.sheet || link.dataset.failed === 'true') {
        finish(Boolean(link.sheet));
      }
    });
  };

  themeToggle.addEventListener('click', async () => {
    if (themeToggle.disabled) return;
    const nextTheme = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
    const target = nextTheme === 'light' ? lightStylesheet : darkStylesheet;
    themeToggle.disabled = true;
    try {
      if (!(await waitForStylesheet(target))) {
        themeToggle.title = 'Theme unavailable. Reload to retry.';
        return;
      }
      darkStylesheet.media = nextTheme === 'dark' ? 'all' : 'not all';
      lightStylesheet.media = nextTheme === 'light' ? 'all' : 'not all';
      document.documentElement.dataset.theme = nextTheme;
      if (themeColor) themeColor.content = nextTheme === 'light' ? '#F3EEE3' : '#090909';
      try {
        localStorage.setItem('maxqstudio-theme', nextTheme);
      } catch (_) {
        // Switching works when storage is blocked; reload defaults to dark.
      }
      updateThemeToggle();
    } finally {
      themeToggle.disabled = false;
    }
  });

  updateThemeToggle();
}

const year = document.querySelector('#year');
if (year) year.textContent = new Date().getFullYear();

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
