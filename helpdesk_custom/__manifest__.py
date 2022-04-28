# -*- coding: utf-8 -*-
{
    'name': "Customized Portal Ticket View",

    'summary': """
        Reported on and assigned to fields are added in the ticket view in portal""",

    'description': """
        Reported on and assigned to fields are added in the ticket view in portal, Filter by stage and group by, User 
        can choose background colour for each stage
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website/Website',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
