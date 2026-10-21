"""Content of the service pages, extracted from the Figma file (Dev Handoff).

Edit here, then run scripts/build_pages.py."""

SERVICES = {'services': {'process': {'heading': 'How Hekau’s IT Service Works',
                          'lead': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod '
                                  'tempor incididunt ut labore et dolore magna aliqua',
                          'steps': [{'icon': 'step_research',
                                     'title': 'Initial Analysis',
                                     'text': 'Hekau checks your business processes, finds your pain points, '
                                             'and creates a map of your business goals and needs.'},
                                    {'icon': 'step_jigsaw',
                                     'title': 'Project Planning',
                                     'text': 'Our team brainstorms exactly how, when, and by which '
                                             'technological methods your requested IT services would be '
                                             'carried out.'},
                                    {'icon': 'step_head',
                                     'title': 'Design',
                                     'text': 'We prioritize user-centric designs. Our designs are intuitive '
                                             'with clear visual directions for customers to achieve the task '
                                             'at hand.'},
                                    {'icon': 'step_design',
                                     'title': 'Develop',
                                     'text': 'From concept to code, the development phase is carried out '
                                             'with precision and care. We ramp up the security and adjust '
                                             'the IT solution based on your feedback.'},
                                    {'icon': 'step_kursor',
                                     'title': 'Testing & Deployment',
                                     'text': 'We put your applications and custom solutions through rounds '
                                             'of real-world testing before they’re activated.'},
                                    {'icon': 'step_icon2',
                                     'title': 'Monitoring & Maintenance',
                                     'text': 'You can avail post-deployment maintenance and ongoing '
                                             'support.'}]}},
 'web': {'process': {'heading': '5 Steps to a Web Application\nThat Lasts',
                     'lead': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                             'incididunt ut labore et dolore magna aliqua',
                     'steps': [{'icon': 'step_research',
                                'title': 'Research & Planning',
                                'text': 'Get on a free call where we identify your business goals, '
                                        "functional needs, and perform competitors' research. The details "
                                        'help us form a clear outline of the deliverables.'},
                               {'icon': 'step_jigsaw',
                                'title': 'UI/UX Design',
                                'text': 'We create visual guides and elements to give you an idea of the '
                                        'ultimate look of the user interface.'},
                               {'icon': 'step_head',
                                'title': 'Agile Development',
                                'text': 'Hekau developers start building your web apps from concept to code. '
                                        'Every feature is a reflection of your business needs.'},
                               {'icon': 'step_design',
                                'title': 'Testing & QA',
                                'text': 'Your custom web application goes through strict functionality and '
                                        'compatibility tests. This means we check how your web application '
                                        'performs across devices and browsers.'},
                               {'icon': 'step_kursor',
                                'title': 'Deployment & Maintenance',
                                'text': 'Once your website goes live, we keep a firm eye on the analytics if '
                                        'you desire so. Hekau also regularly updates your web app to meet '
                                        'the ever-changing business needs.'}]},
         'features': {'heading': 'Growth Partner for Startups and SMBs',
                      'cards': [{'icon': 'feat_web_1',
                                 'title': 'Scalability For Expanding Startups',
                                 'text': 'Woverload, features that don’t measure up, frustrated employees, '
                                         'and customers. Hekau’s scalable web apps automatically adjust to '
                                         'your current and future business needs. Limited scalability means '
                                         'you lose more customers.',
                                 'title_w': 200},
                                {'icon': 'feat_web_2',
                                 'title': 'Responsiveness SMBs Love',
                                 'text': 'Device and browser type affect the performance of web '
                                         'applications. Hekau gets this. Our team builds responsive web '
                                         'applications with devices and screens of all types and sizes in '
                                         'mind. This leads to minimum lag and fast-loading across all '
                                         'devices.',
                                 'title_w': 280},
                                {'icon': 'feat_web_3',
                                 'title': 'Customized Web Apps For Your Industry',
                                 'text': 'Content platforms need features such as advanced text formatting. '
                                         'Corporate web apps benefit from role-based access for improved '
                                         'security. Hekau builds custom web solutions you can use to connect '
                                         'to CRMs, manage inventory, or generate support tickets.',
                                 'title_w': 300}]},
         'hero': {'icons': [('kotlin', 'Kotlin'),
                            ('flutter', 'Flutter'),
                            ('react', 'React'),
                            ('swift', 'Swift'),
                            ('firebase', 'Database')],
                  'title': 'Web Application Development',
                  'sub': 'Adjusts to Your Team',
                  'text': 'Hekau avoids this by using 12+ years of experience and the latest technologies to '
                          'create unique. Poor mobile app development results in budget waste, bugs, and '
                          'battery drain.'}},
 'mobileapp': {'process': {'heading': 'Mobile App Development Process You Can Trust',
                           'lead': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod '
                                   'tempor incididunt ut labore et dolore magna aliqua',
                           'steps': [{'icon': 'step_research',
                                      'title': 'Establish App Concept',
                                      'text': 'How does your app benefit your customers? Your target '
                                              'audience and their needs decide your app’s core features and '
                                              'user journeys.'},
                                     {'icon': 'step_jigsaw',
                                      'title': 'Design Your App',
                                      'text': 'Hekau builds a blueprint of the screen layout and user flows. '
                                              'It’s the phase where we form a style guide for the colors, '
                                              'typography, and UI elements to build consistency. The goal is '
                                              'to design a user interface that both Android and iOS users '
                                              'will like.'},
                                     {'icon': 'step_head',
                                      'title': 'Development',
                                      'text': 'We build a structure we can refer to for the final app and '
                                              'create elements we can use on both iOS and Android. Next, '
                                              'it’s a matter of implementing core features and connecting to '
                                              'the important data sources.'},
                                     {'icon': 'step_design',
                                      'title': 'Testing & Optimization',
                                      'text': 'We test your app’s performance on multiple screen sizes and '
                                              'devices. The intention is to check if the app is responsive '
                                              'and fast on both iOS and Android. Hekau lets your target '
                                              'audience test the app to gather real user opinions and refine '
                                              'it further.'},
                                     {'icon': 'step_kursor',
                                      'title': 'Prepare For Deployment',
                                      'text': 'We’re close to launching the app. Let’s set up your developer '
                                              'account and app store assets to help with the eventual '
                                              'marketing.'},
                                     {'icon': 'step_kursor',
                                      'title': 'Launch & Monitor',
                                      'text': 'Once your app is live on the app stores, we monitor the '
                                              'response to the app upon your request. The engagement metrics '
                                              'and reviews tell us if there is room for improvement.'}]},
               'features': {'heading': 'Own Apps You’re Proud Of',
                            'cards': [{'icon': 'feat_mobileapp_1',
                                       'title': 'Tailored Approach',
                                       'text': 'You control our designs. We carefully analyze your business '
                                               'needs, future goals, and your target audience’s desires. '
                                               'Hekau’s custom mobile apps are a reflection of your vision.',
                                       'title_w': 200},
                                      {'icon': 'feat_mobileapp_2',
                                       'title': 'Cost-Effective Solution',
                                       'text': 'Are you a startup owner? Or a small business owner? We '
                                               'believe the size of your company shouldn’t stop you from '
                                               'commissioning high-quality apps. That’s why we offer free '
                                               'consultation and mobile app development solutions that let '
                                               'you stay within budget.',
                                       'title_w': 280},
                                      {'icon': 'feat_mobileapp_3',
                                       'title': 'Latest Technology',
                                       'text': 'As cross-platform specialists, we’re always updated with the '
                                               'latest technology. Despite the fast update cycle of mobile '
                                               'technology, we make sure your app stays fresh.',
                                       'title_w': 300}]},
               'hero': {'icons_m': [('kotlin', 'Kotlin'), ('flutter', 'Flutter'), ('react', 'React'), ('swift', 'Swift'), ('firebase', 'Database')],
                 'label': 'Services',
                        'title': 'Mobile Application Development',
                        'sub': 'That Turns Your Ideas Into Reality.',
                        'text': 'Hekau avoids this by using 12+ years of experience and the latest '
                                'technologies to create unique, feature-packed custom mobile app designs. '
                                'Build apps your customers like using, whether they are iOS or Android '
                                'users.'}},
 'ux': {'process': {'heading': 'Your UI/UX Experience Guide',
                    'lead': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                            'incididunt ut labore et dolore magna aliqua',
                    'steps': [{'icon': 'step_research',
                               'title': 'User Research',
                               'text': '30% of UI/UX design is research. Hekau interviews potential users, '
                                       'creates empathy maps, and develops user journeys to turn the end '
                                       'product into an attention-grabbing success.'},
                              {'icon': 'step_jigsaw',
                               'title': 'Design Workshops',
                               'text': 'Creativity runs free as Hekau’s design team brainstorms intuitive '
                                       'design solutions, builds user flow, and freestyles sketches. All the '
                                       'while, business objectives, project goals, and end user needs guide '
                                       'every decision.'},
                              {'icon': 'step_head',
                               'title': 'UX Optimization',
                               'text': 'User experience strategy hinges on one key factor — usability. We '
                                       'make sure it takes users the fewest steps and the shortest time '
                                       'possible to achieve their goals.'},
                              {'icon': 'step_design',
                               'title': 'UI Design',
                               'text': 'The UX shapes the direction of the UI. We create visually '
                                       'breathtaking, responsive UI designs with organized interactive '
                                       'buttons and accessible elements.'},
                              {'icon': 'step_kursor',
                               'title': 'Prototyping',
                               'text': 'Test a blueprint of the navigation experience and responsive UI '
                                       'design. We build on your feedback, reducing the chances of rework '
                                       'later and eliminating unnecessary development costs.'},
                              {'icon': 'step_icon2',
                               'title': 'Implementation & Testing',
                               'text': 'Hekau’s team uses the latest frameworks and technology to build the '
                                       'user interface. We test multiple versions — for iOS and Android — '
                                       'until the usability passes every benchmark.'}]},
        'features': {'heading': 'UI/UX Design to Convert Users Into Loyal Customers',
                     'cards': [{'icon': 'feat_ux_1',
                                'title': 'Attract and Retain Users',
                                'text': 'Good UI/UX design is code for a low bounce rate, increased brand '
                                        'loyalty, and returning customers. Your users know your product can '
                                        'help them achieve their goals, so why wouldn’t they come to you?',
                                'title_w': 200},
                               {'icon': 'feat_ux_2',
                                'title': 'Reduce Costs',
                                'text': 'Engaging UX design has an ROI of 100%. When you invest in the UI/UX '
                                        'design upfront, you avoid redesign costs and make sure your product '
                                        'grows with the customer base.',
                                'title_w': 280},
                               {'icon': 'feat_ux_3',
                                'title': 'Become Industry Leaders',
                                'text': '89% of users go to a competitor after a poor user experience. But '
                                        'the opposite can be true. When your UI/UX design outshines your '
                                        'competitors, users will turn to you after a subpar experience '
                                        'elsewhere.',
                                'title_w': 300}]},
        'hero': {'icons': [('kotlin', 'Kotlin'),
                           ('flutter', 'Flutter'),
                           ('react', 'React'),
                           ('swift', 'Swift'),
                           ('firebase', 'Database')],
                 'title': 'UX/UI Design',
                 'sub': 'Strong Brand, Even Better Design',
                 'text': 'Hekau builds brand loyalty by creating a consistent, accessible, and intuitive '
                         'design. Our designs reflect the quality of the work you’re willing to do for your '
                         'customers.'}},
 'cloud': {'process': {'heading': 'You Achieve Your Dreams, We Provide The Support',
                       'lead': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod '
                               'tempor incididunt ut labore et dolore magna aliqua',
                       'steps': [{'icon': 'step_research',
                                  'title': 'Cloud Assessment',
                                  'text': 'AWS provides scalability. Azure excels in enterprise integration. '
                                          'Hekau assesses the best cloud solution for your business based on '
                                          'pricing, security, features, and storage.'},
                                 {'icon': 'step_jigsaw',
                                  'title': 'Strategy & Planning',
                                  'text': 'Your business goals are our priority. We will plan a migration '
                                          'strategy that doesn’t disrupt your business processes by '
                                          'selecting the most compatible architecture and creating a phased '
                                          'deployment plan.'},
                                 {'icon': 'step_head',
                                  'title': 'Migration & Integration',
                                  'text': 'In this execution phase, Hekau will move and integrate your data, '
                                          'applications, and IT workloads.'},
                                 {'icon': 'step_design',
                                  'title': 'Security Implementation',
                                  'text': 'Security implementation is a critical part of cloud management. '
                                          'We enable security features to protect your data and '
                                          'infrastructure from malicious traffic. Our approach strictly '
                                          'follows compliance regulations based on region and industry.'},
                                 {'icon': 'step_kursor',
                                  'title': 'Ongoing Management & Support',
                                  'text': 'Hekau’s managed cloud services extend to periodic maintenance and '
                                          'ongoing support. Focus on your business goals while we keep your '
                                          'system performance at its best.'}]},
           'features': {'heading': 'Growth Partner for Startups and SMBs',
                        'cards': [{'icon': 'feat_cloud_1',
                                   'title': 'Launch Your Projects Faster',
                                   'text': 'Businesses using cloud solutions tend to launch projects faster. '
                                           'By handling the technicalities, we free up your time so you can '
                                           'focus on actual project execution.',
                                   'title_w': 280},
                                  {'icon': 'feat_cloud_2',
                                   'title': 'Low Infrastructure Cost',
                                   'text': 'Cloud solutions reduce the cost of buying and running physical '
                                           'servers. Pay only for what you need. Our efficient analytical '
                                           'optimization will keep your cloud servers running smoothly, even '
                                           'with minimal resource allocation.',
                                   'title_w': 280},
                                  {'icon': 'feat_cloud_3',
                                   'title': 'Scalability As You Need',
                                   'text': 'Websites and apps experience ups and downs in traffic during '
                                           'holidays and special events. Hekau scales your system to '
                                           'automatically adjust to the high data volumes and traffic spikes '
                                           'on multiple device types.',
                                   'title_w': 300}]},
           'hero': {'icons': [('kotlin', 'Kotlin'),
                              ('flutter', 'Flutter'),
                              ('react', 'React'),
                              ('swift', 'Swift'),
                              ('firebase', 'Database')],
                    'title': 'Cloud-Managed Services',
                    'sub': 'Power Your Business',
                    'text': '94% of major companies worldwide use cloud services in some form. Cloud '
                            'solutions, when tailored to your exact business needs, can have massive '
                            'advantages.'}},
 'bpa': {'process': {'heading': 'Business Process Automation That Molds to Your Business',
                     'lead': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                             'incididunt ut labore et dolore magna aliqua',
                     'steps': [{'icon': 'step_research',
                                'title': 'Process Analysis',
                                'text': 'We identify your existing workflows and how your processes connect '
                                        'to each other. We find areas slowing you down and analyze their '
                                        'potential for automation.'},
                               {'icon': 'step_jigsaw',
                                'title': 'Automation Strategy',
                                'text': 'Our automation strategy states which processes to transform via '
                                        'which tools and the benefits the automation will bring. Ultimately, '
                                        'the benefits should overpower the cost in the long run.'},
                               {'icon': 'step_head',
                                'title': 'Workflow Design',
                                'text': 'We will create a map of the automation workflow, including user '
                                        'needs, data sources, task sequence, responsibilities, and the '
                                        'conditions under which tasks get approval.'},
                               {'icon': 'step_design',
                                'title': 'Integration & Implementation',
                                'text': 'We build and activate integration solutions that transfer the data '
                                        'wherever and whenever it is needed — often at the same time.'},
                               {'icon': 'step_kursor',
                                'title': 'Monitoring & Optimization',
                                'text': 'Your automations will go through multiple flow tests and '
                                        'monitoring. They will only go live when they work exactly as'}]},
         'features': {'heading': 'Business Process Automation Startups & SMBs Can Rely On',
                      'cards': [{'icon': 'feat_bpa_1',
                                 'title': 'Get Rid of Repetitive Tasks',
                                 'text': 'If you own a startup, the small, boring tasks end up taking 61% of '
                                         'the day. Often, the boredom is what leads to the errors. Hekau can '
                                         'prevent you from turning into a data-copying machine by creating '
                                         'auto-running shortcuts for long-winded tasks.',
                                 'title_w': 280},
                                {'icon': 'feat_bpa_2',
                                 'title': 'Surge in Profit',
                                 'text': 'Your customers are up at all hours of the night researching your '
                                         'business. But when they reach out and get no reply, they’re quick '
                                         'to switch to someone else. Automation workflows keep your '
                                         'customers hooked by scheduling meetings and onboarding clients '
                                         'while you sleep.',
                                 'title_w': 280},
                                {'icon': 'feat_bpa_3',
                                 'title': 'Automatic Assistance',
                                 'text': 'Accumulating invoices, unprocessed orders, and a slow employee '
                                         'onboarding process are a few of the challenges startups face. But '
                                         "it doesn't have to be that way. With Hekau’s automation solutions, "
                                         'your bills get paid, customers receive timely delivery, and new '
                                         'employees feel supported at work.',
                                 'title_w': 300}]},
         'hero': {'icons': [('kotlin', 'Kotlin'),
                            ('flutter', 'Flutter'),
                            ('react', 'React'),
                            ('swift', 'Swift'),
                            ('firebase', 'Database')],
                  'title': 'Business Process Automation',
                  'sub': 'So You Can Focus On Your Dreams.',
                  'text': 'With Hekau’s automation strategy, you don’t do any work you don’t want to. We '
                          'keep your business connected, smooth running, and fast while you exercise your '
                          'creative energy.'}},
 'ai': {'process': {'heading': 'Your Personal AI Assistant Trains On Your Business Strategy',
                    'lead': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                            'incididunt ut labore et dolore magna aliqua',
                    'steps': [{'icon': 'step_research',
                               'title': 'AI Opportunity Discovery',
                               'text': 'We assess your business objectives and identify where AI can reduce '
                                       'costs, improves efficiency, and aligns with your goals.ange.'},
                              {'icon': 'step_jigsaw',
                               'title': 'Custom AI Model Development',
                               'text': 'Generic AI models don’t understand your business goals, customer '
                                       'needs, or industry. We develop custom models highly tuned to your '
                                       'business.'},
                              {'icon': 'step_head',
                               'title': 'AI Model Training',
                               'text': 'As your AI model trains on your business data, Hekau tests it '
                                       'against real-world scenarios.'},
                              {'icon': 'step_design',
                               'title': 'AI Implementation & Integration',
                               'text': 'We start activating the AI model on your website, mobile app, CRM, '
                                       'and other systems you want it on. Hekau integrates AI with minimal '
                                       'disruption to your existing processes.'},
                              {'icon': 'step_kursor',
                               'title': 'Monitoring & Refinement',
                               'text': 'With analytics and user reviews, we get a clear picture of how the '
                                       'AI solution is performing in the real world.'}]},
        'features': {'heading': 'Custom AI Solutions Startups and SMBs Can Use',
                     'cards': [{'icon': 'feat_ai_1',
                                'title': 'Increase Customer Engagement',
                                'text': 'AI solutions for business go beyond the generic chatbots. Custom AI '
                                        'solutions can adapt to customer queries and offer intelligent '
                                        'answers and recommendations.',
                                'title_w': 280},
                               {'icon': 'feat_ai_2',
                                'title': 'Get a Digital Assistant',
                                'text': 'AI solutions learn from your habits. Use them to automate all the '
                                        'small and big stuff, from emails to scheduling appointments.',
                                'title_w': 280},
                               {'icon': 'feat_ai_3',
                                'title': 'Guide Your Customers',
                                'text': 'When fed the right data, AI solutions can act as excellent '
                                        'predictive tools. With Hekau’s artificial intelligence '
                                        'implementation, you can predict what your customers will like and '
                                        'suggest accordingly.',
                                'title_w': 300}]},
        'hero': {'icons': [('ai_0', 'AI', 40), ('ai_1', 'AI assistant'), ('ai_2', 'Automation'), ('ai_3', 'Workflows')],
                 'title': 'AI Solutions',
                 'sub': 'Cut Your Business Costs',
                 'text': 'Hekau builds AI solutions for your business that won’t break the bank, boost '
                         'customer loyalty, and give you a competitive edge.'}}}


