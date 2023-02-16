from odoo import models, fields, api ,exceptions,_
from datetime import datetime


  ############################  Module class#  #######################

class Create_feature(models.Model):
  _name = 'create.feature'

################### Inheritance for all cneeded classes   ##############################

class PurchaseFeatureInherit(models.Model):
  _inherit = "purchase.order"
  _inherit = "purchase.order.line"
  _description="Recipt products"

class SaleFeatureInherit(models.Model):
  _inherit = "sale.order"
  _inherit = "sale.order.line"
  _description="Recipt products"










  

  
