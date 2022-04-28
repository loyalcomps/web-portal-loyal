# -*- coding: utf-8 -*-
# from odoo import http


# class PortalTaskFields(http.Controller):
#     @http.route('/portal_task_fields/portal_task_fields/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/portal_task_fields/portal_task_fields/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('portal_task_fields.listing', {
#             'root': '/portal_task_fields/portal_task_fields',
#             'objects': http.request.env['portal_task_fields.portal_task_fields'].search([]),
#         })

#     @http.route('/portal_task_fields/portal_task_fields/objects/<model("portal_task_fields.portal_task_fields"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('portal_task_fields.object', {
#             'object': obj
#         })
