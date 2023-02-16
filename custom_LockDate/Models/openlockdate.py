from odoo import models, fields, api

class OpenLockdate(models.Model):
  _name = 'open.lockdate'
  name = fields.Char(string="Name",required=True)
  Description=fields.Text(string="Description")


class AccounttGroup(models.Model):
  _inherit = "res.groups"
  _description='Lock date group'

  

  