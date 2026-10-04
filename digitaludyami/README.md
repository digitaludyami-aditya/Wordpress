# Digital Udyami: Website Pages (Elementor HTML widgets)

Self-contained, mobile-first page designs for **www.digitaludyami.com**. Each file in `dist/` is pasted into **one Elementor HTML widget**.

## Pages

| File | WordPress page URL | Status |
|---|---|---|
| `dist/home.html` | `/` | Replaces Home Page V13 |
| `dist/services.html` | `/services/` | Services hub (all 8 services) |
| `dist/about.html` | `/about/` | About page |
| `dist/contact.html` | `/contact/` | Contact page |
| `dist/industries.html` | `/industries/` | **New page** |
| `dist/free-digital-audit.html` | `/free-digital-audit/` | **New page** (lead magnet) |
| `dist/privacy-policy.html` | `/privacy-policy/` | **New page** |
| `dist/terms-and-conditions.html` | `/terms-and-conditions/` | **New page** |
| `dist/digital-india-roadmap.html` | `/digitalindiaroadmap/` | Road Map 2026 landing page v5 (₹24,999/month, festive price, price calculator). Own header/footer: use the **Elementor Canvas** template. Set `data-catalogue` at the top to your catalogue PDF link. Source: `src/roadmap.html` |
| `dist/portfolio.html` | `/portfolio/` | Portfolio with Type / Technology / Category filters. **Run the capture tool first**, see *Portfolio* below |
| `dist/blog-single-post.html` | Every blog post | **Single post template**: see *Installing the blog post template* below. Source: `src/blog-post.html` |
| `dist/header.html` | Every page | **Site header V2**: see *Installing the header* below |
| `dist/footer.html` | Every page | **Site footer**: see *Installing the footer* below |

The SEO title, meta description and focus keyword for each page are in the comment at the top of each file.

## What changed on the home page (vs V13)

- **Hero slider.** 5 slides (Growth, SEO, Ads, Web & Brand, AI) with autoplay, a progress bar, arrows, pause, swipe on phones and keyboard arrows. Autoplay pauses on hover, when the tab is hidden, and for visitors who prefer reduced motion. Only slide 1 contains the H1.
- **Removed the in-page header/nav bar** (brand mark + Home/Services/About/Contact pills). Your theme header already handles navigation.
- **Services in a 2×3 grid.** 3 columns × 2 rows on desktop, 2 columns × 3 rows on mobile (compact cards).
- **Quick Look popup** on every service. It shows an overview, what's included, how we start, who it suits and what we measure, with *Full details* and *Discuss on WhatsApp* buttons and Previous/Next to browse services. On phones it opens as a bottom sheet (swipe down or ✕ to close). Direct link format: `/#quick-look-seo-services`.
- The two AI services moved into their own **AI Solutions** section so the core grid stays exactly 2×3.
- **New sections:** trust bar, 5-step process, platforms marquee, engagement plans (Launch / Grow / Scale), free-audit banner, and contact cards with social links.
- **Mobile:** sticky Call + WhatsApp bar (appears after the first screen), 16px form inputs (no iOS zoom), 48px+ tap targets, no horizontal scroll. Desktop gets a floating WhatsApp button.

## How to install in WordPress

1. Create or edit the page and choose the **Elementor Full Width** template. Hide the page title.
2. Add one **HTML** widget and paste the full contents of the matching `dist/*.html` file.
3. Set the SEO title and meta description in your SEO plugin, using the comment at the top of the file.
4. Create the two new pages with slugs `industries` and `free-digital-audit`, and add them to your menu.
5. Before launch, replace the Unsplash image URLs with your own WordPress-hosted WebP images.

## Installing the header

- Elementor Pro → Templates → Theme Builder → **Header** → edit your current header (or Add New). Delete the old V1 HTML widget, add one HTML widget, paste `dist/header.html`, and set the display condition to **Entire Site**.
- Set the header container to **Full Width** with **0 padding**. Do **not** turn on Elementor's Sticky option, because the header is already sticky. To make it non-sticky, change `data-duh-sticky="true"` to `"false"`.
- Links: Home, About, Services (mega menu), Blog (`/blog`), Digital India Roadmap (`/digitalindiaroadmap`), Let's Talk (`/contact`).
- `preview/*-full-site.html` shows each page with the header and footer together.

