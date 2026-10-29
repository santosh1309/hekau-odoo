from odoo import api, SUPERUSER_ID

from odoo.addons.website_hekau import add_missing_menus, apply_header_options, hide_header_contact


def migrate(cr, version):
    """5.3: no phone number in the header (website-specific copies included),
    "Contact us" in the main menu."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    apply_header_options(env)
    hide_header_contact(env)
    add_missing_menus(env)
