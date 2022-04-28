# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PortalEmployeeTimesheet(models.TransientModel):
    _name = 'portal.timesheet.wizard'

    customer = fields.Many2one('res.partner', string="Customer")


    def print_timesheet(self):
        """Redirects to the report with the values obtained from the wizard
        'data['form']': name of employee and the date duration"""

        self.ensure_one()
        context = self._context
        datas = {'ids': context.get('active_ids', [])}
        datas['model'] = 'sale.order'
        datas['form'] = self.read()[0]
        for field in datas['form'].keys():
            if isinstance(datas['form'][field], tuple):
                datas['form'][field] = datas['form'][field][0]
        # data = {
        #
        #     'customer': self.customer.id
        # }
        return self.env.ref('portal_timesheet_report.portal_report_print_timesheets').report_action(self, data=datas)