# --------------------------------------------------------------------------------------------
# About Us (Figma Dev Handoff "About Us Page" 205:20402, mobile 223:12658)
# --------------------------------------------------------------------------------------------

ABOUT = {
    'hero': {
        'badge': 'Why Hekau?',
        'title': 'Hekau is built on a\nsimple idea:',
        'text': 'Professional-grade technology should be accessible to everyone.\n\n'
                'Small businesses and startups shouldn’t have to spend all their time fixing operational '
                'inefficiencies. Not when the time can be delegated to optimizing products and serving customers.\n\n'
                'At Hekau, we build custom, innovative, and industry-specific solutions molded to your business '
                'needs. Our solutions strike a unique balance of creativity, functionality, and cost-effectiveness.',
    },
    'story': {
        'title': 'This straightforward motto is what led to the birth of Hekau in 2021. Inspired by the Egyptian '
                 'word Heka or Hekau, our name directly translates to “magic.”',
        'text': 'Because Hekau may have been a reality for only a couple of years, but the company is run by a '
                'passionate team of people with over 12 years of experience.',
        'button': ('Schedule a Free Call', '/contactus'),
    },
    'team': {
        'title': 'Our Dynamic Co-Founders',
        'members': [
            {'name': 'Santosh Yadav', 'role': 'Co-Founder', 'photo': 'about/founder_santosh.webp',
             'bio': 'As a co-founder, Santosh oversees the business side of Hekau, all the while providing support '
                    'to the company using his experience in mechanical engineering. His years of involvement in '
                    'sales and customer service grant him a unique perspective on the needs of Hekau’s clients.'},
            {'name': 'Anu Unni', 'role': 'Co-Founder', 'photo': 'about/founder_anu.webp',
             'bio': 'After earning his engineering degree in 2014, Anu honed his skills by collaborating with '
                    'international clients until he became a co-founder of Hekau in 2021. With over a decade of '
                    'experience in IT, Anu has taken Hekau to new heights, overseeing critical projects to this day.'},
        ],
    },
    'vision': {
        # Figma repeats "Our Dynamic Co-Founders" above this section
        'title': 'Our Vision & Mission',
        'items': [
            {'icon': 'vision', 'title': 'Our Vision',
             'text': 'To be the #1 technology partner for startups and small businesses through innovative, '
                     'tailored solutions, dedicated support, and exceptional service.'},
            {'icon': 'mission', 'title': 'Our Mission',
             'text': 'To empower emerging businesses to reach new heights by building enterprise-grade technology '
                     'that enables them to compete with industry giants.'},
        ],
    },
    'values': {
        'heading': 'Own Apps You’re Proud Of',
        'cards': [
            {'icon': 'value_innovation', 'title': 'Innovation',
             'text': 'We are committed to delivering cutting-edge technology solutions with thought and care. By '
                     'continuously pushing creative boundaries, we develop unique, inspiring, and original '
                     'innovations while maintaining peak efficiency.'},
            {'icon': 'value_flexibility', 'title': 'Flexibility',
             'text': 'Our clients deserve access to professional-grade technology whenever and wherever they need '
                     'it to achieve their ambitions.'},
            {'icon': 'value_empowerment', 'title': 'Empowerment',
             'text': 'Our clients deserve access to professional-grade technology whenever and wherever they need '
                     'it to achieve their ambitions.'},
            {'icon': 'value_innovation', 'title': 'Partnership',
             'text': 'We aren’t here to conduct mere business. Our tailored technological solutions aim to be your '
                     'launchpad for unprecedented success.'},
            {'icon': 'value_flexibility', 'title': 'Affordability',
             'text': 'We’re committed to transparent and honest pricing. With our state-of-the-art tech solutions, '
                     'the benefits will always outweigh the cost.'},
        ],
    },
}


