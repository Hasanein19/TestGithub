# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Razan",
    'website': "http://www.SAID Company.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
   
      
    
    'security/security.xml',
    'security/ir.model.access.csv',
    #'views/openacademy.xml',
    'views/partner.xml',
    #'views/razan.xml',
     #'views/Configuration.xml',
    #'Report/Session_Report.xml',
    #'Report/sale_report_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    'demo/demo.xml',
    ],
}