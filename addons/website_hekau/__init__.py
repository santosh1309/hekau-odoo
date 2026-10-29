from odoo.tools import BinaryBytes
from odoo.tools.misc import file_open

# Main navigation (copy deck, October 2026).
MAIN_MENU = [
    ('Services', '/services'),
    ('Projects', '/projects'),
    ('About', '/about-us'),
    ('How we work', '/how-we-work'),
    ('Blog', '/blog'),
    ('Contact us', '/contactus'),
]
# Pages Odoo owns whose content this module replaces: the floating nav bar
# sits on top of their hero, like on the module's own pages.
OVERLAY_PAGE_URLS = ['/', '/contactus', '/contactus-thank-you', '/privacy']
# Menu links of earlier versions, pointing at Home page sections.
OLD_MENU_URLS = {
    '/#services': '/services',
    '/#projects': '/projects',
    '/#why-hekau': '/about-us',
}

# Header options that are not part of the design.
VIEWS_TO_DISABLE = [
    'website.header_search_box',
    'portal.user_sign_in',
    'website.header_visibility_standard',
    # Phone number next to the menu: the bar has a "Contact us" item instead.
    'website.header_text_element',
]
VIEWS_TO_ENABLE = [
    'website.template_header_default_align_center',
    # Header stays on screen while scrolling and compacts (Figma nav state 2).
    'website.header_visibility_fixed',
]


def post_init_hook(env):
    setup_websites(env)


def apply_header_options(env):
    """Header options of the design (also applied when upgrading the module)."""
    for xmlid in VIEWS_TO_DISABLE:
        view = env.ref(xmlid, raise_if_not_found=False)
        if view:
            view.active = False
    for xmlid in VIEWS_TO_ENABLE:
        view = env.ref(xmlid, raise_if_not_found=False)
        if view:
            view.active = True


def update_menu_links(env):
    """Point the menus created by earlier versions at the new pages."""
    for old, new in OLD_MENU_URLS.items():
        env['website.menu'].search([('url', '=', old)]).write({'url': new})


def remove_duplicate_menus(env):
    """website_blog adds a "Blog" entry to every main menu: keep only one."""
    for website in env['website'].search([]):
        if not website.menu_id:
            continue
        blog_menus = website.menu_id.child_id.filtered(lambda m: (m.url or '').rstrip('/') == '/blog')
        keep = blog_menus.filtered(lambda m: m.name == 'Blog')[:1] or blog_menus[:1]
        (blog_menus - keep).unlink()


def setup_blog(env):
    """Name the default blog (website_blog's "Our blog")."""
    blog = env.ref('website_blog.blog_blog_1', raise_if_not_found=False)
    if blog and blog.name == 'Our blog':
        blog.write({'name': 'Hekau Blog', 'subtitle': 'Insights from the Hekau team.'})


def add_missing_menus(env):
    """Add the MAIN_MENU entries a website's main menu lacks and put MAIN_MENU's
    entries in its order, keeping any other entry made in the website builder."""
    for website in env['website'].search([]):
        top_menu = website.menu_id
        if not top_menu:
            continue
        for sequence, (name, url) in enumerate(MAIN_MENU, start=1):
            menu = top_menu.child_id.filtered(lambda m: (m.url or '').rstrip('/') == url)[:1]
            if menu:
                menu.sequence = sequence * 10
            else:
                env['website.menu'].create({
                    'name': name,
                    'url': url,
                    'parent_id': top_menu.id,
                    'website_id': website.id,
                    'sequence': sequence * 10,
                })


def hide_header_contact(env):
    """Turn the header text element (phone number) off, including the
    website-specific copies the website builder makes: an inactive copy hides
    the element on its website even if the generic view is active."""
    views = env['ir.ui.view'].with_context(active_test=False).search([
        ('key', '=', 'website.header_text_element')])
    views.filtered('active').write({'active': False})


