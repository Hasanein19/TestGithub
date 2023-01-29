from odoo import models, fields, api

class Prtner(models.Model):
  
  _inherit= 'res.partner'
  instructor=fields.Boolean("Instructor",defult=False)  
  session_ids=fields.One2many('openacademy.session','course_id',string="Sessions")
