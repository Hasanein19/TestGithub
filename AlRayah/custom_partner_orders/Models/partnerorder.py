from odoo import models, fields, api ,exceptions,_
from datetime import datetime


  ############################  Module class#  #######################

class PartnerOrder(models.Model):
  _name = 'partner.order'


################### Inheritance for all cneeded classes   ##############################

class PurchasePartnerInherit(models.Model):
  _inherit = "purchase.order"
  _inherit = "purchase.order.line"
  _description="Recipt products"


class SalePartnerInherit(models.Model):
  _inherit = "sale.order"
  _inherit = "sale.order.line"
  _description="Recipt products"


