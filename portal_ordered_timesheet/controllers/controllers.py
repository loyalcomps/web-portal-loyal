# -*- coding: utf-8 -*-
# from odoo import http


# class PortalOrderedTimesheet(http.Controller):
#     @http.route('/portal_ordered_timesheet/portal_ordered_timesheet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/portal_ordered_timesheet/portal_ordered_timesheet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('portal_ordered_timesheet.listing', {
#             'root': '/portal_ordered_timesheet/portal_ordered_timesheet',
#             'objects': http.request.env['portal_ordered_timesheet.portal_ordered_timesheet'].search([]),
#         })

#     @http.route('/portal_ordered_timesheet/portal_ordered_timesheet/objects/<model("portal_ordered_timesheet.portal_ordered_timesheet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('portal_ordered_timesheet.object', {
#             'object': obj
#         })
