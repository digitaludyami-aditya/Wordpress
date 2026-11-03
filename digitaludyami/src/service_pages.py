"""Service landing pages (one Elementor HTML widget each).

Every page follows the same story, without naming it on the page:
  1. where it goes wrong (the common issues + our fix)
  2. what it is costing the business
  3. why trust us (how we work, what we do, reviews / portfolio / ownership)
  4. what changes for the business (outcomes, final call to action, FAQ)

Edit the text in PAGES below, then run `python3 build.py`.
Shared look: src/svc/style.css, src/svc/icons.svg, src/svc/script.js
Rules kept on purpose: no fees on these pages, no invented numbers, logos or guarantees.
"""
from html import escape as e
from pathlib import Path

SVC = Path(__file__).parent / "svc"

CLIENTS = ["Hitech Pipes", "Zelux LED", "Archies Online", "Rossette Coffee", "Jaypee Greens Properties",
           "Pivot Real Estate", "Dezire Homes", "NewGen Healthcare", "Metics Fashion", "Sleep N Slip",
           "Truckinzy", "Uni Travels"]

# shared trust points (true for every service)
OWN_COMMON = ["Plain-language progress report every month", "Google certified SEO and Meta Ads specialists"]

PAGES = [
# ------------------------------------------------------------------ WEBSITE
dict(
  slug="website-development", path="/services/website-development/", name="Website Development",
  seo_title="Website Development Company in India | Fast, Mobile-First Websites | Digital Udyami",
  meta="Fast, mobile-first websites that turn visitors into enquiries. WordPress, WooCommerce and Shopify with SEO, speed and WhatsApp built in. Free website review.",
  kw="website development company",
  eyebrow="Mobile-first · Built to sell",
  h1a="A website that turns visitors into", h1b="enquiries, not just a pretty page.",
  lead="Every ad, post and Google search ends on your website. We build fast, clear, mobile-first websites that make people trust you and get in touch.",
  pills=["More enquiries", "Fast on mobile", "SEO-ready", "Easy to update"],
  chips_label="We build on", chips=["WordPress", "WooCommerce", "Shopify", "Custom HTML"],
  form_title="Get a free website review", form_intro="Tell us about your business. We’ll show you how your website can bring in more enquiries.",
  choice_label="What do you need?", choices=["A new website", "Redesign my website", "An online store", "A landing page"],
  goal_ph="e.g. more enquiries from Google and ads", wa_intro="Hi Digital Udyami, I’d like a free website review.",
  leak=("Lost", "visitors"),
  p_eye="Where it goes wrong", p_h2a="Visitors arrive.", p_h2b="So why don’t they get in touch?",
  p_sub="A website can be your best salesperson, working day and night. Most sites lose people in the first few seconds, for reasons that are easy to fix.",
  problems=[
    ("🐢", "Slow on mobile", "Pages take too long to load, so people leave before they see your offer.", "Speed-optimised, mobile-first build"),
    ("😕", "Unclear message", "Visitors can’t tell what you do or why they should choose you.", "Clear headlines and a simple customer journey"),
    ("📵", "No easy way to contact", "Forms are hidden and there’s no WhatsApp or call button.", "WhatsApp, call and forms on every page"),
    ("🔍", "Invisible on Google", "No SEO basics, so the site never shows up when people search.", "On-page SEO and schema from day one"),
  ],
  grow1="Fix these, and the same visitors can start turning into real enquiries.",
  pain_h="What a weak website quietly costs you",
  pain_sub="Your website works for you, or against you, 24 hours a day.",
  pain=[
    ("💸", "Wasted ad money", "Ads send people to a page that doesn’t convince them to act."),
    ("🏃", "Lost to competitors", "A faster, clearer site down the road gets the enquiry instead."),
    ("🤨", "Lower trust", "An outdated site makes a good business look small or inactive."),
  ],
  grow2="A good website makes every rupee you spend on marketing work harder.",
  flow=[
    ("🧭", "Plan the journey", "Goals, pages and what each visitor should do next.", "Sitemap ready"),
    ("✍️", "Clear messaging", "Headlines and page copy that explain your value simply.", "Content ready"),
    ("🎨", "Design mobile-first", "A clean design built for phones first, then desktop.", "Design approved"),
    ("⚙️", "Build and connect", "Fast build with forms, WhatsApp, SEO and tracking.", "Site built"),
    ("🚀", "Launch and improve", "Tested on real devices, then refined with visitor data.", "Live"),
  ],
  duo=[("🧑‍💻", "Your own project lead", "One person who plans, builds and stays with you after launch."),
       ("📊", "Built to measure", "Forms, calls and WhatsApp clicks tracked, so you know what the site brings in.")],
  bar=["More enquiries", "Faster pages", "SEO-ready", "Easy to update"],
  svc_h2a="Everything your website needs to", svc_h2b="bring in business",
  svc_sub="From the first sketch to after launch, one team handles it all.",
  svcs=[("B", "Business websites", "Clear, credible sites for service businesses and companies."),
        ("E", "Online stores", "WooCommerce and Shopify stores that are easy to shop and manage."),
        ("L", "Landing pages", "Focused pages for ads and offers, built to get enquiries."),
        ("S", "Speed & SEO", "Core Web Vitals, on-page SEO and schema set up properly."),
        ("W", "WhatsApp & forms", "Lead forms, WhatsApp and call buttons, with tracking."),
        ("T", "Training & support", "We show your team how to update it, and support you after launch.")],
  fits=["🚀 New businesses", "🔄 Old-site rebuilds", "🛍️ D2C & online stores", "💼 Professional services", "🏥 Clinics", "🏠 Real estate"],
  out_h2b="with a website that works",
  outs=[("📱", "Looks great on every phone", "Where most of your customers will see it."),
        ("💬", "More enquiries", "Easy WhatsApp, call and form options on every page."),
        ("🔍", "Easier to find", "Built with SEO basics so Google understands it."),
        ("🤝", "More trust", "A professional site that makes choosing you easy.")],
  grow3="Your website is open 24/7. Built right, it keeps bringing you customers while you sleep.",
  own=["Domain, hosting and website in your name", "Full admin access, so you can update it any time"],
  final_h2a="Ready to see what your website", final_h2b="could be doing for you?",
  final_sub="We review your current site (or your plan, if you don’t have one yet), show you where visitors are being lost and what to fix first. Free, whether or not you work with us.",
  final_btn="Book a Free Review",
  faqs=[
    ("Will my website work well on mobile?", "Yes. We design for phones first, because that’s where most of your customers will see it, then make sure it looks great on tablets and desktops too."),
    ("Which platform do you use?", "Mostly WordPress, WooCommerce or Shopify, depending on your needs. We recommend the one that’s easiest for you to manage and grow."),
    ("How long does a website take?", "It depends on the number of pages, features and how quickly content is ready. We agree a clear timeline before we start."),
    ("Who owns the website?", "You do. The domain, hosting and website are set up in your name, and you get full admin access."),
    ("Can I update the website myself?", "Yes. We build it so you can change text, images and offers easily, and we show your team how."),
    ("Will it be ready for Google?", "Yes. Speed, mobile-friendliness, on-page SEO and schema are set up from day one, so search engines understand your site."),
    ("How much does a website cost?", "It depends on the pages, features and platform. We share a clear quote after a short free consultation."),
  ],
),
# ------------------------------------------------------------------ SEO
dict(
  slug="seo-services", path="/services/seo-services/", name="SEO Services",
  seo_title="SEO Services in India | Rank on Google, Maps & AI Search | Digital Udyami",
  meta="Get found on Google, Maps and AI answers when customers are searching. Technical SEO, local SEO, content and monthly reporting. Free SEO audit.",
  kw="SEO services",
  eyebrow="Get found · Get chosen",
  h1a="Show up on Google when customers", h1b="are searching for what you sell.",
  lead="Every day, people in your area search for businesses like yours. SEO puts you in front of them on Google, Maps and AI answers, and keeps bringing enquiries month after month.",
  pills=["More visibility", "More enquiries", "Local Maps ranking", "Lasting results"],
  chips_label="Be found on", chips=["Google Search", "Google Maps", "AI answers", "Your website"],
  form_title="Get a free SEO audit", form_intro="Share your website. We’ll show you how SEO can bring more customers to your business.",
  choice_label="Where do you want to be found?", choices=["In my city", "All over India", "For my online store", "Not sure yet"],
  goal_ph="e.g. rank for “best dentist in Noida”", wa_intro="Hi Digital Udyami, I’d like a free SEO audit.",
  leak=("Missed", "searches"),
  p_eye="Where it goes wrong", p_h2a="Customers are searching.", p_h2b="So why aren’t they finding you?",
  p_sub="SEO can bring a steady flow of customers without paying for every click. Most websites miss out because of a few common gaps.",
  problems=[
    ("🧱", "Technical issues", "Slow pages, broken links and crawl errors hold the whole site back.", "Technical audit and fixes"),
    ("🎯", "Wrong keywords", "Pages target words people don’t search, or that never lead to sales.", "Keyword research based on buying intent"),
    ("📍", "Weak local presence", "Not in the Google Maps pack, with an incomplete Business Profile.", "Local SEO and Google Business Profile"),
    ("📝", "Thin content", "Pages don’t answer customers’ questions, so Google ranks others first.", "Helpful pages and a content plan"),
  ],
  grow1="Close these gaps, and your website can start bringing in customers on its own.",
  pain_h="What staying invisible quietly costs you",
  pain_sub="Every search you don’t show up for is a customer who finds someone else.",
  pain=[
    ("🏃", "Competitors get the click", "The businesses on page one get the calls, visits and sales."),
    ("💸", "Paying for every visitor", "Without organic traffic, you rely only on ads to be seen."),
    ("📉", "Growth stalls", "Without search visibility, new customers depend on word of mouth."),
  ],
  grow2="SEO keeps working for you, long after an ad budget would have stopped.",
  flow=[
    ("🔎", "Audit the site", "Technical health, rankings and competitors checked.", "Audit done"),
    ("🎯", "Find the right keywords", "Searches your buyers actually make, mapped to pages.", "Keywords mapped"),
    ("🛠️", "Fix the foundations", "Speed, structure, on-page SEO and schema improved.", "Site fixed"),
    ("📍", "Build local and authority", "Google Business Profile, citations and quality links.", "Authority growing"),
    ("📈", "Publish and report", "Helpful content and a monthly ranking report.", "Ranking up"),
  ],
  duo=[("🧑‍💼", "A dedicated SEO specialist", "Someone who knows your business, your city and your competitors."),
       ("📊", "Progress you can see", "Rankings, traffic and enquiries tracked and explained every month.")],
  bar=["More visibility", "More enquiries", "Better rankings", "Lasting results"],
  svc_h2a="Everything that helps you", svc_h2b="rank and get chosen",
  svc_sub="Technical, local and content SEO, handled by one team with one plan.",
  svcs=[("T", "Technical SEO", "Speed, crawl errors, structure and Core Web Vitals fixed."),
        ("K", "Keyword research", "Searches that bring buyers, not just traffic."),
        ("O", "On-page SEO", "Titles, headings and content tuned on your key pages."),
        ("L", "Local SEO", "Google Business Profile and Maps visibility in your area."),
        ("C", "Content & blogs", "Helpful pages that answer real customer questions."),
        ("A", "AI search readiness", "AEO and GEO basics, so AI assistants can mention you.")],
  fits=["📍 Local businesses", "💼 Service companies", "🛍️ Online stores", "🏢 B2B brands", "🏥 Clinics", "🎓 Institutes"],
  out_h2b="when customers can find you",
  outs=[("🔝", "Higher on Google", "Show up for the searches that matter to you."),
        ("📍", "On the map", "Appear in local Maps results near your customers."),
        ("📞", "More enquiries", "Calls and messages from people already searching."),
        ("🌱", "Results that last", "Visibility that keeps building month after month.")],
  grow3="Your customers search on Google every day. SEO helps them find you first.",
  own=["Website, Search Console and Analytics stay in your name", "Clean, guideline-safe SEO, no shortcuts that risk penalties"],
  final_h2a="Ready to see why customers", final_h2b="aren’t finding you yet?",
  final_sub="We check your website, rankings and competitors, and show you the quickest wins to fix first. Free, whether or not you work with us.",
  final_btn="Book a Free SEO Audit",
  faqs=[
    ("How long does SEO take to show results?", "SEO builds over months, not days. Quick technical fixes can help sooner, and results keep growing over time. We agree realistic milestones before we start."),
    ("Can you get me on the first page of Google?", "No honest agency can guarantee a ranking. We focus on the things that move rankings: a healthy website, the right keywords, helpful content and local trust signals."),
    ("Do you do local SEO for my city?", "Yes. We optimise your Google Business Profile and local signals so you can appear in Maps results near your customers."),
    ("What is AEO and GEO?", "They help your business show up in AI answers, like Google’s AI results and chat assistants, by making your content clear, structured and trustworthy."),
    ("Will you write content for my website?", "Yes. Content planning and blog strategy are part of SEO, and we create pages that answer real buying questions."),
    ("What reports will I get?", "A clear monthly report: rankings, traffic, enquiries, what we did and what’s next, in plain language."),
    ("How much do SEO services cost?", "It depends on your website, competition and goals. We share a clear quote after the free audit."),
  ],
),
# ------------------------------------------------------------------ SOCIAL
dict(
  slug="social-media-marketing", path="/services/social-media-marketing/", name="Social Media Marketing",
  seo_title="Social Media Marketing Agency in India | Instagram, Facebook & LinkedIn | Digital Udyami",
  meta="Stay visible and trusted where your customers spend time. Content calendar, posts, reels and community management for Instagram, Facebook and LinkedIn.",
  kw="social media marketing agency",
  eyebrow="Visible · Trusted · Remembered",
  h1a="Social media that makes customers", h1b="trust you before they call.",
  lead="Before people buy, they check your Instagram and Facebook. We keep your pages active, useful and on-brand, so customers remember you and reach out when they’re ready.",
  pills=["More followers", "More trust", "More enquiries", "Consistent posting"],
  chips_label="We manage", chips=["Instagram", "Facebook", "LinkedIn", "Reels"],
  form_title="Get a free social media review", form_intro="Share your pages. We’ll show you how social media can bring you more customers.",
  choice_label="Which platforms matter most?", choices=["Instagram", "Facebook", "LinkedIn", "All of them"],
  goal_ph="e.g. more enquiries from Instagram", wa_intro="Hi Digital Udyami, I’d like a free social media review.",
  leak=("Lost", "attention"),
  p_eye="Where it goes wrong", p_h2a="You post.", p_h2b="So why doesn’t it bring customers?",
  p_sub="Social media can build trust and bring steady enquiries. Most business pages miss out because of a few common habits.",
  problems=[
    ("📅", "Posting on and off", "Weeks without posts make the business look inactive.", "A monthly content calendar"),
    ("🎨", "Off-brand content", "Every post looks different, so people don’t remember you.", "On-brand posts, carousels and reels"),
    ("💬", "Comments left unanswered", "Questions go unanswered and interested people move on.", "Community and comment management"),
    ("❓", "No clear plan", "Posting without knowing what each platform is for.", "Platform strategy and content pillars"),
  ],
  grow1="Fix these, and your pages can start turning followers into customers.",
  pain_h="What an inactive page quietly costs you",
  pain_sub="Customers judge your business by your page, often before they ever call.",
  pain=[
    ("🤨", "Lost trust", "An empty or outdated page makes people wonder if you’re still open."),
    ("🏃", "Competitors stay top of mind", "Brands that post regularly get remembered, and chosen."),
    ("💸", "Ads work harder", "Ads perform better when your page already looks credible."),
  ],
  grow2="An active, useful page helps every other part of your marketing work better.",
  flow=[
    ("🧭", "Plan the strategy", "Content pillars, tone and the role of each platform.", "Strategy ready"),
    ("🗓️", "Build the calendar", "A month of posts planned around your goals.", "Calendar ready"),
    ("🎨", "Create the content", "Posts, carousels, reels and captions for your approval.", "Content approved"),
    ("📲", "Publish and engage", "Scheduled on time, comments and messages answered.", "Live"),
    ("📈", "Learn and improve", "Monthly insights, then more of what your audience loves.", "Growing"),
  ],
  duo=[("🧑‍🎨", "A dedicated content team", "Strategy, design and captions handled by people who know your brand."),
       ("📊", "Insights every month", "Reach, engagement and profile actions tracked and explained.")],
  bar=["More reach", "More trust", "More enquiries", "Consistent brand"],
  svc_h2a="Everything that keeps your pages", svc_h2b="active and growing",
  svc_sub="One team for strategy, content and community, across all your platforms.",
  svcs=[("S", "Strategy & pillars", "What to post, where, and why, mapped to your goals."),
        ("C", "Content calendar", "A month of posts planned and shared for approval."),
        ("D", "Posts & carousels", "On-brand designs that people stop to read."),
        ("R", "Reels", "Short videos and scripts that reach new people."),
        ("M", "Community management", "Comments and messages answered, so no lead is missed."),
        ("P", "Profile optimisation", "Bio, highlights and links set up to bring enquiries.")],
  fits=["🛍️ Consumer brands", "💇 Clinics & salons", "☕ Restaurants & cafes", "👤 Personal brands", "🎓 Coaching", "🏠 Real estate"],
  out_h2b="when your pages come alive",
  outs=[("👀", "More people see you", "Regular, useful content reaches new followers."),
        ("🤝", "More trust", "An active page shows customers you’re real and reliable."),
        ("💬", "More messages", "Interested people reach out through DMs and WhatsApp."),
        ("🧠", "Remembered first", "When they’re ready to buy, they think of you.")],
  grow3="Your customers scroll every day. Show up consistently and they’ll remember you when it’s time to buy.",
  own=["Pages and accounts stay in your name", "Every post shared with you for approval"],
  final_h2a="Ready to see what your pages", final_h2b="could be doing for you?",
  final_sub="We review your social pages, show you what’s working, what’s missing and what to fix first. Free, whether or not you work with us.",
  final_btn="Book a Free Review",
  faqs=[
    ("Which platforms should my business be on?", "It depends on your customers. Most consumer businesses do well on Instagram and Facebook, while B2B brands often need LinkedIn. We recommend the right mix in the free review."),
    ("Do you create the content?", "Yes. We plan the calendar and create posts, carousels, reels and captions, then share everything with you for approval."),
    ("Will you reply to comments and messages?", "Yes. Community management is included, so questions get answered and interested people aren’t missed."),
    ("How soon will I see results?", "Your pages look active straight away. Trust, reach and enquiries build over the following months with consistent posting."),
    ("Is paid advertising included?", "Social media management focuses on your pages and content. Paid ads are a separate service (Meta Ads) and work well together with it."),
    ("Who owns the pages?", "You do. Your accounts stay in your name, and we work on them with access you control."),
    ("How much does social media management cost?", "It depends on the platforms and how much content you need. We share a clear quote after the free review."),
  ],
),
# ------------------------------------------------------------------ BRANDING
dict(
  slug="branding-advertising", path="/services/branding-advertising/", name="Branding and Advertising",
  seo_title="Branding & Advertising Agency in India | Logo, Identity & Campaigns | Digital Udyami",
  meta="A clear identity and message that makes your business easier to recognise and easier to choose. Brand strategy, logo, guidelines, packaging and ad creative.",
  kw="branding agency",
  eyebrow="Recognised · Remembered · Chosen",
  h1a="A brand customers recognise,", h1b="remember and choose.",
  lead="Strong brands spend less to convince. We give your business a clear message and a look people remember, carried through everything from your logo to your ads.",
  pills=["Stand out", "Look professional", "Easier to choose", "Consistent everywhere"],
  chips_label="We design", chips=["Logo", "Brand guidelines", "Packaging", "Ad creative"],
  form_title="Get a free brand review", form_intro="Tell us about your business. We’ll show you how a stronger brand can help you win more customers.",
  choice_label="What do you need?", choices=["A new brand", "A rebrand", "Packaging & print", "Campaign creative"],
  goal_ph="e.g. launching a new product range", wa_intro="Hi Digital Udyami, I’d like a free brand review.",
  leak=("Lost", "recall"),
  p_eye="Where it goes wrong", p_h2a="Good business.", p_h2b="So why do customers forget you?",
  p_sub="A clear brand makes every ad, post and sales call easier. Most businesses struggle because of a few common gaps.",
  problems=[
    ("🌫️", "Unclear message", "People can’t tell what makes you different from others.", "Clear positioning and messaging"),
    ("🧩", "Inconsistent look", "Logo, colours and fonts change from place to place.", "Visual identity and brand guidelines"),
    ("🪫", "Dated design", "An old logo or packaging makes a good product look ordinary.", "A refreshed, modern identity"),
    ("📢", "Ads that don’t stick", "Creative that looks like everyone else’s is quickly forgotten.", "Campaign ideas built on your brand"),
  ],
  grow1="Fix these, and every rupee you spend on marketing can work harder.",
  pain_h="What a weak brand quietly costs you",
  pain_sub="When customers can’t tell you apart, they choose on price, or choose someone else.",
  pain=[
    ("💸", "Competing on price", "Without a clear difference, discounts become your only lever."),
    ("🧠", "Forgotten after the ad", "People see you, but don’t remember you when it’s time to buy."),
    ("🤨", "Less trust", "An inconsistent look makes a business feel less established."),
  ],
  grow2="A strong brand makes customers choose you, even before they compare.",
  flow=[
    ("🔎", "Discover", "Your audience, competitors and what makes you different.", "Insights ready"),
    ("🧭", "Define positioning", "Your message, tagline and personality agreed.", "Message ready"),
    ("🎨", "Design the identity", "Logo, colours, fonts and visual style created.", "Identity approved"),
    ("📘", "Create guidelines", "A simple rulebook so everything stays consistent.", "Guidelines ready"),
    ("🚀", "Launch everywhere", "Print, packaging, digital and campaign creative.", "Brand live"),
  ],
  duo=[("🧑‍🎨", "A dedicated brand team", "Strategy and design handled by people who take time to understand you."),
       ("🧪", "Ideas that are tested", "Concepts shared and refined with you before anything is final.")],
  bar=["Clear message", "Memorable look", "Consistent everywhere", "Easier to choose"],
  svc_h2a="Everything that makes your brand", svc_h2b="easy to choose",
  svc_sub="From positioning to packaging, one team keeps it all consistent.",
  svcs=[("P", "Brand positioning", "What you stand for and why customers should care."),
        ("M", "Messaging & tagline", "Words that explain your value in seconds."),
        ("L", "Logo & identity", "Logo, colours and fonts that people remember."),
        ("G", "Brand guidelines", "One simple guide so everything stays on-brand."),
        ("K", "Packaging & print", "Packaging, labels, stationery and brochures."),
        ("A", "Campaign creative", "Ad concepts and creative built on your brand.")],
  fits=["🚀 New ventures", "🔄 Rebrands", "📦 Product launches", "🏢 Growing SMEs", "🛍️ D2C brands", "🏥 Clinics"],
  out_h2b="with a brand people remember",
  outs=[("👀", "Recognised instantly", "A look customers spot across every channel."),
        ("🤝", "More trust", "A consistent brand feels established and reliable."),
        ("💬", "Clear message", "People understand your value in seconds."),
        ("🏆", "Chosen more often", "Customers pick you, not just the cheapest option.")],
  grow3="When customers remember you, every ad and post brings more of them back.",
  own=["All final logo and design files handed over to you", "Brand guidelines your whole team can use"],
  final_h2a="Ready to see how your brand", final_h2b="could win more customers?",
  final_sub="We review your current brand, show you what’s working, what’s holding you back and what to fix first. Free, whether or not you work with us.",
  final_btn="Book a Free Brand Review",
  faqs=[
    ("Do I need a full rebrand?", "Not always. Sometimes a clearer message and a refreshed look are enough. We’ll tell you honestly in the free review."),
    ("What do I get at the end?", "Depending on your project: positioning and messaging, logo and identity, brand guidelines, and the creative you need, such as packaging, print or campaign designs."),
    ("Do I own the logo and designs?", "Yes. All final files are handed over to you, ready to use."),
    ("How many design options will I see?", "We share initial concepts, then refine the chosen direction with your feedback until it’s right."),
    ("Can you design packaging and print too?", "Yes. Packaging, labels, stationery, brochures and sales presentations are all part of our branding work."),
    ("How long does a branding project take?", "It depends on the scope. We agree a clear timeline before we start."),
    ("How much does branding cost?", "It depends on what you need. We share a clear quote after the free review."),
  ],
),
# ------------------------------------------------------------------ AI CONTENT
dict(
  slug="ai-content-management", path="/services/ai-content-management/", name="AI Content Management",
  seo_title="AI Content Management Services in India | Blogs, Reels & Social Content | Digital Udyami",
  meta="Publish more useful content, faster, without losing your brand voice. AI-assisted blogs, reels scripts, social posts and newsletters with human editing.",
  kw="AI content management",
  eyebrow="AI-assisted · Human-edited",
  h1a="More content, every week,", h1b="in your brand’s own voice.",
  lead="Customers trust businesses that share what they know. We turn your expertise into a steady flow of blogs, posts, reels and newsletters, made faster with AI and checked by people.",
  pills=["More content", "Your brand voice", "Human-checked", "Time saved"],
  chips_label="We create", chips=["Blogs", "Social posts", "Reel scripts", "Newsletters"],
  form_title="Get a free content consultation", form_intro="Tell us about your business. We’ll show you how regular content can bring more customers your way.",
  choice_label="What content do you need?", choices=["Blogs & articles", "Social posts", "Reels & video scripts", "All of it"],
  goal_ph="e.g. 4 blogs and 12 posts a month", wa_intro="Hi Digital Udyami, I’d like a free content consultation.",
  leak=("Lost", "reach"),
  p_eye="Where it goes wrong", p_h2a="You know your business.", p_h2b="So why aren’t customers hearing it?",
  p_sub="Regular, useful content builds trust and brings customers to you. Most businesses fall behind for the same few reasons.",
  problems=[
    ("⏳", "No time to write", "Content keeps slipping down the to-do list.", "A content team that does it for you"),
    ("🤖", "Generic AI content", "Copy-paste AI text sounds robotic and can be wrong.", "Human editing and fact-checking"),
    ("🧩", "Inconsistent voice", "Every piece sounds different, so the brand feels scattered.", "A brand voice guide and prompt library"),
    ("🔁", "One idea, used once", "A good idea becomes one post and is never reused.", "Repurposing across every platform"),
  ],
  grow1="Fix these, and your knowledge can start working for you on every platform.",
  pain_h="What going quiet quietly costs you",
  pain_sub="When you don’t share what you know, customers learn from someone else.",
  pain=[
    ("🏃", "Competitors look like experts", "The businesses that publish regularly earn the trust."),
    ("🔍", "Less search visibility", "Without fresh, helpful content, Google and AI tools pass you by."),
    ("⏰", "Hours lost", "Your team spends time writing instead of serving customers."),
  ],
  grow2="Steady, useful content keeps customers coming to you, week after week.",
  flow=[
    ("🎙️", "Capture expertise", "Short interviews and your existing material.", "Ideas captured"),
    ("🗣️", "Set the brand voice", "A voice guide and prompts so everything sounds like you.", "Voice ready"),
    ("✍️", "Create with AI", "Blogs, posts, scripts and newsletters drafted faster.", "Drafts ready"),
    ("🧑‍💼", "Human editing", "Every piece checked for accuracy, tone and quality.", "Approved"),
    ("📣", "Publish and repurpose", "Shared everywhere, then improved using results.", "Published"),
  ],
  duo=[("🧑‍💼", "Real editors, not just tools", "People check every piece for facts, tone and quality before it goes out."),
       ("📊", "See what works", "Reach, engagement and time saved tracked every month.")],
  bar=["More content", "Your voice", "Human-checked", "Time saved"],
  svc_h2a="Everything that keeps your content", svc_h2b="flowing",
  svc_sub="One idea, turned into content for every platform, with quality checks built in.",
  svcs=[("V", "Brand voice guide", "Your tone and prompts, so AI writes like you."),
        ("C", "Content calendar", "A clear plan for what to publish and when."),
        ("B", "Blogs & articles", "Helpful, SEO-friendly articles, edited by people."),
        ("R", "Reel & video scripts", "Short-form scripts that are easy to record."),
        ("N", "Newsletters & email", "Regular emails that keep customers engaged."),
        ("E", "Editing & fact-checking", "Every piece reviewed for accuracy and quality.")],
  fits=["👤 Founders & experts", "🏢 B2B brands", "🎓 Coaches & educators", "🏥 Clinics", "💼 Consultants", "🛍️ D2C brands"],
  out_h2b="with a steady content flow",
  outs=[("📚", "Seen as the expert", "Customers learn from you, so they trust you."),
        ("🔍", "Easier to find", "Fresh content helps Google and AI tools notice you."),
        ("💬", "More conversations", "Useful content brings questions and enquiries."),
        ("⏰", "Time back", "Your team focuses on customers, not writing.")],
  grow3="Every useful piece you publish keeps working for you, long after it goes live.",
  own=["All content is yours to use anywhere", "Nothing goes live without your approval"],
  final_h2a="Ready to turn your knowledge", final_h2b="into customers?",
  final_sub="We look at your current content, show you the easiest wins and a simple plan to publish more without more work for you. Free, whether or not you work with us.",
  final_btn="Book a Free Consultation",
  faqs=[
    ("Is the content written by AI?", "AI helps us draft faster, but people plan, edit and fact-check every piece, so it’s accurate and sounds like your brand."),
    ("Will it sound like my business?", "Yes. We start by creating a brand voice guide from your existing material and short interviews, and use it for everything."),
    ("What kinds of content can you create?", "Blogs and articles, social posts, reel and video scripts, newsletters and emails, all from the same core ideas."),
    ("Do I need to approve everything?", "Yes. Nothing is published without your approval."),
    ("Will this help my SEO?", "Helpful, well-structured content supports SEO and AI search visibility. It works best alongside our SEO service."),
    ("Who owns the content?", "You do. Everything we create for you is yours to use anywhere."),
    ("How much does it cost?", "It depends on how much content you need and which formats. We share a clear quote after the free consultation."),
  ],
),
# ------------------------------------------------------------------ AI AUTOMATION
dict(
  slug="ai-automation-services", path="/services/ai-automation-services/", name="AI Automation",
  seo_title="AI Automation Services in India | WhatsApp Chatbots & Lead Follow-up | Digital Udyami",
  meta="Reply faster and never miss a lead. WhatsApp and website chatbots, lead qualification, CRM updates and follow-up automation, always under human control.",
  kw="AI automation services",
  eyebrow="Faster replies · Fewer missed leads",
  h1a="Reply in seconds and follow up", h1b="every lead, automatically.",
  lead="Most leads are lost to slow replies and forgotten follow-ups. We build practical AI workflows that answer, qualify and follow up for you, while your team stays in control.",
  pills=["Faster replies", "No missed leads", "Hours saved", "Human in control"],
  chips_label="Works with", chips=["WhatsApp", "Website chat", "Your CRM", "Reports"],
  form_title="Get a free automation consultation", form_intro="Tell us where your team loses time. We’ll show you what can be automated first.",
  choice_label="What would you like to automate?", choices=["WhatsApp replies", "Lead follow-up", "CRM updates", "Reports"],
  goal_ph="e.g. reply to every enquiry within 1 minute", wa_intro="Hi Digital Udyami, I’d like a free AI automation consultation.",
  leak=("Missed", "leads"),
  p_eye="Where it goes wrong", p_h2a="Leads come in.", p_h2b="So why do so many go cold?",
  p_sub="Fast replies and steady follow-up turn more enquiries into customers. Most teams lose leads in the same few places.",
  problems=[
    ("🐢", "Slow replies", "Enquiries wait hours for an answer, and buyers move on.", "Instant WhatsApp and website replies"),
    ("🗂️", "Leads not followed up", "Busy teams forget the second and third follow-up.", "Automatic follow-up and reminders"),
    ("⌨️", "Manual data entry", "Hours spent copying leads into sheets and the CRM.", "CRM updates that happen on their own"),
    ("📊", "Reports by hand", "Every week someone builds the same report again.", "Automated reports and dashboards"),
  ],
  grow1="Fix these, and the same enquiries can turn into more customers.",
  pain_h="What slow follow-up quietly costs you",
  pain_sub="Every hour a lead waits, the chance of winning it gets smaller.",
  pain=[
    ("🏃", "Leads go to faster competitors", "The business that replies first often gets the sale."),
    ("💸", "Wasted marketing spend", "You paid for the enquiry, then let it go cold."),
    ("😩", "A tired team", "Repetitive work leaves less time for real customers."),
  ],
  grow2="Automation helps you win more of the leads you’re already paying for.",
  flow=[
    ("🗺️", "Map your workflow", "Where time is lost and which task to fix first.", "Map ready"),
    ("🧩", "Design the flow", "Replies, questions and hand-offs to your team planned.", "Flow approved"),
    ("⚙️", "Build and connect", "Connected to WhatsApp, your website and CRM.", "Built"),
    ("🧪", "Test with real data", "Checked carefully before it talks to customers.", "Tested"),
    ("🎓", "Train and expand", "Your team trained, results monitored, next task added.", "Live"),
  ],
  duo=[("🧑‍💼", "Human in the loop", "Your team can step in any time, and important decisions stay with people."),
       ("📊", "Measured results", "Response time, hours saved and follow-up rate tracked.")],
  bar=["Faster replies", "More follow-ups", "Hours saved", "Human control"],
  svc_h2a="Practical automations that", svc_h2b="win you more customers",
  svc_sub="Start with one workflow that saves the most time, then grow step by step.",
  svcs=[("W", "WhatsApp chatbot", "Answers common questions and captures leads 24/7."),
        ("C", "Website chatbot", "Helps visitors and books enquiries while you’re busy."),
        ("Q", "Lead qualification", "Asks the right questions and routes hot leads to your team."),
        ("F", "Follow-up sequences", "Reminders and messages that keep leads warm."),
        ("R", "CRM updates", "Leads and notes added automatically, no copy-paste."),
        ("D", "Reports & dashboards", "The numbers you need, ready without manual work.")],
  fits=["📈 High enquiry volumes", "💼 Sales teams", "🎧 Support desks", "🏥 Clinics", "🎓 Institutes", "🏠 Real estate"],
  out_h2b="with automation that works",
  outs=[("⚡", "Replies in seconds", "Every enquiry gets an instant, helpful answer."),
        ("🔁", "No lead forgotten", "Follow-ups happen on time, every time."),
        ("⏰", "Hours back every week", "Your team spends time selling, not typing."),
        ("📈", "More sales", "More of your enquiries turn into customers.")],
  grow3="You already pay to get enquiries. Automation helps you win more of them.",
  own=["Workflows and data stay in your accounts", "Your team can take over a conversation any time"],
  final_h2a="Ready to stop losing leads", final_h2b="to slow follow-up?",
  final_sub="We map how enquiries flow through your business today and show you the one automation that would save the most time first. Free, whether or not you work with us.",
  final_btn="Book a Free Consultation",
  faqs=[
    ("Will a chatbot replace my team?", "No. Automation handles repetitive questions and follow-ups, and passes real conversations to your team. People stay in control."),
    ("Can it work on WhatsApp?", "Yes. WhatsApp and website chatbots are among the most common workflows we build."),
    ("Will it work with my CRM?", "In most cases, yes. We connect to the tools you already use. We’ll confirm what’s possible in the free consultation."),
    ("What should we automate first?", "Usually the task that wastes the most time or loses the most leads, often replying to new enquiries and following up."),
    ("Is my customer data safe?", "Workflows run in your own accounts, and we only use the access a workflow needs."),
    ("How long does it take to set up?", "Simple workflows can be ready quickly. Larger ones are built step by step. We agree a timeline before we start."),
    ("How much does AI automation cost?", "It depends on the workflows and tools involved. We share a clear quote after the free consultation."),
  ],
),
# ------------------------------------------------------------------ GOOGLE ADS
dict(
  slug="google-ads-management", path="/services/google-ads-management/", name="Google Ads",
  seo_title="Google Ads Management Agency in India | Search, Shopping & PMax | Digital Udyami",
  meta="Show up the moment customers search on Google, and know which rupee brought which lead. Search, Performance Max, Shopping and YouTube. Free Google Ads audit.",
  kw="Google Ads management",
  eyebrow="High intent · Measured results",
  h1a="Be the first business customers see", h1b="when they search on Google.",
  lead="People searching on Google already want what you sell. We put your business in front of them at the right moment, and track which ads bring real calls, enquiries and sales.",
  pills=["Ready-to-buy customers", "More enquiries", "Less wasted spend", "Full transparency"],
  chips_label="We run", chips=["Search", "Performance Max", "Shopping", "YouTube"],
  form_title="Get a free Google Ads audit", form_intro="Tell us about your business. We’ll show you how Google Ads can bring you more customers.",
  choice_label="Monthly ad spend on Google", choices=["Not started yet", "Under ₹25,000", "₹25,000 – ₹1 lakh", "₹1 lakh +"],
  goal_ph="e.g. more calls from people searching in Delhi", wa_intro="Hi Digital Udyami, I’d like a free Google Ads audit.",
  leak=("Budget", "leakage"),
  p_eye="Where the money goes", p_h2a="Every click costs money.", p_h2b="So why do so few turn into customers?",
  p_sub="Google Ads can bring customers who are ready to buy. Most accounts waste budget because of a few common mistakes.",
  problems=[
    ("🎯", "Wrong searches", "Ads show for searches that never turn into customers.", "Intent-focused keywords and negative lists"),
    ("📡", "No conversion tracking", "Nobody knows which ads bring calls, forms or WhatsApp leads.", "GA4 and conversion tracking, set up properly"),
    ("🧾", "Weak ads", "Ads that look like everyone else’s get skipped.", "Ad copy and extensions that pre-qualify"),
    ("🚪", "Poor landing pages", "Clicks land on a page that doesn’t convince people to act.", "Landing page recommendations"),
  ],
  grow1="Fix the leaks, and the same budget can start bringing in more real enquiries.",
  pain_h="What a leaky account quietly costs you",
  pain_sub="The budget gets spent either way. The question is whether it brings customers.",
  pain=[
    ("💸", "Paying for the wrong clicks", "Money goes on searches that were never going to buy."),
    ("🏃", "Competitors take the top spot", "Ready buyers click the business that shows up first."),
    ("❓", "Decisions in the dark", "Without tracking, you can’t tell what to grow or stop."),
  ],
  grow2="Your customers are searching on Google right now. The right ads help them find you first.",
  flow=[
    ("📡", "Set up tracking", "Every call, form and WhatsApp lead measured.", "Tracking live"),
    ("🔎", "Research keywords", "High-intent searches and negative keywords mapped.", "Keywords ready"),
    ("🚀", "Launch focused", "The best keywords first, with a controlled budget.", "Ads live"),
    ("✂️", "Cut the waste", "Poor searches and weak ads removed every week.", "Waste cut"),
    ("📈", "Grow what works", "More budget behind campaigns that convert.", "Growing"),
  ],
  duo=[("🧑‍💼", "A real ads expert", "Campaigns planned and optimised by a specialist who knows your business."),
       ("📊", "Data-backed decisions", "Cost per lead, conversions and wasted spend watched closely.")],
  bar=["More enquiries", "Better leads", "Less wasted spend", "Full visibility"],
  svc_h2a="Every kind of Google ad that", svc_h2b="brings customers",
  svc_sub="One team, one plan: reach people searching now, and remind those who visited.",
  svcs=[("S", "Search ads", "Show up when people search for what you sell."),
        ("P", "Performance Max", "Reach buyers across Google with one campaign."),
        ("C", "Shopping ads", "Product ads with images and prices for online stores."),
        ("Y", "YouTube & Display", "Remind people who visited your website."),
        ("A", "Ad copy & extensions", "Ads that stand out and pre-qualify the click."),
        ("T", "Tracking & reporting", "GA4, conversions and a report you can actually read.")],
  fits=["📞 Lead-driven services", "📍 Local businesses", "🛍️ Online stores", "🏢 B2B companies", "🏥 Clinics", "🎓 Institutes"],
  out_h2b="with Google Ads that work",
  outs=[("🔝", "Seen at the right moment", "Show up exactly when customers search."),
        ("📞", "More calls and enquiries", "From people who already want what you sell."),
        ("💸", "Less wasted budget", "Money moves to what actually brings customers."),
        ("📊", "Clear numbers", "Know which rupee brought which lead.")],
  grow3="Every day, people search for what you sell. Google Ads puts you in front of them first.",
  own=["Google Ads account and tracking stay in your name", "Ad spend paid directly to Google from your card"],
  final_h2a="Ready to see what Google Ads", final_h2b="can do for your business?",
  final_sub="We review your ads (or your plan, if you haven’t started), show you where budget is leaking and what to fix first. Free, whether or not you work with us.",
  final_btn="Book a Free Audit",
  faqs=[
    ("How soon will I see enquiries?", "Google Ads can bring enquiries within days of launch. The first weeks are for learning and refining, so results usually improve over the first month or two."),
    ("Is the ad budget separate from your charges?", "Yes. Your ad budget is paid directly to Google from your own card, so you always see exactly what was spent. Our charges depend on your goals and budget, and we share a clear quote after the free audit."),
    ("How much should I spend on Google Ads?", "It depends on your industry, city and how much a customer is worth to you. After the audit we recommend a starting budget that’s enough to learn properly."),
    ("Do I keep ownership of my account?", "Yes. The Google Ads account, Analytics and tracking stay in your name. We work on them with access you control."),
    ("Search or Performance Max: which is better?", "Search is great for capturing people actively looking for you. Performance Max can add reach across Google. We often start with Search and add others once tracking proves what works."),
    ("Will you track calls and WhatsApp leads?", "Yes. We set up tracking so calls, forms and WhatsApp enquiries are measured, not just clicks."),
    ("Can you guarantee a number of leads?", "No, and be careful of anyone who does. What you get from us is a sound setup, honest optimisation, clear reporting and steady improvement."),
  ],
),
# ------------------------------------------------------------------ META ADS
dict(
  slug="meta-ads-management", path="/services/meta-ads-management/", name="Meta Ads",
  seo_title="Meta Ads Management Agency in India | Facebook & Instagram Ads | Digital Udyami",
  meta="Turn Facebook and Instagram into a steady source of enquiries and customers. Expert-managed Meta Ads with proper tracking, fresh creative and a focus on lead quality. Free ad audit.",
  kw="Meta Ads management",
  eyebrow="Human-led · Data-driven",
  h1a="Facebook & Instagram ads that bring you", h1b="customers, not just clicks.",
  lead="Expert-managed Meta Ads for Indian businesses. We put your offer in front of people who are ready to buy, so more of them call, message and visit.",
  pills=["More enquiries", "Better leads", "Less wasted spend", "Full transparency"],
  chips_label="We run your ads on", chips=["Facebook", "Instagram", "WhatsApp", "Messenger"],
  form_title="Get your free ad audit", form_intro="Tell us a little about your business. We’ll show you how Meta ads can bring you more enquiries.",
  choice_label="Monthly ad spend on Meta", choices=["Not started yet", "Under ₹25,000", "₹25,000 – ₹1 lakh", "₹1 lakh +"],
  goal_ph="e.g. more WhatsApp enquiries in Noida", wa_intro="Hi Digital Udyami, I’d like a free Meta ads audit.",
  leak=("Budget", "leakage"),
  p_eye="Where the money goes", p_h2a="Every rupee counts.", p_h2b="So why do most Meta ads waste budget?",
  p_sub="Meta ads can bring a steady flow of customers. Most businesses lose money not because ads don’t work, but because they’re run the wrong way.",
  problems=[
    ("🔥", "Wasted ad spend", "“Boost post”, wrong audiences and old ads burn your budget.", "Right audience, tested ads, smart bidding"),
    ("📵", "Junk leads", "Fake numbers and people who never pick up the phone.", "Qualifying questions and WhatsApp ads"),
    ("📡", "Meta can’t see buyers", "No working Pixel, so Meta can’t find more people like your customers.", "Pixel + Conversions API, set up and tested"),
    ("❓", "No clear numbers", "Reports full of reach and likes, but nothing about sales.", "A simple monthly report on what brings customers"),
  ],
  grow1="Fix the leaks, and the same ad money can start bringing in more real enquiries.",
  pain_h="What badly run ads quietly cost you",
  pain_sub="The money is spent either way. The question is whether it brings you customers.",
  pain=[
    ("🧠", "Meta learns the wrong lesson", "Junk form fills teach Meta to find you more junk."),
    ("😩", "Your team wastes hours", "Calling numbers that never pick up, while real buyers wait."),
    ("🏃", "Warm buyers go elsewhere", "Without reminder ads, a competitor’s ad is what they see next."),
  ],
  grow2="Your customers are on Facebook and Instagram every day. Ads done right help them find you first.",
  flow=[
    ("🧭", "Plan the route", "Your offer, buyers, city and goal mapped out.", "Plan ready"),
    ("📡", "Set up tracking", "Pixel and Conversions API, so Meta learns who buys.", "Tracking live"),
    ("🚀", "Launch and test", "Several ads and audiences go live to find winners fast.", "Ads live"),
    ("✂️", "Cut the waste", "Weak ads switched off. Lead quality checked with you.", "Waste cut"),
    ("📈", "Grow what works", "More budget behind winners. Clear monthly report.", "Growing"),
  ],
  duo=[("🧑‍💼", "A real ad expert", "Strategy, audiences and creative handled by a dedicated specialist who knows your business."),
       ("📊", "Data-backed decisions", "Cost per lead, lead quality and wasted spend watched closely, so budget goes where it works.")],
  bar=["More enquiries", "Better leads", "Less wasted spend", "Full visibility"],
  svc_h2a="Every kind of Meta ad that", svc_h2b="brings customers",
  svc_sub="One team, one plan: different ads for people who’ve never heard of you, people who are interested, and people ready to buy.",
  svcs=[("L", "Lead generation ads", "Instant forms with qualifying questions, so you get enquiries worth calling."),
        ("W", "WhatsApp click ads", "One tap starts a chat with you. Real conversations, not cold forms."),
        ("R", "Reels & creative", "Scroll-stopping ads, reels and copy, refreshed before they get stale."),
        ("B", "Retargeting", "Reminder ads bring back people who visited but didn’t buy."),
        ("S", "Sales & catalogue ads", "Show the right products to the right shoppers for online stores."),
        ("T", "Tracking & reporting", "Pixel, Conversions API and a monthly report you can actually read.")],
  fits=["🛍️ D2C brands", "🏠 Real estate", "🎓 Education & coaching", "📍 Local services", "🏥 Clinics", "✈️ Travel"],
  out_h2b="with ads that work",
  outs=[("👀", "More people find you", "Buyers in your city see your offer every day."),
        ("💬", "A busier WhatsApp", "Real questions from people who want to buy."),
        ("📞", "Better-quality calls", "People who already know what you sell."),
        ("🔁", "Customers come back", "Reminder ads turn visitors into buyers.")],
  grow3="Good ads don’t just bring leads this month. They build a steady flow of customers for your business.",
  own=["Ad account and Pixel stay in your name", "Ad spend paid directly to Meta from your card"],
  final_h2a="Ready to see what Meta ads", final_h2b="can do for your business?",
  final_sub="We review your ads (or your plan, if you haven’t started), show you where the enquiries are being lost and what to fix first. Free, whether or not you work with us.",
  final_btn="Book a Free Audit",
  faqs=[
    ("Can Meta ads really bring more customers?", "Yes, for most businesses that sell to consumers or local customers. Facebook and Instagram let you reach people by city, age and interests and start conversations on WhatsApp. Results depend on your offer and follow-up, which is why we start with a free audit."),
    ("How soon will I see enquiries?", "Meta ads can bring enquiries within days of launch. The first few weeks are for testing, so results usually get better and more consistent over the first month or two."),
    ("Is the ad budget separate from your charges?", "Yes. Your ad budget is paid directly to Meta from your own card, so you always see exactly what was spent. Our charges depend on your goals and budget, and we share a clear quote after the free audit."),
    ("How much should I spend on ads?", "It depends on your city, product and how much a customer is worth to you. After the audit we recommend a starting budget that’s enough to test properly, and increase it only once ads are working."),
    ("Do I keep ownership of my ad account?", "Yes. The ad account, Pixel, audiences and Facebook page stay in your name. We work on them with partner access, which you control."),
    ("Do you make the ads and reels?", "Yes. Ad creative, reels and copy are included. We test several versions and replace tired ads before results drop."),
    ("Can you guarantee a number of leads?", "No, and be careful of anyone who does. What you get from us is a sound setup, honest testing, clear reporting and steady improvement."),
  ],
),
]

