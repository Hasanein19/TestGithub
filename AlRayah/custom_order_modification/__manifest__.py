# -*- coding: utf-8 -*-
{
   'name': "Modify delivedrd/recived order",

    'summary': """Manage modification  on delivedrd/recived order
   """,

    'description': """
       Help to envorce modification on order quantity/price after confirmed and stock proecee have been done
       """,

    'author': "Eng.Razan Elnor",

    'category': 'Account',

    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','sale','stock','account','product'],

    # always loaded
    'data': [
      
    'security/ir.model.access.csv',
     
    ],
    # only loaded in demonstration mode
    'demo': [
   # 'demo/demo.xml',
    ],
}
