"""Privacy Policy and Terms and Conditions content.

Fill in the optional business details below. When a value is empty the
text falls back to a neutral wording, so nothing half-filled ever goes live.
These documents are a starting point, not legal advice: have them reviewed
by a qualified lawyer before publishing.
"""
from data import EMAIL, PHONE_DISPLAY, SITE

EFFECTIVE_DATE = "27 September 2026"
LEGAL_NAME = "Digital Udyami"          # registered business name, e.g. "Digital Udyami (Proprietor: ...)"
REGISTERED_ADDRESS = ""                # full postal address
GRIEVANCE_OFFICER = ""                 # name of the Grievance Officer
JURISDICTION_CITY = ""                 # city whose courts have jurisdiction, e.g. "New Delhi"
PAYMENT_DAYS = 7                       # invoice payment period in days
NOTICE_DAYS = 30                       # notice period to end a monthly retainer

_addr = f"<br>{REGISTERED_ADDRESS}" if REGISTERED_ADDRESS else ""
_courts = (f"the courts at {JURISDICTION_CITY}, India" if JURISDICTION_CITY
           else "the competent courts having jurisdiction over our registered place of business in India")
_contact_block = (f'<div class="du-legal-contact"><strong>{LEGAL_NAME}</strong>{_addr}<br>'
                  f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>Phone / WhatsApp: {PHONE_DISPLAY}<br>'
                  f'Website: <a href="{SITE}/">{SITE.replace("https://", "")}</a></div>')

_grievance_block = _contact_block.replace(
    f"<strong>{LEGAL_NAME}</strong>",
    f"<strong>Grievance Officer{': ' + GRIEVANCE_OFFICER if GRIEVANCE_OFFICER else ''}</strong><br>{LEGAL_NAME}")

PRIVACY_SUMMARY = [
    ("dui-shield", "We collect only what we need", "Contact details you choose to share, and basic usage data that keeps the website working."),
    ("dui-users", "We never sell your data", "Your information is used to reply to you and deliver our services, never sold or rented."),
    ("dui-whatsapp", "Our forms open WhatsApp", "Website forms prepare a message in your browser. Nothing is sent until you press send."),
    ("dui-check", "You stay in control", "Ask us to access, correct or delete your data at any time."),
]

