#!/usr/bin/env python3
"""Build self-contained Elementor HTML widgets for digitaludyami.com.

    python3 build.py

Writes:
  dist/<page>.html     paste the whole file into ONE Elementor HTML widget
  preview/<page>.html  same markup wrapped in a full HTML document for local preview
"""
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))
from data import *  # noqa: E402,F403

CORE_CSS = (SRC / "core.css").read_text()
CORE_JS = (SRC / "core.js").read_text()
ICONS = (SRC / "icons.svg").read_text()
e = html.escape


# ---------------------------------------------------------------- helpers
def icon(name):
    return f'<svg aria-hidden="true"><use href="#{name}"></use></svg>'


def img_url(key, w):
    return f"https://images.unsplash.com/{IMG[key]}?auto=format&fit=crop&w={w}&q=80"


def img(key, alt, sizes="(max-width:760px) 100vw, 50vw", eager=False, cls="", lazy_src=False):
    srcset = ", ".join(f"{img_url(key, w)} {w}w" for w in (480, 800, 1200, 1600))
    load = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    if lazy_src:  # slider slides: JS swaps data-src in when the slide is first shown
        return (f'<img{c} data-src="{img_url(key, 1600)}" srcset="{srcset}" sizes="{sizes}" '
                f'width="1600" height="1000" decoding="async" alt="{e(alt)}">')
    return (f'<img{c} src="{img_url(key, 1200)}" srcset="{srcset}" sizes="{sizes}" '
            f'width="1200" height="800" {load} decoding="async" alt="{e(alt)}">')


def wa(msg):
    from urllib.parse import quote
    return f"https://wa.me/{WHATSAPP}?text={quote(msg)}"


def btn(label, href, kind="primary", ico="dui-arrow", external=False):
    ext = ' target="_blank" rel="noopener"' if external else ""
    return f'<a class="du-btn du-btn-{kind}" href="{href}"{ext}>{e(label)}{icon(ico)}</a>'


def checks(items):
    return '<ul class="du-check-list">' + "".join(f"<li>{icon('dui-check')}{e(t)}</li>" for t in items) + "</ul>"


def head(eyebrow, title, lead="", center=False):
    if center:
        return (f'<div class="du-center-head"><span class="du-eyebrow">{e(eyebrow)}</span><h2>{title}</h2>'
                + (f'<p class="du-lead">{lead}</p>' if lead else "") + "</div>")
    return (f'<div class="du-section-head"><div><span class="du-eyebrow">{e(eyebrow)}</span><h2>{title}</h2></div>'
            + (f'<p class="du-lead">{lead}</p>' if lead else "") + "</div>")


def section(body, cls="du-white", sid=""):
    i = f' id="{sid}"' if sid else ""
    return f'<section class="du-section {cls}"{i}><div class="du-wrap">{body}</div></section>'


# ---------------------------------------------------------------- components
def service_card(slug, n):
    s = SERVICE_BY_SLUG[slug]
    return f'''<article class="du-service-card du-card" data-du-reveal data-du-delay="{n % 3 + 1}">
  <a class="du-service-image" href="{s["url"]}" tabindex="-1" aria-hidden="true">{img(s["img"], "", "(max-width:760px) 50vw, 33vw")}<span class="du-service-label">{e(s["label"])}</span></a>
  <div class="du-service-body">
    <div class="du-service-icon">{icon(s["icon"])}</div>
    <h3><a href="{s["url"]}">{e(s["name"])}</a></h3>
    <p>{e(s["short"])}</p>
    {checks(s["bullets"])}
    <div class="du-service-actions">
      <button type="button" class="du-quick-btn" data-du-quick="{slug}" aria-haspopup="dialog" aria-label="Quick look: {e(s["name"])}">{icon("dui-eye")}Quick Look</button>
      <a class="du-link" href="{s["url"]}">Explore{icon("dui-arrow")}</a>
    </div>
  </div>
</article>'''


def service_grid(slugs, cols2=False):
    cls = "du-service-grid du-cols-2" if cols2 else "du-service-grid"
    return f'<div class="{cls}">' + "".join(service_card(s, i) for i, s in enumerate(slugs)) + "</div>"


def modal():
    data = {s["slug"]: {
        "name": s["name"], "url": s["url"], "img": img_url(s["img"], 1200), "alt": f'{s["name"]} by Digital Udyami',
        "label": s["label"], "tagline": s["tagline"], "overview": s["overview"], "included": s["included"],
        "steps": s["steps"], "ideal": s["ideal"], "metrics": s["metrics"],
    } for s in SERVICES}
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return f'''<div class="du-modal" role="dialog" aria-modal="true" aria-labelledby="du-modal-name" aria-hidden="true">
  <div class="du-modal-backdrop" data-du-close></div>
  <div class="du-modal-panel">
    <button type="button" class="du-modal-close" data-du-close aria-label="Close quick look">{icon("dui-close")}</button>
    <div class="du-modal-scroll">
      <div class="du-modal-media"><img src="" alt="" width="1200" height="420" decoding="async">
        <div class="du-modal-title"><span class="du-eyebrow" data-m="label"></span><h2 id="du-modal-name" data-m="name"></h2><p data-m="tagline"></p></div>
      </div>
      <div class="du-modal-body">
        <p class="du-overview" data-m="overview"></p>
        <div class="du-modal-cols">
          <div>
            <div class="du-modal-block"><h3>What is included</h3><ul class="du-check-list" data-m="included"></ul></div>
            <div class="du-modal-block"><h3>How we start</h3><ol class="du-modal-steps" data-m="steps"></ol></div>
          </div>
          <aside class="du-modal-side">
            <div class="du-modal-block"><h3>Best suited for</h3><div class="du-chips" data-m="ideal"></div></div>
            <div class="du-modal-block"><h3>What we measure</h3><div class="du-chips" data-m="metrics"></div></div>
            <div class="du-modal-block"><h3>Not sure yet?</h3><p style="margin:0;font-size:14px">Ask for a free audit and we will tell you honestly whether this service is the right first step.</p><a class="du-link" href="{URL["audit"]}">Get a free digital audit{icon("dui-arrow")}</a></div>
          </aside>
        </div>
      </div>
    </div>
    <div class="du-modal-foot">
      <div class="du-modal-nav"><button type="button" class="du-flip" data-m="prev">{icon("dui-arrow")}Previous</button><button type="button" data-m="next">Next{icon("dui-arrow")}</button></div>
      <div class="du-btn-row"><a class="du-btn du-btn-outline" data-m="page" href="#"><span>Full details</span>{icon("dui-arrow")}</a><a class="du-btn du-btn-wa" data-m="wa" href="#" target="_blank" rel="noopener"><span class="du-hide-sm">Discuss on&nbsp;</span>WhatsApp{icon("dui-whatsapp")}</a></div>
    </div>
  </div>
</div>
<script type="application/json" id="du-services-data">{payload}</script>'''


def faq(items):
    return '<div class="du-faq-list">' + "".join(
        f'<details class="du-faq" data-du-reveal><summary>{e(q)}</summary><div class="du-faq-answer"><p>{e(a)}</p></div></details>'
        for q, a in items) + "</div>"


def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


PROCESS = [
    ("Discover", "A free conversation and audit to understand your business, customers, competitors and current numbers."),
    ("Plan", "A focused roadmap: which channel first, what success looks like and how it will be measured."),
    ("Build", "Set up the website, tracking, campaigns, content or automations with clear review points."),
    ("Launch", "Go live carefully, check every lead path works and start collecting real performance data."),
    ("Improve", "Monthly reviews in plain language, then optimise what works and fix the weakest step."),
]


def process():
    return '<ol class="du-process">' + "".join(
        f'<li data-du-reveal data-du-delay="{i % 4 + 1}"><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>'
        for i, (t, d) in enumerate(PROCESS)) + "</ol>"


PLANS = [
    ("dui-rocket", "Launch", "For new or early-stage businesses building their digital foundation.", False,
     ["Conversion-ready website or landing page", "Google Business Profile setup", "Basic SEO and tracking setup",
      "Social media profile setup and launch posts", "WhatsApp and call enquiry journey"]),
    ("dui-trend", "Grow", "For businesses that have a foundation and now need consistent enquiries.", True,
     ["Everything in Launch, plus", "Monthly SEO and content", "Google Ads or Meta Ads management",
      "Social media content calendar", "Monthly performance review call"]),
    ("dui-layers", "Scale", "For growing teams that want a connected, measurable growth system.", False,
     ["Everything in Grow, plus", "Multi-channel ads with remarketing", "AI chatbot and lead follow-up automation",
      "CRM and reporting dashboard", "Dedicated growth manager"]),
]


def plans():
    out = []
    for i, (ic, name, who, featured, items) in enumerate(PLANS):
        badge = '<span class="du-plan-badge">Most popular</span>' if featured else ""
        kind = "primary" if featured else "outline"
        out.append(f'''<article class="du-plan du-card{' is-featured' if featured else ''}" data-du-reveal data-du-delay="{i + 1}">{badge}
  <div class="du-icon">{icon(ic)}</div><h3>{name}</h3><p class="du-plan-for">{e(who)}</p>
  <p class="du-plan-price">Custom quote<span>Scoped to your goals after a free discovery call</span></p>
  {checks(items)}
  {btn(f"Discuss the {name} plan", wa(f"Hello Digital Udyami, I am interested in the {name} plan."), kind, "dui-whatsapp", True)}
</article>''')
    return '<div class="du-plans">' + "".join(out) + "</div>"


