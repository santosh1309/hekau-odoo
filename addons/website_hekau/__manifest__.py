{
    'name': 'Hekau Website',
    'summary': 'Hekau company website built from the Figma design (palette, fonts, header, footer, pages)',
    'description': """
Implements the "Hekau WIP" Figma design on Odoo 20 Website:

* Hekau colour palette and DM Sans / Montserrat typography (also selectable in the website builder)
* Floating navigation bar, "Book a free audit" call to action and the fat footer
* Every page section is a website builder block (Blocks > Hekau): hero, partners,
  why-partner, stats, services, domains, projects, testimonials and call-to-action,
  each with its Figma desktop and mobile layout and animations
* Pages assembled from those blocks: Home, Services and the eight service pages,
  About Us, How we work, Projects and nineteen case studies, Terms and Conditions
* Contact page with an audit request form that creates a CRM lead (website_crm),
  thank-you page with the System Disconnection Checklist, privacy policy
* Blog listing (website_blog) in the Hekau design, with sample posts

Page content stays editable in the website builder, and new pages can be built by
dragging Hekau blocks.
    """,
    'version': '20.0.5.4.0',
    'category': 'Website/Website',
    'author': 'Hekau Business Solutions',
    'website': 'https://www.hekautech.com',
    'license': 'LGPL-3',
    'depends': ['website', 'website_blog', 'website_crm'],
    'data': [
        'views/layout.xml',
        # Blocks (one template per section, registered under Blocks > Hekau)
        'views/snippets/s_hk_hero.xml',
        'views/snippets/s_hk_partners.xml',
        'views/snippets/s_hk_why.xml',
        'views/snippets/s_hk_stats.xml',
        'views/snippets/s_hk_services.xml',
        'views/snippets/s_hk_domains.xml',
        'views/snippets/s_hk_projects.xml',
        'views/snippets/s_hk_testimonials.xml',
        'views/snippets/s_hk_cta.xml',
        'views/snippets/s_hk_service_hero.xml',
        'views/snippets/s_hk_highlight.xml',
        'views/snippets/s_hk_attributes.xml',
        'views/snippets/s_hk_ai_intro.xml',
        'views/snippets/s_hk_features.xml',
        'views/snippets/s_hk_process.xml',
        'views/snippets/s_hk_page_hero.xml',
        'views/snippets/s_hk_team.xml',
        'views/snippets/s_hk_vision.xml',
        'views/snippets/s_hk_project_list.xml',
        'views/snippets/s_hk_case_hero.xml',
        'views/snippets/s_hk_case_text.xml',
        'views/snippets/s_hk_case_figure.xml',
        'views/snippets/snippets.xml',
        # Pages
        'views/homepage.xml',
        'views/pages/services.xml',
        'views/pages/about.xml',
        'views/pages/projects.xml',
        'views/pages/how_we_work.xml',
        'views/pages/odoo_pages.xml',
        # Blog (website_blog) listing in the Hekau design, with sample posts
        'views/blog.xml',
        'data/blog_data.xml',
    ],
    'assets': {
        # Palette, fonts and website values must be assigned after Odoo's `!default`
        # declarations in website/static/src/scss/primary_variables.scss.
        'web._assets_primary_variables': [
            'website_hekau/static/src/scss/primary_variables.scss',
        ],
        # SCSS files of a bundle are compiled together: tokens and mixins first.
        'web.assets_frontend': [
            'website_hekau/static/src/scss/hk_tokens.scss',
            'website_hekau/static/src/scss/hekau.scss',
            'website_hekau/static/src/snippets/**/*.scss',
            'website_hekau/static/src/scss/hk_blog.scss',
            'website_hekau/static/src/js/scroll_indicator.js',
            'website_hekau/static/src/js/process.js',
            'website_hekau/static/src/js/testimonials.js',
            'website_hekau/static/src/js/project_filter.js',
            'website_hekau/static/src/js/booking.js',
            'website_hekau/static/src/js/menu_active.js',
        ],
    },
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': False,
}
