# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class fishing(models.Model):
     _name = 'fishing.list'
#     _description = 'fishing.fishing'

     name = fields.Char()
     Number = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
