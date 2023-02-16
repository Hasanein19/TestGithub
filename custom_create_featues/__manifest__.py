# -*- coding: utf-8 -*-
{
   'name': "Create Feature",

    'summary': """Manage  create feature for Nany2one feilds""",

    'description': """
       Help admin to control disable  this feature for specific users throgh securiy group 
       """,

    'author': "Eng.Razan Elnour",

    'category': 'Account',

    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','sale'],

    # always loaded
    'data': [
      
    'security/ir.model.access.csv',
    'security/security.xml',
    'views/createfeature.xml',
  
    ],
    # only loaded in demonstration mode
    'demo': [
   # 'demo/demo.xml',
    ],
}
