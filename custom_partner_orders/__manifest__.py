# -*- coding: utf-8 -*-
{
   'name': "Partner Orders",

    'summary': """Manage  Partner Manadtory fields
   """,

    'description': """
       Help  to envorce complete all partners manadtory data before crate orders
       """,

    'author': "Eng.Razan Elnor",

    'category': 'Account',

    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','sale','stock','account','product'],

    # always loaded
    'data': [
      
    'security/ir.model.access.csv',
    
     'views/partnerorder.xml',
  
    ],
    # only loaded in demonstration mode
    'demo': [
   # 'demo/demo.xml',
    ],
}
