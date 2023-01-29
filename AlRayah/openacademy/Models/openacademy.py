from odoo import models, fields, api

class OpenAcademyy(models.Model):
  _name = 'open.academyy'
  name = fields.Char(string="Name",required=True)
  Description=fields.Text(string="Description")


class AccounttGroup(models.Model):
  _inherit = "res.groups"
  _description='Lock date group'

  

  