# --------------------------------------------------------------------------------------------
# Projects (Figma "Project Page" 225:38685, mobile 225:38909) and the case study page
# ("Individual Project Page" 199:11928, mobile 223:17200)
# --------------------------------------------------------------------------------------------

LOREM = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore '
         'et dolore magna aliqua Lorem ipsum dolor.')

WORK_FILTERS = [
    ('web', 'Web App'), ('mobile', 'Mobile App'), ('ux', 'UX/UI Design'), ('cloud', 'Cloud-Managed Services'),
    ('bpa', 'Business Process Automation'), ('ai', 'AI Solutions'),
]

WORK = {
    'hero': {
        'badge': 'Work',
        'title': 'Showcasing Our Expertise Through Our Impactful Projects',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                'labore et dolore magna aliqua Lorem ipsum dolor.',
    },
    'list_title': 'Showcasing Our Expertise Through Our Impactful Projects',
    # One sample card per category (Figma: six identical placeholder cards)
    'projects': [
        {'category': 'web', 'title': 'Bringing Order to Speed: Web Development for The Arc', 'url': '/projects/the-arc',
         'image': 'projects/the_arc.webp', 'tags': ['Web App', 'Media', 'Startup'],
         'text': 'A shared design and development foundation that brought consistency to a fast-growing new-media platform.'},
    ] + [
        {'category': key, 'title': 'Showcasing Our Expertise Through Our Impactful Projects', 'url': '/projects',
         'image': 'projects/placeholder.webp', 'tags': ['Work', 'Work', 'Work'], 'text': LOREM}
        for key in ('mobile', 'ux', 'cloud', 'bpa', 'ai')
    ],
}

