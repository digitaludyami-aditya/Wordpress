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

## Editing content

Don't edit `dist/` by hand. Edit the source and rebuild:

- `src/data.py`: contact details, all 8 services (card text **and** Quick Look popup content), FAQs
- `build.py`: page sections and layouts
- `src/core.css`, `src/pages/*.css`: styles · `src/core.js`: slider, popup, forms · `src/icons.svg`: icons

```bash
python3 build.py        # regenerates dist/ and preview/
```

Open `preview/*.html` in a browser to check a page locally.

## Please confirm before going live

A few statements are reasonable defaults, not facts taken from your site. Check or edit them in `src/data.py` and `build.py`:
- "We usually reply on the same working day", "Monday to Saturday", and "audit within three to five working days"
- The tools list in the platforms marquee (Semrush, Ahrefs, HubSpot, Zoho, etc.)
- The Launch / Grow / Scale plan contents (all shown as "Custom quote", no prices)
