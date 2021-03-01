# -*- coding: utf-8 -*-
{
    'name': "个人-记录",

    'summary': """
        个人记录
        """,

    'description': """
        个人记录
    """,

    'author': "czt",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'views/person_record_view.xml',
        'security/ir.model.access.csv',

    ],
    'application': True,
}
