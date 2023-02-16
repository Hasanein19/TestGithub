# -*- coding: utf-8 -*-
{
    'name': "Salled and Purchased Report",

    'summary': """
             Manage Salled and Purchased Excell Report""",

    'description': """
           Help Manger to quick compare betwwen products values and quantities in invoices/bills and stocks 
    """,

      'author': "Eng.Razan Elnor",

      'category': 'Account',

      'version': '1.0',


    # any module necessary for this one to work correctly
    'depends': ['base','purchase','sale','stock','account','sale_management','account_accountant'],

    # always loaded
    'data': [
    'security/ir.model.access.csv',  
    'Report/action.xml',
    'Report/Inoice_inheritance.xml',
   
    ],
    # only loaded in demonstration mode
    'demo': [
   # 'demo/demo.xml',
    ],
}
