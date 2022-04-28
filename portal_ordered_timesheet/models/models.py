# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    def _timesheet_get_portal_domain(self):
        res = super(AccountAnalyticLine, self)._timesheet_get_portal_domain()
        # res.append('|')
        # res.append(('task_id.project_id.privacy_visibility', '=', 'portal'))
        # res.append(('timesheet_invoice_type', 'in', ['billable_time', 'non_billable','billable_fixed']))

        res = [('timesheet_invoice_type', 'in', ['billable_time', 'non_billable','billable_fixed']) if i == ('timesheet_invoice_type', 'in', ['billable_time', 'non_billable']) else i for i in res]
        return res
        # return expression.OR([res, [('timesheet_invoice_type', 'in', ['billable_time', 'non_billable','billable_fixed'])]])
    # #
    # @api.depends('so_line.product_id', 'project_id', 'task_id')
    # def _compute_timesheet_invoice_type(self):
    #     for timesheet in self:
    #         if timesheet.project_id:  # AAL will be set to False
    #             invoice_type = 'non_billable_project' if not timesheet.task_id else 'non_billable'
    #             if timesheet.task_id and timesheet.so_line.product_id.type == 'service':
    #                 if timesheet.so_line.product_id.invoice_policy == 'delivery':
    #                     if timesheet.so_line.product_id.service_type == 'timesheet':
    #                         invoice_type = 'billable_time'
    #                     else:
    #                         invoice_type = 'billable_fixed'
    #                 elif timesheet.so_line.product_id.invoice_policy == 'order':
    #                     if timesheet.so_line.product_id.service_policy == 'ordered_timesheet':
    #                         invoice_type = 'billable_time'
    #                     else:
    #                         invoice_type = 'billable_fixed'
    #             timesheet.timesheet_invoice_type = invoice_type
    #         else:
    #             timesheet.timesheet_invoice_type = False