TOOLS_A = ["Google Ads", "Meta Ads Manager", "Google Analytics 4", "Google Search Console", "Google Tag Manager",
           "Google Business Profile", "Looker Studio", "Semrush", "Ahrefs"]
TOOLS_B = ["WordPress", "Elementor", "WooCommerce", "Shopify", "WhatsApp Business API", "HubSpot", "Zoho CRM",
           "Canva", "Figma", "ChatGPT", "Claude", "Make", "Zapier"]


def marquee(items, reverse=False):
    chips = "".join(f'<span class="du-tool"><i></i>{e(t)}</span>' for t in items)
    # duplicated once so the CSS loop is seamless; the copy is hidden from screen readers
    return (f'<div class="du-marquee{" is-reverse" if reverse else ""}"><div class="du-marquee-track">'
            f'<div style="display:flex;gap:12px" role="list" aria-label="Platforms we work with">{chips}</div>'
            f'<div style="display:flex;gap:12px" aria-hidden="true">{chips}</div></div></div>')


def tools_section(cls="du-white"):
    return section(head("Platforms we work with", "Certified Tools, Familiar Platforms, No Lock-In",
                        "We work inside the platforms your business already uses, set everything up in your name and keep you in control of your data and accounts.", True)
                   + marquee(TOOLS_A) + marquee(TOOLS_B, True), cls)


def audit_banner():
    return section(f'''<div class="du-audit" data-du-reveal>
  <div><span class="du-eyebrow">Free, no obligation</span><h2>Get a Free Digital Growth Audit</h2>
  <p class="du-lead" style="margin-top:16px">Find out what is holding your website, search visibility, ads and social media back, and which fix will make the biggest difference first.</p>
  <div class="du-btn-row">{btn("Claim My Free Audit", URL["audit"], "light")}{btn("Ask on WhatsApp", wa("Hello Digital Udyami, I would like a free digital growth audit."), "ghost", "dui-whatsapp", True)}</div></div>
  <ul class="du-audit-list">{"".join(f"<li>{icon('dui-check')}{t}</li>" for t in ["Website speed, mobile and conversion review", "SEO and Google Business Profile health check", "Ad account and tracking review", "Social media presence snapshot", "Competitor comparison", "Prioritised action plan"])}</ul>
</div>''', "du-soft-bg")


GOALS = ["Build or improve a website", "Get found on Google", "Generate leads with ads", "Grow social media trust",
         "Improve branding", "Automate repetitive work", "Not sure and need a recommendation"]


def lead_form(fid, title, sub, intro, extra_fields="", submit="Continue on WhatsApp"):
    opts = "".join(f"<option>{e(g)}</option>" for g in GOALS)
    return f'''<div class="du-form-card" data-du-reveal data-du-side="right">
  <h3>{title}</h3><p style="margin:0">{sub}</p>
  <form id="{fid}" data-du-form data-du-intro="{e(intro)}" novalidate>
    <div class="du-form-grid">
      <div class="du-field"><label for="{fid}-name">Your name</label><input id="{fid}-name" name="name" required autocomplete="name" placeholder="Full name"></div>
      <div class="du-field"><label for="{fid}-phone">Phone or WhatsApp</label><input id="{fid}-phone" name="phone" required type="tel" inputmode="tel" autocomplete="tel" placeholder="Mobile number"></div>
      <div class="du-field"><label for="{fid}-business">Business or website</label><input id="{fid}-business" name="business" autocomplete="organization" placeholder="Brand or website"></div>
      <div class="du-field"><label for="{fid}-goal">Main goal</label><select id="{fid}-goal" name="goal" required><option value="">Choose one</option>{opts}</select></div>
      {extra_fields}
    </div>
    <button class="du-btn du-btn-primary du-form-submit" type="submit">{submit}{icon("dui-whatsapp")}</button>
    <p class="du-form-note">Your details stay in your browser until you choose to send the WhatsApp message.</p>
    <div class="du-form-status" aria-live="polite"></div>
  </form>
</div>'''


def cta_section(fid, eyebrow, title, lead, form_title, form_sub, intro, extra_fields=""):
    return f'''<section class="du-cta-section" id="contact-form"><div class="du-wrap"><div class="du-cta-grid">
  <div data-du-reveal data-du-side="left"><span class="du-eyebrow">{e(eyebrow)}</span><h2>{title}</h2><p class="du-lead" style="margin-top:18px">{lead}</p>
    <div class="du-btn-row">{btn("Call " + PHONE_DISPLAY, "tel:" + PHONE_TEL, "light", "dui-phone")}{btn("Email Us", "mailto:" + EMAIL, "ghost", "dui-mail")}</div></div>
  {lead_form(fid, form_title, form_sub, intro, extra_fields)}
</div></div></section>'''


EXT = ' target="_blank" rel="noopener"'


def contact_strip():
    cards = [
        ("dui-phone", "Call us", PHONE_DISPLAY, "tel:" + PHONE_TEL, False),
        ("dui-whatsapp", "WhatsApp", "Chat with our team", wa("Hello Digital Udyami, I would like to know more about your services."), True),
        ("dui-mail", "Email", EMAIL, "mailto:" + EMAIL, False),
        ("dui-star", "Google Reviews", "See what clients say", REVIEWS_URL, True),
    ]
    out = "".join(
        f'<a class="du-contact-card" href="{h}"{EXT if ext else ""} data-du-reveal data-du-delay="{i + 1}">'
        f'<div class="du-icon">{icon(ic)}</div><strong>{t}</strong><span>{e(v)}</span></a>'
        for i, (ic, t, v, h, ext) in enumerate(cards))
    return f'<div class="du-contact-strip">{out}</div>'


def socials_row():
    links = "".join(f'<a class="du-social" href="{u}" target="_blank" rel="noopener" aria-label="Digital Udyami on {n}">{icon(i)}</a>'
                    for n, u, i in SOCIALS)
    return f'<div class="du-socials-row"><div><strong>Follow Digital Udyami</strong><p style="margin:2px 0 0;font-size:14px">Tips, campaigns and behind-the-scenes from our work.</p></div><div class="du-socials">{links}</div></div>'


def floating_actions():
    msg = wa("Hello Digital Udyami, I would like to discuss my business growth.")
    return (f'<a class="du-float-wa" href="{msg}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{icon("dui-whatsapp")}</a>'
            f'<nav class="du-mobile-bar" aria-label="Quick contact"><a class="is-call" href="tel:{PHONE_TEL}">{icon("dui-phone")}Call</a>'
            f'<a class="is-wa" href="{msg}" target="_blank" rel="noopener">{icon("dui-whatsapp")}WhatsApp</a></nav>')


def page_hero(crumb, pill, h1, lead, buttons, img_key, img_alt, label):
    return f'''<section class="du-page-hero"><div class="du-wrap"><div class="du-page-hero-grid">
  <div data-du-reveal data-du-side="left">
    <ol class="du-crumbs" aria-label="Breadcrumb"><li><a href="{URL["home"]}">Home</a></li><li aria-current="page">{e(crumb)}</li></ol>
    <div class="du-pill"><span class="du-dot"></span>{e(pill)}</div>
    <h1>{h1}</h1><p class="du-lead">{lead}</p>
    <div class="du-btn-row">{buttons}</div>
  </div>
  <div class="du-photo" data-du-reveal data-du-side="right" data-du-delay="2">{img(img_key, img_alt, eager=True)}<div class="du-photo-label">{e(label)}</div></div>
</div></div></section>'''


def breadcrumb_schema(name, url):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": URL["home"]},
        {"@type": "ListItem", "position": 2, "name": name, "item": url}]}


ORG_SCHEMA = {"@context": "https://schema.org", "@type": "ProfessionalService", "@id": URL["home"] + "#organization",
              "name": "Digital Udyami", "url": URL["home"], "email": EMAIL, "telephone": PHONE_TEL,
              "description": "Digital marketing agency in India offering SEO, website development, Google Ads, Meta Ads, social media marketing, branding and AI automation.",
              "areaServed": {"@type": "Country", "name": "India"}, "priceRange": "₹₹",
              "sameAs": [u for _, u, _ in SOCIALS]}


def services_schema():
    return {"@context": "https://schema.org", "@type": "ItemList", "name": "Digital Udyami Services",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {
                "@type": "Service", "name": s["name"], "url": s["url"], "description": s["tagline"],
                "provider": {"@id": URL["home"] + "#organization"}, "areaServed": "IN"}} for i, s in enumerate(SERVICES)]}


