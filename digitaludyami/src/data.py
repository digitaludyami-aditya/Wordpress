"""Content for the Digital Udyami pages.

Edit text here, then run `python3 build.py`. Service data feeds the service
cards, the Quick Look popups and the JSON-LD, so all three stay in sync.
"""

SITE = "https://www.digitaludyami.com"
PHONE_DISPLAY = "+91 859 5565 628"
PHONE_TEL = "+918595565628"
WHATSAPP = "918595565628"
EMAIL = "start@digitaludyami.com"
REVIEWS_URL = "https://share.google/rA5Qp1LxjH8SAxs50"
SOCIALS = [
    ("Facebook", "https://www.facebook.com/digitaludyami", "dui-facebook-brand"),
    ("Instagram", "https://www.instagram.com/digitaludyami", "dui-instagram-brand"),
    ("LinkedIn", "https://www.linkedin.com/company/digitaludyami/", "dui-linkedin-brand"),
    ("X", "https://www.x.com/digitaludyami", "dui-x-brand"),
]

# Page URLs. Existing pages keep the paths used by the live site.
URL = {
    "home": f"{SITE}/",
    "services": f"{SITE}/services/",
    "about": f"{SITE}/about/",
    "contact": f"{SITE}/contact/",
    "industries": f"{SITE}/industries/",
    "audit": f"{SITE}/free-digital-audit/",
    "process": f"{SITE}/how-we-work/",
    "blog": "https://digitaludyami.com/blog",
    "roadmap": "https://digitaludyami.com/digitalindiaroadmap",
    "privacy": f"{SITE}/privacy-policy/",
    "terms": f"{SITE}/terms-and-conditions/",
}

IMG = {
    "team": "photo-1552664730-d307ca884978",
    "analytics": "photo-1551288049-bebda4e38f71",
    "laptop": "photo-1516321318423-f06f85e504b3",
    "ads": "photo-1460925895917-afdab827c52f",
    "group": "photo-1522202176988-66273c2fd55f",
    "design": "photo-1561070791-2526d30994b5",
    "ai": "photo-1677442136019-21780ecad995",
    "video": "photo-1574717024653-61fd2cf4d44d",
    "planning": "photo-1454165804606-c3d57bc86b40",
    "founders": "photo-1524758631624-e2822e304c36",
    "office": "photo-1497366811353-6870744d04b2",
}

