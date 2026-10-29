"""Text of the Hekau inner pages, from the copy deck (October 2026):
https://claude.ai/artifact/SshR1okUt5iQYn56KRFNjf

Edit here, then run scripts/build_pages.py. Home-page text lives in the block
files (views/snippets/s_hk_*.xml)."""

CTA = ('Book a free systems audit', '/book-a-call')
CHECKLIST_URL = '/website_hekau/static/src/files/hekau-system-disconnection-checklist.pdf'
CHECKLIST_LINK = 'Or download the System Disconnection Checklist'
STEP_ICONS = ['step_research', 'step_jigsaw', 'step_head', 'step_design', 'step_kursor', 'step_icon2']

COMPANY = {
    'name': 'Hekau Business Solutions Private Limited',
    'email': 'admin@hekautech.com',
    'phone': '+91 81497 49282',
    'phone_href': '+918149749282',
    'address': 'Vijayashree, S. No. 33/92, near MSEB Office, Katraj, Pune 411046',
    'linkedin': 'https://www.linkedin.com/company/hekaubiz',
    'linkedin_santosh': 'https://www.linkedin.com/in/santosh-yadav-hekau/',
}


def steps(*pairs):
    return [{'icon': STEP_ICONS[i % len(STEP_ICONS)], 'title': title, 'text': text}
            for i, (title, text) in enumerate(pairs)]


def cards(icons, *pairs):
    """Feature cards; `icons` is a prefix (feat_web -> feat_web_1..3) or a list of icon names."""
    out = []
    for i, (title, text) in enumerate(pairs):
        icon = icons[i] if isinstance(icons, (list, tuple)) else f'{icons}_{i + 1}'
        out.append({'icon': icon, 'title': title, 'text': text})
    return out


# The six steps every engagement follows (Services page and How we work)
ENGAGEMENT_PROCESS = {
    'heading': 'How every engagement runs',
    'lead': 'Six steps from the first call to support after launch. You see working software early and often.',
    'steps': steps(
        ('Systems audit', 'We map how work moves today: tools, spreadsheets, handoffs and the decisions that wait on them.'),
        ('Plan and priorities', 'We agree what to fix first, what it will cost and how we’ll measure the result.'),
        ('Design', 'Screens and workflows designed around the people who will use them every day.'),
        ('Build in sprints', 'Working software every few weeks, so you can steer while we build.'),
        ('Test and go live', 'Real-world testing, data migration and training before anyone depends on it.'),
        ('Support and improve', 'Monitoring, fixes and improvements after launch, as your business changes.'),
    ),
}


# --------------------------------------------------------------------------------------------
# Services overview and the eight service pages. `intro` is the panel after the hero:
# highlight (statement and four tiles), attributes (ring diagram and list) or pyramid.
# `featured`: case studies shown in the "Proof, not promises" block.
# --------------------------------------------------------------------------------------------

