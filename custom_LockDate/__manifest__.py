# -*- coding: utf-8 -*-
{
    'name': "Lock Date User",

    'summary': """Manage  lock Date Users""",

    'description': """
       Help Manger to control users who can modify on invoice /journals for closed Fiscal Year
    """,

    'author': "Eng.Razan Elnor",

    'category': 'Account',

    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base' ,'account'],

    # always loaded
    'data': [
   
    'security/security.xml',
    'security/ir.model.access.csv',
    'views/lockdatemenu.xml',
 
  
    ],
    # only loaded in demonstration mode
    'demo': [
    'demo/demo.xml',
    ],
}
