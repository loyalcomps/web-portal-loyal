# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class portal_task_fields(models.Model):
#     _name = 'portal_task_fields.portal_task_fields'
#     _description = 'portal_task_fields.portal_task_fields'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
