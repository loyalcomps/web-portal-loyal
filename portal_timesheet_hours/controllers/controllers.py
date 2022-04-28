# -*- coding: utf-8 -*-
# from odoo import http


# class PortalTimesheetHours(http.Controller):
#     @http.route('/portal_timesheet_hours/portal_timesheet_hours/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/portal_timesheet_hours/portal_timesheet_hours/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('portal_timesheet_hours.listing', {
#             'root': '/portal_timesheet_hours/portal_timesheet_hours',
#             'objects': http.request.env['portal_timesheet_hours.portal_timesheet_hours'].search([]),
#         })

#     @http.route('/portal_timesheet_hours/portal_timesheet_hours/objects/<model("portal_timesheet_hours.portal_timesheet_hours"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('portal_timesheet_hours.object', {
#             'object': obj
#         })
