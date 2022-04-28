# -*- coding: utf-8 -*-
{
    'name': "Customized Website Helpdesk Team",

    'summary': """
        Help desk assigned to project will be visible in help form after user login. User has to login first to submit a ticket.""",

    'description': """
        Help desk assigned to project will be visible in help form after user login. User has to login first to submit a ticket.
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website/Website',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_helpdesk', 'website_helpdesk_form'],

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