# ---------------------------------------------------------------- pages
def page_home():
    slides = [
        dict(key="team", tag="h1", label="Growth", eyebrow="Digital marketing agency · PAN India",
             title='Digital Marketing Services in India That Help You Get <span class="du-gradient-text">Found, Chosen and Remembered</span>',
             copy="Websites, SEO, Google Ads, Meta Ads, social media, branding and AI automation, connected into one clear growth system for your business.",
             cta=("Explore Our Services", "#services"), card=("One connected growth system", ["Strategy led by people", "Execution assisted by AI", "Reporting you can understand"])),
        dict(key="analytics", tag="h2", label="SEO", eyebrow="SEO · AEO · GEO",
             title='Get Found on Google <span class="du-gradient-text">When Customers Are Searching</span>',
             copy="Rank for the searches that bring buyers, show up on Google Maps and get cited in AI answers from ChatGPT, Gemini and Google AI Overviews.",
             cta=("Quick Look: SEO", "quick:seo-services"), card=("Search visibility", ["Technical SEO fixes", "Local SEO and Maps", "Content that answers buyers"])),
        dict(key="ads", tag="h2", label="Ads", eyebrow="Google Ads · Meta Ads",
             title='Turn Ad Spend Into <span class="du-gradient-text">Qualified Enquiries</span>',
             copy="High-intent Google campaigns and scroll-stopping Meta creatives, with tracking that shows exactly which rupee produced which lead.",
             cta=("Quick Look: Google Ads", "quick:google-ads-management"), card=("Performance marketing", ["Conversion tracking first", "Creative testing", "Lead quality over volume"])),
        dict(key="laptop", tag="h2", label="Web & Brand", eyebrow="Websites · Branding",
             title='Websites and Brands <span class="du-gradient-text">Built to Convert</span>',
             copy="Fast, mobile-first websites and a brand identity that make your business easier to trust, easier to remember and easier to contact.",
             cta=("Quick Look: Websites", "quick:website-development"), card=("Digital foundation", ["Mobile-first design", "Speed and SEO built in", "WhatsApp and form leads"])),
        dict(key="ai", tag="h2", label="AI", eyebrow="AI automation · AI content",
             title='AI Automation That <span class="du-gradient-text">Gives Your Team Time Back</span>',
             copy="WhatsApp chatbots, instant lead follow-up, CRM updates and AI-assisted content, always with a human in control.",
             cta=("Quick Look: AI Automation", "quick:ai-automation"), card=("Practical AI", ["Reply to leads in seconds", "Automated follow-up", "Human oversight"])),
    ]
    slide_html, dot_html = [], []
    for i, s in enumerate(slides):
        first = i == 0
        pic = img(s["key"], "", "100vw", eager=True) if first else img(s["key"], "", "100vw", lazy_src=True)
        label, target = s["cta"]
        if target.startswith("quick:"):
            primary = f'<button type="button" class="du-btn du-btn-primary" data-du-quick="{target[6:]}" aria-haspopup="dialog">{e(label)}{icon("dui-eye")}</button>'
        else:
            primary = btn(label, target)
        slide_html.append(f'''<div class="du-slide{' is-active' if first else ''}" role="group" aria-roledescription="slide" aria-label="{i + 1} of {len(slides)}"{'' if first else ' aria-hidden="true"'}>
  <div class="du-slide-bg">{pic}</div>
  <div class="du-wrap du-slide-inner">
    <div class="du-slide-copy">
      <div class="du-pill du-pill-dark"><span class="du-dot"></span>{e(s["eyebrow"])}</div>
      <{s["tag"]} class="du-slide-title">{s["title"]}</{s["tag"]}>
      <p class="du-slide-text">{e(s["copy"])}</p>
      <div class="du-btn-row">{primary}{btn("Get a Free Audit", URL["audit"], "ghost", "dui-arrow")}</div>
    </div>
    <div class="du-slide-card" aria-hidden="true"><strong>{e(s["card"][0])}</strong>{checks(s["card"][1])}</div>
  </div>
</div>''')
        dot_html.append(f'<button type="button" class="du-slider-dot{" is-active" if first else ""}" aria-label="Show slide {i + 1}: {e(s["label"])}"><span class="du-dot-label">{e(s["label"])}</span><span class="du-dot-bar"><i></i></span></button>')

    hero = f'''<section class="du-hero-slider" data-du-slider aria-roledescription="carousel" aria-label="Digital Udyami highlights">
  <div class="du-slides">{"".join(slide_html)}</div>
  <div class="du-wrap du-slider-ui">
    <div class="du-slider-dots">{"".join(dot_html)}</div>
    <div class="du-slider-arrows">
      <button type="button" class="du-slider-toggle" aria-pressed="false" aria-label="Pause slideshow">{icon("dui-pause")}{icon("dui-play")}</button>
      <button type="button" class="du-slider-prev" aria-label="Previous slide">{icon("dui-chev")}</button>
      <button type="button" class="du-slider-next" aria-label="Next slide">{icon("dui-chev")}</button>
    </div>
  </div>
</section>
<div class="du-trust"><div class="du-wrap"><div class="du-trust-bar">
  <a class="du-trust-item" href="{REVIEWS_URL}" target="_blank" rel="noopener"><span class="du-stars">{icon("dui-star") * 5}</span><span><strong>Rated on Google</strong>Read our reviews</span></a>
  <div class="du-trust-item">{icon("dui-globe")}<span><strong>PAN India delivery</strong>Remote-first collaboration</span></div>
  <div class="du-trust-item">{icon("dui-users")}<span><strong>Human-led strategy</strong>AI-assisted execution</span></div>
  <div class="du-trust-item">{icon("dui-shield")}<span><strong>No fake guarantees</strong>Clear scope and reporting</span></div>
</div></div></div>'''

    pain = section(head("The real growth problem", "Growth Slows When Your Digital Channels Work Separately",
                        "A beautiful website cannot fix weak traffic. Advertising cannot fix a confusing landing page. Content cannot build trust when the brand message changes every week. The strongest opportunity is often in connecting the system.") +
                   '<div class="du-pain-grid">' + "".join(
        f'<article class="du-pain-card du-card" data-du-reveal data-du-delay="{i}"><span class="du-pain-number">0{i + 1}</span><h3>{t}</h3><p>{d}</p></article>'
        for i, (t, d) in enumerate([
            ("Website achhi ho par enquiry na aaye toh growth ruk jaati hai", "Visitors need clear positioning, fast mobile performance and an obvious next step before design can support revenue."),
            ("Ads chal rahe ho par tracking weak ho toh budget waste hota hai", "Clicks feel productive, but the business needs to know which campaign, keyword and page created a useful lead."),
            ("Content post ho par trust build na ho toh attention sales nahi banti", "Consistency matters, but relevance, proof and a recognisable point of view are what move customers closer to action."),
        ])) + "</div>")

    services = section(head("Connected capabilities", "Digital Marketing Services That Work Together",
                            "Start with the biggest bottleneck, then connect the services that improve the complete customer journey. Tap <strong>Quick Look</strong> on any service to see what is included.", True)
                       + service_grid(CORE_SLUGS)
                       + f'<div class="du-btn-row" style="justify-content:center;margin-top:34px">{btn("View All Services", URL["services"], "dark")}</div>',
                       "du-soft-bg", "services")

    ai = section(f'''<div class="du-ai-grid">
  <div data-du-reveal data-du-side="left"><span class="du-eyebrow">AI-powered growth</span><h2>AI Solutions That Save Time Without Losing the Human Touch</h2>
  <p class="du-lead" style="margin-top:16px">Most businesses lose leads because replies are slow and follow-up is manual. We use AI where it removes busywork, and keep people in charge of strategy, quality and customer relationships.</p>
  <div class="du-chips" style="margin-top:22px">{"".join(f'<span class="du-chip">{icon("dui-check")}{t}</span>' for t in ["WhatsApp chatbots", "Lead qualification", "CRM automation", "AI content systems", "Automated reports"])}</div></div>
  {service_grid(AI_SLUGS, True)}
</div>''', "du-dark du-ai-section")

    paths = section(head("Fewer choices, clearer action", "Choose the Growth Outcome You Need First",
                         "You do not need to buy every service at once. Choose the result that matters now, then build the next layer when the foundation is ready.") +
                    '<div class="du-path-grid">' + "".join(
        f'<article class="du-path-card du-card" data-du-reveal data-du-delay="{i}"><div class="du-icon">{icon(ic)}</div><h3>{t}</h3><p>{d}</p><a class="du-link" href="{u}">{l}{icon("dui-arrow")}</a></article>'
        for i, (ic, t, d, u, l) in enumerate([
            ("dui-search", "Visibility chahiye toh search aur content se shuru karein", "Ideal when customers cannot find your business or your website does not answer the questions they search.", SERVICE_BY_SLUG["seo-services"]["url"], "Build organic visibility"),
            ("dui-target", "Leads chahiye toh ads aur landing page ko connect karein", "Ideal when the business needs faster demand capture and a measurable path from click to enquiry.", SERVICE_BY_SLUG["google-ads-management"]["url"], "Build a lead system"),
            ("dui-automation", "Efficiency chahiye toh AI se repetitive work kam karein", "Ideal when leads, follow-up, support, reporting or content workflows consume too much manual time.", SERVICE_BY_SLUG["ai-automation"]["url"], "Explore practical automation"),
        ])) + "</div>")

    proc = section(head("How we work", "A Simple 5-Step Process From First Call to Growth",
                        "Clear steps, clear owners and clear review points, so you always know what is happening and why.", True)
                   + process()
                   + f'<div class="du-btn-row" style="justify-content:center;margin-top:34px">{btn("Start With Step 1: Free Audit", URL["audit"])}</div>', "du-soft-bg")

    why = section(head("Trust before the sale", "Why Businesses Choose Digital Udyami",
                       "The objective is not to make digital marketing sound complicated. It is to make the business decision clearer and the execution easier to understand.", True) +
                  '<div class="du-why-grid">' + "".join(
        f'<article class="du-why-card" data-du-reveal data-du-delay="{i}"><div class="du-icon">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></article>'
        for i, (ic, t, d) in enumerate([
            ("dui-target", "Business outcome pe focus rahe", "Work is connected to enquiries, sales support, trust, efficiency and customer experience."),
            ("dui-shield", "Promises realistic aur reporting clear rahe", "No guaranteed ranking or lead claims. Scope, priorities and measurement stay visible."),
            ("dui-users", "Human judgement ke saath AI use ho", "AI supports research, production and workflows while people remain responsible for strategy and quality."),
            ("dui-globe", "PAN India delivery simple rahe", "Remote collaboration, clear review points and structured communication support businesses across India."),
        ])) + f'</div><div class="du-btn-row" style="justify-content:center;margin-top:34px">{btn("About Digital Udyami", URL["about"], "light")}{btn("Read Google Reviews", REVIEWS_URL, "ghost", "dui-star", True)}</div>', "du-dark")

    inds = [("founders", "Startups and MSMEs", "Clear foundations, focused acquisition and practical budgets"),
            ("design", "D2C and E-commerce", "Store experience, demand capture and repeatable content"),
            ("office", "Professional Services", "Authority, trust and qualified enquiry journeys"),
            ("analytics", "B2B and Manufacturing", "Longer sales cycles, lead quality and clear information"),
            ("ai", "Growth-Stage Teams", "Automation, reporting and connected execution")]
    industries = section(head("Indian market relevance", "Built for Businesses at Different Growth Stages",
                              "The same service should not look identical for every company. Priorities change with the sales cycle, customer value, geography, team size and digital maturity.") +
                         '<div class="du-industry-grid">' + "".join(
        f'<a class="du-industry-item" href="{URL["industries"]}" data-du-reveal data-du-delay="{i}">{img(k, "", "(max-width:760px) 100vw, 33vw")}<div class="du-industry-copy"><strong>{t}</strong><span>{d}</span></div></a>'
        for i, (k, t, d) in enumerate(inds)) +
        f'</div><div class="du-btn-row" style="justify-content:center;margin-top:30px">{btn("See Industries We Serve", URL["industries"], "outline")}</div>')

    pricing = section(head("Engagement models", "Flexible Plans for Every Growth Stage",
                           "Every business is different, so every plan is scoped after a free discovery call. These are the three most common starting points.", True) + plans(), "du-white")

    faqs = section(head("Decision support", "Questions Businesses Ask Before Starting",
                        "Clear answers reduce uncertainty and help you choose a sensible first step.", True) + faq(FAQ_HOME), "du-soft-bg")

    contact = section(head("Talk to us", "Reach Digital Udyami Your Way", "", True) + contact_strip() + socials_row(), "du-white")

    cta = cta_section("du-home-form", "Start with the right next step", "Tell Us What Is Slowing Your Growth",
                      "Share four quick details. The form prepares a WhatsApp message so you can review it before sending.",
                      "Aapki priority samajhkar right starting point choose karein", "Short form. Clear conversation. No unnecessary questions.",
                      "I want to discuss a digital growth requirement.")

    body = hero + pain + services + ai + paths + proc + why + industries + tools_section("du-soft-bg") + pricing + audit_banner() + faqs + cta + contact
    schema = [ORG_SCHEMA, {"@context": "https://schema.org", "@type": "WebSite", "name": "Digital Udyami", "url": URL["home"]},
              services_schema(), faq_schema(FAQ_HOME)]
    return body, schema


