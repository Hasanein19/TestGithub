# -*- coding: utf-8 -*-
{
   'name': "Inoice Sales Team",

    'summary': """Manage  Sales team drom invoice 
    """,

    'description': """
       Help to determine sale person within inoicing process 
       """,

    'author': "Eng.Razan Elnor",

    'category': 'Account',

    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','sale','stock','account','product'],

    # always loaded
    'data': [
      
    'security/ir.model.access.csv',
  
     'views/invoicesalesteam.xml',
  
    ],
    # only loaded in demonstration mode
    'demo': [
   # 'demo/demo.xml',
    ],
}