PRIVACY = [
    ("introduction", "Introduction", f"""
<p>This Privacy Policy explains how {LEGAL_NAME} (“<strong>Digital Udyami</strong>”, “<strong>we</strong>”, “<strong>us</strong>” or “<strong>our</strong>”) collects, uses, shares and protects personal data when you visit <a href="{SITE}/">{SITE.replace("https://", "")}</a> (the “<strong>Website</strong>”), contact us, or use our digital marketing, website development, advertising, branding and AI automation services (the “<strong>Services</strong>”).</p>
<p>We follow the Digital Personal Data Protection Act, 2023 (“<strong>DPDP Act</strong>”), the Information Technology Act, 2000 and the Information Technology (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules, 2011, and other applicable Indian laws. By using the Website or sharing your details with us, you agree to this Policy.</p>"""),
    ("data-we-collect", "Information we collect", """
<h3>Information you give us</h3>
<ul>
<li><strong>Contact details:</strong> your name, phone or WhatsApp number, email address, business name and website.</li>
<li><strong>Enquiry details:</strong> your goals, budget, industry, city and any message you send us.</li>
<li><strong>Client information:</strong> if you become a client, billing details, GST number and the information needed to deliver the Services.</li>
<li><strong>Account access:</strong> access you grant us to your website, analytics, ad accounts, social media or CRM so we can do the work you asked for.</li>
</ul>
<h3>Information collected automatically</h3>
<ul>
<li><strong>Usage data:</strong> pages visited, time on page, referring website, device type, browser and approximate location (city level), collected through cookies and analytics tools.</li>
<li><strong>Technical data:</strong> IP address and server logs needed to keep the Website secure and working.</li>
</ul>
<p>We do not knowingly collect sensitive personal data such as passwords (other than access you choose to grant for a project), financial account details, health information or biometric data through the Website.</p>"""),
    ("how-forms-work", "How our website forms work", """
<p>The enquiry forms on our Website do <strong>not</strong> store your details on our servers. When you submit a form, your browser prepares a message and opens WhatsApp (or your email app). Your details are shared with us <strong>only if you choose to send that message</strong>.</p>
<p>Once you send it, the message is handled under this Policy and under WhatsApp’s own privacy policy, which is operated by WhatsApp LLC / Meta Platforms.</p>"""),
    ("how-we-use", "How we use your information", """
<p>We use personal data only for clear, lawful purposes:</p>
<ul>
<li>to reply to your enquiry, call you back or send you a proposal;</li>
<li>to deliver, manage and improve the Services you have engaged us for;</li>
<li>to send invoices, collect payments and keep accounting and tax records;</li>
<li>to understand how visitors use the Website and improve its content and performance;</li>
<li>to run and measure our own advertising, including remarketing on Google and Meta platforms;</li>
<li>to send you updates or useful information, only where you have agreed or where it relates to Services you use (you can opt out at any time);</li>
<li>to keep the Website secure, prevent fraud and comply with legal obligations.</li>
</ul>
<p>Our legal basis is your <strong>consent</strong>, which you give when you contact us or accept cookies, together with the <strong>legitimate uses</strong> permitted under the DPDP Act, such as performing a contract you have requested and meeting legal obligations.</p>"""),
    ("cookies", "Cookies and tracking", """
<p>Cookies are small files stored on your device. We and our partners may use:</p>
<ul>
<li><strong>Essential cookies</strong> that make the Website work (for example, security and WordPress functions);</li>
<li><strong>Analytics cookies</strong>, such as Google Analytics, that show how the Website is used;</li>
<li><strong>Advertising cookies and pixels</strong>, such as Google Ads and the Meta Pixel, that measure our campaigns and show relevant ads.</li>
</ul>
<p>You can block or delete cookies in your browser settings, and you can manage ad preferences in your Google and Meta account settings. Blocking some cookies may affect how the Website works.</p>"""),
    ("sharing", "How we share information", """
<p>We <strong>do not sell or rent</strong> your personal data. We share it only when needed, with:</p>
<ul>
<li><strong>Service providers</strong> who help us operate: hosting, email, WhatsApp, cloud storage, CRM, analytics, payment and accounting tools;</li>
<li><strong>Advertising and technology platforms</strong> (such as Google, Meta, LinkedIn and AI tools) when this is needed to deliver Services you have asked for;</li>
<li><strong>Professional advisers</strong> such as accountants and lawyers, under confidentiality obligations;</li>
<li><strong>Government or law enforcement authorities</strong>, when required by law or a valid legal order.</li>
</ul>
<p>Some of these providers may store data on servers outside India. When that happens we take reasonable steps to make sure your data stays protected, in line with the DPDP Act and any restrictions notified by the Government of India.</p>"""),
    ("ai-tools", "Use of AI tools", """
<p>We use AI tools to support research, content drafting, reporting and automation. We avoid putting personal data into AI tools unless this is needed for a Service you have asked for. When we do, we use business-grade tools with data-protection settings wherever available. People review AI-assisted work before it is delivered.</p>"""),
    ("retention", "How long we keep information", """
<ul>
<li><strong>Enquiries that do not become projects:</strong> kept for up to 24 months, then deleted.</li>
<li><strong>Client records, contracts and invoices:</strong> kept for as long as the law requires, generally up to 8 years for tax and accounting purposes.</li>
<li><strong>Analytics data:</strong> kept according to the retention settings of the analytics tool, usually 14 months.</li>
</ul>
<p>When data is no longer needed, we delete or anonymise it. Access to your accounts that you granted for a project should be removed by you when the engagement ends, and we will help you do this.</p>"""),
    ("security", "How we protect information", """
<p>We use reasonable security practices, including access controls, strong passwords and two-factor authentication where available, encrypted (HTTPS) connections, limited staff access on a need-to-know basis, and trusted service providers. No method of transmission or storage is completely secure. If a personal data breach occurs, we will act quickly and notify affected people and the authorities as required by law.</p>"""),
    ("your-rights", "Your rights", """
<p>Under the DPDP Act you have the right to:</p>
<ul>
<li><strong>access</strong> a summary of the personal data we hold about you and how it is used;</li>
<li><strong>correct, complete or update</strong> your personal data;</li>
<li><strong>erase</strong> your personal data when it is no longer needed, unless the law requires us to keep it;</li>
<li><strong>withdraw consent</strong> at any time, as easily as you gave it (this does not affect processing already done);</li>
<li><strong>raise a grievance</strong> with us and, if not resolved, with the Data Protection Board of India;</li>
<li><strong>nominate</strong> another person to exercise these rights in case of your death or incapacity.</li>
</ul>
<p>To use any of these rights, contact us using the details below. We may need to verify your identity before acting on a request.</p>"""),
    ("children", "Children’s privacy", """
<p>The Website and Services are meant for businesses and adults. We do not knowingly collect personal data from anyone under 18 years of age. If you believe a child has shared personal data with us, please contact us and we will delete it.</p>"""),
    ("third-party-links", "Third-party websites", """
<p>The Website links to third-party sites and platforms such as WhatsApp, Google Reviews, Facebook, Instagram, LinkedIn and X. We are not responsible for their content or privacy practices, so please read their policies before sharing information with them.</p>"""),
    ("changes", "Changes to this policy", f"""
<p>We may update this Policy from time to time. The latest version will always be on this page with the “Last updated” date. If we make important changes, we will make reasonable efforts to let you know, for example with a notice on the Website.</p>"""),
    ("grievance", "Contact and Grievance Officer", f"""
<p>For questions, requests or complaints about this Policy or your personal data, please contact our Grievance Officer:</p>
{_grievance_block}
<p>We will acknowledge your request within 48 hours and aim to resolve it within 30 days.</p>"""),
]

