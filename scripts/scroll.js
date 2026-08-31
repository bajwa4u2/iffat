/**
 * Scroll-linked section reveal.
 * Implements scroll-choreography.md doctrine: substrate-clock pacing,
 * IntersectionObserver triggered, reduced-motion aware, never scroll-jacked.
 */
(function () {
  'use strict';

  // Respect prefers-reduced-motion at runtime
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (prefersReducedMotion) {
    // All sections appear immediately; no observer needed
    document.querySelectorAll('.section').forEach(function (el) {
      el.classList.add('revealed');
    });
    return;
  }

  // IntersectionObserver — fire when section's top reaches 75% of viewport
  const observerOptions = {
    threshold: 0,
    rootMargin: '0px 0px -25% 0px',
  };

  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        // Once revealed, stop observing — section stays revealed regardless of scroll
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.section').forEach(function (el) {
    observer.observe(el);
  });

  // Register toggle (dark / light switcher)
  const toggle = document.querySelector('[data-register-toggle]');
  if (toggle) {
    toggle.addEventListener('click', function () {
      const current = document.documentElement.getAttribute('data-register');
      const next = current === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-register', next);
      try { localStorage.setItem('register', next); } catch (e) { /* private mode */ }
    });

    // Restore preference on load
    try {
      const saved = localStorage.getItem('register');
      if (saved === 'light' || saved === 'dark') {
        document.documentElement.setAttribute('data-register', saved);
      }
    } catch (e) { /* private mode */ }
  }
})();
(()=>{const b=document.querySelector('.member-menu-toggle'),p=document.querySelector('#member-mobile-menu');if(!b||!p)return;const close=()=>{b.setAttribute('aria-expanded','false');p.hidden=true;p.classList.remove('is-open');document.body.classList.remove('menu-open')};b.addEventListener('click',()=>{const open=b.getAttribute('aria-expanded')!=='true';b.setAttribute('aria-expanded',String(open));p.hidden=!open;p.classList.toggle('is-open',open);document.body.classList.toggle('menu-open',open);if(open)p.querySelector('a')?.focus()});p.addEventListener('click',e=>{if(e.target.closest('a'))close()});document.addEventListener('keydown',e=>{if(e.key==='Escape')close()});window.addEventListener('resize',()=>{if(innerWidth>800)close()})})();