def page_services():
    hero = page_hero("Services", "Full-service digital marketing agency",
                     'Digital Marketing Services <span class="du-gradient-text">Built Around Your Growth Goal</span>',
                     "Eight connected services covering how customers find you, trust you and contact you. Start with one, add the next when the foundation is ready. Tap <strong>Quick Look</strong> on any service for a full summary.",
                     btn("See All Services", "#core-services") + btn("Get a Free Audit", URL["audit"], "outline"),
                     "planning", "Digital Udyami team planning a client growth strategy", "Strategy, execution and reporting under one roof")
    core = section(head("Marketing and growth", "Core Digital Marketing Services",
                        "The channels that bring customers to your business and convince them to get in touch.") + service_grid(CORE_SLUGS), "du-white", "core-services")
    ai = section(head("AI solutions", "AI Automation and Content Services",
                      "Practical AI that speeds up response, follow-up and content production while people stay in control.") + service_grid(AI_SLUGS, True), "du-soft-bg", "ai-services")
    compare = section(head("Which service first?", "Match the Service to Your Biggest Bottleneck", "", True) + '''<div class="du-table-wrap" data-du-reveal><table class="du-table">
<thead><tr><th scope="col">If your problem is…</th><th scope="col">Start with</th><th scope="col">Then add</th></tr></thead><tbody>''' + "".join(
        f'<tr><td>{p}</td><td><button type="button" class="du-table-link" data-du-quick="{a}">{SERVICE_BY_SLUG[a]["name"]}</button></td><td>{b}</td></tr>'
        for p, a, b in [
            ("Customers cannot find you on Google", "seo-services", "Website Development, AI Content Management"),
            ("Your website looks outdated or gets few enquiries", "website-development", "SEO Services, Google Ads"),
            ("You need enquiries quickly", "google-ads-management", "Meta Ads, Website Development"),
            ("People do not know your brand yet", "meta-ads-management", "Social Media Marketing, Branding"),
            ("Your social pages look inactive", "social-media-marketing", "AI Content Management, Meta Ads"),
            ("Your business looks like everyone else", "branding-advertising", "Website Development, Social Media"),
            ("Leads go cold before anyone replies", "ai-automation", "Google Ads, Meta Ads"),
            ("You never have enough content", "ai-content-management", "Social Media Marketing, SEO"),
        ]) + "</tbody></table></div>", "du-white")
    proc = section(head("How we work", "Our 5-Step Delivery Process", "", True) + process(), "du-soft-bg")
    pricing = section(head("Engagement models", "Choose How You Want to Work With Us",
                           "Projects for websites and branding, monthly retainers for ongoing growth. Every plan is scoped after a free discovery call.", True) + plans(), "du-white")
    faqs = section(head("Service FAQs", "Questions About Our Services", "", True) + faq(FAQ_SERVICES), "du-soft-bg")
    cta = cta_section("du-services-form", "Get a recommendation", "Not Sure Which Service You Need?",
                      "Tell us your goal and we will suggest the most sensible starting point, even if it is a small one.",
                      "Get a service recommendation", "Takes less than a minute.", "I would like a recommendation on which service to start with.")
    body = hero + core + ai + compare + proc + tools_section() + pricing + faqs + cta
    return body, [ORG_SCHEMA, services_schema(), faq_schema(FAQ_SERVICES), breadcrumb_schema("Services", URL["services"])]


def page_about():
    hero = page_hero("About", "About Digital Udyami",
                     'We Help Indian Businesses Build <span class="du-gradient-text">Digital Growth Systems</span> That Make Sense',
                     "Digital Udyami is a digital marketing agency for founders, MSMEs and growing teams who want marketing that is connected, measurable and explained in plain language.",
                     btn("Work With Us", URL["contact"]) + btn("Explore Services", URL["services"], "outline"),
                     "team", "Digital Udyami team collaborating on a client project", "Human-led strategy, AI-assisted execution")
    story = section(f'''<div class="du-split">
  <div class="du-photo" data-du-reveal data-du-side="left" style="min-height:420px">{img("founders", "Business owners discussing a digital growth plan")}</div>
  <div data-du-reveal data-du-side="right"><span class="du-eyebrow">Our story</span><h2>Why "Udyami"?</h2>
  <p class="du-lead" style="margin-top:16px"><em>Udyami</em> means entrepreneur. We started Digital Udyami because too many Indian business owners were paying for scattered marketing activity (a website from one vendor, ads from another, social posts from a third) with nobody connecting it to enquiries and sales.</p>
  <p>Our job is to be the partner that connects those pieces: understand the business first, fix the weakest step in the customer journey, and report progress honestly. We combine human strategy with AI-assisted execution, so small teams can get the kind of joined-up marketing that used to need a large budget.</p></div>
</div>''')
    mv = section('<div class="du-mv-grid">' + "".join(
        f'<article class="du-card du-mv-card" data-du-reveal data-du-delay="{i + 1}"><div class="du-icon">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></article>'
        for i, (ic, t, d) in enumerate([
            ("dui-target", "Our mission", "Help Indian businesses get found, chosen and remembered online, with marketing that is connected to real business outcomes."),
            ("dui-rocket", "Our vision", "Make professional, measurable digital growth accessible to every udyami, from first-time founders to established family businesses."),
            ("dui-heart", "Our promise", "Realistic advice, transparent work and reporting you can understand. If something is not working, we will say so and fix it."),
        ])) + "</div>", "du-soft-bg")
    values = section(head("What we believe", "The Principles Behind Our Work", "", True) + '<div class="du-why-grid">' + "".join(
        f'<article class="du-why-card" data-du-reveal data-du-delay="{i}"><div class="du-icon">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></article>'
        for i, (ic, t, d) in enumerate([
            ("dui-chart", "Outcomes over activity", "Posts, clicks and reports matter only when they move enquiries, sales or efficiency."),
            ("dui-shield", "Honesty over hype", "No guaranteed rankings, no inflated numbers, no lock-in. You own your accounts and data."),
            ("dui-users", "People plus AI", "AI speeds up research, production and workflows. People remain responsible for strategy and quality."),
            ("dui-layers", "Systems over silos", "Website, search, ads, social and automation are planned together, not bought separately."),
        ])) + "</div>", "du-dark")
    diff = section(head("What makes us different", "A Growth Partner, Not Just a Vendor",
                        "Here is what working with Digital Udyami looks like in practice.") + '<div class="du-diff-grid">' + "".join(
        f'<div class="du-diff" data-du-reveal data-du-delay="{i % 3 + 1}">{icon("dui-check")}<div><strong>{t}</strong><p>{d}</p></div></div>'
        for i, (t, d) in enumerate([
            ("One team for the full journey", "Website, SEO, ads, social, branding and automation planned together."),
            ("Bilingual, India-first thinking", "Messaging that works for Indian buyers, in English, Hindi and Hinglish."),
            ("WhatsApp-first lead journeys", "Because that is where most Indian customers actually want to talk."),
            ("Plain-language reporting", "What was done, what changed and what happens next, every month."),
            ("You own everything", "Domains, websites, ad accounts and analytics set up in your name."),
            ("Start small, scale smart", "Begin with the biggest bottleneck, add layers when the foundation works."),
        ])) + "</div>")
    proc = section(head("How we work", "Our 5-Step Process", "", True) + process(), "du-soft-bg")
    cta = cta_section("du-about-form", "Let's talk", "Ready to Build Your Growth System?",
                      "Tell us about your business. We will reply with honest suggestions, not a sales script.",
                      "Start a conversation", "We usually reply on the same working day.", "I would like to discuss working with Digital Udyami.")
    body = hero + story + mv + values + diff + proc + cta
    about = {"@context": "https://schema.org", "@type": "AboutPage", "name": "About Digital Udyami", "url": URL["about"], "about": {"@id": URL["home"] + "#organization"}}
    return body, [ORG_SCHEMA, about, breadcrumb_schema("About", URL["about"])]


