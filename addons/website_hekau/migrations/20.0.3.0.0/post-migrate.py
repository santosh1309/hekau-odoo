from odoo import api, SUPERUSER_ID

from odoo.addons.website_hekau import update_menu_links


def migrate(cr, version):
    """3.0: Services, service, About Us and Projects pages; menus point at them."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    update_menu_links(env)
