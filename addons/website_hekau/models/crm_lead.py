"""Contact form answers -> CRM lead tag and source.

The contact page's form (scripts/hk_render.py, ``contact``) asks "What do you need
help with?" (field "Service needed") and "How did you hear about us?" (field
"Heard about us via"). Neither is a lead field, so Odoo only writes them into the
lead's description. This override also tags the lead with the service and sets
its source, so the pipeline can be filtered and reported on by both.
"""
from odoo import models
from odoo.fields import Command

SERVICE_FIELD = 'Service needed'
SOURCE_FIELD = 'Heard about us via'

# Form choice (hk_content.SERVICE_CHOICES) -> CRM tag. "Not sure yet" adds no tag.
SERVICE_TAGS = {
    'ERP, CRM & CMS Implementation': 'ERP, CRM & CMS',
    'Workflow & Process Automation': 'Workflow Automation',
    'Custom Web Applications & B2B Portals': 'Web Apps & B2B Portals',
    'Secure In-House AI & Data': 'AI & Data',
    'Mobile App Development': 'Mobile Apps',
    'UX & Conversion-Focused Websites': 'UX & Websites',
    'Cloud-Managed Services': 'Cloud-Managed Services',
    'Project Rescue & Dedicated Developers': 'Project Rescue & Dedicated Devs',
}
# Form choice (hk_content.CONTACT['sources']) -> lead source. "Other" or no answer
# -> DEFAULT_SOURCE.
SOURCES = {'LinkedIn': 'LinkedIn', 'Google': 'Google', 'Referral': 'Referral', 'Event': 'Event'}
DEFAULT_SOURCE = 'Website form'


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def website_form_input_filter(self, request, values):
        values = super().website_form_input_filter(request, values)
        params = request.params if request else {}

        tag_name = SERVICE_TAGS.get((params.get(SERVICE_FIELD) or '').strip())
        if tag_name:
            Tag = self.env['crm.tag'].sudo()
            tag = Tag.search([('name', '=ilike', tag_name)], limit=1) or Tag.create({'name': tag_name})
            values['tag_ids'] = [Command.link(tag.id)]

        # A source from a tracked link (utm_source cookie) wins over the visitor's answer.
        if request and not values.get('source_id') and not request.cookies.get('odoo_utm_source'):
            heard = (params.get(SOURCE_FIELD) or '').strip()
            source = self.env['utm.mixin'].sudo()._find_or_create_record(
                'utm.source', SOURCES.get(heard, DEFAULT_SOURCE))
            values['source_id'] = source.id
        return values
