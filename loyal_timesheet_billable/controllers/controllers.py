# -*- coding: utf-8 -*-
# from odoo import http


# class LoyalTimesheetBillable(http.Controller):
#     @http.route('/loyal_timesheet_billable/loyal_timesheet_billable/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loyal_timesheet_billable/loyal_timesheet_billable/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loyal_timesheet_billable.listing', {
#             'root': '/loyal_timesheet_billable/loyal_timesheet_billable',
#             'objects': http.request.env['loyal_timesheet_billable.loyal_timesheet_billable'].search([]),
#         })

#     @http.route('/loyal_timesheet_billable/loyal_timesheet_billable/objects/<model("loyal_timesheet_billable.loyal_timesheet_billable"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loyal_timesheet_billable.object', {
#             'object': obj
#         })