def rebuild_main_menu(env):
    """Recreate every website's main menu from MAIN_MENU."""
    for website in env['website'].search([]):
        top_menu = website.menu_id
        if not top_menu:
            continue
        top_menu.child_id.unlink()
        for sequence, (name, url) in enumerate(MAIN_MENU, start=1):
            env['website.menu'].create({
                'name': name,
                'url': url,
                'parent_id': top_menu.id,
                'website_id': website.id,
                'sequence': sequence * 10,
            })


# Company details shown in the header, footer and legal pages (Odoo reads the
# header phone and the contact email from the company).
COMPANY_DETAILS = {
    'name': 'Hekau Business Solutions Private Limited',
    'phone': '+91 81497 49282',
    'email': 'admin@hekautech.com',
    'website': 'https://www.hekautech.com',
    'street': 'Vijayashree, S. No. 33/92, near MSEB Office',
    'street2': 'Katraj',
    'city': 'Pune',
    'zip': '411046',
}
# Values that Odoo or the website configurator put there: safe to replace.
PLACEHOLDERS = {'', 'My Company', 'YourCompany', 'My Website', '+1 555-555-5556', 'info@yourcompany.com',
                'http://www.example.com', 'https://www.example.com'}


def setup_company_details(env):
    """Fill the main company's contact details and name the websites "Hekau",
    without overwriting anything someone already entered."""
    company = env.ref('base.main_company', raise_if_not_found=False)
    if company:
        values = {k: v for k, v in COMPANY_DETAILS.items() if (company[k] or '') in PLACEHOLDERS}
        india = env.ref('base.in', raise_if_not_found=False)
        if india and not company.country_id:
            values['country_id'] = india.id
            maharashtra = env['res.country.state'].search([('country_id', '=', india.id), ('code', '=', 'MH')], limit=1)
            if maharashtra and not company.state_id:
                values['state_id'] = maharashtra.id
        if values:
            company.write(values)
    env['website'].search([('name', 'in', ['My Website', 'Website'])]).write({'name': 'Hekau'})


# Odoo's placeholder contact details in the header text element.
HEADER_CONTACT = [
    ('tel:+1 555-555-5556', 'tel:+918149749282'),
    ('+1 555-555-5556', '+91 81497 49282'),
    ('info@yourcompany.example.com', 'admin@hekautech.com'),
]


def fix_header_contact(env):
    """Website-specific copies of the header text element (made when header
    options are changed in the website builder) keep Odoo's placeholder phone
    and email and miss this module's override: put Hekau's details in them.
    Their link to Odoo's source file is dropped so that the stored version is
    also the one shown with --dev=xml."""
    views = env['ir.ui.view'].with_context(active_test=False).search([
        ('key', '=', 'website.header_text_element'), ('website_id', '!=', False)])
    for view in views:
        arch = view.arch_db or ''
        for old, new in HEADER_CONTACT:
            arch = arch.replace(old, new)
        values = {}
        if arch != view.arch_db:
            values['arch_db'] = arch
        if view.arch_fs and '81497 49282' in arch:
            values['arch_fs'] = False
        if values:
            view.write(values)


def set_header_overlay(env):
    env['website.page'].search([('url', 'in', OVERLAY_PAGE_URLS)]).write({'header_overlay': True})


def setup_websites(env):
    """Apply the Hekau design settings to every website.

    Safe to run again (e.g. from an Odoo shell) after creating a new website.
    """
    with file_open('website_hekau/static/src/img/logo_full.svg', 'rb') as f:
        logo = BinaryBytes(f.read(), filename='hekau_logo.svg')

    apply_header_options(env)
    hide_header_contact(env)

    for website in env['website'].search([]):
        website.write({
            'logo': logo,
            # Skip the theme configurator: it would override the Hekau palette and fonts.
            'configurator_done': True,
        })

    rebuild_main_menu(env)
    set_header_overlay(env)
    setup_company_details(env)
