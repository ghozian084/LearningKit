// Fit + interaction check for a direct-teaching board.
// Usage: NODE_PATH=$(npm root -g) node check_board.js <path/to/bd-0N.html> [mathjax-es5-dir]
// Reveals every step on every slide and reports anything that runs past the slide at
// 1280x720, 1366x768 and 1920x1080, MathJax errors, JS errors, and tests reveal keys + timer.
const { chromium } = require('playwright'); const path = require('path');
const FILE = 'file://' + path.resolve(process.argv[2]); const MJ = process.argv[3];
(async () => {
  const b = await chromium.launch(); let ok = true;
  const route = pg => MJ ? pg.route(/cdn\.jsdelivr\.net\/npm\/mathjax.*/, r => r.fulfill({ path: path.join(MJ, r.request().url().split('/es5/')[1]) })) : null;
  for (const [w, h] of [[1280, 720], [1366, 768], [1920, 1080]]) {
    const pg = await b.newPage({ viewport: { width: w, height: h } }); const errs = [];
    pg.on('pageerror', e => errs.push(e.message)); pg.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await route(pg); await pg.goto(FILE); await pg.waitForTimeout(3500);
    const res = await pg.evaluate(() => {
      document.querySelectorAll('.step').forEach(s => s.classList.add('shown'));
      return [...document.querySelectorAll('.slide')].map((s, i) => {
        s.classList.add('active'); const sb = s.getBoundingClientRect(); let worst = 0, who = '';
        s.querySelectorAll('.content-layer *').forEach(e => { const r = e.getBoundingClientRect(); if (!r.height) return;
          const o = Math.max(r.bottom - (sb.bottom - 4), r.right - (sb.right - 4)); if (o > worst) { worst = o; who = (e.className || e.tagName) + ': ' + (e.textContent || '').trim().slice(0, 40); } });
        s.classList.remove('active');
        return { slide: i + 1, overflowPx: Math.round(worst), who, mathErrors: s.querySelectorAll('mjx-merror').length };
      }).filter(x => x.overflowPx > 0 || x.mathErrors);
    });
    if (res.length || errs.length) ok = false;
    console.log(`${w}x${h}`, res.length ? JSON.stringify(res, null, 1) : 'all slides fit', errs.length ? errs : '');
    await pg.close();
  }
  const pg = await b.newPage({ viewport: { width: 1366, height: 768 } }); await route(pg); await pg.goto(FILE); await pg.waitForTimeout(1500);
  const n = await pg.evaluate(() => slides.length); let presses = 0;
  while (presses < 2000 && await pg.evaluate(() => currentSlide < slides.length - 1 || document.querySelectorAll('.slide.active .step:not(.shown)').length)) { await pg.keyboard.press('Space'); presses++; }
  const hidden = await pg.evaluate(() => document.querySelectorAll('.step:not(.shown)').length);
  const tslide = await pg.evaluate(() => [...slides].findIndex(s => s.dataset.timer));
  let timer = 'no timer slides';
  if (tslide >= 0) { await pg.evaluate(i => { currentSlide = i; updateNav(); timerStart(); }, tslide); await pg.waitForTimeout(2200); timer = await pg.textContent('#tmr'); await pg.evaluate(() => timerReset()); }
  console.log(`${n} slides · Space walked through everything in ${presses} presses · steps left hidden: ${hidden} · timer after 2 s: ${timer}`);
  if (hidden) ok = false;
  await b.close(); process.exit(ok ? 0 : 1);
})();