def page_contact():
    hero = page_hero("Contact", "We reply on WhatsApp, phone and email",
                     'Let\'s Talk About <span class="du-gradient-text">Growing Your Business</span>',
                     "Whether you need a new website, more leads, better visibility or less manual work, the first conversation is free and focused on your goals.",
                     btn("WhatsApp Us", wa("Hello Digital Udyami, I would like to discuss my business."), "wa", "dui-whatsapp", True) + btn("Call " + PHONE_DISPLAY, "tel:" + PHONE_TEL, "outline", "dui-phone"),
                     "office", "Digital Udyami workspace", "PAN India · Remote-first · Same-day replies")
    strip = section(contact_strip() + socials_row(), "du-white")
    extra = '<div class="du-field du-full"><label for="du-contact-form-message">Message</label><textarea id="du-contact-form-message" name="message" placeholder="Tell us briefly about your business and goal"></textarea></div>'
    form = cta_section("du-contact-form", "Send us a message", "Share Your Requirement",
                       "Fill in the form and it opens WhatsApp with your message ready to send. Prefer email? Write to us at " + f'<a href="mailto:{EMAIL}" style="color:#FFB15E">{EMAIL}</a>.',
                       "Tell us what you need", "We usually reply on the same working day.", "I want to discuss a digital growth requirement.", extra)
    nxt = section(head("What happens next", "From Message to Plan in Three Simple Steps", "", True) + '<div class="du-path-grid">' + "".join(
        f'<article class="du-path-card du-card" data-du-reveal data-du-delay="{i}"><span class="du-pain-number">0{i + 1}</span><h3>{t}</h3><p>{d}</p></article>'
        for i, (t, d) in enumerate([
            ("We reply and understand", "A short call or WhatsApp chat to understand your business, goals and current situation."),
            ("We review and recommend", "We look at your website and channels, then recommend a clear, prioritised starting point."),
            ("You decide", "You get a scoped proposal. No pressure, no lock-in, no confusing jargon."),
        ])) + "</div>", "du-soft-bg")
    faqs = section(head("Before you reach out", "Contact FAQs", "", True) + faq(FAQ_CONTACT))
    body = hero + strip + form + nxt + faqs
    cp = {"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact Digital Udyami", "url": URL["contact"], "about": {"@id": URL["home"] + "#organization"}}
    return body, [ORG_SCHEMA, cp, faq_schema(FAQ_CONTACT), breadcrumb_schema("Contact", URL["contact"])]


INDUSTRIES = [
    ("dui-rocket", "Startups and MSMEs", "Limited budgets, many priorities and the need to look credible fast.", ["website-development", "seo-services", "meta-ads-management"]),
    ("dui-cart", "D2C and E-commerce", "Rising ad costs, abandoned carts and the need for repeat customers.", ["meta-ads-management", "google-ads-management", "ai-content-management"]),
    ("dui-building", "B2B and Manufacturing", "Long sales cycles, complex products and few but valuable leads.", ["seo-services", "google-ads-management", "ai-automation"]),
    ("dui-heart", "Healthcare and Clinics", "Trust, local visibility and strict advertising policies.", ["seo-services", "social-media-marketing", "ai-automation"]),
    ("dui-book", "Education and Coaching", "Seasonal admissions, high enquiry volumes and fast follow-up.", ["meta-ads-management", "ai-automation", "social-media-marketing"]),
    ("dui-key", "Real Estate", "High-value leads, lead quality problems and project launches.", ["meta-ads-management", "google-ads-management", "ai-automation"]),
    ("dui-file", "Professional Services", "CAs, lawyers and consultants who sell expertise and trust.", ["seo-services", "branding-advertising", "ai-content-management"]),
    ("dui-cup", "Hospitality and Food", "Restaurants, cafes and hotels that live on reviews and local discovery.", ["social-media-marketing", "seo-services", "meta-ads-management"]),
    ("dui-store", "Local Retail and Services", "Shops, salons and service providers competing within a few kilometres.", ["seo-services", "social-media-marketing", "website-development"]),
]


def page_industries():
    hero = page_hero("Industries", "Industry-aware digital marketing",
                     'Digital Marketing Strategies <span class="du-gradient-text">Tailored to Your Industry</span>',
                     "A clinic, a D2C brand and a manufacturer do not buy or sell the same way. We shape the channel mix, messaging and lead journey around how your customers actually decide.",
                     btn("Find Your Industry", "#industries") + btn("Get a Free Audit", URL["audit"], "outline"),
                     "founders", "Business owners from different industries discussing growth", "Same principles, different playbooks")
    cards = "".join(
        f'''<article class="du-ind-card du-card" data-du-reveal data-du-delay="{i % 3 + 1}"><div class="du-icon">{icon(ic)}</div><h3>{t}</h3><p>{d}</p>
<span class="du-ind-sub">Recommended starting stack</span><div class="du-ind-tags">{"".join(f'<button type="button" class="du-chip" data-du-quick="{s}">{icon("dui-eye")}{SERVICE_BY_SLUG[s]["name"]}</button>' for s in stack)}</div>
<a class="du-link" href="{wa(f'Hello Digital Udyami, I run a business in {t} and want to discuss digital marketing.')}" target="_blank" rel="noopener">Discuss my industry{icon("dui-arrow")}</a></article>'''
        for i, (ic, t, d, stack) in enumerate(INDUSTRIES))
    grid = section(head("Who we work with", "Industries We Serve",
                        "Tap a recommended service to see a quick look of what is included.") + f'<div class="du-ind-grid">{cards}</div>', "du-white", "industries")
    stages = section(head("Growth stages", "Wherever You Are, There Is a Sensible Next Step", "", True) + '<div class="du-path-grid">' + "".join(
        f'<article class="du-path-card du-card" data-du-reveal data-du-delay="{i}"><span class="du-pain-number">0{i + 1}</span><h3>{t}</h3><p>{d}</p>{checks(c)}</article>'
        for i, (t, d, c) in enumerate([
            ("Just starting", "You need to look credible and be easy to find.", ["Website and Google Business Profile", "Brand basics", "First social presence"]),
            ("Growing", "You need a steady, predictable flow of enquiries.", ["SEO and content", "Google and Meta Ads", "Conversion tracking"]),
            ("Scaling", "You need efficiency and a connected system.", ["Automation and CRM", "Multi-channel remarketing", "Reporting dashboards"]),
        ])) + "</div>", "du-soft-bg")
    faqs = section(head("Industry FAQs", "Common Questions", "", True) + faq(FAQ_INDUSTRIES))
    cta = cta_section("du-industries-form", "Talk to a specialist", "Get a Plan Built for Your Industry",
                      "Tell us what you sell and who you sell to. We will suggest the channels that fit your market.",
                      "Tell us about your business", "We will reply with an industry-specific starting point.", "I would like an industry-specific digital marketing plan.",
                      '<div class="du-field du-full"><label for="du-industries-form-industry">Your industry</label><input id="du-industries-form-industry" name="industry" placeholder="For example: clinic, real estate, D2C skincare"></div>')
    body = hero + grid + stages + audit_banner() + faqs + cta
    return body, [ORG_SCHEMA, faq_schema(FAQ_INDUSTRIES), breadcrumb_schema("Industries", URL["industries"])]


