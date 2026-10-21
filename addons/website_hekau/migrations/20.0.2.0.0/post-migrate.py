from odoo import api, SUPERUSER_ID

from odoo.addons.website_hekau import apply_header_options


def migrate(cr, version):
    """2.0: the Home page is built from Hekau blocks and the header stays on
    screen while scrolling (it compacts to the Figma "scrolled" pill)."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    apply_header_options(env)