## Installing the blog post template

Elementor Pro → Templates → Theme Builder → **Single Post** → Add New (no preset). In one **Full Width** container with 0 padding, add these widgets top to bottom:

1. **HTML** widget: paste `dist/blog-single-post.html`
2. **Post Title** (HTML tag H1)
3. **Featured Image**
4. **Post Content**
5. **Post Comments** (optional)

Publish with the condition **Posts → All**. The design moves widgets 2–5 into its layout automatically, so leave their styling at the defaults. The article text stays normal WordPress HTML, which is good for SEO. Author, category, tags and "Keep reading" come from the WordPress REST API; if the REST API is blocked, those parts hide quietly. You get a table of contents (built from H2/H3 when a post has 2+ H2s), a reading progress bar, share buttons, a mid-article CTA (posts with 3+ H2s), an author box, and a Road Map sidebar card. Change the WhatsApp number and links in the `data-*` attributes on the first `<div>`. Preview: `preview/blog-single-post.html`.

## Installing the footer

- **Elementor Pro:** Templates → Theme Builder → Footer → Add New. Add one HTML widget, paste `dist/footer.html`, publish, and set the display condition to **Entire Site**.
- **Free Elementor:** paste `dist/footer.html` into an HTML widget at the bottom of each page, and hide the theme's default footer (for example, Astra → Customize → Footer Builder).
- Make sure `/privacy-policy/` and `/terms-and-conditions/` exist, or change the `LEGAL` links in `build.py`.

## Editing content

Don't edit `dist/` by hand. Edit the source and rebuild:

- `src/data.py`: contact details, all 8 services (card text **and** Quick Look popup content), FAQs
- `build.py`: page sections and layouts
- `src/core.css`, `src/pages/*.css`: styles · `src/core.js`: slider, popup, forms · `src/icons.svg`: icons

```bash
python3 build.py        # regenerates dist/ and preview/
```

Open `preview/*.html` in a browser to check a page locally.

## Portfolio

The site list is `src/portfolio_sites.py`. Type and Category there are best guesses from each site's name (rows marked `True` in the last column need checking). Technology is detected from the live site.

1. `cd tools && npm install playwright && npx playwright install chromium`
2. `node capture.js`. For each site it opens the home page, **skips sites that are offline, suspended or parked**, saves a screenshot to `portfolio/shots/<name>.jpg`, detects WordPress / Shopify / React / Wix and so on, and prints each site's title so you can check its Category. Re-run one site with `--only hitechpipes-in`.
3. Upload `portfolio/shots/*.jpg` to WordPress at `wp-content/uploads/portfolio/` (Media Library, or FTP so the filenames stay the same).
4. `python3 build.py`, then paste `dist/portfolio.html` into an HTML widget on `/portfolio/`.

Without step 2 the page still works, but it lists every site (including any that are offline), takes live screenshots from WordPress mShots, and has no Technology filter. The file starts with a warning comment while that is the case. To preview with local screenshots: `PF_SHOTS_BASE=file:///path/to/shots/ python3 build.py`.

## Legal pages: before publishing

Fill in the business details at the top of `src/legal.py` (legal business name, registered address, Grievance Officer name, court city, payment and notice periods), then run `python3 build.py`. Empty values fall back to neutral wording, so the pages are safe to publish as they are. They are a starting point, not legal advice: please have a lawyer review them. If you add a cookie banner or new tools (for example Hotjar or a CRM), update the Cookies and Sharing sections.

## Please confirm before going live

A few statements are reasonable defaults, not facts taken from your site. Check or edit them in `src/data.py` and `build.py`:
- "We usually reply on the same working day", "Monday to Saturday", and "audit within three to five working days"
- The tools list in the platforms marquee (Semrush, Ahrefs, HubSpot, Zoho, etc.)
- The Launch / Grow / Scale plan contents (all shown as "Custom quote", no prices)
