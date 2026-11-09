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
const themeStylesheet = document.querySelector('#theme-stylesheet');
const themeColor = document.querySelector('meta[name="theme-color"]');

if (themeToggle && themeStylesheet) {
  const updateThemeToggle = () => {
    const switchTo = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
    const label = `Switch to ${switchTo} mode`;
    themeToggle.setAttribute('aria-label', label);
    themeToggle.title = label;
    themeToggle.querySelector('.theme-toggle-symbol').textContent = switchTo === 'light' ? '☀' : '☾';
    themeToggle.querySelector('.theme-toggle-label').textContent = switchTo === 'light' ? 'Light' : 'Dark';
  };

  themeToggle.addEventListener('click', () => {
    const theme = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
    document.documentElement.dataset.theme = theme;
    themeStylesheet.href = theme === 'light' ? 'style.css' : 'style-dark.css';
    if (themeColor) themeColor.content = theme === 'light' ? '#F3EEE3' : '#090909';
    try {
      localStorage.setItem('maxqstudio-theme', theme);
    } catch (_) {
      // Toggling remains functional when browser storage is blocked.
    }
    updateThemeToggle();
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
