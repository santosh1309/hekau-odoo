from odoo import api, SUPERUSER_ID

from odoo.addons.website_hekau import remove_duplicate_menus, setup_blog


def migrate(cr, version):
    """4.0: About Us, Projects, case study and blog pages (website_blog is now a dependency)."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    remove_duplicate_menus(env)
    setup_blog(env)
