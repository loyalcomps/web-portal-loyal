# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class portal_my_home_access(models.Model):
#     _name = 'portal_my_home_access.portal_my_home_access'
#     _description = 'portal_my_home_access.portal_my_home_access'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
