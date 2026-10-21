{
    'name': 'Odoo 20 Starter',
    'summary': 'Minimal example module showing Odoo 20 module conventions',
    'description': """
A small task tracker used to verify the local dev stack and as a template
for new modules. Shows: a model with a computed field, list/form/search
views, an action, a menu, and the Odoo 20 security file (ir.access.csv).
    """,
    'version': '20.0.1.0.0',
    'category': 'Tools',
    'author': 'Your Company',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        # Odoo 20: security/ir.access.csv replaces ir.model.access.csv + ir.rule XML
        'security/ir.access.csv',
        'views/starter_task_views.xml',
    ],
    'application': True,
    'installable': True,
}
