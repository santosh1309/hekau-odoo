from odoo.tools import BinaryBytes
from odoo.tools.misc import file_open

# Main navigation from the Figma nav bar.
MAIN_MENU = [
    ('Services', '/services'),
    ('Portfolio', '/projects'),
    ('Blogs', '/blog'),
    ('About Us', '/about-us'),
]
# Menu links of earlier versions, pointing at Home page sections.
OLD_MENU_URLS = {
    '/#services': '/services',
    '/#projects': '/projects',
    '/#why-hekau': '/about-us',
}

# Header options that are not part of the design.
VIEWS_TO_DISABLE = [
    'website.header_search_box',
    'website.header_text_element',
    'portal.user_sign_in',
    'website.header_visibility_standard',
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
    """website_blog adds a "Blog" entry to every main menu: keep the design's "Blogs"."""
    for website in env['website'].search([]):
        if not website.menu_id:
            continue
        blog_menus = website.menu_id.child_id.filtered(lambda m: (m.url or '').rstrip('/') == '/blog')
        keep = blog_menus.filtered(lambda m: m.name == 'Blogs')[:1] or blog_menus[:1]
        (blog_menus - keep).unlink()


def setup_blog(env):
    """Name the default blog (website_blog's "Our blog")."""
    blog = env.ref('website_blog.blog_blog_1', raise_if_not_found=False)
    if blog and blog.name == 'Our blog':
        blog.write({'name': 'Hekau Blog', 'subtitle': 'Insights from the Hekau team.'})


def setup_websites(env):
    """Apply the Hekau design settings to every website.

    Safe to run again (e.g. from an Odoo shell) after creating a new website.
    """
    with file_open('website_hekau/static/src/img/logo_full.svg', 'rb') as f:
        logo = BinaryBytes(f.read(), filename='hekau_logo.svg')

    apply_header_options(env)

    for website in env['website'].search([]):
        website.write({
            'logo': logo,
            # Skip the theme configurator: it would override the Hekau palette and fonts.
            'configurator_done': True,
        })

        top_menu = website.menu_id
        if top_menu:
            top_menu.child_id.unlink()
            for sequence, (name, url) in enumerate(MAIN_MENU, start=1):
                env['website.menu'].create({
                    'name': name,
                    'url': url,
                    'parent_id': top_menu.id,
                    'website_id': website.id,
                    'sequence': sequence * 10,
                })

    # The floating nav bar sits on top of the hero image on the Home page.
    homepages = env['website.page'].search([('url', '=', '/')])
    homepages.write({'header_overlay': True})