SERVICES = {
    'services': {
        'hero': {
            'title': 'Technology that fits how your business <span class="hk-gradient-text">actually works</span>',
            'text': 'ERP and CRM, automation, custom portals, private AI, mobile apps and websites. Every engagement '
                    'starts with the same question: what’s slowing your business down?',
            'button': ('See all services', '#services'),
        },
        'why': {
            'heading': 'A partner, not another vendor',
            'cards': [
                ('Between an in-house team and a vendor list',
                 'Building an internal team for every initiative is slow. Juggling vendors with different priorities '
                 'is worse. We sit in between: close enough to understand your business, flexible enough to change with it.'),
                ('No tools you don’t need',
                 'We recommend whatever removes the most friction, even when that’s a small automation instead of a big '
                 'project. No add-on fees, no hidden charges.'),
                ('We stay after go-live',
                 'Support is part of every engagement. When your team has a question six months later, the people who '
                 'built your system answer it.'),
            ],
        },
        'process': ENGAGEMENT_PROCESS,
        'featured': ['inali-foundation', 'the-arc'],
    },

    'odoo': {
        'hero': {
            'label': 'Odoo · HubSpot · WordPress · Next.js · APIs',
            'title': 'ERP, CRM & CMS Implementation',
            'sub': 'One source of truth for the whole business',
            'text': 'Operations, sales and your website on systems that share the same data. We implement and connect '
                    'ERP, CRM and content management platforms, so orders, customers and content stop living in '
                    'separate spreadsheets.',
        },
        'intro': {
            'kind': 'highlight',
            'title': 'When every team works from the same data, the gaps show up fast.',
            'text': 'Sales hands over to operations without re-typing. Stock, purchasing and production stay in sync. '
                    'Invoices follow completed work. And your website publishes from the same products and customers '
                    'your teams work with.',
            'tiles': [{'icon': 'why_growth', 'label': 'CRM & sales pipeline'},
                      {'icon': 'svc_erp', 'label': 'Inventory, purchasing & production'},
                      {'icon': 'svc_web', 'label': 'Website & content (CMS)'},
                      {'icon': 'why_money', 'label': 'Projects, timesheets & invoicing'}],
            'note': None,
        },
        'features': {
            'heading': 'Why growing companies implement with Hekau',
            'cards': cards(['feat_cloud_1', 'feat_bpa_2', 'feat_web_3'],
                ('The right platform, chosen honestly',
                 'We start from how you work, not from a product. If the ERP, CRM or CMS you already pay for can do '
                 'the job, we configure it before suggesting anything new, and use standard features before custom '
                 'code, which keeps upgrades cheap.'),
                ('Your data comes with you',
                 'Customers, products, open orders, contacts and website content move across before go-live, checked '
                 'against your old system, so day one starts with real numbers.'),
                ('Set up for US operations',
                 'US chart of accounts, sales tax for the states you sell in, USD with multi-currency where you need '
                 'it, and month-end reports your CPA can close from.'),
            ),
        },
        # Extra section of this page only: the platform we recommend first.
        'preferred': {
            'badge': 'Our preferred platform',
            'title': 'Why we usually start with Odoo',
            'lead': 'Odoo runs ERP, CRM and your website in one system, so for most growing companies it does the most '
                    'for the least cost. When another platform fits you better, we say so. What Odoo brings:',
            'items': ['ERP, CRM and website in one system', 'No licence fee on the Community edition',
                      'Enterprise apps when you need them', 'Open source, so no vendor lock-in',
                      'Sales, stock, manufacturing and accounting', 'Little custom code, so upgrades stay cheap',
                      'We run Hekau on it, this website included'],
        },
        'process': {
            'heading': 'From spreadsheets to one system in five steps',
            'lead': 'Most rollouts go live in phases, so each team is productive before the next one moves.',
            'steps': steps(
                ('Process mapping', 'We walk through how orders, stock, customers, content and billing move today, and where they break.'),
                ('Fit-gap and plan', 'We match your process to the platform’s standard features, list the real gaps and agree on phases and costs.'),
                ('Configure and connect', 'Apps set up, custom pieces built where needed, and integrations to the tools you keep.'),
                ('Migrate and train', 'Your data moved and checked; each team trained on its own daily tasks.'),
                ('Go live and support', 'We stay through the first month-end close and beyond, fixing and improving as you use it.'),
            ),
        },
        'featured': ['odoo-manufacturing', 'the-arc'],
    },

    'bpa': {
        'hero': {
            'label': 'Odoo · HubSpot · MSG91 · APIs & webhooks',
            'title': 'Workflow & Process Automation',
            'sub': 'Stop paying people to copy data',
            'text': 'Approvals, follow-ups, reports and data entry that run on their own. We automate the work your team '
                    'does around your systems, so they can focus on the work your customers pay for.',
        },
        'intro': {
            'kind': 'highlight',
            'title': 'If someone re-types the same data every day, it’s a candidate for automation.',
            'text': 'We start with the steps that cost the most hours or cause the most errors, and automate those first.',
            'tiles': [{'icon': 'bpa_3', 'label': 'Hours back every week'},
                      {'icon': 'bpa_2', 'label': 'Fewer manual errors'},
                      {'icon': 'bpa_1', 'label': 'Faster approvals'},
                      {'icon': 'bpa_4', 'label': 'Reports without the chasing'}],
            'note': 'Start with the costliest step.',
        },
        'features': {
            'heading': 'Automation that fits how your company works',
            'cards': cards('feat_bpa',
                ('Find the leaks first',
                 'We map your workflows and measure where the time goes before automating anything, so the first '
                 'automation pays for itself.'),
                ('Connect what you already use',
                 'Your CRM, ERP, forms, email, SMS and spreadsheets pass data to each other directly, instead of through a person.'),
                ('Proven where it matters',
                 'Inali Foundation cut CSR campaign turnaround from 7 days to 2. Idamoss Systems generates every vendor '
                 'contract automatically at sign-up.'),
            ),
        },
        'process': {
            'heading': 'Five steps to automation that sticks',
            'lead': 'Small, measurable wins first; bigger workflows once the team trusts them.',
            'steps': steps(
                ('Process analysis', 'We trace each workflow and note where data is re-typed, chased or lost.'),
                ('Automation plan', 'We rank the candidates by hours saved and risk, and agree which come first.'),
                ('Workflow design', 'Triggers, rules, approvals and notifications written down before anything is built.'),
                ('Build and connect', 'Automations built into your systems and tested against real cases.'),
                ('Monitor and improve', 'We watch them in daily use, fix edge cases and extend what works.'),
            ),
        },
        'featured': ['idamoss-systems', 'mywanderloop'],
    },

    'web': {
        'hero': {
            'label': 'React · Next.js · Node.js · Django · Laravel',
            'title': 'Custom Web Applications & B2B Portals',
            'sub': 'Built around how you work',
            'text': 'Customer portals, vendor platforms and internal tools that replace email threads and spreadsheets. '
                    'Fast, secure and connected to your ERP and CRM.',
        },
        'intro': {
            'kind': 'attributes',
            'badge': 'Our standard',
            'title': 'What every application we build has to be',
            'lead': 'Working features are the minimum. Your application also has to be:',
            'items': ['Fast, even at peak traffic', 'Secure, with role-based access', 'Connected to your ERP and CRM',
                      'Responsive on every device', 'Accessible', 'Easy to find on Google', 'Easy to maintain and hand over'],
        },
        'features': {
            'heading': 'Web platforms for companies that have outgrown templates',
            'cards': cards('feat_web',
                ('Portals for customers, vendors and teams',
                 'Self-service portals cut the back-and-forth. Customers track their orders, vendors onboard '
                 'themselves, and staff stop answering the same email.'),
                ('Performance you can measure',
                 'We rebuilt The Arc on Next.js with a custom CMS. It now serves 50,000+ visitors a month with top '
                 'PageSpeed scores.'),
                ('Payments, logins and integrations done right',
                 'Razorpay event payments for MCCIA, one login across web and mobile for Ragya, contracts generated '
                 'automatically for Idamoss. The plumbing that makes a platform work.'),
            ),
        },
        'process': {
            'heading': 'Five steps to a web application\nthat lasts',
            'lead': 'Working software every few weeks, so you steer while we build.',
            'steps': steps(
                ('Research and planning', 'A free call to understand your goals, users and constraints, then a clear outline of what we’ll deliver.'),
                ('UX and UI design', 'Wireframes and clickable designs, so you see the application before it’s built.'),
                ('Agile development', 'Built in short sprints, with a demo at the end of each one.'),
                ('Testing and QA', 'Functional, performance and security checks across browsers and devices.'),
                ('Launch and maintenance', 'Deployment, monitoring and regular updates as your business changes.'),
            ),
        },
        'featured': ['the-arc', 'mccia'],
    },

    'ai': {
        'hero': {
            'icons': [('ai_0', 'AI', 40), ('ai_1', 'AI assistant'), ('ai_2', 'Automation'), ('ai_3', 'Workflows')],
            'title': 'Secure In-House AI & Data',
            'sub': 'AI that understands your business',
            'text': 'Public AI tools don’t know your margins, your live inventory or your production constraints. We '
                    'build AI on top of your own ERP and CRM data, inside your control.',
        },
        'intro': {
            'kind': 'pyramid',
            'badge': 'Why most AI projects stall:',
            'title': 'AI gets added, not embedded. Without clean, connected data underneath, it stays a smart assistant '
                     'instead of a business tool. Built on the right foundation, it can:',
            'items': ['Flag margin risks before an order is confirmed', 'Spot procurement issues early',
                      'Surface bottlenecks automatically'],
        },
        'features': {
            'heading': 'AI built on your data, not someone else’s',
            'cards': cards('feat_ai',
                ('Data foundation first',
                 'We make sure ERP, CRM, production and inventory records are clean and connected before any model touches them.'),
                ('Private by design',
                 'Customer data, pricing logic and vendor contracts stay in environments you control, with access by role.'),
                ('Models that learn your patterns',
                 'We built the AI/ML engine that matches investors with startups for Mohur, and a scoring system that '
                 'feeds a job platform’s AI model.'),
            ),
        },
        'process': {
            'heading': 'From AI experiment to everyday tool',
            'lead': 'Start with one decision that matters, then scale what works.',
            'steps': steps(
                ('Opportunity discovery', 'We find the decisions where better data or prediction would save the most time or money.'),
                ('Data readiness', 'We check and connect the data the model will depend on.'),
                ('Model development', 'Models built and tuned on your own data, tested against real cases.'),
                ('Integration', 'AI placed inside the tools your team already uses: ERP, CRM, website or app.'),
                ('Monitoring and refinement', 'Accuracy tracked in daily use and improved as more data comes in.'),
            ),
        },
        'featured': ['mohur', 'job-post-scoring'],
    },

    'mobileapp': {
        'hero': {
            'label': 'React Native · Android · iOS · NFC & QR',
            'title': 'Mobile App Development',
            'sub': 'Apps your teams and customers actually use',
            'text': 'Field apps, customer apps and on-site data capture for Android and iOS, connected to the systems '
                    'your office already runs on.',
        },
        'intro': {
            'kind': 'highlight',
            'title': 'Mobile apps that replace paper, phone calls and re-typed data.',
            'text': None,
            'tiles': [{'value': '7 → 2', 'small': 'days', 'label': 'CSR campaign turnaround with the Inali Foundation app'},
                      {'value': '1', 'small': 'login', 'label': 'Across web and mobile for Ragya’s listeners'},
                      {'value': 'Real-time', 'label': 'Machine test results captured on the shop floor'},
                      {'value': 'NFC', 'label': 'Collar tags that help volunteers find and care for street dogs'}],
            'note': 'Built for Android and iOS.',
            'note_top': 290,  # the statement is a line shorter than the Figma one
        },
        'features': {
            'heading': 'Built for the people who carry the phone',
            'cards': cards('feat_mobileapp',
                ('Designed for field work',
                 'Large touch targets, quick capture and simple flows for supervisors, technicians and volunteers who '
                 'don’t sit at a desk.'),
                ('Connected, not another silo',
                 'Every app syncs with your ERP, CRM or web platform, so data entered on a phone shows up everywhere else.'),
                ('One account across devices',
                 'Logins, subscriptions and preferences stay in step between app and website, as we built for Ragya.'),
            ),
        },
        'process': {
            'heading': 'From idea to app store in six steps',
            'lead': 'Built and tested with real users before launch.',
            'steps': steps(
                ('App concept', 'Who uses the app, what they need to get done in a minute, and which systems it connects to.'),
                ('Design', 'Screens, flows and a style guide for Android and iOS.'),
                ('Development', 'Shared code for both platforms where it makes sense, native where it matters.'),
                ('Testing', 'Real devices, real screen sizes and real users.'),
                ('Launch', 'Store listings, developer accounts and the release handled for you.'),
                ('Monitor and improve', 'Crash reports, usage and reviews guide the next release.'),
            ),
        },
        'featured': ['inali-foundation', 'ragya'],
    },

    'ux': {
        'hero': {
            'label': 'Figma · WordPress · HubSpot · Analytics',
            'title': 'UX & Conversion-Focused Websites',
            'sub': 'Turn visitors into enquiries',
            'text': 'Most business websites get traffic but few enquiries. We rebuild navigation, content and calls to '
                    'action around what your buyers need, and wire every form into your CRM.',
        },
        'features': {
            'heading': 'Design judged by results, not looks',
            'cards': cards('feat_ux',
                ('Research before redesign',
                 'Heatmaps, behavior tracking and short buyer surveys show where visitors get lost, before we change a single page.'),
                ('Results you can count',
                 'MaxintelB2B saw 15% more conversions and 30% more high-intent leads. FYHBA’s bounce rate fell 35% and leads rose 32%.'),
                ('From Instagram DMs to an online store',
                 'YB Perfumes moved its sales from direct messages to a mobile-first store, and sales grew 17%.'),
            ),
        },
        'process': {
            'heading': 'Six steps from traffic to enquiries',
            'lead': 'Every change is checked against how real visitors behave.',
            'steps': steps(
                ('Buyer research', 'Who your buyers are, what they look for and where they drop off.'),
                ('Content and structure', 'Navigation and pages reorganized around the questions buyers ask.'),
                ('UX design', 'Wireframes that cut the steps to an enquiry or a purchase.'),
                ('UI design', 'Visual design that fits your brand and works on every screen.'),
                ('Build and connect', 'Fast, search-friendly pages, with every form feeding your CRM.'),
                ('Measure and improve', 'Analytics and heatmaps guide the next round of changes.'),
            ),
        },
        'featured': ['maxintelb2b', 'fyhba-medical-billing'],
    },

    'cloud': {
        'hero': {
            'label': 'Hosting · Monitoring · Backups · Security',
            'title': 'Cloud-Managed Services',
            'sub': 'Systems that stay fast and available',
            'text': 'Hosting, monitoring, backups and security for your ERP, portals and apps. We keep them running, so '
                    'your team never has to think about servers.',
        },
        'features': {
            'heading': 'Infrastructure you don’t have to think about',
            'cards': cards('feat_cloud',
                ('Ready for launch-day traffic',
                 'Quatch’s store handled its launch-day rush with zero downtime, and The Arc serves 50,000+ visitors every month.'),
                ('Backups you’ve actually tested',
                 'Daily off-site backups and regular restore tests, so a bad day stays a small one.'),
                ('Security and access control',
                 'Encrypted connections, role-based access and regular patching, set up from day one and kept up after.'),
            ),
        },
        'process': {
            'heading': 'How we take over your infrastructure',
            'lead': 'No disruption to the business while we move or tidy things up.',
            'steps': steps(
                ('Assessment', 'We review what runs where, what it costs and where the risks are.'),
                ('Plan', 'The target setup, migration steps and a rollback plan, agreed before anything moves.'),
                ('Migration and setup', 'Servers, databases and applications moved or rebuilt, with downtime planned outside business hours.'),
                ('Security and backups', 'Access control, encryption, monitoring and tested backups in place.'),
                ('Ongoing management', 'Monitoring, updates, cost reviews and support on a monthly plan.'),
            ),
        },
        'featured': ['quatch', 'the-arc'],
    },

    'rescue': {
        'hero': {
            'label': 'React · Next.js · Node.js · Django · Laravel',
            'title': 'Project Rescue & Dedicated Developers',
            'sub': 'When a project stalls, we finish it',
            'text': 'Your previous vendor left mid-build, nobody understands the code, and launch keeps slipping. We '
                    'audit what exists, finish what’s missing and stay on, or embed experienced developers in your own team.',
        },
        'intro': {
            'kind': 'attributes',
            'badge': 'Code audit',
            'title': 'What our code audit checks',
            'lead': 'Before we promise a date, we find out what you actually have. We review:',
            'items': ['Code quality', 'Architecture', 'Security', 'Performance', 'Missing features', 'Deployment setup',
                      'Documentation'],
        },
        'features': {
            'heading': 'Two ways we get you moving again',
            'cards': cards(['feat_web_1', 'feat_mobileapp_2', 'feat_ux_3'],
                ('Rescue and finish',
                 'When The Arc’s previous vendor walked away mid-build, we took over, finished the features, moved the '
                 'site to Next.js and built a custom CMS. It now serves 50,000+ visitors a month.'),
                ('Developers inside your team',
                 'Our developers joined Fashquik’s own team to optimize the codebase, rebuild the delivery integration '
                 'and get the marketplace scaling again.'),
                ('A straight answer first',
                 'Sometimes fixing beats rewriting, sometimes it doesn’t. The audit tells you which, with costs, before you commit.'),
            ),
        },
        'process': {
            'heading': 'From stalled to shipping in five steps',
            'lead': 'A clear plan before any big commitment, then steady releases.',
            'steps': steps(
                ('Code and project audit', 'We review the code, the infrastructure and the backlog, and talk to whoever is still on the project.'),
                ('Recovery plan', 'Fix, refactor or rebuild, with priorities, costs and a realistic launch date.'),
                ('Stabilize', 'Critical bugs, security gaps and deployment problems fixed first.'),
                ('Finish and launch', 'Missing features built and shipped in short sprints.'),
                ('Support or hand over', 'We stay on to maintain it, or hand it to your team with documentation.'),
            ),
        },
        'featured': ['the-arc', 'fashquik'],
    },
}

