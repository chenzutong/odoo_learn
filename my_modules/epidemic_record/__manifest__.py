# -*- coding: utf-8 -*-
{
    'name': "疫情记录",

    'summary': """
        疫情记录
        """,

    'description': """
        疫情记录
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data':[
        'security/epidemic_record_security.xml',
        'views/epidemic_record_view.xml',
        'security/ir.model.access.csv',

    ],
    'application': True,
}