def page_audit():
    hero = page_hero("Free Digital Audit", "Free · No obligation · Written summary",
                     'Get a Free <span class="du-gradient-text">Digital Growth Audit</span> for Your Business',
                     "Find out exactly what is stopping your website, Google visibility, ads and social media from producing more enquiries, and what to fix first.",
                     btn("Request My Free Audit", "#contact-form") + btn("Ask on WhatsApp", wa("Hello Digital Udyami, I would like a free digital growth audit."), "outline", "dui-whatsapp", True),
                     "analytics", "Marketing analytics dashboard reviewed during a digital audit", "Clear findings, prioritised actions")
    areas = [
        ("dui-code", "Website", ["Mobile experience and speed", "Clarity of message and offer", "Calls to action and lead forms"]),
        ("dui-search", "SEO and local search", ["Technical health", "Keyword visibility gaps", "Google Business Profile"]),
        ("dui-target", "Paid advertising", ["Campaign structure", "Wasted spend", "Conversion tracking accuracy"]),
        ("dui-users", "Social media", ["Profile and content consistency", "Engagement quality", "Brand presentation"]),
        ("dui-chart", "Tracking and data", ["GA4 and Tag Manager setup", "Lead source visibility", "Reporting gaps"]),
        ("dui-automation", "Follow-up and automation", ["Response time to enquiries", "Manual work that can be automated", "CRM usage"]),
    ]
    grid = section(head("What we review", "Six Areas, One Clear Action Plan",
                        "We look at your digital presence the way a customer experiences it, from first search to final enquiry.", True) +
                   '<div class="du-audit-grid">' + "".join(
        f'<article class="du-card du-audit-card" data-du-reveal data-du-delay="{i % 3 + 1}"><div class="du-icon">{icon(ic)}</div><h3>{t}</h3>{checks(c)}</article>'
        for i, (ic, t, c) in enumerate(areas)) + "</div>", "du-white")
    how = section(head("How it works", "Three Steps, No Obligation", "", True) + '<div class="du-path-grid">' + "".join(
        f'<article class="du-path-card du-card" data-du-reveal data-du-delay="{i}"><span class="du-pain-number">0{i + 1}</span><h3>{t}</h3><p>{d}</p></article>'
        for i, (t, d) in enumerate([
            ("Share a few details", "Your website, your main goal and the areas you want reviewed."),
            ("We run the audit", "Our team reviews your website, search, ads, social and tracking."),
            ("Walk-through call", "We share the findings in writing and explain the priorities on a short call."),
        ])) + "</div>", "du-soft-bg")
    get = section(head("What you receive", "Useful Even If You Never Work With Us", "", True) + '<div class="du-why-grid">' + "".join(
        f'<article class="du-why-card" data-du-reveal data-du-delay="{i}"><div class="du-icon">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></article>'
        for i, (ic, t, d) in enumerate([
            ("dui-file", "Written summary", "Key issues across each channel, explained in plain language."),
            ("dui-spark", "Quick wins", "Changes you can make straight away, often at no cost."),
            ("dui-layers", "Priority order", "What to fix first, second and later, based on impact."),
            ("dui-chat", "Honest advice", "If you do not need our help for something, we will tell you."),
        ])) + "</div>", "du-dark")
    faqs = section(head("Audit FAQs", "Questions About the Free Audit", "", True) + faq(FAQ_AUDIT), "du-soft-bg")
    extra = '<div class="du-field du-full"><label for="du-audit-form-city">City or region you serve</label><input id="du-audit-form-city" name="city" placeholder="For example: Delhi NCR, all India"></div>'
    cta = cta_section("du-audit-form", "Request your audit", "Claim Your Free Digital Growth Audit",
                      "Fill in the form and send it on WhatsApp. We will confirm the details and share your audit within a few working days.",
                      "Request my free audit", "Your website link is the most useful detail.", "I would like a free digital growth audit.", extra)
    body = hero + grid + how + get + faqs + cta
    return body, [ORG_SCHEMA, faq_schema(FAQ_AUDIT), breadcrumb_schema("Free Digital Audit", URL["audit"])]


PAGES = {
    "home": dict(fn=page_home, url=URL["home"], title="Digital Marketing Agency in India | SEO, Ads, Websites & AI | Digital Udyami",
                 desc="Digital Udyami is a digital marketing agency in India offering SEO, website development, Google Ads, Meta Ads, social media, branding and AI automation.",
                 kw="digital marketing agency in India"),
    "services": dict(fn=page_services, url=URL["services"], title="Digital Marketing Services | SEO, Ads, Websites, AI | Digital Udyami",
                     desc="Explore Digital Udyami services: SEO, website development, Google Ads, Meta Ads, social media marketing, branding, AI automation and AI content.",
                     kw="digital marketing services"),
    "about": dict(fn=page_about, url=URL["about"], title="About Digital Udyami | Digital Marketing Agency for Indian Businesses",
                  desc="Learn about Digital Udyami, a digital marketing agency helping Indian founders and MSMEs build connected, measurable digital growth systems.",
                  kw="about Digital Udyami"),
    "contact": dict(fn=page_contact, url=URL["contact"], title="Contact Digital Udyami | Call, WhatsApp or Email",
                    desc=f"Contact Digital Udyami on {PHONE_DISPLAY} or {EMAIL}. Free first consultation for SEO, ads, websites, social media and AI automation.",
                    kw="contact digital marketing agency"),
    "industries": dict(fn=page_industries, url=URL["industries"], title="Industries We Serve | Digital Marketing by Industry | Digital Udyami",
                       desc="Industry-specific digital marketing for startups, D2C, B2B, healthcare, education, real estate, professional services, hospitality and local businesses.",
                       kw="digital marketing for industries"),
    "free-digital-audit": dict(fn=page_audit, url=URL["audit"], title="Free Digital Growth Audit | Website, SEO & Ads Review | Digital Udyami",
                               desc="Get a free digital growth audit covering your website, SEO, Google Business Profile, ads, social media and tracking, with a prioritised action plan.",
                               kw="free digital marketing audit"),
}

PAGE_CSS = {name: (SRC / "pages" / f"{name}.css").read_text() if (SRC / "pages" / f"{name}.css").exists() else ""
            for name in PAGES}
SHARED_PAGE_CSS = (SRC / "pages" / "shared.css").read_text()


# ---------------------------------------------------------------- legal pages
import legal as L  # noqa: E402


def legal_page(kind):
    is_privacy = kind == "privacy"
    sections = L.PRIVACY if is_privacy else L.TERMS
    summary = L.PRIVACY_SUMMARY if is_privacy else L.TERMS_SUMMARY
    title = "Privacy Policy" if is_privacy else "Terms and Conditions"
    url = URL["privacy"] if is_privacy else URL["terms"]
    other = ("Terms and Conditions", URL["terms"]) if is_privacy else ("Privacy Policy", URL["privacy"])
    lead = ("How Digital Udyami collects, uses and protects your personal data when you visit our website or work with us."
            if is_privacy else "The terms that apply when you use our website or engage Digital Udyami for digital marketing, website, advertising, branding and AI services.")
    toc_items = "".join(f'<li><a href="#{sid}">{e(t)}</a></li>' for sid, t, _ in sections)
    hero = f'''<section class="du-page-hero du-legal-hero"><div class="du-wrap"><div class="du-page-hero-grid"><div data-du-reveal>
  <ol class="du-crumbs" aria-label="Breadcrumb"><li><a href="{URL["home"]}">Home</a></li><li aria-current="page">{title}</li></ol>
  <div class="du-pill"><span class="du-dot"></span>Legal</div>
  <h1>{title}</h1><p class="du-lead">{lead}</p>
  <div class="du-legal-meta"><span class="du-chip">{icon("dui-clock")}Last updated: {L.EFFECTIVE_DATE}</span><span class="du-chip">{icon("dui-shield")}Governed by Indian law</span><button type="button" class="du-chip" data-du-print>{icon("dui-file")}Print or save as PDF</button></div>
</div></div></div></section>'''
    cards = "".join(f'<article class="du-card du-summary-card" data-du-reveal data-du-delay="{i + 1}"><div class="du-icon">{icon(ic)}</div><h3>{e(t)}</h3><p>{e(d)}</p></article>'
                    for i, (ic, t, d) in enumerate(summary))
    secs = "".join(f'<section class="du-legal-section" id="{sid}"><h2><span>{i + 1:02d}</span>{e(t)}</h2>{body}</section>'
                   for i, (sid, t, body) in enumerate(sections))
    main = section(f'''<div class="du-center-head" style="margin-bottom:28px"><span class="du-eyebrow">In short</span><h2>The Key Points at a Glance</h2></div>
<div class="du-summary">{cards}</div>
<div class="du-legal-layout" style="margin-top:56px">
  <nav class="du-toc" aria-label="On this page"><span class="du-toc-title">On this page</span><ol>{toc_items}</ol></nav>
  <div class="du-legal-body">
    <details class="du-toc-mobile"><summary>On this page</summary><nav aria-label="On this page (mobile)"><ol>{toc_items}</ol></nav></details>
    {secs}
    <p class="du-legal-note"><strong>Please note:</strong> this summary and the “In short” cards are for convenience only. The full text above is what applies.</p>
    <div class="du-legal-related"><a href="{other[1]}"><span><small>Also read</small>{other[0]}</span>{icon("dui-arrow")}</a><a href="{URL["contact"]}"><span><small>Questions?</small>Contact Digital Udyami</span>{icon("dui-arrow")}</a></div>
  </div>
</div>''', "du-white")
    schema = [{"@context": "https://schema.org", "@type": "WebPage", "name": title, "url": url, "dateModified": "2026-09-27",
               "publisher": {"@id": URL["home"] + "#organization"}}, breadcrumb_schema(title, url)]
    return hero + main, schema