FEATURED = {
    'heading': 'Proof, not promises',
    'lead': 'Real problems, real fixes and real numbers from companies like yours.',
    'button': ('View all projects', '/projects'),
}


# --------------------------------------------------------------------------------------------
# About Us
# --------------------------------------------------------------------------------------------

ABOUT = {
    'description': 'Hekau is a Pune-based technology partner for growing companies: ERP and CRM, automation, '
                   'custom portals, AI, mobile apps and websites.',
    'hero': {
        'badge': 'Why Hekau?',
        'title': 'Built for companies that\noutgrew their tools',
        'text': 'Most growing companies don’t wake up one day and decide they need custom software. A process gets '
                'hard to manage. Teams build workarounds. Information ends up in five places, and decisions start '
                'waiting on follow-ups.\n\n'
                'That’s the moment we’re built for. Hekau is a Pune-based technology partner for $2M–$15M companies in '
                'India and abroad. We connect ERP, CRM, workflows and data, so the whole business runs on one version of the truth.\n\n'
                'We rarely start by asking what software to build. We start with what’s slowing the business down.',
    },
    'story': {
        'title': 'We started in December 2021 as Anubit Solutions and grew into Hekau. The name comes from Heka, the '
                 'ancient Egyptian word for magic.',
        'text': 'The magic we care about is the unglamorous kind: fewer reconciliations, fewer follow-ups, fewer “which '
                'number is correct?” meetings. Our team brings over a decade of hands-on delivery across web, mobile, '
                'automation and ERP.',
        'button': CTA,
    },
    'team': {
        'title': 'The people you’ll work with',
        'members': [
            {'name': 'Santosh Yadav', 'role': 'Director & Co-Founder', 'photo': 'about/founder_santosh.webp',
             'bio': 'Santosh leads digital infrastructure strategy and systems architecture at Hekau, working directly '
                    'with founders and operations heads. An engineer by training, he started as a front-end developer '
                    'and UX designer, then ran marketing and growth. So he looks at every system from three sides: how '
                    'it’s built, how people use it, and what it does for revenue.'},
            {'name': 'Anu Unni', 'role': 'Co-Founder', 'photo': 'about/founder_anu.webp',
             'bio': 'After earning his engineering degree in 2014, Anu spent years delivering software for '
                    'international clients before co-founding Hekau in 2021. With over a decade in IT, he oversees '
                    'Hekau’s critical projects and engineering quality.'},
        ],
    },
    'vision': {
        'title': 'Our Vision & Mission',
        'items': [
            {'icon': 'vision', 'title': 'Our Vision',
             'text': 'To be the technology partner growing companies trust to run on one connected system.'},
            {'icon': 'mission', 'title': 'Our Mission',
             'text': 'To help businesses grow by using technology in a smarter, more strategic way, with systems that '
                     'are scalable, reliable and built for each client, and that give them a clear operational and '
                     'competitive advantage.'},
        ],
    },
    'values': {
        'heading': 'What we hold ourselves to',
        'cards': [
            {'icon': 'value_empowerment', 'title': 'Partnership',
             'text': 'We act as a long-term technology partner: close enough to understand your business, and '
                     'accountable for the outcome, not just the delivery.'},
            {'icon': 'value_flexibility', 'title': 'Customer-Centricity',
             'text': 'Every recommendation starts with what creates the most value for you, even when that’s the smaller project.'},
            {'icon': 'value_flexibility', 'title': 'Adaptability',
             'text': 'Technology changes and so do businesses. We stay flexible and adjust the plan when your priorities move.'},
            {'icon': 'value_innovation', 'title': 'Innovation',
             'text': 'We keep looking for better ways to solve problems with modern technology, and use it only where it earns its place.'},
            {'icon': 'value_empowerment', 'title': 'Transparency',
             'text': 'Clear estimates, honest trade-offs and no hidden charges. What you’re quoted is what you pay.'},
        ],
    },
}


