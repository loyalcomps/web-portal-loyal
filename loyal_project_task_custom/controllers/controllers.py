# -*- coding: utf-8 -*-
# from odoo import http


# class LoyalProjectTaskCustom(http.Controller):
#     @http.route('/loyal_project_task_custom/loyal_project_task_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loyal_project_task_custom/loyal_project_task_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loyal_project_task_custom.listing', {
#             'root': '/loyal_project_task_custom/loyal_project_task_custom',
#             'objects': http.request.env['loyal_project_task_custom.loyal_project_task_custom'].search([]),
#         })

#     @http.route('/loyal_project_task_custom/loyal_project_task_custom/objects/<model("loyal_project_task_custom.loyal_project_task_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loyal_project_task_custom.object', {
#             'object': obj
#         })
