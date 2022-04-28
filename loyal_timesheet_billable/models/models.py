# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Task(models.Model):
    _inherit = "project.task"

    pack_type = fields.Selection([('support', 'Support'), ('implementation', 'Implementation')], string='Pack Type')
    task_ref = fields.Char(string='Task Reference', required=True, copy=False, index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('task_ref', _('New')) == _('New'):
            vals['task_ref'] = self.env['ir.sequence'].next_by_code('project.task.ref') or _('New')
        result = super(Task, self).create(vals)
        return result


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    is_billable = fields.Boolean('Is Billable', default=False)
    pack_type = fields.Selection([('support', 'Support'), ('implementation', 'Implementation')], string='Pack Type',
                                 related='task_id.pack_type')

