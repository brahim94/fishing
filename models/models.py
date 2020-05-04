# -*- coding: utf-8 -*-

from odoo import models, fields


class fishing(models.Model):
 
     _name = 'fishing.list'
#     _description = 'fishing.fishing'

     name = fields.Char()
     number = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
