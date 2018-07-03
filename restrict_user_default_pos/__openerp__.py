# -*- coding: utf-8 -*-
{
    'name': "restrict_user_default_pos",

    'summary': """
        LIMITING USER TO ITS DEFAULT POS""",

    'description': """
        THIS MODULE MAKES THE USER HAVE ACCESS ONLY TO HIS OWN POINT OF SALE
    """,

    'author': "EDER MACHADO(TITUTEC, LDA)",
    'website': "https://titutec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/record_rule.xml',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'price':10,
    'currency':"EUR",
    'images':['images/pos_sc_02.jpg'],
}