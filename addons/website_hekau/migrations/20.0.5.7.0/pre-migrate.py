from odoo import api, SUPERUSER_ID

# Records created by data/blog_data.xml and data/blog_posts.xml that may
# already exist under the same name (blog tag and tag category names are
# unique): adopt them instead of failing on the unique constraint.
CATEGORIES = {
    "blog_tag_category_topics": "Topics",
    "blog_tag_category_keywords": "Keywords",
}

BLOG_TAGS = {
    "blog_topic_connected_systems": "Connected Systems",
    "blog_topic_erp_manufacturing": "ERP & Manufacturing",
    "blog_topic_automation_ai": "Automation & AI",
    "blog_topic_leadership_strategy": "Leadership & Strategy",
    "blog_topic_websites_platforms": "Websites & Platforms",
    "blog_tag_systems": "Systems",
    "blog_tag_integration": "Integration",
    "blog_tag_operations": "Operations",
    "blog_tag_growth": "Growth",
    "blog_tag_spreadsheets": "Spreadsheets",
    "blog_tag_erp": "ERP",
    "blog_tag_data_trust": "Data Trust",
    "blog_tag_dashboards": "Dashboards",
    "blog_tag_reporting": "Reporting",
    "blog_tag_data": "Data",
    "blog_tag_leadership": "Leadership",
    "blog_tag_decision_making": "Decision Making",
    "blog_tag_information_flow": "Information Flow",
    "blog_tag_roi": "ROI",
    "blog_tag_business_case": "Business Case",
    "blog_tag_strategy": "Strategy",
    "blog_tag_saas": "SaaS",
    "blog_tag_software_audit": "Software Audit",
    "blog_tag_costs": "Costs",
    "blog_tag_odoo": "Odoo",
    "blog_tag_custom_software": "Custom Software",
    "blog_tag_build_vs_buy": "Build vs Buy",
    "blog_tag_implementation": "Implementation",
    "blog_tag_change_management": "Change Management",
    "blog_tag_manufacturing": "Manufacturing",
    "blog_tag_mes": "MES",
    "blog_tag_production_reporting": "Production Reporting",
    "blog_tag_automation": "Automation",
    "blog_tag_workflows": "Workflows",
    "blog_tag_productivity": "Productivity",
    "blog_tag_ai": "AI",
    "blog_tag_ai_readiness": "AI Readiness",
    "blog_tag_ai_strategy": "AI Strategy",
    "blog_tag_ai_adoption": "AI Adoption",
    "blog_tag_data_quality": "Data Quality",
    "blog_tag_data_readiness": "Data Readiness",
    "blog_tag_data_privacy": "Data Privacy",
    "blog_tag_security": "Security",
    "blog_tag_case_study": "Case Study",
    "blog_tag_publishing": "Publishing",
    "blog_tag_lessons_learned": "Lessons Learned",
    "blog_tag_project_rescue": "Project Rescue",
    "blog_tag_code_audit": "Code Audit",
    "blog_tag_vendors": "Vendors",
    "blog_tag_risk": "Risk",
    "blog_tag_website": "Website",
    "blog_tag_conversion": "Conversion",
    "blog_tag_lead_generation": "Lead Generation",
    "blog_tag_b2b": "B2B",
    "blog_tag_technology_partner": "Technology Partner",
    "blog_tag_vendor_selection": "Vendor Selection"
}


def _adopt(env, model, xmlid, record):
    imd = env['ir.model.data']
    if imd.search_count([('module', '=', 'website_hekau'), ('name', '=', xmlid)]):
        return
    imd.create({'module': 'website_hekau', 'name': xmlid, 'model': model, 'res_id': record.id, 'noupdate': True})


def migrate(cr, version):
    """5.7: before the 20 articles are loaded, reuse existing tags, tag
    categories and the author's contact (a user or contact named Santosh
    Yadav), so nothing is duplicated."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    for xmlid, name in CATEGORIES.items():
        record = env['blog.tag.category'].search([('name', '=', name)], limit=1)
        if record:
            _adopt(env, 'blog.tag.category', xmlid, record)
    for xmlid, name in BLOG_TAGS.items():
        record = env['blog.tag'].search([('name', '=', name)], limit=1)
        if record:
            _adopt(env, 'blog.tag', xmlid, record)
    user = env['res.users'].with_context(active_test=False).search([('name', '=ilike', 'Santosh Yadav')], limit=1)
    partner = user.partner_id or env['res.partner'].search([('name', '=ilike', 'Santosh Yadav')], limit=1)
    if partner:
        _adopt(env, 'res.partner', 'blog_author_santosh', partner)
