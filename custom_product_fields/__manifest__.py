# -*- coding: utf-8 -*-
{
   'name': "Product Fields",

    'summary': """Manage  Manadatory" Fields
    """,

    'description': """
       Help to ensure manadatoryfields are filled by users before using this products 
       """,

    'author': "Eng.Razan Elnor",

    'category': 'Account',

    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','sale','stock','account','product'],

    # always loaded
    'data': [
      
    'security/ir.model.access.csv',
  
     'views/productreqfields.xml',
  
    ],
    # only loaded in demonstration mode
    'demo': [
   # 'demo/demo.xml',
    ],
}