CASE = {
    'title': 'Bringing Order to Speed: Web Development for The Arc',
    'image': 'projects/the_arc.webp',
    'meta': [('Project', 'Web Application Development'), ('Client Name', 'The Arc : copy, copy, copy'),
             ('Team Members', 'The Arc, copy, copy copu')],
    'eyebrow': 'Project Details',
    'intro': [
        {'title': 'About the Client',
         'text': 'The Arc, a seed-funded new-media startup, has its finger on the pulse of India’s high-growth '
                 'companies. It delivers sharp, objective and research-backed news reports and analysis that resonate '
                 'with both general readers and corporate executives.We supported the redesign of The Arc’s platform, '
                 'working closely with its founders and developers. A key area of focus was settling on a common '
                 'design language, which served as the foundation for collaboration and faster results.'},
        {'title': 'The Brief',
         'text': 'We built the MVP for The Arc, but as the product grew, so did the chaos. Features were shipping '
                 'fast, but not always in sync. Designers, developers, and founders found themselves speaking '
                 'slightly different design languages—which made decisions slower and development heavier than it '
                 'needed to be.\n\nThere was a clear need for a shared foundation. Something that could bring '
                 'consistency, reduce back-and-forth, and support the pace of growth.'},
    ],
    'outro': [
        {'title': 'The Process',
         'text': 'The Arc, a seed-funded new-media startup, has its finger on the pulse of India’s high-growth '
                 'companies. It delivers sharp, objective and research-backed news reports and analysis that resonate '
                 'with both general readers and corporate executives.We supported the redesign of The Arc’s platform, '
                 'working closely with its founders and developers. A key area of focus was settling on a common '
                 'design language, which served as the foundation for collaboration and faster results.'},
        {'title': 'The Impact',
         'text': 'We built the MVP for The Arc, but as the product grew, so did the chaos. Features were shipping '
                 'fast, but not always in sync. Designers, developers, and founders found themselves speaking '
                 'slightly different design languages—which made decisions slower and development heavier than it '
                 'needed to be.\n\nThere was a clear need for a shared foundation. Something that could bring '
                 'consistency, reduce back-and-forth, and support the pace of growth.'},
    ],
    'caption': 'There was a clear need for a shared foundation. Something that could bring consistency, reduce '
               'back-and-forth, and support the pace of growth.',
}