# --------------------------------------------------------------------------------------------
# Projects and case studies
# --------------------------------------------------------------------------------------------

# Filter keys double as `?filter=` values (the Home and Services cards link to them).
WORK_FILTERS = [
    ('erp', 'ERP, CRM & CMS'), ('automation', 'Automation'), ('apps', 'Web Apps & Portals'), ('ai', 'AI & Data'),
    ('mobile', 'Mobile Apps'), ('ux', 'UX & Websites'), ('cloud', 'Cloud'), ('rescue', 'Project Rescue'),
]

WORK = {
    'description': 'Nineteen Hekau projects across manufacturing, healthcare services, e-commerce, media and '
                   'non-profits: ERP, automation, portals, AI, mobile apps and websites.',
    'hero': {
        'badge': 'Work',
        'title': 'Real problems, fixed for\nreal companies',
        'text': 'Nineteen projects across manufacturing, healthcare services, e-commerce, media and the non-profit '
                'sector. Each one started with something slowing a business down.',
    },
    'list_title': 'Filter by what you need',
}

# card_*: projects page card; page fields: case study at /projects/<slug>.
CASES = [
    {
        'slug': 'odoo-manufacturing', 'categories': ['erp', 'automation'], 'tags': ['ERP, CRM & CMS', 'Manufacturing'],
        'card_title': 'One system for a manufacturing and projects company',
        'card_text': 'Sales, purchasing, inventory, manufacturing, maintenance, projects and invoicing, all on Odoo.',
        'service': 'ERP, CRM & CMS Implementation', 'client': 'A manufacturing and projects company', 'industry': 'Manufacturing',
        'about': 'A growing company that manufactures, maintains equipment and delivers projects for its customers.',
        'challenge': 'Sales, purchasing, stock, production, maintenance and billing each lived in a different tool or '
                     'spreadsheet. Month-end meant reconciling numbers that didn’t match.',
        'built': 'An Odoo implementation with sales, purchasing, inventory, manufacturing, maintenance, projects, '
                 'timesheets and invoicing on one platform. Sales orders connect directly to procurement and '
                 'production, inventory and maintenance data stay in sync, and timesheets record real effort rather than estimates.',
        'impact': 'Work became visible across teams. Invoicing now follows completed work instead of being a separate '
                  'exercise, with fewer gaps, fewer reconciliations and fewer “which number is correct?” conversations.',
        'quote': 'Invoicing became a result of completed work, not a separate exercise.',
        'related': ['manufacturing-test-records', 'inali-foundation'],
    },
    {
        'slug': 'inali-foundation', 'categories': ['mobile', 'automation'], 'tags': ['Mobile App', 'Non-Profit'],
        'card_title': 'Inali Foundation: CSR campaigns in 2 days, not 7',
        'card_text': 'One app replaced the spreadsheets behind a non-profit’s patients, inventory and CSR campaigns.',
        'featured_text': 'A non-profit that has fitted thousands of prosthetic arms across India was running on '
                         'spreadsheets. We gave CSR, clinical and inventory teams one app.',
        'service': 'Mobile App Development, Workflow Automation', 'client': 'Inali Foundation', 'industry': 'Non-profit, healthcare',
        'about': 'A non-profit that has provided thousands of accessible prosthetic arms across India, funded through CSR partnerships.',
        'challenge': 'Patient registration, appointments, CSR campaigns, inventory and staff tasks all ran on paper and '
                     'spreadsheets. Pulling a campaign report took days, and the foundation nearly lost a major '
                     'recurring CSR partner because of it. The founder couldn’t see inventory, fitments or campaign '
                     'status without waiting for someone to compile the data.',
        'built': 'One mobile and web app for the whole operation: patient registration and records, appointment '
                 'booking with automatic reminders, CSR campaign tracking with updates for partners, real-time '
                 'inventory, vendor and partner profiles, and role-based dashboards for CSR managers, doctors, '
                 'supervisors, lead managers and inventory managers.',
        'impact': 'Campaign turnaround fell from 7 days to 2. Every team works from the same live data, partners see '
                  'progress without asking, and the foundation can serve more people.',
        'quote': 'From spreadsheet chaos to one live view of patients, inventory and campaigns.',
        'related': ['devdoot', 'indies'],
    },
    {
        'slug': 'idamoss-systems', 'categories': ['apps', 'automation'], 'tags': ['Web Platform', 'Events'],
        'card_title': 'Idamoss Systems: event ticketing with contracts that write themselves',
        'card_text': 'A ticketing marketplace for 6,000 regular users, with vendor contracts generated at sign-up.',
        'service': 'Custom Web Apps & Portals, Workflow Automation', 'client': 'Idamoss Systems', 'industry': 'Events and entertainment',
        'about': 'Idamoss Systems runs a marketplace where organizers sell tickets for festivals, raves and parties.',
        'challenge': 'Every new vendor meant collecting details and drafting a contract by hand, and the platform '
                     'needed full e-commerce and analytics to grow.',
        'built': 'Self-service vendor registration; a contract generated automatically from the registration details '
                 'and emailed to both the vendor and Idamoss; ticket listings, payments through several gateways and '
                 'ticket delivery; and Google Analytics with Microsoft Clarity to show how users behave.',
        'impact': 'The platform serves 6,000 regular users and a growing vendor base, and onboarding a vendor no '
                  'longer needs anyone to draft a contract.',
        'quote': 'Every vendor contract is generated the moment registration is complete.',
        'related': ['mccia', 'mywanderloop'],
    },
    {
        'slug': 'manufacturing-test-records', 'categories': ['mobile', 'automation', 'cloud'], 'tags': ['Mobile App', 'Manufacturing'],
        'card_title': 'Machine test results captured in real time',
        'card_text': 'An Android app records test results at the machine, with secure storage and live dashboards.',
        'service': 'Mobile App Development, Workflow Automation, Cloud', 'client': 'An industrial manufacturer', 'industry': 'Manufacturing',
        'about': 'A manufacturer that tests every unit it builds against strict quality standards and keeps the records for its stakeholders.',
        'challenge': 'Test results were written down by hand: slow, error-prone and hard to analyze. Quality teams '
                     'needed the data captured at the machine, stored securely and easy to read.',
        'built': 'An Android app that connects to the testing machines and records results in real time, encrypted '
                 'transfer to a central server, a web platform with role-based access, and dashboards each team can arrange for itself.',
        'impact': 'Manual entry errors are gone, results are available the moment a test finishes, and managers spot '
                  'trends and anomalies on dashboards instead of in spreadsheets.',
        'quote': 'Test data captured at the machine, not copied from a clipboard.',
        'related': ['odoo-manufacturing', 'secure-field-data-capture'],
    },
    {
        'slug': 'mywanderloop', 'categories': ['automation', 'apps'], 'tags': ['Automation', 'Integrations'],
        'card_title': 'MyWanderloop: notifications users actually receive',
        'card_text': 'Automated SMS and email through MSG91, tracked from send to delivery.',
        'service': 'Workflow Automation, Custom Web Apps & Portals', 'client': 'MyWanderloop', 'industry': 'Consumer platform',
        'about': 'MyWanderloop’s platform depends on real-time messages: sign-up verification, transactional alerts and user updates.',
        'challenge': 'They needed fast, high-volume SMS and email delivery without delays or a complicated setup to run themselves.',
        'built': 'MSG91 integrated into their back end, with automated SMS workflows on DLT-compliant templates '
                 '(India’s telecom rules), transactional email pipelines, and webhook and API routing.',
        'impact': 'Onboarding and security checks run automatically, and every message is delivered quickly and '
                  'tracked, with real-time logs.',
        'quote': 'Every SMS and email tracked from send to delivery.',
        'related': ['idamoss-systems', 'devdoot'],
    },
    {
        'slug': 'the-arc', 'categories': ['rescue', 'apps', 'cloud', 'erp'], 'tags': ['Project Rescue', 'Media'],
        'image': 'projects/the_arc.webp',
        'card_title': 'The Arc: rescued mid-build, now 50,000+ monthly visitors',
        'card_text': 'We took over an abandoned media platform, rebuilt it on Next.js and gave journalists a custom CMS.',
        'featured_text': 'A news platform left half-built by its previous vendor. We finished it, moved it to Next.js '
                         'and built a custom CMS. It now serves 50,000+ visitors a month.',
        'service': 'Project Rescue, Custom Web Apps & Portals', 'client': 'The Arc', 'industry': 'Media',
        'about': 'A seed-funded news platform covering India’s high-growth companies, with research-backed reporting '
                 'for general readers and executives.',
        'challenge': 'The previous IT vendor abandoned the platform mid-development. Editorial, organizational and '
                     'reader-facing features were left unfinished, and the team struggled to publish and run daily operations.',
        'built': 'We audited the existing code and finished the incomplete features, then moved the reader-facing site '
                 'to Next.js for speed and search visibility. Journalists got a custom CMS with rich formatting; '
                 'articles gained components for company financials, shareholding and author insights; and the team '
                 'got tools to manage organizational information and track progress.',
        'impact': 'The Arc now serves 50,000+ visitors a month, with PageSpeed scores ahead of its competitors.',
        'quote': '“They quickly understood our vision at The Arc and turned it into practical digital solutions.” '
                 'Aditi Shrivastava, Co-founder, The Arc',
        'related': ['fashquik', 'ragya'],
    },
    {
        'slug': 'mccia', 'categories': ['apps'], 'tags': ['Web Platform', 'Industry Body'],
        'card_title': 'MCCIA: online event payments for Pune’s chamber of commerce',
        'card_text': 'Razorpay payments and automatic receipts for a chamber of 3,000+ members.',
        'service': 'Custom Web Apps & Portals', 'client': 'MCCIA (Mahratta Chamber of Commerce, Industries and Agriculture)', 'industry': 'Industry body',
        'about': 'Pune’s chamber of commerce, with over 80 years of history and 3,000+ members across sectors. It runs '
                 'seminars, workshops, networking sessions and conferences all year.',
        'challenge': 'Event registration and payment were manual, which meant delays for members and extra work for staff.',
        'built': 'Razorpay integrated into MCCIA’s event system, accepting cards, net banking and wallets; a simple '
                 'booking flow for members and non-members; automatic confirmation emails and receipts; real-time sync '
                 'of bookings and seats; and PCI DSS-compliant handling of payment data.',
        'impact': 'MCCIA handles more registrations without extra admin work, attendees get instant confirmation, and '
                  'finance reconciles event payments far more easily.',
        'quote': 'Book, pay and get a receipt in one step.',
        'related': ['idamoss-systems', 'temple-qr-passes'],
    },
    {
        'slug': 'fashquik', 'categories': ['rescue', 'apps'], 'tags': ['Dedicated Developers', 'E-Commerce'],
        'card_title': 'Fashquik: developers inside the team, a marketplace scaling again',
        'card_text': 'Our developers joined Fashquik’s team to clean up the code and fix delivery.',
        'service': 'Project Rescue & Dedicated Developers', 'client': 'Fashquik', 'industry': 'Local e-commerce',
        'about': 'A marketplace that helps local vendors sell to customers in their own neighborhood, with its own delivery service.',
        'challenge': 'Technical debt and performance bottlenecks were slowing development just as vendor onboarding '
                     'needed to scale, and the delivery integration was unreliable.',
        'built': 'Our developers joined Fashquik’s own team. Together we reviewed and optimized the codebase for '
                 'speed, refined the vendor management features and rebuilt the local delivery dispatch integration.',
        'impact': 'The platform is faster, more stable and ready to scale, with delivery that vendors and customers can rely on.',
        'quote': 'Our developers, their team, one roadmap.',
        'related': ['the-arc', 'quatch'],
    },
    {
        'slug': 'ragya', 'categories': ['apps', 'mobile'], 'tags': ['Web & Mobile', 'Music'],
        'card_title': 'Ragya: one login across web and mobile',
        'card_text': 'Unified accounts, subscriptions and playlists for a classical music platform.',
        'service': 'Custom Web Apps & Portals, Mobile App Development', 'client': 'Ragya', 'industry': 'Music streaming',
        'about': 'A streaming platform for classical music, with a mobile app and a website.',
        'challenge': 'The app and the website behaved like separate products. Listeners had separate accounts, '
                     'playlists didn’t follow them between devices, and there was no proper way to subscribe or pay.',
        'built': 'One login across web and mobile, a subscription and payment system, real-time sync of playlists and '
                 'listening history, and stronger security for accounts and transactions.',
        'impact': 'One experience on every device, and a smoother path from free listening to a premium subscription.',
        'quote': 'One account, every device.',
        'related': ['the-arc', 'inali-foundation'],
    },
    {
        'slug': 'maxintelb2b', 'categories': ['ux'], 'tags': ['Website', 'B2B Services'],
        'card_title': 'MaxintelB2B: 30% more high-intent leads',
        'card_text': 'A rebuilt B2B website with segmented landing pages and HubSpot lead capture.',
        'service': 'UX & Conversion-Focused Websites', 'client': 'MaxintelB2B', 'industry': 'B2B lead generation',
        'about': 'A B2B data and lead generation company that helps its clients build their revenue pipeline.',
        'challenge': 'Traffic wasn’t turning into leads. Navigation was confusing, calls to action were scattered, and '
                     'the site worked poorly on mobile.',
        'built': 'Heatmaps, surveys and behavior tracking to find where visitors dropped off; a new navigation and '
                 'content structure; a landing page for each audience segment with one focused call to action; a fully '
                 'responsive design; and HubSpot forms for lead capture.',
        'impact': 'Conversions rose 15% and high-intent leads 30%, with far fewer visitors dropping off on mobile.',
        'quote': 'Same traffic, 30% more of the leads that matter.',
        'related': ['fyhba-medical-billing', 'yb-perfumes'],
    },
    {
        'slug': 'fyhba-medical-billing', 'categories': ['ux'], 'tags': ['Website', 'Healthcare'],
        'card_title': 'FYHBA Medical Billing: 35% lower bounce rate, 32% more leads',
        'card_text': 'A conversion-focused website for a US medical billing company.',
        'service': 'UX & Conversion-Focused Websites', 'client': 'FYHBA Medical Billing', 'industry': 'Healthcare services (US)',
        'about': 'A medical billing and coding company in Westwood, New Jersey, offering billing management, '
                 'consulting and revenue cycle services to medical practices.',
        'challenge': 'The website had traffic but few leads. The interface was complicated, the services weren’t '
                     'clearly explained, and the site didn’t work on mobile.',
        'built': 'Buyer research through surveys and behavior analysis; simpler navigation; service pages restructured '
                 'around what practices need to know; a responsive design; lead forms and calls to action where '
                 'visitors make decisions; and automated appointment scheduling.',
        'impact': 'Leads rose 32% and the bounce rate fell 35%.',
        'quote': '“They went the extra mile to deliver solutions that added real value to our business.” '
                 'Ismail Shaikh, Co-founder, FYHBA Medical Billing',
        'related': ['maxintelb2b', 'yb-perfumes'],
    },
    {
        'slug': 'yb-perfumes', 'categories': ['ux'], 'tags': ['E-Commerce', 'D2C'],
        'card_title': 'YB Perfumes: from Instagram DMs to an online store',
        'card_text': 'A mobile-first store that grew a fragrance brand’s sales by 17%.',
        'service': 'UX & Conversion-Focused Websites', 'client': 'YB Perfumes', 'industry': 'D2C fragrance',
        'about': 'A premium fragrance brand selling directly to customers.',
        'challenge': 'Every sale ran through Instagram direct messages, so orders got lost and interested buyers dropped off before paying.',
        'built': 'A mobile-first online store with collections for him and for her, a quick checkout, automated order '
                 'management and CRM integration.',
        'impact': 'Sales grew 17%, and repeat purchases rose as casual followers became regular customers.',
        'quote': 'Instagram followers turned into repeat customers.',
        'related': ['quatch', 'maxintelb2b'],
    },
    {
        'slug': 'quatch', 'categories': ['ux', 'cloud'], 'tags': ['E-Commerce', 'Luxury'],
        'card_title': 'Quatch: a luxury watch store that held up on launch day',
        'card_text': 'Premium e-commerce for a Vietnamese watch brand, with zero downtime at launch.',
        'service': 'UX & Conversion-Focused Websites, Cloud', 'client': 'Quatch', 'industry': 'Luxury e-commerce (Vietnam)',
        'about': 'A luxury watch brand rooted in Vietnam’s cultural heritage.',
        'challenge': 'The old website didn’t feel premium, browsing the collection was confusing, and checkout took too many steps.',
        'built': 'Working with Quatch’s design team: a premium visual design true to the brand, clearer navigation '
                 'through the collections, a shorter checkout, personalized recommendations and curated collections, '
                 'secure multi-currency payments and real-time inventory.',
        'impact': 'A store that matches the brand, longer browsing, smoother purchases, and launch-day traffic handled with zero downtime.',
        'quote': 'Luxury on screen, and zero downtime on launch day.',
        'related': ['yb-perfumes', 'the-arc'],
    },
    {
        'slug': 'indies', 'categories': ['mobile'], 'tags': ['Mobile App', 'Non-Profit'],
        'card_title': 'Indies: NFC tags that help volunteers care for street dogs',
        'card_text': 'An app and website that track street dogs, their health and the volunteers who feed them.',
        'service': 'Mobile App Development', 'client': 'Indies, an initiative of the NGO Sare Jahan Se Acha', 'industry': 'Non-profit, animal welfare',
        'about': 'Indies supports street dogs and the volunteers who feed and care for them.',
        'challenge': 'Volunteers needed a way to find dogs, keep track of feeding and medical care, and coordinate with each other.',
        'built': 'With a partner company, an app and website with NFC chips on dog collars to locate each dog; a '
                 'profile for every dog with vaccinations, health status, treatment and feeding schedules; volunteer '
                 'profiles and activity tracking; and self-help groups with messaging and notifications.',
        'impact': 'Volunteers find dogs faster, feeding and medical care happen on schedule, and the NGO coordinates '
                  'its whole volunteer network in one place.',
        'quote': 'Every dog with a profile, every volunteer in the loop.',
        'related': ['devdoot', 'inali-foundation'],
    },
    {
        'slug': 'temple-qr-passes', 'categories': ['mobile', 'apps'], 'tags': ['Mobile & Web', 'Events'],
        'card_title': 'QR passes that speed up entry',
        'card_text': 'Passes issued online and scanned at the gate, with no duplicate entries.',
        'service': 'Mobile App Development, Custom Web Apps & Portals', 'client': 'A temple', 'industry': 'Religious institution',
        'about': 'A temple that issues passes for visitors to attend its events and ceremonies.',
        'challenge': 'Passes were checked by hand at the entrance: slow, error-prone and frustrating for visitors at busy events.',
        'built': 'Passes with unique QR codes carrying visitor and event details, issued online through the temple’s '
                 'website or app and sent by email; QR scanning at the gate, by hardware scanner or phone, that shows '
                 'the pass details instantly; and a back end that tracks issued passes and blocks duplicate entries.',
        'impact': 'Entry is faster, verification errors are gone, and staff can see how many passes have been issued and used.',
        'quote': 'Scan, verify, enter.',
        'related': ['mccia', 'idamoss-systems'],
    },
    {
        'slug': 'mohur', 'categories': ['ai'], 'tags': ['AI & Data', 'Startup Funding'],
        'card_title': 'Mohur: AI that matches investors with the right startups',
        'card_text': 'A machine-learning engine that recommends startups to investors, and investors to startups.',
        'service': 'Secure In-House AI & Data', 'client': 'Mohur', 'industry': 'Startup funding',
        'about': 'A platform that connects investors with startups looking for funding.',
        'challenge': 'As the platform grew, matching investors with the right startups by hand became slow and inconsistent.',
        'built': 'A data pipeline over investment history, investor profiles and startup information; machine-learning '
                 'models that weigh industry preference, investment size and growth potential; recommendations in both '
                 'directions, startups for investors and investors for startups; and models that keep learning as data grows.',
        'impact': 'More relevant matches, more engagement from investors and founders, and a matching process that scales with the platform.',
        'quote': 'The right investor, suggested before anyone has to search.',
        'related': ['job-post-scoring', 'idamoss-systems'],
    },
    {
        'slug': 'job-post-scoring', 'categories': ['ai'], 'tags': ['AI & Data', 'HR Tech'],
        'card_title': 'Scoring that makes job posts better',
        'card_text': 'A quality score for every job post, feeding the platform’s own AI model.',
        'service': 'Secure In-House AI & Data', 'client': 'A job posting platform', 'industry': 'HR technology',
        'about': 'A job board that connects employers with job seekers.',
        'challenge': 'Job post quality varied widely, and the platform’s own AI model needed an objective quality signal to improve listings.',
        'built': 'A scoring system that rates each job post on description quality, keyword relevance, completeness '
                 'and industry norms; scores passed straight into the client’s existing AI/ML model; and the score, '
                 'with tips to improve it, shown to employers in their dashboard.',
        'impact': 'Employers write better posts, the AI model improves listings automatically, and jobs reach more qualified candidates.',
        'quote': 'A clear score, and a clear way to improve it.',
        'related': ['mohur', 'maxintelb2b'],
    },
    {
        'slug': 'devdoot', 'categories': ['apps', 'automation'], 'tags': ['Web Platform', 'Non-Profit'],
        'card_title': 'Devdoot: connecting 1,000+ people with donors during COVID-19',
        'card_text': 'A verified donation platform built for an NGO in the lockdowns.',
        'service': 'Custom Web Apps & Portals, Workflow Automation', 'client': 'Devdoot, by the NGO Sare Jahan Se Acha', 'industry': 'Non-profit',
        'about': 'Devdoot was launched during the COVID-19 pandemic to connect people who wanted to donate with people in urgent need.',
        'challenge': 'Lockdowns broke the usual ways of distributing aid. Donors couldn’t reach the people who needed help, and requests went unanswered.',
        'built': 'A platform where donors offer items (laptops, phones, stationery, food) and recipients ask for help '
                 'through simple forms with OTP verification; an admin check on every request; verified posts shared '
                 'automatically on Telegram and Facebook; and donor–recipient matching that protects privacy.',
        'impact': 'More than 1,000 people received verified help, from laptops and phones to food and essentials.',
        'quote': 'Verified help, delivered when it mattered most.',
        'related': ['inali-foundation', 'indies'],
    },
    {
        'slug': 'secure-field-data-capture', 'categories': ['apps'], 'tags': ['Custom Software', 'Public Sector'],
        'card_title': 'Secure data capture for field investigations',
        'card_text': 'A bootable, encrypted pen drive that captures data from devices in the field.',
        'service': 'Custom Web Apps & Portals', 'client': 'A law enforcement agency', 'industry': 'Public sector',
        'about': 'A law enforcement agency that collects data from electronic devices during field operations.',
        'challenge': 'Officers needed a portable tool that works on almost any laptop or PC, runs without user input, '
                     'and keeps captured data secure and intact.',
        'built': 'A customized operating system that boots from a pen drive and starts capturing automatically; tools '
                 'to extract and view files and logs; encryption and tamper-resistant storage; and compatibility with '
                 'a wide range of devices and operating systems.',
        'impact': 'Officers capture data quickly in the field without bulky equipment, and every capture stays encrypted and intact.',
        'quote': 'Plug in, capture, secure.',
        'related': ['manufacturing-test-records', 'mohur'],
    },
]
for _c in CASES:
    _c.setdefault('image', f'projects/{_c["slug"]}.webp')
    _c.setdefault('featured_text', _c['card_text'])
    _c['quote_image'] = f'projects/{_c["slug"]}_quote.webp'
    _c['url'] = f'/projects/{_c["slug"]}'