# Order matters: the first six form the 2x3 "core services" grid,
# the last two form the "AI solutions" row.
SERVICES = [
    {
        "slug": "seo-services",
        "name": "SEO Services",
        "url": f"{SITE}/services/seo-services/",
        "icon": "dui-search",
        "img": "analytics",
        "label": "Organic visibility",
        "short": "Build search visibility that helps the right customers discover, understand and contact your business.",
        "bullets": ["Commercial keyword visibility", "Technical and content foundations", "AEO and GEO readiness"],
        "tagline": "Get found on Google, in AI answers and on Maps when customers are actively searching.",
        "overview": "SEO at Digital Udyami starts with how your customers search, not with a keyword list. We fix the technical foundation, build pages that answer real buying questions and strengthen the signals that help Google and AI assistants trust your business. The result is visibility that keeps compounding long after an ad budget would have stopped.",
        "included": [
            "Technical SEO audit and fixes",
            "Keyword and search-intent research",
            "On-page optimisation of key pages",
            "Local SEO and Google Business Profile",
            "Content planning and blog strategy",
            "AEO and GEO readiness for AI search",
            "Quality link and citation building",
            "Monthly ranking and traffic reporting",
        ],
        "steps": [
            ("Audit", "Crawl the site, benchmark competitors and find the quickest wins."),
            ("Fix and build", "Resolve technical issues and improve pages that can rank and convert."),
            ("Grow", "Publish helpful content, earn authority and report progress every month."),
        ],
        "ideal": ["Local businesses", "Service companies", "E-commerce stores", "B2B brands"],
        "metrics": ["Keyword visibility", "Organic traffic", "Map pack presence", "Organic enquiries"],
    },
    {
        "slug": "website-development",
        "name": "Website Development",
        "url": f"{SITE}/services/website-development/",
        "icon": "dui-code",
        "img": "laptop",
        "label": "Digital foundation",
        "short": "Create a fast, credible and conversion-ready website that supports every marketing channel.",
        "bullets": ["Clear customer journey", "Mobile-first experience", "Lead and sales readiness"],
        "tagline": "A fast, mobile-first website that explains your value clearly and turns visitors into enquiries.",
        "overview": "Your website is where every ad, post and search result finally lands. We plan the structure around your customer journey, write clear messaging, design a mobile-first experience and build it on WordPress, WooCommerce or Shopify with SEO, speed and tracking in place from day one.",
        "included": [
            "Sitemap and customer journey planning",
            "Conversion-focused UI and UX design",
            "WordPress, WooCommerce or Shopify build",
            "Mobile-first, responsive layouts",
            "Speed and Core Web Vitals optimisation",
            "On-page SEO and schema setup",
            "Lead forms, WhatsApp and call tracking",
            "Training and post-launch support",
        ],
        "steps": [
            ("Plan", "Define goals, pages, content and the actions visitors should take."),
            ("Design and build", "Create the design, develop the site and connect forms and tracking."),
            ("Launch and improve", "Test on real devices, go live and refine using visitor data."),
        ],
        "ideal": ["New businesses", "Brands rebuilding an old site", "D2C and online stores", "Professional services"],
        "metrics": ["Page speed", "Conversion rate", "Enquiries per month", "Bounce rate"],
    },
    {
        "slug": "google-ads-management",
        "name": "Google Ads",
        "url": f"{SITE}/services/google-ads-management/",
        "icon": "dui-target",
        "img": "ads",
        "label": "High intent demand",
        "short": "Reach people already searching for a solution and connect campaign spend with measurable actions.",
        "bullets": ["Search intent targeting", "Conversion tracking", "Landing page alignment"],
        "tagline": "Show up at the exact moment customers search, and know which rupee produced which lead.",
        "overview": "Google Ads works best when intent, message and landing page line up. We structure campaigns around high-intent searches, write ads that pre-qualify the click, set up accurate conversion tracking and keep optimising bids, keywords and pages so budget moves towards what produces real enquiries and sales.",
        "included": [
            "Account audit and campaign structure",
            "Keyword research and negative lists",
            "Search, Performance Max and Shopping",
            "YouTube and Display remarketing",
            "Ad copy and extension writing",
            "GA4 and conversion tracking setup",
            "Landing page recommendations",
            "Weekly optimisation and clear reports",
        ],
        "steps": [
            ("Set up tracking", "Make sure every call, form and WhatsApp lead is measured correctly."),
            ("Launch focused", "Start with the highest-intent keywords and a controlled budget."),
            ("Optimise and scale", "Cut waste, test ads and scale the campaigns that convert."),
        ],
        "ideal": ["Lead-driven services", "Local businesses", "E-commerce stores", "B2B companies"],
        "metrics": ["Cost per lead", "Conversion rate", "ROAS", "Search impression share"],
    },
    {
        "slug": "meta-ads-management",
        "name": "Meta Ads",
        "url": f"{SITE}/services/meta-ads-management/",
        "icon": "dui-megaphone",
        "img": "group",
        "label": "Demand generation",
        "short": "Turn attention on Facebook and Instagram into qualified enquiries, sales and remarketing opportunities.",
        "bullets": ["Creative testing", "Lead quality focus", "Retargeting systems"],
        "tagline": "Create demand on Facebook and Instagram with creative that stops the scroll and audiences that convert.",
        "overview": "Meta Ads reach people before they start searching. We plan the funnel from awareness to retargeting, produce and test ad creatives, set up the Pixel and Conversions API, and focus on lead quality rather than cheap form fills, so your sales team spends time on people who are genuinely interested.",
        "included": [
            "Funnel and audience strategy",
            "Ad creative, reels and copy",
            "Lead forms and WhatsApp click ads",
            "Pixel and Conversions API setup",
            "Creative and audience A/B testing",
            "Retargeting and lookalike audiences",
            "Catalogue ads for online stores",
            "Lead quality review and reporting",
        ],
        "steps": [
            ("Research", "Understand buyers, offers and the creative angles likely to work."),
            ("Test", "Launch several creatives and audiences to find the winners quickly."),
            ("Scale", "Increase budget on proven ads and build retargeting around them."),
        ],
        "ideal": ["D2C brands", "Real estate", "Education and coaching", "Local services"],
        "metrics": ["Cost per qualified lead", "CTR", "ROAS", "Frequency"],
    },
    {
        "slug": "social-media-marketing",
        "name": "Social Media Marketing",
        "url": f"{SITE}/services/social-media-marketing/",
        "icon": "dui-users",
        "img": "team",
        "label": "Trust and recall",
        "short": "Build consistent visibility and useful conversations before the customer reaches the buying decision.",
        "bullets": ["Platform strategy", "Content consistency", "Community engagement"],
        "tagline": "Stay visible, useful and memorable on the platforms your customers use every day.",
        "overview": "Social media is where customers check whether a business feels active, credible and relatable. We build a platform strategy, a monthly content calendar, on-brand posts, carousels and reels, and manage engagement so your pages look alive and support every other channel.",
        "included": [
            "Platform and content strategy",
            "Monthly content calendar",
            "Post, carousel and reel design",
            "Captions, hashtags and scheduling",
            "Instagram, Facebook and LinkedIn",
            "Community and comment management",
            "Profile optimisation",
            "Monthly performance insights",
        ],
        "steps": [
            ("Strategy", "Define content pillars, tone and the role of each platform."),
            ("Create", "Produce a month of content for review and approval."),
            ("Engage and learn", "Publish, respond and double down on what the audience values."),
        ],
        "ideal": ["Consumer brands", "Clinics and salons", "Restaurants and cafes", "Personal brands"],
        "metrics": ["Reach", "Engagement rate", "Follower growth", "Profile actions"],
    },
    {
        "slug": "branding-advertising",
        "name": "Branding and Advertising",
        "url": f"{SITE}/services/branding-advertising/",
        "icon": "dui-spark",
        "img": "design",
        "label": "Recognition and preference",
        "short": "Give your business a clear identity, stronger message and visual system customers can remember.",
        "bullets": ["Brand positioning", "Visual identity", "Campaign creative"],
        "tagline": "A clear identity and message that makes your business easier to recognise and easier to choose.",
        "overview": "Strong brands spend less to convince. We help you define positioning, messaging and personality, then turn it into a logo, colour palette, typography and brand guidelines, and carry it through to campaigns, packaging, print and digital creative so every touchpoint looks like the same trusted business.",
        "included": [
            "Brand discovery and positioning",
            "Messaging and tagline development",
            "Logo and visual identity design",
            "Brand guidelines document",
            "Stationery and print collateral",
            "Packaging and label design",
            "Campaign concepts and ad creative",
            "Brochures and sales presentations",
        ],
        "steps": [
            ("Discover", "Understand your audience, competitors and what makes you different."),
            ("Define", "Shape the positioning, message and visual direction."),
            ("Deliver", "Produce the identity, guidelines and launch creative."),
        ],
        "ideal": ["New ventures", "Rebrands", "Product launches", "Growing SMEs"],
        "metrics": ["Brand recall", "Message consistency", "Creative performance", "Branded search"],
    },
    {
        "slug": "ai-automation",
        "name": "AI Automation",
        "url": f"{SITE}/services/ai-automation/",
        "icon": "dui-automation",
        "img": "ai",
        "label": "Operational efficiency",
        "short": "Reduce repetitive work across leads, support, follow-up, reporting and internal workflows.",
        "bullets": ["Faster response", "Connected workflows", "Human oversight"],
        "tagline": "Respond faster and give your team time back with practical AI workflows that stay under human control.",
        "overview": "Most businesses lose leads through slow replies and manual follow-up. We map where time is being lost, then build practical automations such as WhatsApp and website chatbots, lead qualification, CRM updates, follow-up sequences and automated reports, connected to the tools you already use and always with a human in the loop.",
        "included": [
            "Workflow audit and opportunity map",
            "WhatsApp and website AI chatbots",
            "Lead capture and qualification",
            "CRM integration and auto-updates",
            "Follow-up and reminder sequences",
            "Automated reports and dashboards",
            "Internal knowledge assistants",
            "Team training and documentation",
        ],
        "steps": [
            ("Map", "List repetitive tasks and pick the one with the biggest payoff."),
            ("Build", "Create and test the workflow with your real data and tools."),
            ("Hand over", "Train your team, monitor results and expand step by step."),
        ],
        "ideal": ["High enquiry volumes", "Sales teams", "Support desks", "Clinics and institutes"],
        "metrics": ["Response time", "Hours saved", "Lead follow-up rate", "Conversion rate"],
    },
    {
        "slug": "ai-content-management",
        "name": "AI Content Management",
        "url": f"{SITE}/services/ai-content-management/",
        "icon": "dui-file",
        "img": "video",
        "label": "Scalable content systems",
        "short": "Turn business expertise into a repeatable flow of written, visual, video and audio content.",
        "bullets": ["Content repurposing", "Brand voice systems", "Human quality control"],
        "tagline": "Publish more useful content, faster, without losing your brand voice or quality.",
        "overview": "Your team knows a lot that customers never hear about. We turn that expertise into a content engine: brand voice guides, AI-assisted drafting, repurposing one idea into blogs, posts, reels, newsletters and podcasts, and a human editing layer that keeps everything accurate and on-brand.",
        "included": [
            "Brand voice and prompt library",
            "Content strategy and calendar",
            "AI-assisted blogs and articles",
            "Short-form video and reel scripts",
            "Repurposing across platforms",
            "Newsletter and email content",
            "Human editing and fact-checking",
            "Content performance tracking",
        ],
        "steps": [
            ("Capture", "Collect expertise through short interviews and existing material."),
            ("Produce", "Create multi-format content with AI support and human editing."),
            ("Distribute", "Publish, repurpose and learn from what performs."),
        ],
        "ideal": ["Founders and experts", "B2B brands", "Coaches and educators", "Content-led businesses"],
        "metrics": ["Content output", "Organic reach", "Engagement", "Time saved"],
    },
]

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}
CORE_SLUGS = [s["slug"] for s in SERVICES[:6]]
AI_SLUGS = [s["slug"] for s in SERVICES[6:]]