def page_privacy():
    return legal_page("privacy")


def page_terms():
    return legal_page("terms")


PAGES["privacy-policy"] = dict(fn=page_privacy, url=URL["privacy"], title="Privacy Policy | Digital Udyami",
                               desc="How Digital Udyami collects, uses, shares and protects personal data, in line with India's Digital Personal Data Protection Act, 2023.",
                               kw="Digital Udyami privacy policy")
PAGES["terms-and-conditions"] = dict(fn=page_terms, url=URL["terms"], title="Terms and Conditions | Digital Udyami",
                                     desc="Terms for using the Digital Udyami website and engaging our SEO, website, advertising, social media, branding and AI services.",
                                     kw="Digital Udyami terms and conditions")
PAGE_CSS["privacy-policy"] = PAGE_CSS["terms-and-conditions"] = (SRC / "pages" / "legal.css").read_text()


def build():
    dist, prev = ROOT / "dist", ROOT / "preview"
    dist.mkdir(exist_ok=True)
    prev.mkdir(exist_ok=True)
    for name, p in PAGES.items():
        body, schema = p["fn"]()
        needs_modal = "data-du-quick" in body
        header = f'''<!--
DIGITAL UDYAMI · ELEMENTOR HTML WIDGET · {name.upper()} PAGE (generated by build.py, edit src/ and rebuild)
- Page URL: {p["url"]}
- SEO title: {p["title"]}
- Meta description: {p["desc"]}
- Primary keyword: {p["kw"]}
- Template: Elementor Full Width (or Canvas + theme header/footer). Hide the default page title.
- Paste this entire file into ONE Elementor HTML widget. Do not add another H1 on the page.
-->'''
        ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema)
        font = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap">'
        widget = (f'{header}\n<div id="du-app" class="du-page-{name}">\n{font}\n<style>\n{CORE_CSS}\n{SHARED_PAGE_CSS}\n{PAGE_CSS[name]}</style>\n'
                  f'{ICONS}\n{body}\n{modal() if needs_modal else ""}\n{floating_actions()}\n<script>\n{CORE_JS}</script>\n{ld}\n</div>\n')
        (dist / f"{name}.html").write_text(widget)
        (prev / f"{name}.html").write_text(
            f'<!doctype html><html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{e(p["title"])}</title><meta name="description" content="{e(p["desc"])}"><link rel="canonical" href="{p["url"]}">'
            f'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            f'<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">'
            f'<style>body{{margin:0}}</style></head><body>{widget}</body></html>')
        print(f"built {name:20s} {len(widget) / 1024:6.1f} KB")


# ---------------------------------------------------------------- footer
FOOTER_CSS = (SRC / "footer.css").read_text()
LEGAL = [("Privacy Policy", URL["privacy"]), ("Terms and Conditions", URL["terms"])]


def footer_icons(names):
    import re
    syms = re.findall(r'(<symbol id="dui-([\w-]+)".*?</symbol>)', ICONS, re.S)
    keep = "".join(sym.replace('id="dui-', 'id="duf-') for sym, n in syms if n in names)
    return f'<svg aria-hidden="true" focusable="false" style="position:absolute;width:0;height:0;overflow:hidden">{keep}</svg>'


def build_footer():
    fi = lambda n: f'<svg aria-hidden="true"><use href="#duf-{n}"></use></svg>'
    used = ["arrow", "whatsapp", "phone", "mail", "map", "star", "clock", "shield", "globe", "users",
            "facebook-brand", "instagram-brand", "linkedin-brand", "x-brand"]
    svc = "".join(f'<li><a href="{x["url"]}">{e(x["name"])}</a></li>' for x in SERVICES)
    company = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in [
        ("Home", URL["home"]), ("About Us", URL["about"]), ("All Services", URL["services"]),
        ("Industries We Serve", URL["industries"]), ("Blog", URL["blog"]), ("Digital India Roadmap", URL["roadmap"]),
        ("Free Digital Audit", URL["audit"]), ("Contact Us", URL["contact"])])
    social = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="Digital Udyami on {n}">{fi(i[4:])}</a>' for n, u, i in SOCIALS)
    legal = "".join(f'<a href="{u}">{t}</a>' for t, u in LEGAL)
    msg = wa("Hello Digital Udyami, I would like to discuss my business growth.")
    body = f'''<footer id="du-footer" aria-label="Site footer">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap">
<style>
{FOOTER_CSS}</style>
{footer_icons(used)}
<div class="f-cta"><div class="f-wrap"><div class="f-cta-box">
  <div><h2>Ready to grow your business online?</h2><p>Get a free digital growth audit and a clear, prioritised plan. No obligation, no jargon.</p></div>
  <div class="f-cta-actions"><a class="f-btn f-btn-light" href="{URL["audit"]}">Get My Free Audit{fi("arrow")}</a><a class="f-btn f-btn-ghost" href="{msg}" target="_blank" rel="noopener">WhatsApp Us{fi("whatsapp")}</a></div>
</div></div></div>
<div class="f-wrap"><div class="f-main">
  <div class="f-brand">
    <a class="f-brand-mark" href="{URL["home"]}" aria-label="Digital Udyami home"><span>DU</span>Digital Udyami</a>
    <p class="f-about">A digital marketing agency helping Indian businesses get found, chosen and remembered, with connected SEO, websites, ads, social media, branding and AI automation.</p>
    <div class="f-badges"><span class="f-badge">{fi("globe")}PAN India</span><span class="f-badge">{fi("users")}Human-led strategy</span><span class="f-badge">{fi("shield")}No fake guarantees</span></div>
    <div class="f-social">{social}</div>
  </div>
  <nav class="f-col" aria-label="Services"><h3>Our Services</h3><ul class="f-links">{svc}</ul></nav>
  <nav class="f-col" aria-label="Company"><h3>Company</h3><ul class="f-links">{company}</ul></nav>
  <div class="f-col f-col-contact"><h3>Get in Touch</h3>
    <address class="f-contact" style="font-style:normal">
      <a href="tel:{PHONE_TEL}"><i>{fi("phone")}</i><span><strong>Call us</strong>{PHONE_DISPLAY}</span></a>
      <a href="{msg}" target="_blank" rel="noopener"><i>{fi("whatsapp")}</i><span><strong>WhatsApp</strong>{PHONE_DISPLAY}</span></a>
      <a href="mailto:{EMAIL}"><i>{fi("mail")}</i><span><strong>Email</strong>{EMAIL}</span></a>
      <div><i>{fi("map")}</i><span><strong>Service area</strong>Serving businesses across India</span></div>
      <a href="{REVIEWS_URL}" target="_blank" rel="noopener"><i>{fi("star")}</i><span><strong>Google Reviews</strong><span class="f-stars">{fi("star") * 5}</span></span></a>
    </address>
  </div>
</div></div>
<div class="f-bottom"><div class="f-wrap f-bottom-inner">
  <p>&copy; <span data-f-year>2026</span> Digital Udyami. All rights reserved.</p>
  <nav class="f-legal" aria-label="Legal">{legal}<a href="{URL["contact"]}">Contact</a></nav>
  <p class="f-made">Made with <b>&hearts;</b> in India</p>
</div></div>
<button type="button" class="f-top" aria-label="Back to top">{fi("arrow")}</button>
<script>
(function(){{var f=document.getElementById('du-footer');if(!f)return;
var y=f.querySelector('[data-f-year]');if(y)y.textContent=new Date().getFullYear();
var t=f.querySelector('.f-top'),tick=false;
function chk(){{tick=false;t.classList.toggle('is-visible',window.pageYOffset>window.innerHeight*1.2)}}
window.addEventListener('scroll',function(){{if(!tick){{tick=true;requestAnimationFrame(chk)}}}},{{passive:true}});chk();
t.addEventListener('click',function(){{var r=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;window.scrollTo({{top:0,behavior:r?'auto':'smooth'}})}});
}})();
</script>
</footer>'''
    header = """<!--
DIGITAL UDYAMI · SITE FOOTER · ELEMENTOR HTML WIDGET (generated by build.py)
- Best: Elementor Pro > Templates > Theme Builder > Footer > add ONE HTML widget, paste this file, display on Entire Site.
- Without Elementor Pro: paste into an HTML widget at the bottom of each page (or a Custom HTML block in the theme footer widget area)
  and hide the theme's default footer.
- Confirm the Privacy Policy and Terms pages exist, or edit LEGAL in build.py.
-->
"""
    return header + body


def build_footer_files():
    dist, prev = ROOT / "dist", ROOT / "preview"
    f = build_footer()
    (dist / "footer.html").write_text(f + "\n")
    (prev / "footer.html").write_text('<!doctype html><html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Footer preview</title><style>body{margin:0;background:#FFF9F4}</style></head><body><div style="height:140vh;display:grid;place-items:center;font:600 18px system-ui;color:#999">Page content above the footer</div>' + f + '</body></html>')
    # home preview with the footer attached, to check both widgets together
    home = (prev / "home.html").read_text().replace("</body>", f + "</body>")
    (prev / "home-with-footer.html").write_text(home)
    print(f"built footer               {len(f) / 1024:6.1f} KB")