CASE_BY_SLUG = {c['slug']: c for c in CASES}


# --------------------------------------------------------------------------------------------
# How we work
# --------------------------------------------------------------------------------------------

HOW = {
    'description': 'How Hekau works: a free systems audit, then a fixed price, time and material, or a monthly '
                   'retainer, with support after launch.',
    'hero': {
        'badge': 'How we work',
        'title': 'Clear scope, clear price,\nand a partner who stays',
        'text': 'Every engagement starts with a free systems audit. From there we agree how to work together: a fixed '
                'price for defined projects, time and material when the scope will evolve, or a monthly retainer for ongoing support.',
    },
    'models': {
        'heading': 'Three ways to work with us',
        'cards': cards(['feat_web_1', 'feat_bpa_3', 'feat_cloud_3'],
            ('Fixed price, paid by milestone',
             'For projects with a clear scope, like a website, an Odoo rollout or a new portal. You know the total '
             'upfront and pay as each milestone is delivered and accepted.'),
            ('Time and material',
             'For work where the scope will change as we learn: product development, project rescues, dedicated '
             'developers. You pay for the hours worked, tracked in timesheets you can see.'),
            ('Monthly retainer and AMC',
             'For systems you depend on. Support, maintenance, hosting and small improvements for a fixed monthly fee, '
             'with response times agreed upfront.'),
        ),
    },
    'audit': {
        'badge': 'Free systems audit',
        'title': 'What the free systems audit covers',
        'lead': 'One conversation about how your business actually runs. You leave with a clear view of what to fix '
                'first, whether or not you work with us. We look at:',
        'items': ['How work and data move between teams', 'Where spreadsheets and manual steps fill the gaps',
                  'Which numbers teams disagree on', 'What your current tools can already do', 'What to fix first',
                  'Roughly what it would cost'],
    },
    'faq_title': 'Questions buyers ask',
    'faq': [
        {'title': 'How much does a project cost?',
         'text': 'It depends on the scope. After the audit we give you a written fixed quote or an hourly estimate. '
                 'What you’re quoted is what you pay, with no add-on fees.'},
        {'title': 'How long does it take?',
         'text': 'You get a timeline with the quote. Larger projects go live in phases, so each part is useful before the next one starts.'},
        {'title': 'Do we have to use Odoo?',
         'text': 'No. We recommend Odoo when its standard apps fit your process, and build custom software when they '
                 'don’t. Often it’s a mix of both.'},
        {'title': 'Can you take over a project another vendor started?',
         'text': 'Yes. We start with a code audit and tell you honestly whether to fix, refactor or rebuild.'},
        {'title': 'Do you work with companies outside India?',
         'text': 'Yes. We work with clients in India, the US and Southeast Asia, by video call, email and shared project boards.'},
        {'title': 'What happens after launch?',
         'text': 'Support is part of every engagement. After launch you can move to a monthly retainer that covers '
                 'fixes, updates, hosting and small improvements.'},
        {'title': 'Who owns the code and the data?',
         'text': 'You do. Once the project is paid for, the code we write for you and all your data belong to your company.'},
        {'title': 'Will you sign an NDA?',
         'text': 'Yes, before we look at your code or data.'},
    ],
}