SITE = "https://www.digitaludyami.com"
SHORT = {"website-development": "website", "seo-services": "SEO", "social-media-marketing": "social media",
         "branding-advertising": "branding", "ai-content-management": "AI content", "ai-automation-services": "AI automation",
         "google-ads-management": "Google Ads", "meta-ads-management": "Meta Ads"}
FUNNEL = """<svg viewBox="0 0 320 300">
          <defs><linearGradient id="svc-f" x1="0" x2="1"><stop offset="0" stop-color="#FF5904"/><stop offset="1" stop-color="#FF9A01"/></linearGradient></defs>
          <ellipse cx="160" cy="40" rx="130" ry="26" fill="#FFE2CC"/>
          <path d="M30 40 C30 60 290 60 290 40 L190 170 L190 215 L130 215 L130 170 Z" fill="url(#svc-f)"/>
          <ellipse cx="160" cy="40" rx="118" ry="20" fill="#C2410C" opacity=".35"/>
          <g font-family="Arial" font-weight="700" font-size="15" fill="#7A2E00" text-anchor="middle">
            <circle cx="120" cy="34" r="14" fill="#FFD27A"/><text x="120" y="39">₹</text>
            <circle cx="165" cy="44" r="14" fill="#FFD27A"/><text x="165" y="49">₹</text>
            <circle cx="205" cy="32" r="14" fill="#FFD27A"/><text x="205" y="37">₹</text>
            <circle cx="160" cy="238" r="13" fill="#FFD27A"/><text x="160" y="243">₹</text>
            <circle cx="132" cy="262" r="12" fill="#FFD27A" opacity=".8"/><text x="132" y="267">₹</text>
            <circle cx="192" cy="270" r="12" fill="#FFD27A" opacity=".7"/><text x="192" y="275">₹</text>
            <circle cx="160" cy="288" r="10" fill="#FFD27A" opacity=".5"/>
          </g>
          <path d="M215 120 h70 m-12 -10 l12 10 -12 10" fill="none" stroke="#FF9A01" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>"""


