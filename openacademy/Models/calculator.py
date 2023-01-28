from odoo import models, fields, api ,exceptions,_
import tkinter as tk

class CalculatorMachine(models.Model):
	_name = 'calculator.machinee'
	_description = 'calculator Machine'
	Number1=fields.Float(default=0)
	Number2=fields.Float(default=0)
	sign= fields.Char(string='Sign' ,help='please insert +,-,* or /')
	Result=fields.Float(default=0,compute='_resut_Calculation')
	@api.onchange('Number1','Number2','sign')
	def _resut_Calculation(self):
		if self.sign == '+':
			self.Result=self.Number1 + self.Number2
		elif self.sign =='-':
			self.Result=self.Number1 - self.Number2
		elif self.sign =='*':	
			self.Result=self.Number1 * self.Number2
		elif self.sign =='/':
			self.Result=self.Number1  / self.Number2
	
	def zero(self):
		self.Number1 =0