# --------------------------------------------------------------------------------------------
# Contact, thank-you, legal
# --------------------------------------------------------------------------------------------

SERVICE_CHOICES = [
    'ERP, CRM & CMS Implementation', 'Workflow & Process Automation', 'Custom Web Applications & B2B Portals',
    'Secure In-House AI & Data', 'Mobile App Development', 'UX & Conversion-Focused Websites',
    'Cloud-Managed Services', 'Project Rescue & Dedicated Developers', 'Not sure yet',
]

CONTACT = {
    'badge': 'Contact',
    'title': 'Let’s find what’s slowing you down',
    'text': 'Tell us a little about your business. We’ll reply within one business day to set up your free systems audit.',
    'lead_name': 'Website enquiry: free systems audit',
    'revenue': ['Under $2M', '$2M–$15M', 'Above $15M', 'Prefer not to say'],
    'sources': ['LinkedIn', 'Google', 'Referral', 'Event', 'Other'],
    'consent': 'Hekau may contact me about this enquiry. See the privacy policy.',
    'newsletter': 'Send me the System Disconnection Checklist and occasional insights. Unsubscribe anytime.',
    'button': 'Book my free systems audit',
    'booking_link': ('Book a 30-minute call', '/book-a-call'),
}

# Calendly event for the free systems audit (free plan: embed and prefill work;
# bookings made here don't reach Odoo CRM on their own, the contact form does).
CALENDLY_URL = 'https://calendly.com/admin-hekautech/30min'

