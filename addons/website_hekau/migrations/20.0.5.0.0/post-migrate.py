from odoo import api, SUPERUSER_ID

from odoo.addons.website_hekau import (
    rebuild_main_menu, remove_duplicate_menus, set_header_overlay, setup_company_details,
)


def migrate(cr, version):
    """5.0: rewritten copy, new service pages, How we work, case studies, contact
    form (website_crm), terms and privacy. New main menu; the contact, thank-you
    and privacy pages get the floating nav bar; company contact details."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    rebuild_main_menu(env)
    remove_duplicate_menus(env)
    set_header_overlay(env)
    setup_company_details(env)
