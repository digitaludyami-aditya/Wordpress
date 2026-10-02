#!/usr/bin/env node
/*
 Digital Udyami portfolio capture tool
 --------------------------------------
 For every site in portfolio/sites.json it:
   1. opens the home page and checks the site is really live (not 404, suspended, parked or expired)
   2. takes a screenshot of the top of the home page  -> out/shots/<slug>.jpg
   3. detects the technology (WordPress, Shopify, React, Wix, ...)
   4. writes out/status.json, which build.py reads

 Run on your own computer (needs Node 18+):
   cd digitaludyami/tools
   npm install playwright && npx playwright install chromium
   node capture.js                       # all sites
   node capture.js --only hitechpipes-in # re-run one site (keeps the others)
   node capture.js --sites ../portfolio/sites.json --out ../portfolio   # defaults shown
*/
const fs = require('fs');
const path = require('path');
const args = process.argv.slice(2);
const arg = (n, d) => { const i = args.indexOf('--' + n); return i > -1 ? args[i + 1] : d; };
const SITES = path.resolve(arg('sites', path.join(__dirname, '..', 'portfolio', 'sites.json')));
const OUT = path.resolve(arg('out', path.join(__dirname, '..', 'portfolio')));
const ONLY = arg('only', '');
const W = 1366, H = 768, TIMEOUT = 35000;

let chromium;
try { ({ chromium } = require('playwright')); }
catch (e) { console.error('Playwright is not installed. Run:  npm install playwright && npx playwright install chromium'); process.exit(1); }

const DEAD_TITLE = /(suspended|parked|domain (is )?for sale|buy this domain|expired|account has been|default web page|coming soon|under construction|site can.t be reached|404|not found|index of \/|welcome to nginx|apache2|it works!?|this domain)/i;
const base = h => h.replace(/^www\./, '').toLowerCase();

function detect(html, headers, finalUrl) {
  const h = html.toLowerCase(), hd = JSON.stringify(headers || {}).toLowerCase();
  const found = [];
  if (/cdn\.shopify\.com|shopify\.theme|myshopify\.com|x-shopid|x-shopify/.test(h + hd)) found.push('Shopify');
  if (/wp-content\/|wp-includes\/|wp-json|name=["']generator["'][^>]*wordpress/.test(h) || /x-powered-by.*wordpress|link.*wp-json/.test(hd)) found.push('WordPress');
  if (/woocommerce/.test(h)) found.push('WooCommerce');
  if (/static\.wixstatic\.com|wix\.com website builder|x-wix/.test(h + hd)) found.push('Wix');
  if (/webflow\.com|data-wf-page|data-wf-site/.test(h)) found.push('Webflow');
  if (/squarespace/.test(h)) found.push('Squarespace');
  if (/__next_data__|\/_next\/static/.test(h)) found.push('Next.js');
  if (/data-reactroot|id=["']root["']|id=["']__next["']|react-dom|\/static\/js\/main\.[a-f0-9]+\.js|vite|webpackjsonp/.test(h) && !found.includes('WordPress') && !found.includes('Shopify')) found.push('React');
  if (/ng-version|<app-root/.test(h)) found.push('Angular');
  if (/id=["']__nuxt["']|\/_nuxt\//.test(h)) found.push('Vue');
  if (/elementor/.test(h)) found.push('Elementor');
  // pick a single primary technology for the filter
  const primary = ['Shopify', 'WordPress', 'Wix', 'Webflow', 'Squarespace', 'Next.js', 'React', 'Angular', 'Vue']
    .find(t => found.includes(t));
  const tech = primary === 'Next.js' ? 'React' : primary; // group Next.js with React
  return { tech: tech || 'HTML', all: found };
}

(async () => {
  const sites = JSON.parse(fs.readFileSync(SITES, 'utf8'));
  fs.mkdirSync(path.join(OUT, 'shots'), { recursive: true });
  const statusFile = path.join(OUT, 'status.json');
  const status = fs.existsSync(statusFile) ? JSON.parse(fs.readFileSync(statusFile, 'utf8')) : {};
  const browser = await chromium.launch();
  const ctx = await browser.newContext({
    viewport: { width: W, height: H }, deviceScaleFactor: 1, ignoreHTTPSErrors: false,
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36',
    locale: 'en-IN',
  });
  const list = sites.filter(s => !ONLY || s.slug === ONLY);
  console.log(`Checking ${list.length} site(s)...\n`);
  for (const s of list) {
    const rec = { url: s.url, active: false, checked: new Date().toISOString() };
    for (let attempt = 1; attempt <= 2 && !rec.active; attempt++) {
      const page = await ctx.newPage();
      try {
        const resp = await page.goto(s.url, { waitUntil: 'domcontentloaded', timeout: TIMEOUT });
        await page.waitForLoadState('networkidle', { timeout: 9000 }).catch(() => {});
        await page.waitForTimeout(1800); // let hero sliders / animations settle
        const code = resp ? resp.status() : 0;
        const finalUrl = page.url();
        const title = (await page.title().catch(() => '')).trim();
        const text = await page.evaluate(() => (document.body ? document.body.innerText : '').trim()).catch(() => '');
        const desc = await page.evaluate(() => { const m = document.querySelector('meta[name="description"]'); return m ? m.content : ''; }).catch(() => '');
        const html = await page.content();
        const sameSite = base(new URL(finalUrl).hostname) === base(new URL(s.url).hostname);
        rec.http = code; rec.finalUrl = finalUrl; rec.title = title; rec.description = desc.slice(0, 200);
        if (code >= 400 || code === 0) rec.reason = 'HTTP ' + code;
        else if (!sameSite) rec.reason = 'redirects to ' + new URL(finalUrl).hostname;
        else if (DEAD_TITLE.test(title) && text.length < 1500) rec.reason = 'looks parked/suspended: "' + title + '"';
        else if (text.length < 80) rec.reason = 'page is blank';
        else {
          // hide cookie banners / chat bubbles that ruin the screenshot
          await page.addStyleTag({ content: '[id*="cookie" i],[class*="cookie" i],[id*="cmplz" i],[class*="cmplz" i],[class*="consent" i],[id*="onetrust" i],[class*="gdpr" i]{display:none!important}' }).catch(() => {});
          await page.evaluate(() => window.scrollTo(0, 0));
          await page.waitForTimeout(300);
          await page.screenshot({ path: path.join(OUT, 'shots', s.slug + '.jpg'), type: 'jpeg', quality: 80, clip: { x: 0, y: 0, width: W, height: H } });
          const d = detect(html, resp.headers(), finalUrl);
          rec.active = true; rec.tech = d.tech; rec.techAll = d.all; rec.shot = s.slug + '.jpg';
          delete rec.reason;
        }
      } catch (err) {
        rec.reason = String(err.message || err).split('\n')[0].slice(0, 120);
      } finally { await page.close(); }
    }
    status[s.slug] = rec;
    console.log(`${rec.active ? 'ACTIVE  ' : 'INACTIVE'}  ${s.slug.padEnd(34)} ${rec.active ? (rec.tech || '').padEnd(10) + ' ' + (rec.title || '').slice(0, 50) : rec.reason}`);
  }
  await browser.close();
  fs.writeFileSync(statusFile, JSON.stringify(status, null, 2));
  const all = Object.values(status);
  console.log(`\nDone. ${all.filter(r => r.active).length} active, ${all.filter(r => !r.active).length} inactive.`);
  console.log(`Wrote ${statusFile}\nNext: upload ${path.join(OUT, 'shots')}/*.jpg to WordPress (Media or wp-content/uploads/portfolio/), then run  python3 build.py`);
})();