THANKS = {
    'title': 'Thanks, we’ve got it',
    'text': 'Pick a time below and your free systems audit is booked. Prefer to wait? We’ll be in touch within one '
            'business day.',
    'link': ('Download the System Disconnection Checklist', CHECKLIST_URL),
    'booking_heading': 'Pick a time for your audit',
    'booking_lead': '30 minutes with our team. Your details from the form are already filled in.',
}

BOOKING = {
    'description': 'Book a free 30-minute systems audit with Hekau: pick a time that suits you.',
    'label': 'Free systems audit',
    'title': 'Book your free systems audit',
    'sub': '30 minutes, no obligation',
    'text': 'Pick a time that suits you. We’ll look at how work and data move through your business, and tell you '
            'what’s worth fixing first.',
    'heading': 'Choose a time',
    'lead': 'Times are shown in your own time zone.',
}

LAST_UPDATED = 'Last updated October 2026'

TERMS = {
    'title': 'Terms and Conditions',
    'text': 'The terms for using www.hekautech.com. Work for clients is covered by its own written agreement.',
    'groups': [
        {'title': '1. About these terms',
         'text': f'These terms govern your use of www.hekautech.com, run by {COMPANY["name"]}, {COMPANY["address"]}, '
                 'Maharashtra, India. By using the website, you accept them.'},
        {'title': '2. Our services',
         'text': 'Service descriptions on this website are general information, not an offer. Every engagement is '
                 'governed by a separate written proposal or agreement, which takes precedence over these terms.'},
        {'title': '3. Using the website',
         'text': 'Use the website lawfully. Don’t try to disrupt it, gain unauthorized access, or collect its content by '
                 'automated means, and give accurate information in our forms.'},
        {'title': '4. Intellectual property',
         'text': 'The content, design and logos on this website belong to Hekau or are used with permission. Client '
                 'names and trademarks belong to their owners. You may link to our pages and quote short extracts with credit.'},
        {'title': '5. Case studies and results',
         'text': 'Case studies describe specific projects for specific clients. They are not a promise of the same results for your business.'},
        {'title': '6. Downloads',
         'text': 'The System Disconnection Checklist and other resources are provided for information only, as they are.'},
        {'title': '7. Links to other websites',
         'text': 'We are not responsible for the content or practices of websites we link to.'},
        {'title': '8. Disclaimer and limitation of liability',
         'text': 'The website is provided “as is”. To the extent the law allows, Hekau is not liable for any indirect or '
                 'consequential loss arising from your use of it.'},
        {'title': '9. Privacy',
         'text': 'Our privacy policy explains how we handle personal data you share through this website.'},
        {'title': '10. Changes',
         'text': 'We may update these terms. The date at the top shows the current version.'},
        {'title': '11. Governing law',
         'text': 'These terms are governed by the laws of India, and the courts at Pune, Maharashtra have jurisdiction.'},
        {'title': '12. Contact',
         'text': f'Questions about these terms: {COMPANY["email"]}.'},
    ],
}

