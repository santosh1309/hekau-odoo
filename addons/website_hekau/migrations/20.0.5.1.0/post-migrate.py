from odoo import api, SUPERUSER_ID

from odoo.addons.website_hekau import fix_header_contact


def migrate(cr, version):
    """5.1: Hekau's phone and email in the header text element, including the
    website-specific copy made in the website builder; two client testimonials."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    fix_header_contact(env)
