# -*- coding: utf-8 -*-
{
    'name': "e-button",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': "Button For Validate E-Invoice"
Long description of module's purpose
    """,

    'author': "Precomp",
    'website': "https://www.odoo2u.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Button',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/account_move_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