# ---------------------------------------------------------------- header
HEADER_CSS = (SRC / "header.css").read_text()
LOGO = "https://digitaludyami.com/wp-content/uploads/2026/09/cropped-Digital-Udyami-Logo.png"
MENU_BLURB = {
    "seo-services": "Rank on Google, Maps and AI answers",
    "website-development": "Fast, mobile-first sites that convert",
    "google-ads-management": "High-intent search campaigns",
    "meta-ads-management": "Facebook and Instagram lead ads",
    "social-media-marketing": "Consistent content and community",
    "branding-advertising": "Identity, message and creative",
    "ai-automation": "Chatbots, follow-up and CRM workflows",
    "ai-content-management": "Scalable content with human review",
}


def build_header():
    hi = lambda n: f'<svg aria-hidden="true"><use href="#duh-{n}"></use></svg>'
    used = ["arrow", "chev", "close", "phone", "mail", "whatsapp", "star", "check", "globe", "home", "info", "grid",
            "book", "flag", "search", "code", "target", "megaphone", "users", "spark", "automation", "file",
            "facebook-brand", "instagram-brand", "linkedin-brand", "x-brand"]
    icons = footer_icons(used).replace('id="duf-', 'id="duh-')
    msg = wa("Hello Digital Udyami, I would like to discuss my business growth.")
    ext = ' target="_blank" rel="noopener"'
    social = lambda cls: "".join(f'<a href="{u}"{ext} aria-label="Digital Udyami on {n}">{hi(i[4:])}</a>' for n, u, i in SOCIALS)

    def svc_link(s):
        return (f'<a class="duh-svc" href="{s["url"]}"><i>{hi(s["icon"][4:])}</i>'
                f'<span><strong>{e(s["name"])}</strong><small>{e(MENU_BLURB[s["slug"]])}</small></span></a>')

    core = "".join(svc_link(SERVICE_BY_SLUG[x]) for x in CORE_SLUGS)
    ai = "".join(svc_link(SERVICE_BY_SLUG[x]) for x in AI_SLUGS)
    m_svc = "".join(f'<a class="duh-m-svc" href="{s["url"]}">{hi(s["icon"][4:])}{e(s["name"])}</a>' for s in SERVICES)
    pri, lazy = ' fetchpriority="high"', ' loading="lazy"'
    logo = lambda eager: (f'<img class="duh-logo" src="{LOGO}" alt="Digital Udyami" width="210" height="56" decoding="async"'
                          f'{pri if eager else lazy}>'
                          '<span class="duh-logo-fallback" hidden><span>DU</span>Digital Udyami</span>')

    nav = [("Home", URL["home"], "home"), ("About", URL["about"], "info"), None,
           ("Blog", URL["blog"], "book"), ("Digital India Roadmap", URL["roadmap"], "flag"), ("Contact", URL["contact"], "chat")]
    desk = []
    for item in nav:
        if item is None:
            desk.append(f'<button type="button" class="duh-mega-btn" aria-expanded="false" aria-controls="duh-mega" data-duh-services>Services{hi("chev")}</button>')
        elif item[0] != "Contact":
            desk.append(f'<a href="{item[1]}">{item[0]}</a>')
    mob = []
    for item in nav:
        if item is None:
            mob.append(f'''<li><button type="button" class="duh-m-link" aria-expanded="false" aria-controls="duh-m-services" data-duh-acc><i>{hi("grid")}</i>Services{hi("chev").replace("<svg", '<svg class="duh-caret"')}</button>
  <div class="duh-m-sub" id="duh-m-services"><div><div class="duh-m-sub-grid">{m_svc}<a class="duh-m-all" href="{URL["services"]}">Explore all services{hi("arrow")}</a></div></div></div></li>''')
        else:
            ic = "mail" if item[2] == "chat" else item[2]
            mob.append(f'<li><a class="duh-m-link" href="{item[1]}"><i>{hi(ic)}</i>{item[0]}</a></li>')

    body = f'''<div id="du-header" data-duh-sticky="true">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap">
<style>
{HEADER_CSS}</style>
{icons}
<div class="duh-spacer" aria-hidden="true"></div>
<header class="duh-shell">
  <div class="duh-topbar"><div class="duh-wrap">
    <div class="duh-top-left">
      <span class="duh-top-note"><span class="duh-live" aria-hidden="true"></span>PAN India digital growth partner</span>
      <a class="duh-top-item" href="tel:{PHONE_TEL}">{hi("phone")}{PHONE_DISPLAY}</a>
      <a class="duh-top-item duh-top-hide-md" href="mailto:{EMAIL}">{hi("mail")}{EMAIL}</a>
    </div>
    <div class="duh-top-right">
      <a class="duh-top-item" href="{REVIEWS_URL}"{ext}><span class="duh-stars">{hi("star") * 5}</span>Google Reviews</a>
      <div class="duh-top-social">{social("top")}</div>
    </div>
  </div></div>
  <div class="duh-bar">
    <div class="duh-wrap duh-bar-inner">
      <a class="duh-brand" href="{URL["home"]}" aria-label="Digital Udyami home">{logo(True)}</a>
      <nav class="duh-nav" aria-label="Main navigation">{"".join(desk)}</nav>
      <div class="duh-actions">
        <a class="duh-icon-btn is-call" href="tel:{PHONE_TEL}" aria-label="Call {PHONE_DISPLAY}">{hi("phone")}<span class="duh-tip">Call {PHONE_DISPLAY}</span></a>
        <a class="duh-icon-btn is-wa" href="{msg}"{ext} aria-label="Chat on WhatsApp">{hi("whatsapp")}<span class="duh-tip">Chat on WhatsApp</span></a>
        <a class="duh-cta" href="{URL["contact"]}">Let&rsquo;s Talk{hi("arrow")}</a>
        <button type="button" class="duh-burger" aria-label="Open menu" aria-expanded="false" aria-controls="duh-drawer"><span></span><span></span><span></span></button>
      </div>
    </div>
    <div class="duh-mega" id="duh-mega"><div class="duh-wrap"><div class="duh-mega-panel">
      <div class="duh-mega-main">
        <p class="duh-mega-label">Marketing and growth<a href="{URL["services"]}">Explore all services{hi("arrow")}</a></p>
        <div class="duh-mega-grid">{core}</div>
        <p class="duh-mega-label">AI solutions</p>
        <div class="duh-mega-grid">{ai}</div>
      </div>
      <aside class="duh-mega-side">
        <h3>Free Digital Growth Audit</h3>
        <p>Find out what is holding your website, search, ads and social media back.</p>
        <ul class="duh-side-list"><li>{hi("check")}Website and SEO review</li><li>{hi("check")}Ads and tracking check</li><li>{hi("check")}Prioritised action plan</li></ul>
        <a class="duh-side-btn" href="{URL["audit"]}">Claim My Free Audit{hi("arrow")}</a>
        <div class="duh-side-links"><a href="{URL["industries"]}">Industries we serve</a><a href="tel:{PHONE_TEL}">Call us</a></div>
      </aside>
    </div></div></div>
    <div class="duh-progress" aria-hidden="true"></div>
  </div>
</header>
<div class="duh-overlay" data-duh-close></div>
<aside class="duh-drawer" id="duh-drawer" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="duh-drawer-head"><a class="duh-brand" href="{URL["home"]}" aria-label="Digital Udyami home">{logo(False)}</a><button type="button" class="duh-close-btn" data-duh-close aria-label="Close menu">{hi("close")}</button></div>
  <div class="duh-drawer-body">
    <nav aria-label="Mobile navigation"><ul class="duh-m-nav">{"".join(mob)}</ul></nav>
    <div class="duh-m-cta">
      <a class="is-call" href="tel:{PHONE_TEL}">{hi("phone")}Call</a>
      <a class="is-wa" href="{msg}"{ext}>{hi("whatsapp")}WhatsApp</a>
      <a class="duh-cta" href="{URL["audit"]}">Get a Free Audit{hi("arrow")}</a>
    </div>
    <div class="duh-m-card">
      <a href="tel:{PHONE_TEL}">{hi("phone")}{PHONE_DISPLAY}</a>
      <a href="mailto:{EMAIL}">{hi("mail")}{EMAIL}</a>
      <a href="{REVIEWS_URL}"{ext}>{hi("star")}Read our Google Reviews</a>
    </div>
    <div class="duh-m-social">{social("m")}</div>
  </div>
</aside>
<script>
{(SRC / "header.js").read_text()}</script>
</div>'''
    header = """<!--
DIGITAL UDYAMI · SITE HEADER V2 · ELEMENTOR HTML WIDGET (generated by build.py)
- Elementor Pro > Templates > Theme Builder > Header > Add New > one HTML widget > paste this file > Display on Entire Site.
- Set the Elementor container to Full Width with zero padding. Remove the old header (V1) so it does not show twice.
- The header is sticky by itself (hides on scroll down, returns on scroll up). Do NOT also turn on Elementor's "Sticky" option.
  To make it non-sticky, change data-duh-sticky="true" to "false" below.
-->
"""
    return header + body


def build_header_files():
    dist, prev = ROOT / "dist", ROOT / "preview"
    h = build_header()
    (dist / "header.html").write_text(h + "\n")
    f = build_footer()
    for name in PAGES:
        page = (prev / f"{name}.html").read_text()
        (prev / f"{name}-full-site.html").write_text(page.replace("<body>", "<body>" + h, 1).replace("</body>", f + "</body>"))
    (prev / "home-with-footer.html").unlink(missing_ok=True)
    print(f"built header               {len(h) / 1024:6.1f} KB")


if __name__ == "__main__":
    build()
    build_footer_files()
    build_header_files()