FAQ_HOME = [
    ("What does Digital Udyami help businesses achieve?", "Digital Udyami connects website development, SEO, paid advertising, social media, branding and AI automation around practical business goals such as visibility, qualified enquiries, sales support and operational efficiency."),
    ("Which service should a small business start with?", "The right starting point depends on the main bottleneck. A weak website needs a stronger foundation, low search visibility may need SEO, immediate demand can require paid advertising, and repetitive follow-up may benefit from automation."),
    ("Do you work with businesses across India?", "Yes. Digital Udyami is positioned for PAN India delivery and can coordinate strategy, implementation, reporting and reviews remotely."),
    ("Can website development and marketing be managed together?", "Yes. Connecting the website, tracking, SEO, advertising and lead journey usually creates a clearer customer experience than treating every channel separately."),
    ("Do you provide AI automation for existing business systems?", "Yes. Suitable workflows can include lead qualification, WhatsApp conversations, CRM updates, follow-up, internal knowledge access and reporting. The scope depends on the tools and data already in use."),
    ("How are projects priced?", "Pricing is based on the current business stage, required scope, platforms, implementation complexity and ongoing support. A short discovery conversation helps define the right engagement."),
    ("Do you guarantee rankings leads or sales?", "No responsible agency can guarantee platform rankings, lead volumes or revenue. Digital Udyami focuses on sound strategy, clear implementation, tracking and continuous improvement."),
    ("Can I contact Digital Udyami on WhatsApp?", f"Yes. You can call or message Digital Udyami on WhatsApp at {PHONE_DISPLAY}."),
    ("Do you work with startups and MSMEs?", "Yes. The service architecture is suitable for startups, MSMEs, local businesses, professional services, D2C brands and growing companies that need a clearer digital system."),
    ("How is progress measured?", "Measurement depends on the service and can include qualified enquiries, conversion actions, search visibility, lead quality, customer response time, cost efficiency and content performance."),
]

