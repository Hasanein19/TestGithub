from odoo import models, fields, api


  ############################  Module class#  #######################

class OpenAcademyy(models.Model):
  _name = 'open.academyy'
  name = fields.Char(string="Name",required=True)
  Description=fields.Text(string="Description")

################### Inheritance for all cneeded classes   ##############################

class PurchaseOrderInherit(models.Model):
  _inherit = "purchase.order"
  _description="Recipt products"

class PartnerInherit(models.Model):
  _inherit = "stock.picking"
  _description="stock products"


class OrderInherit(models.Model):
  _inherit = "account.move"
  _description="invoice Products"
  p_order=fields.Many2one('purchase.order')
  s_order=fields.Many2one('sale.order')



class SaleOrderInherit(models.Model):
  _inherit = "sale.order"
  _description="Recipt products"









  

  