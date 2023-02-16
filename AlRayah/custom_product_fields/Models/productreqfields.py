from odoo import models, fields, api ,exceptions,_
from datetime import datetime


  ############################  Module class#  #######################

class ProductReqFields(models.Model):
  _name = 'product.reqfields'


################### Inheritance for all cneeded classes   ##############################


class ProductReqFieldsInherit(models.Model):
  _inherit = "product.template"
  _description="required product fields"








  

  