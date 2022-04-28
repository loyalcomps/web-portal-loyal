# -*- coding: utf-8 -*-
# from odoo import http


# class PortalTimesheetReport(http.Controller):
#     @http.route('/portal_timesheet_report/portal_timesheet_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/portal_timesheet_report/portal_timesheet_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('portal_timesheet_report.listing', {
#             'root': '/portal_timesheet_report/portal_timesheet_report',
#             'objects': http.request.env['portal_timesheet_report.portal_timesheet_report'].search([]),
#         })

#     @http.route('/portal_timesheet_report/portal_timesheet_report/objects/<model("portal_timesheet_report.portal_timesheet_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('portal_timesheet_report.object', {
#             'object': obj
#         })
