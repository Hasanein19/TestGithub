from odoo import models, fields, api ,exceptions,_
from datetime import datetime


  ############################  Module class#  #######################

class InoiceSales(models.Model):
  _name = 'invoice.salesteam'
 
################### Inheritance for all cneeded classes   ##############################

class InvoiceSalesPersonInherit(models.Model):
  _inherit = "account.move"
  _description="invoice sales person"
  s_person=fields.Many2one('res.users',"Sale Person")

class InvoiceSalesTeamInherit(models.Model):
  _inherit = "res.partner"
  _description="invoice sale team"






  

  
