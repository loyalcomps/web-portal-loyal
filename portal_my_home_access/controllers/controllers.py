# -*- coding: utf-8 -*-
# from odoo import http


# class PortalMyHomeAccess(http.Controller):
#     @http.route('/portal_my_home_access/portal_my_home_access/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/portal_my_home_access/portal_my_home_access/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('portal_my_home_access.listing', {
#             'root': '/portal_my_home_access/portal_my_home_access',
#             'objects': http.request.env['portal_my_home_access.portal_my_home_access'].search([]),
#         })

#     @http.route('/portal_my_home_access/portal_my_home_access/objects/<model("portal_my_home_access.portal_my_home_access"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('portal_my_home_access.object', {
#             'object': obj
#         })
