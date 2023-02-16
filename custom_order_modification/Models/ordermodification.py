from odoo import models, fields, api ,exceptions,_
from datetime import datetime


  ############################  Module class#  #######################

class OrderModification(models.Model):
  _name = 'order.modification'


  ################### Inheritance for all cneeded classes   ##############################

class SaleOpenOrder(models.Model):
    _inherit = 'sale.order'
    order_line = fields.One2many('sale.order.line', 'order_id', string='Order Lines', states={'cancel': [('readonly', False)], 'done': [('readonly', False)]}, copy=True, auto_join=True)



class PurchaseOpenOrder(models.Model):
    _inherit = 'purchase.order'
    order_line = fields.One2many('purchase.order.line', 'order_id', string='Order Lines', states={'cancel': [('readonly', False)], 'done': [('readonly', False)]}, copy=True, auto_join=True)


