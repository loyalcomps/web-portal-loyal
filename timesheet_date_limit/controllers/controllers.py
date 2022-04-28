# -*- coding: utf-8 -*-
# from odoo import http


# class TimesheetDateLimit(http.Controller):
#     @http.route('/timesheet_date_limit/timesheet_date_limit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/timesheet_date_limit/timesheet_date_limit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('timesheet_date_limit.listing', {
#             'root': '/timesheet_date_limit/timesheet_date_limit',
#             'objects': http.request.env['timesheet_date_limit.timesheet_date_limit'].search([]),
#         })

#     @http.route('/timesheet_date_limit/timesheet_date_limit/objects/<model("timesheet_date_limit.timesheet_date_limit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('timesheet_date_limit.object', {
#             'object': obj
#         })