def ok(t):
    return f'<li class="chk"><svg aria-hidden="true"><use href="#mx-ok"/></svg>{e(t)}</li>'


def render(p):
    """Return the full HTML widget for one service page."""
    css = (SVC / "style.css").read_text()
    icons = (SVC / "icons.svg").read_text()
    js = (SVC / "script.js").read_text()
    url = SITE + p["path"]
    wa_short = p["wa_intro"]
    pills = "".join(f'<span class="pill"><svg aria-hidden="true"><use href="#mx-ok"/></svg>{e(x)}</span>' for x in p["pills"])
    chips = "".join(f"<b>{e(x)}</b>" for x in p["chips"])
    opts = '<option value="">Select</option>' + "".join(f"<option>{e(x)}</option>" for x in p["choices"])
    names = "".join(f"<span>{e(x)}</span>" for x in CLIENTS)
    probs = "".join(
        f'<div class="lc"><span class="no">0{i}</span><span class="ic">{ic}</span><h3>{e(t)}</h3><p>{e(d)}</p>'
        f'<div class="fix"><b>✓ Our fix</b><p>{e(fx)}</p></div></div>'
        for i, (ic, t, d, fx) in enumerate(p["problems"], 1))
    hurts = "".join(f'<div class="hurt"><i>{ic}</i><div><b>{e(t)}</b><span>{e(d)}</span></div></div>' for ic, t, d in p["pain"])
    flow = "".join(
        f'<div class="fc"><span class="no">0{i}</span><span class="ic">{ic}</span><h3>{e(t)}</h3><p>{e(d)}</p><span class="st">{e(s)}</span></div>'
        for i, (ic, t, d, s) in enumerate(p["flow"], 1))
    duo = "".join(f'<div class="dc"><span class="ic">{ic}</span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></div>' for ic, t, d in p["duo"])
    bar = "".join(f"<span>{e(x)}</span>" for x in p["bar"])
    svcs = "".join(f'<div class="sc"><span class="lt">{e(l)}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for l, t, d in p["svcs"])
    fits = "".join(f"<span>{e(x)}</span>" for x in p["fits"])
    outs = "".join(f'<div class="oc"><i>{ic}</i><b>{e(t)}</b><small>{e(d)}</small></div>' for ic, t, d in p["outs"])
    own = "".join(ok(x) for x in p["own"] + OWN_COMMON)
    faqs = "".join(f"<details{' open' if i == 0 else ''}><summary>{e(q)}</summary><p>{e(a)}</p></details>" for i, (q, a) in enumerate(p["faqs"]))
    name = p["name"]
    return f"""<!--
DIGITAL UDYAMI · {name.upper()} · ELEMENTOR HTML WIDGET (generated by build.py from src/service_pages.py)
Page: {url}
SEO title: {p["seo_title"]}
Meta description: {p["meta"]}
Focus keyword: {p["kw"]}

Setup: edit the page with Elementor > Page Layout "Elementor Full Width" > Hide Title > one Full Width container (0 padding)
> one HTML widget > paste this whole file > Publish.
Light and fast: no photos, no animation. The form opens WhatsApp with the visitor's details filled in (no plugin needed).
REAL RESULTS (optional): add real, client-approved results in the <script type="application/json" data-cases> block.
-->
<div id="du-svc" data-whatsapp="918595565628" data-phone="+918595565628" data-roadmap="https://digitaludyami.com/digitalindiaroadmap/" data-portfolio="https://www.digitaludyami.com/portfolio/" data-reviews="https://share.google/rA5Qp1LxjH8SAxs50">
<style>
{css}</style>

{icons}

<!-- HERO -->
<section class="hero dark">
  <div class="w hgrid">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="https://www.digitaludyami.com/">Home</a><span><a href="https://www.digitaludyami.com/services/">Services</a></span><span aria-current="page">{e(name)}</span></nav>
      <span class="eye">{e(p["eyebrow"])}</span>
      <h1>{e(p["h1a"])} <span class="gt">{e(p["h1b"])}</span></h1>
      <p class="lead">{e(p["lead"])}</p>
      <div class="pills">{pills}</div>
      <div class="acts">
        <a class="btn btn-o" href="#audit-form">{e(p["final_btn"].replace("Book a ", "Get My "))} <svg aria-hidden="true"><use href="#mx-arrow"/></svg></a>
        <a class="btn btn-ghost" href="#how-it-works">See how it works</a>
      </div>
      <p class="plat">{e(p["chips_label"])} {chips}</p>
    </div>
    <form class="form" id="audit-form" data-form data-intro="{e(wa_short)}" data-choice="{e(p["choice_label"])}" novalidate>
      <h3>{e(p["form_title"])}</h3>
      <p>{e(p["form_intro"])}</p>
      <div class="fields">
        <label><span>Your name *</span><input name="name" autocomplete="name" required></label>
        <div class="two">
          <label><span>Phone / WhatsApp *</span><input name="phone" type="tel" inputmode="tel" autocomplete="tel" required></label>
          <label><span>Business or website</span><input name="biz" autocomplete="organization"></label>
        </div>
        <label><span>{e(p["choice_label"])}</span><select name="choice">{opts}</select></label>
        <label><span>What do you want more of?</span><textarea name="msg" placeholder="{e(p["goal_ph"])}"></textarea></label>
      </div>
      <p class="err" data-err role="alert">Please add your name and a valid phone number.</p>
      <button type="submit" class="btn btn-o"><svg aria-hidden="true"><use href="#mx-wa"/></svg> Send on WhatsApp</button>
      <small>Opens WhatsApp with your details. No spam, no pressure.</small>
    </form>
  </div>
</section>

<!-- CLIENT STRIP -->
<section class="strip">
  <div class="w">
    <h2>Businesses we’ve worked with</h2>
    <div class="names">{names}</div>
  </div>
</section>

<!-- WHERE IT GOES WRONG + WHAT IT COSTS -->
<section class="sec" id="where-it-goes-wrong">
  <div class="w">
    <div class="leak">
      <div class="funnel" aria-hidden="true">
        {FUNNEL}
        <span class="tagbox">{e(p["leak"][0])} <b>{e(p["leak"][1])}</b></span>
      </div>
      <div>
        <span class="eye">{e(p["p_eye"])}</span>
        <h2>{e(p["p_h2a"])} <span class="gt">{e(p["p_h2b"])}</span></h2>
        <p class="sub">{e(p["p_sub"])}</p>
      </div>
    </div>
    <div class="cards4">{probs}</div>
    <p class="grow"><span>💡</span>{e(p["grow1"])}</p>
    <div class="costs">
      <h3>{e(p["pain_h"])}</h3>
      <p>{e(p["pain_sub"])}</p>
      <div class="hurts">{hurts}</div>
      <p class="grow"><span>📈</span>{e(p["grow2"])}</p>
    </div>
  </div>
</section>

<!-- HOW IT WORKS (dark) -->
<section class="sec dark" id="how-it-works">
  <div class="w center">
    <span class="eye">How we work</span>
    <h2>Inside a <span class="gt">Digital Udyami</span> {e(SHORT.get(p["slug"], name))} project</h2>
    <p class="sub">Nothing left to chance. Every step is planned, checked and improved, so it keeps bringing you customers.</p>
  </div>
  <div class="w">
    <div class="flow">{flow}</div>
    <div class="duo">{duo}</div>
    <div class="bar">{bar}</div>
  </div>
</section>

<!-- WHAT WE DO -->
<section class="sec soft" id="what-we-do">
  <div class="w center">
    <span class="eye">What we do for you</span>
    <h2>{e(p["svc_h2a"])} <span class="gt">{e(p["svc_h2b"])}</span></h2>
    <p class="sub">{e(p["svc_sub"])}</p>
  </div>
  <div class="w">
    <div class="grid6">{svcs}</div>
    <div class="fits">{fits}</div>
  </div>
</section>

<!-- WHY US -->
<section class="sec" id="why-us">
  <div class="w center">
    <span class="eye">Why businesses trust us</span>
    <h2>See our work <span class="gt">before you decide</span></h2>
    <p class="sub">We help businesses grow with work that brings real enquiries. Check us out for yourself.</p>
  </div>
  <div class="w">
    <div class="links">
      <a class="lk" data-href="reviews" target="_blank" rel="noopener"><span class="ic">⭐</span><span><b>Read our Google reviews</b><small>From real clients</small></span><svg class="go" aria-hidden="true"><use href="#mx-arrow"/></svg></a>
      <a class="lk" data-href="portfolio"><span class="ic">🗂️</span><span><b>Browse our portfolio</b><small>Work for real businesses</small></span><svg class="go" aria-hidden="true"><use href="#mx-arrow"/></svg></a>
      <div class="lk"><span class="ic">📱</span><span><b>See how we market ourselves</b><span class="soc">
        <a href="https://www.facebook.com/digitaludyami" target="_blank" rel="noopener" aria-label="Facebook"><svg><use href="#mx-fb"/></svg></a>
        <a href="https://www.instagram.com/digitaludyami" target="_blank" rel="noopener" aria-label="Instagram"><svg><use href="#mx-ig"/></svg></a>
        <a href="https://www.linkedin.com/company/digitaludyami/" target="_blank" rel="noopener" aria-label="LinkedIn"><svg><use href="#mx-li"/></svg></a></span></span></div>
    </div>

    <div data-cases-wrap hidden>
      <div class="cases" data-cases-out></div>
    </div>
    <!-- Add real, client-approved results here. Example:
    [{{"industry":"Real estate · Noida","title":"Launch campaign","result":"₹182 per site visit","detail":"What we did, in one line."}}]
    -->
    <script type="application/json" data-cases>[]</script>

    <div class="banner">
      <span class="shield" aria-hidden="true">🛡️</span>
      <h3>Your business. Your data. Your control.</h3>
      <p>You stay in control from day one, and you always know what we’re doing for your business.</p>
      <ul class="own">{own}</ul>
    </div>
  </div>
</section>

<!-- WHAT CHANGES (dark) -->
<section class="sec dark" id="what-changes">
  <div class="w center">
    <span class="eye">What changes for you</span>
    <h2>Picture your business <span class="gt">{e(p["out_h2b"])}</span></h2>
    <div class="out">{outs}</div>
    <p class="grow" style="text-align:left"><span>🌱</span>{e(p["grow3"])}</p>
  </div>
</section>

<!-- FINAL CTA + FAQ -->
<section class="sec soft" id="faq">
  <div class="w">
    <div class="final">
      <h2>{e(p["final_h2a"])} <span class="gt">{e(p["final_h2b"])}</span></h2>
      <p class="sub">{e(p["final_sub"])}</p>
      <div class="acts">
        <a class="btn btn-o" href="#audit-form">{e(p["final_btn"])} <svg aria-hidden="true"><use href="#mx-arrow"/></svg></a>
        <a class="btn btn-l" data-href="phone"><svg aria-hidden="true"><use href="#mx-phone"/></svg> Call +91 859 5565 628</a>
      </div>
      <p class="rm">🪔 Want website, SEO, social media and ads together? See our Digital India Startup Road Map. <a data-href="roadmap">See the Road Map →</a></p>
    </div>

    <div class="center" style="margin-top:56px"><span class="eye">Common questions</span><h2>Things business owners ask us</h2></div>
    <div class="faqs">{faqs}</div>
  </div>
</section>

<div class="sbar" aria-label="Quick contact">
  <a class="btn btn-l" data-href="phone"><svg aria-hidden="true"><use href="#mx-phone"/></svg> Call</a>
  <a class="btn btn-g" data-wa="{e(wa_short)}"><svg aria-hidden="true"><use href="#mx-wa"/></svg> WhatsApp</a>
</div>

<script type="application/ld+json">
{{"@context":"https://schema.org","@graph":[
{{"@type":"Service","name":"{e(name)}","url":"{url}","areaServed":{{"@type":"Country","name":"India"}},"provider":{{"@type":"Organization","name":"Digital Udyami","url":"https://www.digitaludyami.com/","telephone":"+918595565628"}}}},
{{"@type":"FAQPage","mainEntity":[]}}
]}}
</script>

<script>
{js}</script>
</div>
"""
