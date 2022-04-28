# -*- coding: utf-8 -*-
from odoo import models, fields, api,_,SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import datetime
from datetime import date, timedelta,datetime



class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    #
    @api.onchange('date')
    def onchange_date_val(self):
        previous_date = fields.Date.today() - timedelta(days=1)
        current_date = fields.Date.today()

        user = self.env.uid == SUPERUSER_ID or self.env.user.id==2 or self.env.uid == 1
        # result = super(AccountAnalyticLine, self).write(values)
        for i in self:
            if not user:
                value = False
                if i.date == current_date or i.date == previous_date:
                    value = False
                else:
                    value = True
                if value == True:

                    raise ValidationError(_("You can not enter timesheet of previous day"))
        return

    # @api.model
    # def create(self, vals):
    #     #here you can validate the creation
    #     # self.env.is_superuser()
    #     previous_date = fields.Date.today() - timedelta(days=1)
    #     current_date = fields.Date.today()
    #
    #     user = self.env.uid == SUPERUSER_ID or self.env.user.id==2
    #     res = super(AccountAnalyticLine, self).create(vals)
    #     if not user:
    #         value = False
    #         if 'date' in vals:
    #             if vals['date'] and type(vals['date'])!=str:
    #                 date_now = vals['date']
    #             elif vals['date'] and type(vals['date']) == str:
    #                 date_now = datetime.strptime(str(vals['date']), '%Y-%m-%d').date()
    #
    #             if date_now == current_date or date_now == previous_date:
    #                 value = False
    #             else:
    #                 value = True
    #             if value==True:
    #                 raise ValidationError(_( "You can not enter timesheet of previous day"))
    #     return res
    #
    # def write(self, values):
    #     previous_date = fields.Date.today() - timedelta(days=1)
    #     current_date = fields.Date.today()
    #
    #     user = self.env.uid == SUPERUSER_ID or self.env.user.id==2
    #     result = super(AccountAnalyticLine, self).write(values)
    #     for i in self:
    #         if not user:
    #             value = False
    #             if i.date == current_date or i.date == previous_date:
    #                 value = False
    #             else:
    #                 value = True
    #             if value == True:
    #
    #                 raise ValidationError(_("You can not enter timesheet of previous day"))
    #     return result

# class ProjectTask(models.Model):
#     _inherit = "project.task"
#
#     @api.model
#     def create(self, vals):
#         current_date = fields.Date.today()
#         user = self.env.uid == SUPERUSER_ID  or self.env.user.id == 2
#         # user = self.env.is_superuser() or self.env.user.has_group('base.group_erp_manager')
#         res = super(ProjectTask, self).create(vals)
#         if not user:
#             if 'timesheet_ids' in vals:
#                 if vals['timesheet_ids'][0][2]['date'] and type(vals['timesheet_ids'][0][2]['date'])!=str:
#                     date_now = vals['timesheet_ids'][0][2]['date']
#                 elif vals['timesheet_ids'][0][2]['date'] and type(vals['timesheet_ids'][0][2]['date']) == str:
#                     date_now = datetime.strptime(str(vals['timesheet_ids'][0][2]['date']), '%Y-%m-%d').date()
#                 if vals['timesheet_ids'][0][2]['date']:
#                     if date_now!= current_date:
#                         raise ValidationError(_( "You cannot create a timesheet"))
#
#         return res
#
#
#     def write(self, values):
#         current_date = fields.Date.today()
#         user = self.env.uid == SUPERUSER_ID or self.env.user.id==2
#         result = super(ProjectTask, self).write(values)
#         if not user:
#             if 'timesheet_ids' in values:
#                 if values['timesheet_ids'][0][2]['date'] and type(values['timesheet_ids'][0][2]['date']) != str:
#                     date_now = values['timesheet_ids'][0][2]['date']
#                 elif values['timesheet_ids'][0][2]['date'] and type(values['timesheet_ids'][0][2]['date']) == str:
#                     date_now = datetime.strptime(str(values['timesheet_ids'][0][2]['date']), '%Y-%m-%d').date()
#                 if values['timesheet_ids'][0][2]['date']:
#                     if date_now != current_date:
#                         raise ValidationError(_("You cannot create a timesheet"))
#             # elif 'timesheet_ids' not in values:
#             #     for i in self:
#             #         if i.date != current_date:
#             #             raise ValidationError(_("You cannot create a timesheet"))
#
#         return result