TERMS_SUMMARY = [
    ("dui-file", "Scope is agreed in writing", "Each project or retainer starts with a proposal that sets out deliverables, timelines and fees."),
    ("dui-target", "Ad spend is yours", "Advertising budgets are paid by you directly to Google, Meta and other platforms, from accounts you own."),
    ("dui-key", "You own your work", "Once invoices are paid, the final deliverables and your accounts belong to you."),
    ("dui-shield", "No fake guarantees", "We commit to sound work and honest reporting, not to rankings, leads or revenue we cannot control."),
]

TERMS = [
    ("agreement", "About these terms", f"""
<p>These Terms and Conditions (“<strong>Terms</strong>”) apply to your use of <a href="{SITE}/">{SITE.replace("https://", "")}</a> (the “<strong>Website</strong>”) and to the services provided by {LEGAL_NAME} (“<strong>Digital Udyami</strong>”, “<strong>we</strong>”, “<strong>us</strong>”) to you (“<strong>Client</strong>”, “<strong>you</strong>”).</p>
<p>By using the Website, accepting a proposal, signing a service agreement or paying an invoice, you agree to these Terms. If a signed proposal or agreement says something different, the <strong>signed document takes priority</strong> for that engagement.</p>"""),
    ("services", "Our services", """
<p>We provide digital marketing and related services, including search engine optimisation (SEO), website development, Google Ads and Meta Ads management, social media marketing, branding and advertising, AI automation and AI content management (the “<strong>Services</strong>”).</p>
<p>Service descriptions on the Website are general. The exact scope, deliverables, timelines, number of revisions and fees for your engagement are set out in the proposal or quotation we send you (the “<strong>Proposal</strong>”). Work not included in the Proposal is extra and will be quoted separately.</p>"""),
    ("engagement", "Starting an engagement", """
<ul>
<li>An engagement begins when you accept the Proposal in writing (email or WhatsApp is enough) and pay any advance stated in it.</li>
<li><strong>Projects</strong> (such as websites and branding) run until the agreed deliverables are completed and handed over.</li>
<li><strong>Retainers</strong> (such as SEO, ads management, social media and content) run month to month, or for the minimum term stated in the Proposal.</li>
</ul>"""),
    ("fees", "Fees and payment", f"""
<ul>
<li>Fees are as stated in the Proposal and are <strong>exclusive of GST</strong> and other applicable taxes, which will be added to invoices.</li>
<li>Projects usually need an advance before work starts, with the balance due at the milestones stated in the Proposal. Monthly retainers are billed in advance at the start of each month.</li>
<li>Invoices are payable within <strong>{PAYMENT_DAYS} days</strong> unless the Proposal says otherwise.</li>
<li>If payment is late, we may pause work, campaigns or support until it is received. Timelines will be extended by the length of the delay.</li>
<li>Advances and fees for work already started or completed are <strong>non-refundable</strong>, unless the Proposal says otherwise or the law requires a refund.</li>
</ul>"""),
    ("ad-spend", "Advertising budgets and third-party costs", """
<ul>
<li>Advertising budgets (“<strong>ad spend</strong>”) for Google, Meta, LinkedIn and other platforms are <strong>not included</strong> in our fees. You pay them directly to the platform, using an ad account in your business name.</li>
<li>Third-party costs such as domains, hosting, premium themes and plugins, software subscriptions, stock images, WhatsApp Business API charges and printing are paid by you, unless the Proposal says otherwise.</li>
<li>Platforms may reject ads, limit reach or suspend accounts under their own policies. We will help resolve such issues but are not responsible for platform decisions.</li>
</ul>"""),
    ("client-duties", "Your responsibilities", """
<p>To help us deliver good results, you agree to:</p>
<ul>
<li>provide accurate information, content, brand assets and account access on time;</li>
<li>review and approve work within a reasonable time, usually 5 working days. Delays in feedback may extend timelines;</li>
<li>make sure any content, images, logos, product claims and offers you give us are accurate, lawful, and that you have the right to use them;</li>
<li>comply with the laws and advertising rules that apply to your business, including rules for regulated sectors such as healthcare, finance, education and real estate;</li>
<li>keep your passwords secure and remove our access when the engagement ends.</li>
</ul>"""),
    ("approvals", "Approvals and revisions", """
<p>The Proposal states how many rounds of revisions are included. Once you approve a deliverable, such as a design, content, ad creative or campaign, further changes may be charged as extra work. Content published after your approval is treated as approved by you.</p>"""),
    ("results", "No guarantee of results", """
<p>Search rankings, ad performance, reach, leads and sales depend on many factors outside our control, including search engine and platform algorithms, competition, your market, pricing and your own sales process. We therefore <strong>do not guarantee</strong> any specific ranking, traffic, number of leads, return on ad spend or revenue.</p>
<p>We do commit to planning carefully, working to professional standards, following platform guidelines and reporting honestly on progress.</p>"""),
    ("ownership", "Intellectual property and ownership", """
<ul>
<li><strong>Your materials</strong> (logos, content, images, data) remain yours. You give us permission to use them to deliver the Services.</li>
<li><strong>Final deliverables</strong> created for you, such as your website, final designs, content and ad creatives, become your property once all related invoices are paid in full.</li>
<li><strong>Your accounts</strong>, including domain, hosting, website, analytics, ad accounts and social media pages, should be in your name. If we create any on your behalf, we will hand over full ownership.</li>
<li><strong>Our tools and know-how</strong>, such as templates, frameworks, code libraries, processes, automation workflows and working files, remain ours. Where they form part of your deliverable, you receive a licence to use them for your business.</li>
<li>Third-party items (themes, plugins, fonts, stock media, software) are subject to their own licence terms.</li>
<li>Unless you ask us not to in writing, we may mention your business name and show completed work in our portfolio and marketing, without revealing confidential information.</li>
</ul>"""),
    ("confidentiality", "Confidentiality", """
<p>Both of us will keep the other’s confidential information, such as business plans, pricing, customer data and account access, private. We will use it only for the engagement, and will not disclose it except to team members or service providers who need it and are bound by confidentiality, or where the law requires. This obligation continues after the engagement ends.</p>"""),
    ("data-protection", "Data protection", f"""
<p>We handle personal data in line with our <a href="{SITE}/privacy-policy/">Privacy Policy</a> and applicable Indian law. Where we process your customers’ personal data for you (for example leads, CRM contacts or chatbot conversations), you remain responsible for having a lawful basis and giving any required notices. We process such data only on your instructions and for the purpose of the Services.</p>"""),
    ("termination", "Ending an engagement", f"""
<ul>
<li>Either party may end a monthly retainer by giving <strong>{NOTICE_DAYS} days’ written notice</strong>, after any minimum term stated in the Proposal.</li>
<li>Either party may end an engagement immediately by written notice if the other seriously breaches these Terms and does not fix the breach within 15 days of being told.</li>
<li>If a project is cancelled part-way, you pay for work completed up to the date of cancellation, and the advance is adjusted against it.</li>
<li>When an engagement ends, we will hand over deliverables and account access for which payment has been received.</li>
</ul>"""),
    ("liability", "Limitation of liability", """
<ul>
<li>We are not liable for indirect or consequential losses, such as loss of profit, revenue, data or business opportunity.</li>
<li>We are not responsible for losses caused by third-party platforms, hosting providers, plugins, algorithm changes, account suspensions, cyber attacks outside our reasonable control, or content you supplied.</li>
<li>Our total liability for any claim relating to an engagement is limited to the fees you paid us for that engagement in the <strong>three (3) months</strong> before the claim arose.</li>
</ul>
<p>Nothing in these Terms limits any liability that cannot be limited under applicable law.</p>"""),
    ("indemnity", "Indemnity", """
<p>You agree to protect us against claims, penalties and costs arising from content, claims or materials you provided, your products or services, or your breach of applicable laws or these Terms.</p>"""),
    ("website-use", "Using this website", """
<ul>
<li>Content on the Website, including text, graphics, design and code, belongs to Digital Udyami or its licensors. You may not copy or reuse it for commercial purposes without our written permission.</li>
<li>Website content is general information and not professional advice for your specific situation.</li>
<li>You must not misuse the Website, for example by attempting unauthorised access, spreading malware or scraping content.</li>
<li>Links to third-party websites are provided for convenience. We are not responsible for their content.</li>
</ul>"""),
    ("force-majeure", "Events beyond our control", """
<p>Neither party is responsible for delays or failures caused by events beyond reasonable control, such as natural disasters, epidemics, government actions, internet or power outages, or platform-wide failures. Timelines will be extended for the duration of the event.</p>"""),
    ("law", "Governing law and disputes", f"""
<p>These Terms are governed by the laws of India. We will first try to resolve any dispute through good-faith discussion. If it is not resolved within 30 days, it will be subject to the exclusive jurisdiction of {_courts}.</p>"""),
    ("changes", "Changes to these terms", """
<p>We may update these Terms from time to time. The latest version will always be on this page with the “Last updated” date. Changes do not affect an engagement already agreed in a signed Proposal, unless both parties agree.</p>"""),
    ("contact", "Contact us", f"""
<p>If you have questions about these Terms, please contact us:</p>
{_contact_block}"""),
]
