"""Long-form case studies (/projects/<slug>), merged into hk_content.CASES.

Sources: the Hekau portfolio (Hekau_Portfolio_detailed-3.pdf) and Santosh's
LinkedIn projects and posts (YB Perfumes, MyWanderloop, the Odoo rollout).
Every figure comes from those sources; nothing is estimated.

Fields per project:
    gist      (problem, built, result): the "At a glance" panel
    tools     optional "Built with" line (only where the sources name them)
    about     About the client
    challenge The challenge
    built     intro of What we built, then `features`: (title, text)
    how       optional {'title', 'text'} after What we built
    impact    The impact
    extra     optional groups after The impact: {'title', 'text', 'items'}
Text: blank line between paragraphs; lines starting with "- " make a list;
**text** is bold.
"""

ODOO_EXTRAS = [
    ('Quality control',
     'Quality checks at chosen production steps, with pass or fail results recorded against each manufacturing '
     'order and alerts when something fails.'),
    ('Barcode scanning in the warehouse',
     'Receipts, picking, packing and stock counts done by scanning, which cuts typing errors and speeds up the '
     'warehouse.'),
    ('Field service',
     'Maintenance jobs at customer sites scheduled for technicians, with parts, time and the customer’s signature '
     'captured on a phone and invoiced from the same record.'),
    ('Helpdesk',
     'Customer issues logged as tickets and linked to the customer’s orders and equipment, with response targets '
     'the team can track.'),
    ('Product lifecycle management',
     'Engineering changes to products and bills of materials, versioned and approved before they reach the shop '
     'floor.'),
    ('Customer and vendor portals',
     'Customers check orders, deliveries and invoices online; vendors confirm purchase orders and delivery dates '
     'without email back-and-forth.'),
    ('Website and online store',
     'A website and online store that use the same products, prices and stock as the back office.'),
    ('Dashboards and reporting',
     'Live dashboards for sales, margins, stock value and production, built on the data teams already enter.'),
]

