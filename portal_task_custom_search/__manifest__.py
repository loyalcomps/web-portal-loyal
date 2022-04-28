# -*- coding: utf-8 -*-
{
    'name': "Portal Task Custom Search",

    'summary': """
        This module allows you to sort task by deadline and search task by assigned to""",

    'description': """
        This module allows you to sort task by deadline, search task by assigned to and group by stage. User can choose BG color for stage. 
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'portal_task_fields', 'web_editor'],

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