PRIVACY = {
    'title': 'Privacy Policy',
    'text': 'What personal data this website collects, why, and the choices you have.',
    'groups': [
        {'title': '1. Who we are',
         'text': f'{COMPANY["name"]}, {COMPANY["address"]}, Maharashtra, India, decides how your personal data is used on '
                 f'this website. Privacy questions: {COMPANY["email"]}.'},
        {'title': '2. What we collect',
         'text': 'From our forms: your name, work email, phone, company, revenue band, the service you’re interested in, '
                 'your message and how you heard about us. From the newsletter signup: your name and email. '
                 'When you book a call: the details you enter in the booking calendar, collected through Calendly. '
                 'Automatically: your IP address, browser and device details, and the pages you visit, through cookies '
                 'and analytics tools.'},
        {'title': '3. Why we use it',
         'text': 'To reply to your enquiry and arrange your systems audit; to send the checklist and newsletter if you '
                 'asked for them; to improve the website; to manage our relationship with clients; and to meet legal obligations.'},
        {'title': '4. Your consent',
         'text': 'We use your data on the basis of the consent you give in our forms, or for other uses the law allows. '
                 'You can withdraw consent at any time, as easily as you gave it, by emailing us or using the unsubscribe '
                 'link in any email.'},
        {'title': '5. Cookies',
         'text': 'Essential cookies keep the website working. Analytics cookies are set only if you accept them in the '
                 'cookie banner. The booking calendar is provided by Calendly, which may set its own cookies. You can '
                 'also block cookies in your browser.'},
        {'title': '6. Who we share it with',
         'text': 'Service providers that help us run the business, such as hosting, email (Google Workspace), '
                 'call scheduling (Calendly) and analytics, under contracts that protect your data. We never sell personal data. We disclose it only when '
                 'the law requires.'},
        {'title': '7. Where it’s stored',
         'text': 'On servers used by Hekau and its service providers. Some providers may process data outside India, as the law permits.'},
        {'title': '8. How long we keep it',
         'text': 'Enquiry data, as long as we need it to respond and for any relationship that follows; if no engagement '
                 'follows, we delete it after 24 months. Newsletter data, until you unsubscribe. Records the law requires '
                 'us to keep, such as invoices, for the period it sets.'},
        {'title': '9. How we protect it',
         'text': 'Encryption in transit, access limited by role, two-factor login on our systems, and regular backups.'},
        {'title': '10. Your rights',
         'text': 'You can ask for a summary of the data we hold about you, have it corrected, completed, updated or '
                 'erased, withdraw your consent, nominate someone to act for you, and raise a grievance. Email us and '
                 'we’ll respond within the time the law requires. If you’re not satisfied, you can complain to the Data '
                 'Protection Board of India.'},
        {'title': '11. Children',
         'text': 'This website is for businesses and is not directed at anyone under 18. We don’t knowingly collect their data.'},
        {'title': '12. Changes',
         'text': 'We may update this policy; the date at the top shows the current version.'},
        {'title': '13. Contact for privacy questions and grievances',
         'text': f'Santosh Yadav, Director, {COMPANY["email"]}, {COMPANY["phone"]}.'},
    ],
}