CASE_DETAILS = {
    'odoo-manufacturing': {
        'gist': (
            'Sales, purchasing, stock, production, maintenance and billing lived in separate tools, and month-end '
            'meant reconciling numbers that didn’t match.',
            'One Odoo system for sales, purchasing, inventory, manufacturing, maintenance, projects, timesheets and '
            'invoicing, with each step feeding the next.',
            'Work is visible across teams, invoices follow completed work, and there are far fewer “which number is '
            'correct?” conversations.',
        ),
        'tools': 'Odoo: Sales, Purchase, Inventory, Manufacturing, Maintenance, Project, Timesheets, Invoicing',
        'about': (
            'A growing company that does three kinds of work for its customers: it manufactures products, maintains '
            'equipment and delivers projects. Each has its own rhythm, its own paperwork and its own people, and all '
            'three have to end in an accurate invoice.\n\n'
            'Like many companies at this stage, it had grown one tool at a time: a sales tracker here, a stock '
            'spreadsheet there, and separate ways to log maintenance work and project hours.'
        ),
        'challenge': (
            'Every team had its own version of the truth. When something changed in one place, someone had to '
            'remember to update it everywhere else.\n\n'
            '- **Sales and operations weren’t connected.** A confirmed order didn’t tell purchasing what to buy or '
            'production what to build.\n'
            '- **Stock and maintenance drifted apart.** Parts used on maintenance jobs weren’t always reflected in '
            'inventory.\n'
            '- **Project effort was estimated, not recorded.** Hours lived in separate sheets, so project '
            'profitability was a guess.\n'
            '- **Month-end was a reconciliation exercise.** Numbers had to be matched across tools before invoices '
            'and reports could go out.'
        ),
        'built': (
            'We implemented Odoo as the single system for the whole operation, set up around how the company already '
            'works, and connected each step to the next so data is entered once.'
        ),
        'features': [
            ('Sales connected to procurement and production',
             'A confirmed sales order now drives what happens next: what needs to be bought and what needs to be '
             'made. Sales can see where an order stands without asking.'),
            ('Inventory that stays accurate',
             'Receipts, production and deliveries update stock as they happen, so every team looks at the same '
             'quantities.'),
            ('Manufacturing and maintenance in step',
             'Manufacturing orders and maintenance work sit in the same system as inventory, so parts and materials '
             'used on a job come out of the same stock records.'),
            ('Projects with real timesheets',
             'Project tasks are planned in Odoo and the team logs hours against them, so each project shows the '
             'effort that actually went into it, not an estimate.'),
            ('Invoicing that follows the work',
             'Delivered goods, completed project work and logged hours flow into invoices. Billing became a result '
             'of finished work instead of a separate task at month-end.'),
        ],
        'impact': (
            'There is nothing dramatic about one system, and that is the point. The improvements show up in everyday '
            'work:\n\n'
            '- **Work is visible across teams.** Sales, operations and finance see the same orders, stock and '
            'progress.\n'
            '- **Fewer gaps and reconciliations.** Data is entered once and flows on, so there is less to '
            'cross-check.\n'
            '- **Real project effort.** Timesheets record actual hours, not estimates.\n'
            '- **Invoices follow completed work.** Billing is no longer a separate exercise.'
        ),
        'extra': [{
            'title': 'What else Odoo can do for a company like this',
            'text': (
                'This rollout covered the core of the business. Because Odoo runs dozens of apps on one database, a '
                'company like this can keep adding capability without bringing in another disconnected tool. Some of '
                'these are Odoo Enterprise apps; we tell you what your edition includes, and what each addition '
                'involves, before you commit.'
            ),
            'items': ODOO_EXTRAS,
        }],
    },

    'inali-foundation': {
        'gist': (
            'Patients, appointments, CSR campaigns, inventory and staff tasks ran on paper and spreadsheets, and '
            'campaign reports took days.',
            'One mobile and web app with role-based dashboards for patients, appointments, campaigns, inventory, '
            'vendors and leads.',
            'CSR campaigns are finalized in 2 days instead of 7, and every team works from the same live data.',
        ),
        'tools': 'Mobile app · Web app · Role-based access',
        'about': (
            'Inali Foundation is a non-profit that has provided thousands of accessible prosthetic arms to people '
            'across India. Its work is funded through CSR partnerships, so it answers to two groups at once: the '
            'patients it fits and supports, and the partners who want to see what their funding achieves.\n\n'
            'Doing both well takes close coordination between doctors, CSR managers, inventory staff, supervisors and '
            'the people bringing in new leads.'
        ),
        'challenge': (
            'Almost everything ran on paper and spreadsheets. As the foundation grew, manual work started to hold it '
            'back:\n\n'
            '- **Registration and appointments were manual,** which made booking fittings slow and patient history '
            'hard to find.\n'
            '- **Campaigns, inventory and staff tasks were managed separately,** with no single view of what was '
            'happening.\n'
            '- **Leads weren’t tracked centrally,** so follow-ups depended on memory.\n'
            '- **Teams communicated through calls and messages,** which caused delays and misunderstandings.\n\n'
            'The cost was real. Pulling a campaign report took days, and the foundation nearly lost a major recurring '
            'CSR partner because of it. The founder couldn’t see inventory, fitments or campaign status without '
            'waiting for someone to compile the data.'
        ),
        'built': (
            'We designed and built the Inali App, one mobile and web platform for the whole operation. Each person '
            'sees what their role needs, and every update reaches the people who depend on it.'
        ),
        'features': [
            ('Patient registration and records',
             'Registration collects everything the clinical team needs and stores it securely. Each patient’s '
             'medical history, fitment procedures and rehabilitation progress are organized on a personal '
             'dashboard.'),
            ('Appointments with automatic reminders',
             'Staff book fittings and follow-ups in a few taps. Patients and staff get reminders and updates '
             'automatically, which cuts no-shows and phone calls.'),
            ('CSR campaign management',
             'Campaigns are launched, tracked and reported in the app, and partners receive progress updates, so '
             'they see the impact of their funding without asking for a report.'),
            ('Role-based dashboards',
             'CSR managers, lead managers, inventory managers, supervisors and doctors each have their own dashboard '
             'and access level. People see what they need, and sensitive data stays with those allowed to see it.'),
            ('Inventory, vendors and partners',
             'Stock levels update in real time, so components are replenished before they run out. Vendor and CSR '
             'partner profiles, including vendor performance, live in the same system.'),
            ('Tasks and leads',
             'Daily tasks are assigned and tracked to completion, and leads are managed in a built-in CRM so none '
             'fall through the cracks.'),
        ],
        'impact': (
            'The app replaced paperwork with one live view of the foundation’s work:\n\n'
            '- **CSR campaigns finalized in 2 days instead of 7.**\n'
            '- **Better coordination.** Role-based dashboards keep departments working from the same information.\n'
            '- **Transparency for partners and leadership.** Real-time updates show inventory, fitments and campaign '
            'progress without waiting for a report.\n'
            '- **More people served.** With less time on admin, the team spends more on its mission.'
        ),
    },

    'event-ticketing-marketplace': {
        'gist': (
            'Every new organizer meant collecting details and drafting a contract by hand, and the platform needed '
            'full e-commerce to grow.',
            'Self-service vendor sign-up with contracts generated automatically, plus ticket listings, payments, '
            'delivery and behavior analytics.',
            'A marketplace serving 6,000 regular users and a growing number of vendors, with no contract drafting.',
        ),
        'tools': 'Multiple payment gateways · Google Analytics · Microsoft Clarity',
        'about': (
            'Our client runs an online marketplace where event organizers sell tickets for festivals, raves and '
            'parties. Organizers, the platform’s vendors, list their events; fans discover them, buy tickets and '
            'receive them online.\n\n'
            'A marketplace like this grows on two things: how easily new organizers can join, and how easily fans '
            'can buy.'
        ),
        'challenge': (
            'The client needed a platform that could run both sides of the marketplace without a team doing '
            'paperwork in between:\n\n'
            '- **Vendor onboarding was manual.** Each new organizer meant collecting details and drafting a contract '
            'by hand.\n'
            '- **Selling tickets needed real e-commerce.** Listings, ticket inventory, payments and delivery all had '
            'to work smoothly.\n'
            '- **The team couldn’t see how people used the site,** so it was hard to know where buyers dropped off '
            'or what to improve next.'
        ),
        'built': (
            'We designed and built the marketplace end to end, with the vendor side as automated as the buyer side.'
        ),
        'features': [
            ('Self-service vendor registration',
             'Organizers sign up through a guided form that captures everything needed to start selling, so '
             'onboarding no longer waits on the client’s team.'),
            ('Contracts that write themselves',
             'As soon as a vendor completes registration, the platform builds their contract from the details they '
             'entered and emails it to both the vendor and the client. Everyone has a copy, and nobody drafts it by '
             'hand.'),
            ('Ticket listings and inventory',
             'Vendors list their events and manage ticket availability themselves, and counts update as tickets '
             'sell.'),
            ('Payments and ticket delivery',
             'Buyers pay through several payment gateways and receive their tickets online, with a smooth checkout '
             'from start to finish.'),
            ('Behavior analytics',
             'Google Analytics and Microsoft Clarity show how visitors browse, where they hesitate and where they '
             'drop off, so the team improves the platform with data rather than guesses.'),
        ],
        'how': {'title': 'How it works', 'text': (
            '- An organizer registers and receives their contract by email as soon as they finish.\n'
            '- They list an event and set ticket availability.\n'
            '- Fans find the event, pay through their preferred gateway and get their tickets online.\n'
            '- The client follows sales and behavior in analytics and keeps refining the platform.'
        )},
        'impact': (
            '- **6,000 regular users** buy tickets on the platform.\n'
            '- **A growing vendor base,** helped by onboarding without paperwork.\n'
            '- **No manual contract drafting.** Every vendor contract is generated the moment registration is '
            'complete.\n'
            '- **Decisions based on data,** with analytics showing how buyers actually use the site.'
        ),
    },

    'manufacturing-test-records': {
        'gist': (
            'Test results were written down by hand: slow, error-prone and hard to analyze.',
            'An Android app that records results straight from the testing machines, secure central storage and a '
            'web platform with dashboards.',
            'No manual entry errors, results available the moment a test finishes, and trends visible on '
            'dashboards.',
        ),
        'tools': 'Android app · Encrypted data transfer · Web platform with dashboards',
        'about': (
            'Our client is an industrial manufacturer whose products are tested against strict quality standards. '
            'Every test produces results that have to be stored safely and made available to the people responsible '
            'for quality and production.\n\n'
            'The company manages these results on a dedicated record-keeping platform used across its manufacturing '
            'units.'
        ),
        'challenge': (
            'Recording tests by hand doesn’t scale:\n\n'
            '- **Manual entry caused errors,** and every error in a test record is a quality risk.\n'
            '- **Results took time to reach people,** because they had to be written up first.\n'
            '- **Data was hard to analyze.** Spotting a trend or an anomaly meant digging through records.\n'
            '- **Access had to be controlled.** Different people needed different data sets, and nothing more.\n\n'
            'The client wanted results captured digitally at the machine, stored securely in one place and presented '
            'in a way people could actually read.'
        ),
        'built': 'We built a system that takes test data from the machine to a dashboard without anyone retyping it.',
        'features': [
            ('Data capture at the machine',
             'An Android app connects directly to the testing machines and records results in real time, so the '
             'number in the system is the number the machine produced.'),
            ('Secure transfer and storage',
             'Captured results travel to a central server over encrypted connections and are stored there, ready for '
             'future access and analysis.'),
            ('Web platform with access control',
             'Authorized users log in to a web platform to see the data. Access is managed per user, so each person '
             'sees only the data sets relevant to them.'),
            ('Insights and charts',
             'Results are turned into graphs and charts that make trends, anomalies and performance easy to see, '
             'including for teams monitoring remotely.'),
            ('Custom dashboards',
             'Each user arranges a dashboard with the line charts, bar graphs and pie charts that matter to their '
             'role.'),
        ],
        'how': {'title': 'How it works', 'text': (
            '- A test runs on the machine.\n'
            '- The Android app records the result and sends it, encrypted, to the central server.\n'
            '- The result appears on the web platform for users with access.\n'
            '- Dashboards update, so managers see trends without compiling anything.'
        )},
        'impact': (
            '- **Accurate records.** Automated capture removed manual entry errors.\n'
            '- **Faster decisions.** Results are available as soon as a test finishes, and charts make them easy to '
            'interpret.\n'
            '- **Less effort** for technical staff and managers, who no longer write up or compile results.\n'
            '- **Secure, personal access.** Each user sees the data they need on their own dashboard.'
        ),
    },

    'mywanderloop': {
        'gist': (
            'The platform depends on real-time SMS and email, and needed fast, high-volume delivery without a '
            'complicated setup.',
            'MSG91 integrated into the back end: automated SMS on DLT-compliant templates, transactional email, '
            'webhooks and delivery logs.',
            'Sign-up and security checks run automatically, and every message is delivered quickly and tracked.',
        ),
        'tools': 'MSG91 SMS and email APIs · Webhooks · DLT-compliant templates',
        'about': (
            'MyWanderloop runs a consumer platform that depends on messages arriving on time. Sign-up verification '
            'codes, transactional alerts and account updates reach users by SMS or email, and each one matters at the '
            'moment it is sent.\n\n'
            'A verification code that arrives late is a user who gives up.'
        ),
        'challenge': (
            'MyWanderloop needed messaging that was fast, reliable and simple to run:\n\n'
            '- **High volume without delays.** Codes and alerts had to go out immediately, even at busy times.\n'
            '- **India’s telecom rules.** Transactional SMS in India has to use registered DLT templates to be '
            'delivered.\n'
            '- **Visibility.** The team needed to know a message was delivered, not just sent.\n'
            '- **Low operational overhead.** The setup couldn’t need constant attention from the team.'
        ),
        'built': (
            'We integrated MSG91’s cloud communication APIs into the platform’s back end and automated every message '
            'the platform sends.'
        ),
        'features': [
            ('Automated SMS workflows',
             'Verification codes, alerts and updates trigger automatically from events in the platform, using '
             'DLT-compliant templates.'),
            ('Transactional email pipelines',
             'Account and transaction emails go out through the same integration, with consistent templates.'),
            ('Webhooks and API routing',
             'Delivery events come back to the platform through webhooks, so the system knows what happened to each '
             'message.'),
            ('Delivery tracking and real-time logs',
             'Every SMS and email is logged from send to delivery, which makes problems easy to spot and support '
             'questions easy to answer.'),
        ],
        'impact': (
            '- **Smoother onboarding.** Sign-up verification runs on its own, with codes delivered quickly.\n'
            '- **Security checks without manual steps.**\n'
            '- **Full delivery visibility,** with real-time logs for every message.\n'
            '- **Low maintenance,** so the team spends its time on the product, not the plumbing.'
        ),
    },

    'the-arc': {
        'gist': (
            'The previous vendor abandoned the platform mid-build, leaving editorial, internal and reader-facing '
            'features unfinished.',
            'We finished and refined the platform, moved the reader site to Next.js and built a custom CMS with rich '
            'article components.',
            'The Arc now serves 50,000+ visitors a month, with PageSpeed scores ahead of its competitors.',
        ),
        'tools': 'Next.js · Custom CMS',
        'about': (
            'The Arc is a seed-funded news platform covering India’s high-growth companies, with research-backed '
            'reporting for general readers and executives. Its journalists publish news and insights for an audience '
            'that follows the startup ecosystem closely.\n\n'
            'For a publisher, two things decide success: how easily journalists can publish good work, and how '
            'quickly readers and search engines can find it.'
        ),
        'challenge': (
            'The Arc’s previous IT vendor walked away in the middle of development. That left the team with a '
            'platform they depended on but couldn’t fully use:\n\n'
            '- **Editorial tools were incomplete,** which made writing and managing articles harder than it should '
            'be.\n'
            '- **Internal features were unfinished,** including organizational information and daily team '
            'operations.\n'
            '- **The reader-facing site had to perform.** For a news platform, speed and search visibility drive '
            'audience growth.\n\n'
            'The Arc needed a partner who could take over someone else’s code, finish it properly and raise the '
            'standard.'
        ),
        'built': (
            'We started with a thorough audit of what had been built, refined the existing features until they worked '
            'as intended, then rebuilt the parts that mattered most for growth.'
        ),
        'features': [
            ('A faster site on Next.js',
             'We moved the reader-facing website to Next.js, which renders pages quickly and is easy for search '
             'engines to index. For a news platform, that means more readers finding stories through search.'),
            ('A custom CMS for journalists',
             'The editorial team got a content management system built around how they write, with rich formatting '
             'such as bold, italics and links, so articles are well structured and easy to read.'),
            ('Article components that add depth',
             'Articles can include author insights, company financials and shareholding details, giving readers '
             'context alongside the story.'),
            ('Organizational management',
             'Internal tools to manage organizational information and track the team’s progress, so the newsroom '
             'runs from one place.'),
        ],
        'impact': (
            '- **50,000+ visitors a month.**\n'
            '- **PageSpeed scores ahead of competitors,** which helps readers and search rankings alike.\n'
            '- **A newsroom that publishes without fighting its tools.**\n'
            '- **A platform ready to grow,** after starting from an abandoned build.'
        ),
    },

    'mccia': {
        'gist': (
            'Event registration and payment were manual, causing delays for members and extra work for staff.',
            'Razorpay integrated into MCCIA’s event system, with a simple booking flow, automatic receipts and '
            'real-time booking sync.',
            'More registrations handled without extra admin, instant confirmation for attendees and easier '
            'reconciliation.',
        ),
        'tools': 'Razorpay',
        'about': (
            'The Mahratta Chamber of Commerce, Industries and Agriculture (MCCIA) is Pune’s chamber of commerce, with '
            'more than 80 years of history and over 3,000 members across sectors. From the MCCIA Trade Tower in Pune, '
            'a team of around 90 professionals works on business associations, advocacy and services for members.\n\n'
            'Events are central to that work: industry seminars, workshops, networking sessions and conferences run '
            'throughout the year, for members and non-members alike.'
        ),
        'challenge': (
            'As the event calendar grew, the manual booking process couldn’t keep up:\n\n'
            '- **Registration and payment happened offline,** which meant delays for attendees and follow-ups for '
            'staff.\n'
            '- **Confirmations and receipts were handled by hand.**\n'
            '- **Bookings weren’t synced with event availability,** so seats had to be checked manually.\n'
            '- **Reconciling event payments took effort.**\n\n'
            'MCCIA wanted a secure, simple way for anyone to book and pay for an event online.'
        ),
        'built': (
            'We integrated a payment gateway into MCCIA’s existing event platform and automated everything that happens '
            'after someone pays.'
        ),
        'features': [
            ('Razorpay payment gateway',
             'Attendees pay by credit or debit card, net banking or mobile wallet, whichever they prefer.'),
            ('A simple booking flow',
             'Custom registration and confirmation screens take members and non-members from choosing an event to '
             'paying in a few steps.'),
            ('Automatic confirmations and receipts',
             'As soon as a payment succeeds, the attendee receives a confirmation email and a receipt, with no staff '
             'involvement.'),
            ('Real-time sync with the event system',
             'Bookings update event availability instantly, so MCCIA always knows how many seats are taken.'),
            ('Secure payments',
             'Payments run over encrypted connections and follow PCI DSS standards for handling card data.'),
        ],
        'impact': (
            '- **More registrations, no extra admin.** Staff no longer process bookings by hand.\n'
            '- **Instant confirmation for attendees,** which encourages more people to register online.\n'
            '- **Easier financial management.** Automated payment tracking makes reconciling event revenue '
            'simpler.\n'
            '- **A better experience for members,** who book and pay in one go.'
        ),
    },

    'fashquik': {
        'gist': (
            'Technical debt and performance bottlenecks were slowing development just as vendor onboarding needed to '
            'scale.',
            'Our developers joined Fashquik’s team to optimize the codebase, re-engineer vendor management and rebuild '
            'delivery dispatch.',
            'A faster, more stable marketplace, ready to scale, with delivery that vendors and customers can rely on.',
        ),
        'about': (
            'Fashquik is an e-commerce marketplace that helps local vendors sell to customers in their own '
            'neighborhood. Unlike a typical online store, it also runs the delivery, so products reach customers '
            'quickly from shops nearby.\n\n'
            'That model depends on two things working well: onboarding and managing many small vendors, and reliable '
            'local delivery.'
        ),
        'challenge': (
            'Fashquik hit development hurdles just as it needed to grow:\n\n'
            '- **Technical debt and performance bottlenecks** made the platform slow and every new feature harder to '
            'build.\n'
            '- **Vendor management needed work** to support onboarding more local merchants.\n'
            '- **The delivery integration was unreliable,** and delivery is the core of the business model.\n\n'
            'Fashquik needed experienced developers who could join their team and work inside their roadmap.'
        ),
        'built': 'Our developers joined Fashquik’s own team and worked alongside their developers on one roadmap.',
        'features': [
            ('Code review and optimization',
             'We reviewed the existing codebase, refactored the parts causing bottlenecks and optimized it for speed '
             'and scalability.'),
            ('Vendor management features',
             'With Fashquik’s developers, we re-engineered the vendor management features so onboarding and managing '
             'local merchants matches the business goals.'),
            ('Reliable delivery dispatch',
             'We rebuilt the local delivery dispatch integration so orders reach delivery reliably, for vendors and '
             'customers alike.'),
        ],
        'how': {'title': 'How we worked', 'text': (
            'Embedded developers only help if they fit the team. Ours adapted to Fashquik’s tools, standards and '
            'planning, picked up context quickly and contributed to the existing team rather than working beside it.'
        )},
        'impact': (
            '- **A faster, more stable platform** after the code clean-up.\n'
            '- **Ready to scale** local vendor onboarding.\n'
            '- **Delivery that vendors and customers can rely on.**\n'
            '- **One team, one roadmap,** with our developers working as part of Fashquik’s team.'
        ),
    },

    'ragya': {
        'gist': (
            'The app and the website behaved like separate products: separate accounts, playlists that didn’t sync and '
            'no proper way to subscribe.',
            'One login across web and mobile, subscription billing, real-time sync of playlists and listening history, '
            'and stronger security.',
            'One experience on every device and a smoother path from free listening to a premium subscription.',
        ),
        'about': (
            'Ragya is a streaming platform for classical music, much like Spotify but focused on traditional and '
            'classical genres. Listeners use its mobile app and its website to explore the collection.\n\n'
            'For a subscription product, the experience across devices is the product: listeners expect to pick up '
            'where they left off, wherever they are.'
        ),
        'challenge': (
            'Ragya’s app and website had grown up separately:\n\n'
            '- **Separate accounts.** Listeners couldn’t use the same login on the app and the website.\n'
            '- **Nothing followed them between devices.** Playlists and preferences on one platform didn’t appear on '
            'the other.\n'
            '- **No robust payment system,** which made it hard to subscribe, buy music or unlock premium features.\n\n'
            'To stay competitive, Ragya needed the two platforms to work as one.'
        ),
        'built': 'We unified Ragya’s web and mobile platforms around a single account and a single subscription.',
        'features': [
            ('One login, every device',
             'A unified authentication system lets listeners sign in with the same account on the app and the '
             'website.'),
            ('Subscriptions and payments',
             'A secure, simple payment system for subscriptions and purchases, so upgrading to premium takes a few '
             'taps.'),
            ('Cross-platform sync',
             'Playlists, preferences and listening history sync in real time, so the experience continues from phone '
             'to laptop.'),
            ('Security for accounts and transactions',
             'Stronger security measures protect personal data and payments.'),
        ],
        'impact': (
            '- **A unified experience** across mobile and web.\n'
            '- **More premium subscriptions,** with a simpler path to upgrade.\n'
            '- **Better retention,** as listeners find their library wherever they are.\n'
            '- **Consistent data** across platforms.'
        ),
    },

    'maxintelb2b': {
        'gist': (
            'The site had traffic but few leads: confusing navigation, scattered calls to action and a poor mobile '
            'experience.',
            'A research-led redesign: new navigation, a landing page for each audience segment, responsive design and '
            'HubSpot lead capture.',
            'Conversions up 15%, high-intent leads up 30%, and far fewer visitors dropping off on mobile.',
        ),
        'tools': 'HubSpot · Heatmaps and behavior analytics',
        'about': (
            'MaxintelB2B is a B2B data and lead generation company that helps its clients build their revenue '
            'pipeline. Its own website is one of its most important sales tools: if a lead generation company can’t '
            'generate leads from its own site, prospects notice.\n\n'
            'They came to us to revamp the website so it would engage visitors, capture more leads and convert better.'
        ),
        'challenge': (
            'Traffic wasn’t the problem. Turning it into leads was:\n\n'
            '- **Low conversion rates.** Visitors arrived and left without getting in touch.\n'
            '- **Confusing navigation** made the right service hard to find.\n'
            '- **Scattered, ineffective calls to action** gave visitors no clear next step.\n'
            '- **No proper mobile experience,** which lost a large share of visitors.'
        ),
        'built': 'We started with research, not design, so every change targeted a real drop-off point.',
        'features': [
            ('User research',
             'Surveys, heatmap analysis and behavior tracking showed where visitors hesitated, what they looked for and '
             'where they left.'),
            ('Navigation and content redesign',
             'We rebuilt the navigation and restructured the content so each visitor finds the relevant service '
             'quickly.'),
            ('A landing page for each segment',
             'Each audience segment got its own landing page with one focused call to action, instead of a generic '
             'page for everyone.'),
            ('Mobile optimization',
             'A fully responsive design gives mobile visitors the same experience as desktop.'),
            ('HubSpot lead capture',
             'HubSpot forms capture leads straight into the CRM, making it easy for visitors to get in touch and for '
             'the sales team to follow up.'),
        ],
        'impact': (
            '- **15% more conversions** across the site.\n'
            '- **30% more high-intent B2B leads.**\n'
            '- **Lower bounce rates** as navigation improved.\n'
            '- **Far fewer mobile drop-offs.**\n\n'
            'The work stayed cost-effective by focusing on the changes that mattered to MaxintelB2B’s users, not on a '
            'rebuild for its own sake.'
        ),
    },

    'fyhba-medical-billing': {
        'gist': (
            'The website had traffic but few leads, a complicated interface, unclear services and no mobile support.',
            'A research-led redesign with simpler navigation, clear service pages, responsive design, lead forms and '
            'appointment scheduling.',
            '32% more leads and a 35% lower bounce rate.',
        ),
        'about': (
            'FYHBA Medical Billing is a medical billing and coding company based in Westwood, New Jersey. It offers '
            'billing management, consulting and revenue cycle services to medical practices.\n\n'
            'Its buyers are practice owners and managers who need to trust a billing partner quickly, so the website '
            'has to explain the services clearly and make it easy to start a conversation.'
        ),
        'challenge': (
            'FYHBA’s website was getting visitors, but not turning them into enquiries:\n\n'
            '- **Low lead generation** despite substantial traffic.\n'
            '- **A complicated interface** discouraged visitors from exploring the services.\n'
            '- **No mobile responsiveness,** so visitors on phones had a poor experience.\n'
            '- **Services weren’t clearly presented,** so visitors missed important information.'
        ),
        'built': 'We redesigned the site around what practices need to know before they get in touch.',
        'features': [
            ('Buyer research',
             'Surveys and behavior analysis showed who visits the site, what they look for and where they get '
             'stuck.'),
            ('Simpler navigation',
             'A streamlined structure and interface, so visitors find and understand FYHBA’s services quickly.'),
            ('Clear service pages',
             'Content restructured to present every service in detail, so visitors get the information they came '
             'for.'),
            ('Responsive design',
             'The new site works on every device, from desktop to phone.'),
            ('Lead capture and scheduling',
             'Simple forms and calls to action where visitors make decisions, and automated appointment scheduling so '
             'prospects can book a call without back-and-forth.'),
        ],
        'impact': (
            '- **32% more leads** captured through the site.\n'
            '- **35% lower bounce rate,** with visitors staying longer.\n'
            '- **More engagement,** as visitors spend more time exploring the services.\n'
            '- **A stronger platform for growth,** positioning FYHBA to attract and convert new clients.'
        ),
    },

    'yb-perfumes': {
        'gist': (
            'Every sale ran through Instagram direct messages, so orders got lost and buyers dropped off before '
            'paying.',
            'A mobile-first online store with catalog browsing, a quick checkout, automated order management and CRM '
            'integration.',
            'Sales grew 17%, and repeat purchases rose as followers became regular customers.',
        ),
        'about': (
            'YB Perfumes is a premium fragrance brand that sells directly to its customers. Like many young D2C '
            'brands, it built its audience on Instagram, where followers discovered new scents and asked about them in '
            'direct messages.'
        ),
        'challenge': (
            'Selling through direct messages works until interest grows. Then the manual process starts to cost '
            'sales:\n\n'
            '- **Orders got lost** in long message threads.\n'
            '- **Buyers dropped off** between asking a question and paying.\n'
            '- **Every order meant manual work,** from confirming details to tracking payment.\n'
            '- **Customer details were scattered across chats,** which made repeat purchases hard to encourage.'
        ),
        'built': (
            'We moved the brand from direct messages to its own mobile-first online store, designed for people '
            'arriving from Instagram on their phones.'
        ),
        'features': [
            ('A mobile-first store',
             'Designed for the phone first, because that is where the brand’s audience finds it.'),
            ('Interactive catalog',
             'Browsing the collections, including collections for him and for her, is quick and visual, so buyers '
             'find a scent without having to ask.'),
            ('A quick checkout',
             'A short, dynamic checkout that turns interest into a paid order in a few taps.'),
            ('Automated order management',
             'Orders are recorded and processed automatically, so nothing depends on a chat thread.'),
            ('CRM integration',
             'Customer details and purchases flow into a CRM, giving the brand what it needs to bring customers '
             'back.'),
        ],
        'impact': (
            '- **17% more sales.**\n'
            '- **More repeat customers,** as casual followers became regular buyers.\n'
            '- **Orders no longer get lost** in message threads.\n'
            '- **Less manual work** for the team on every order.'
        ),
    },

    'quatch': {
        'gist': (
            'The old site didn’t feel premium, browsing was confusing and checkout took too many steps.',
            'With Quatch’s design team: a luxury design, clearer navigation, a shorter checkout, recommendations and '
            'secure multi-currency payments.',
            'A store that matches the brand, better engagement, smoother purchases and zero downtime on launch day.',
        ),
        'about': (
            'Quatch is a luxury watch brand rooted in Vietnam’s cultural heritage, known for elegance and exclusivity. '
            'Its customers expect the online experience to feel as refined as the watches themselves.\n\n'
            'To protect and raise its premium status, Quatch wanted a store that reflects the brand and makes buying a '
            'watch online a pleasure.'
        ),
        'challenge': (
            'The existing website fell short of the brand:\n\n'
            '- **An inconsistent brand experience.** The site lacked the premium look and cohesive design of Quatch’s '
            'identity.\n'
            '- **Unintuitive navigation** made the collection hard to explore.\n'
            '- **A cumbersome checkout** with too many steps.\n'
            '- **Limited e-commerce features** for customers used to luxury retail.'
        ),
        'built': 'We worked closely with Quatch’s design team on a store that feels premium and is easy to buy from.',
        'features': [
            ('A premium design',
             'High-quality imagery, refined typography and a harmonious color palette, with every element true to '
             'Quatch’s identity and the feel of its physical stores.'),
            ('Navigation built around the collection',
             'A clearer layout lets customers explore the collections and find the watch they want without effort.'),
            ('A shorter checkout',
             'Fewer steps from choosing a watch to completing the purchase.'),
            ('Recommendations and curated collections',
             'Personalized product recommendations and curated collections for luxury shoppers.'),
            ('Secure, multi-currency payments',
             'Secure payment gateways with multi-currency checkout and real-time inventory updates, so customers buy '
             'with confidence.'),
        ],
        'impact': (
            '- **A refined brand image** that matches Quatch’s luxury positioning.\n'
            '- **Better engagement,** with customers exploring more of the collection.\n'
            '- **Smoother purchases** thanks to the shorter checkout.\n'
            '- **Zero downtime at launch,** with the platform handling high launch-day traffic.'
        ),
    },

    'indies': {
        'gist': (
            'Volunteers caring for street dogs had no way to find dogs, track feeding and medical care, or coordinate '
            'with each other.',
            'With a partner company: an app and website with NFC tags on collars, dog and volunteer profiles, and '
            'self-help groups with messaging.',
            'Volunteers find dogs faster, feeding and care stay on schedule, and the network coordinates in one place.',
        ),
        'tools': 'NFC tags · Mobile app · Website',
        'about': (
            'Indies is an initiative of the NGO Sare Jahan Se Acha to improve the lives of street dogs and support the '
            'volunteers who look after them. Volunteers feed the dogs, take them for treatment and keep an eye on '
            'their health.\n\n'
            'We built the platform together with a partner development company.'
        ),
        'challenge': (
            'Caring for street dogs at scale is a coordination problem. The platform had to:\n\n'
            '- **Track each dog’s location,** so volunteers can find them for feeding and treatment.\n'
            '- **Keep a profile for every dog,** with medical records and feeding schedules.\n'
            '- **Help volunteers coordinate,** manage their activities and form self-help groups.\n'
            '- **Manage volunteer profiles,** so the NGO knows who is doing what.'
        ),
        'built': (
            'Together with our partner, we built a mobile app and a website that give every dog and every volunteer a '
            'profile, connected by NFC.'
        ),
        'features': [
            ('NFC tags on collars',
             'Each dog wears a collar with an NFC chip. Volunteers see a dog’s coordinates on the platform, find '
             'dogs that need feeding and reach those that need medical attention.'),
            ('A profile for every dog',
             'Vaccination history, health status, treatment schedules and feeding schedules in one place.'),
            ('Volunteer profiles',
             'Volunteers create profiles, track their activities and manage their involvement.'),
            ('Self-help groups and messaging',
             'Volunteers create and join self-help groups, with built-in messaging and notifications to coordinate '
             'care.'),
        ],
        'impact': (
            '- **Better care for dogs,** with feeding and treatment happening on time.\n'
            '- **Easier coordination** between volunteers through groups and notifications.\n'
            '- **One system** for dog and volunteer profiles, medical records and feeding schedules.\n'
            '- **A stronger volunteer community** around the NGO’s work.'
        ),
    },

    'temple-qr-passes': {
        'gist': (
            'Passes were checked by hand at the entrance: slow, error-prone and frustrating at busy events.',
            'QR passes issued online, scanning at the gate by scanner or phone, and a back end that blocks duplicate '
            'entries.',
            'Faster entry, no verification errors and a clear record of passes issued and used.',
        ),
        'tools': 'QR codes · Hardware and mobile scanners',
        'about': (
            'Our client is a temple that issues passes for visitors to attend its events and ceremonies. On busy days, '
            'many visitors arrive in a short window, and every pass has to be checked.'
        ),
        'challenge': (
            'The existing process relied on people checking passes at the gate:\n\n'
            '- **Manual verification** was slow and prone to errors.\n'
            '- **Distributing and checking passes** took effort and caused delays.\n'
            '- **Visitors waited** at exactly the moments the temple wanted entry to feel calm and welcoming.'
        ),
        'built': (
            'We built a QR pass system that covers the whole journey, from issuing a pass online to checking it at '
            'the gate.'
        ),
        'features': [
            ('QR passes',
             'Each pass carries a unique QR code with the visitor’s name and age and the event’s date, time and '
             'details.'),
            ('Passes issued online',
             'Visitors get their passes through the temple’s website or app, by email or in the app.'),
            ('Scanning at the gate',
             'Staff scan passes with a hardware scanner or a phone, and the pass details appear instantly, so checking '
             'a pass is quick.'),
            ('Back-end management',
             'The temple tracks every pass issued, checks each scan against the issued passes and blocks duplicate '
             'entries.'),
        ],
        'how': {'title': 'How it works', 'text': (
            '- A visitor gets a pass online, by email or in the app.\n'
            '- At the gate, staff scan the QR code.\n'
            '- The system shows the visitor and event details and confirms the pass hasn’t been used.\n'
            '- The visitor walks in, and the entry is recorded.'
        )},
        'impact': (
            '- **Faster entry** for visitors at events.\n'
            '- **No manual verification errors,** and no duplicate entries.\n'
            '- **Better pass management,** with a clear record of passes issued and used.\n'
            '- **Less admin** for temple staff.'
        ),
    },

    'mohur': {
        'gist': (
            'As the platform grew, matching investors with the right startups by hand became slow and inconsistent.',
            'A machine-learning recommendation engine that suggests startups to investors, and investors to startups, '
            'and keeps learning.',
            'More relevant matches, more engagement and a matching process that scales with the platform.',
        ),
        'tools': 'Machine learning · Recommendation models',
        'about': (
            'Mohur is a platform that connects investors with startups looking for funding. By bringing both sides '
            'into one place, it makes it easier for startups to raise money and for investors to find promising '
            'companies.'
        ),
        'challenge': (
            'Matching by hand worked while the platform was small. With growth, it didn’t:\n\n'
            '- **A diverse pool of startups** across sectors and stages.\n'
            '- **Investors with different interests,** investment sizes and track records.\n'
            '- **Manual matching was slow and inconsistent,** and good matches were easy to miss.\n\n'
            'Mohur needed a system that reads investor profiles, past investments and current interests, and suggests '
            'the most relevant matches automatically.'
        ),
        'built': 'We built an AI/ML recommendation system on Mohur’s own data.',
        'features': [
            ('Data collection and analysis',
             'We brought together historical investment data, investor profiles and startup information from the '
             'platform, the foundation for training the models.'),
            ('Machine-learning models',
             'Models analyze investment patterns and current interests, weighing industry preference, investment size '
             'and growth potential to predict good matches.'),
            ('Recommendations in both directions',
             'Investors see startups that match their history and interests; startups see the investors most likely '
             'to be interested in their sector and stage.'),
            ('Continuous learning',
             'As more data comes in, the models refine their predictions and become more accurate over time.'),
        ],
        'impact': (
            '- **More relevant matches** between investors and startups.\n'
            '- **Higher engagement,** with recommendations personal to each user.\n'
            '- **Matching that scales** as the number of users grows.\n'
            '- **More value from the platform** for both sides.'
        ),
    },

    'job-post-scoring': {
        'gist': (
            'Job post quality varied widely, and the platform’s own AI model needed an objective quality signal.',
            'A scoring system that rates every post on quality, relevance, completeness and industry norms, feeding '
            'the AI model and employers’ dashboards.',
            'Better posts, listings improved automatically and jobs that reach more qualified candidates.',
        ),
        'about': (
            'Our client runs a job posting website that connects employers with job seekers. Listing quality matters '
            'to both sides: a clear, complete post attracts better candidates, and better listings make the site more '
            'useful to job seekers.\n\n'
            'The client already used an AI/ML model to enrich job post content, and wanted to give it a better input.'
        ),
        'challenge': (
            'The client needed an objective way to judge job posts:\n\n'
            '- **Quality varied widely,** from detailed descriptions to a few lines.\n'
            '- **The AI model needed a numerical signal** to know which posts to improve.\n'
            '- **Employers had no feedback** on how good their posts were.\n'
            '- **Scoring had to fit the existing AI/ML process** without disrupting it.'
        ),
        'built': (
            'We designed and implemented a job post scoring system that plugs into the client’s existing website and '
            'model.'
        ),
        'features': [
            ('A score built on clear criteria',
             'Each post is rated on description quality (clarity, detail and completeness), keyword relevance, '
             'completeness of information such as responsibilities, qualifications and company details, and '
             'alignment with industry norms.'),
            ('Integration with the AI/ML model',
             'Scores pass straight into the client’s existing model, which uses them to enrich and optimize the post '
             'content.'),
            ('Feedback for employers',
             'Employers see each post’s score in their dashboard, with recommendations on how to improve it.'),
        ],
        'impact': (
            '- **Better job posts,** as employers improve listings against clear criteria.\n'
            '- **Content optimized automatically** by the AI model, using the scores.\n'
            '- **More visible listings** that attract a larger pool of qualified candidates.\n'
            '- **A more engaging experience** for employers, who can see how their posts rate.'
        ),
    },

    'devdoot': {
        'gist': (
            'Lockdowns broke the usual ways of distributing aid: donors couldn’t reach people in need, and requests '
            'went unanswered.',
            'A donation platform with simple forms, admin verification, automatic sharing on Telegram and Facebook, '
            'and privacy-preserving matching.',
            'More than 1,000 people received verified help, from laptops and phones to food and essentials.',
        ),
        'tools': 'Web platform · Telegram · Facebook',
        'about': (
            'Devdoot was launched in 2021, during the COVID-19 pandemic, by the NGO Sare Jahan Se Acha. Its purpose '
            'was simple: connect people who wanted to donate with people who urgently needed help.\n\n'
            'Many individuals and families faced shortages of basic necessities, while traditional aid channels were '
            'overwhelmed.'
        ),
        'challenge': (
            'During the lockdowns, the gap between donors and recipients grew:\n\n'
            '- **Traditional aid distribution was overwhelmed.**\n'
            '- **Lockdowns and social distancing** made it hard for donors and recipients to connect.\n'
            '- **Requests needed checking,** so donations reached genuine needs.\n'
            '- **Offers needed reach,** so they found the right people quickly.'
        ),
        'built': 'We built Devdoot as a web platform that handles the matching, the checking and the outreach.',
        'features': [
            ('Simple forms for both sides',
             'Donors offer items such as laptops, mobile phones, stationery or food; recipients describe what they '
             'need. Both use short forms with OTP verification.'),
            ('Admin verification',
             'The NGO’s admin team reviews every submission, and only verified offers and requests appear on the '
             'site.'),
            ('Automatic sharing on social media',
             'Verified posts are shared on Telegram and Facebook, extending their reach far beyond the website.'),
            ('Privacy-preserving matching',
             'Donors and recipients are matched without exposing personal details publicly.'),
        ],
        'how': {'title': 'How it works', 'text': (
            '- A donor or recipient fills in a form on the website.\n'
            '- The admin team verifies the submission.\n'
            '- The verified offer or request is published on the site and shared on Telegram and Facebook.\n'
            '- Donors and recipients connect, and the item reaches the person who needs it.'
        )},
        'impact': (
            '- **More than 1,000 people** received verified help.\n'
            '- **Donations ranged** from laptops and phones to paper, pens and food.\n'
            '- **A structured, trusted way** for people to help their communities during one of the hardest periods '
            'in recent memory.\n\n'
            'Devdoot showed how a simple, well-run platform can turn goodwill into help that actually arrives.'
        ),
    },

    'secure-field-data-capture': {
        'gist': (
            'Officers needed a portable tool that works on almost any computer, runs without user input and keeps '
            'captured data secure.',
            'A customized operating system on a bootable pen drive that captures data automatically, with viewing tools '
            'and encryption.',
            'Quick data capture in the field without bulky equipment, with every capture encrypted and intact.',
        ),
        'tools': 'Custom bootable OS · Encryption',
        'about': (
            'Our client is a law enforcement agency that collects data from electronic devices such as laptops and PCs '
            'during field operations. The work has to be quick, consistent and secure, often where specialist '
            'equipment isn’t practical.'
        ),
        'challenge': (
            'The agency needed a field tool that met four requirements at once:\n\n'
            '- **Portability.** Easy to carry and deploy anywhere.\n'
            '- **Automation.** Runs on its own once connected, without user intervention.\n'
            '- **Data security.** Captured data must stay confidential and intact.\n'
            '- **Compatibility.** Works across many devices and operating systems.'
        ),
        'built': 'We built a bootable mechanism on a pen drive: a customized operating system that does the capture work itself.',
        'features': [
            ('A bootable OS on a pen drive',
             'A customized operating system starts from the pen drive and runs automatically when connected, with '
             'preconfigured settings and scripts so every capture is done the same way.'),
            ('Automated data capture',
             'Once running, it extracts files, logs and other relevant information from the connected device without '
             'manual steps.'),
            ('Built-in viewing tools',
             'Officers view and analyze captured data directly from the pen drive.'),
            ('Encryption and secure storage',
             'Captured data is encrypted and stored to prevent unauthorized access, tampering or accidental '
             'deletion.'),
            ('Broad compatibility',
             'Designed to work with a wide range of devices and operating systems.'),
        ],
        'impact': (
            '- **Efficient data capture** in the field.\n'
            '- **Portable,** with no bulky equipment to carry.\n'
            '- **Secure by design,** with encryption keeping data confidential and intact.\n'
            '- **Works across devices,** so one tool covers different situations.'
        ),
    },
}