FAQ_SERVICES = [
    ("Do I need to buy every service?", "No. Most businesses start with one or two services that fix the biggest bottleneck, then add the next layer once the foundation is working."),
    ("Is ad budget included in your fees?", "No. Google and Meta ad spend is paid directly to the platform from your own account, so you always keep ownership and full visibility. Our fee covers strategy, setup, creative and management."),
    ("Who owns the website, ad accounts and content?", "You do. Websites, domains, ad accounts, analytics and content are set up in your name or handed over to you."),
    ("How soon can we see results?", "Paid ads can produce enquiries within days of launch. SEO and brand work build over months. We agree realistic milestones for each service before we start."),
    ("Do you offer monthly retainers or one-time projects?", "Both. Websites and branding are usually projects, while SEO, ads, social media and content work best as monthly retainers. Automation can be either."),
    ("What reports will I receive?", "You get a clear monthly report in plain language: what was done, what changed, what it means for the business and what happens next."),
]

FAQ_CONTACT = [
    ("How quickly will you respond?", "We aim to reply to WhatsApp messages and calls on the same working day, Monday to Saturday."),
    ("Is the first consultation free?", "Yes. The first conversation is free and focused on understanding your business, your goals and the right starting point."),
    ("Do we need to meet in person?", "No. We work with businesses across India through calls, video meetings, WhatsApp and shared documents. In-person meetings can be arranged where practical."),
    ("What should I prepare before the call?", "Your website link, social handles, current marketing activities, rough budget and the one problem you most want solved. Even partial information is fine."),
]

FAQ_AUDIT = [
    ("Is the audit really free?", "Yes. There is no charge and no obligation. The audit helps us understand whether and how we can help, and it gives you useful insight either way."),
    ("What do I need to share?", "Your website link, the city or regions you serve, your main competitors if you know them, and access to Google Analytics or ad accounts only if you want those reviewed."),
    ("How long does it take?", "We usually share the findings within three to five working days, followed by a short call to walk you through them."),
    ("Will you share the findings in writing?", "Yes. You receive a written summary of the key issues, quick wins and a suggested priority order."),
]

FAQ_INDUSTRIES = [
    ("Do you specialise in one industry?", "No. We work across industries, but every plan is built around the sales cycle, customer value and buying behaviour of that specific sector."),
    ("Do you work with businesses outside metro cities?", "Yes. Many of the businesses we support serve tier 2 and tier 3 cities, where local SEO, WhatsApp-led enquiry journeys and regional content work particularly well."),
    ("Can you handle regulated industries like healthcare or finance?", "Yes, with care. We follow platform advertising policies and avoid misleading claims, and we recommend your compliance team reviews sensitive content before it goes live."),
]
