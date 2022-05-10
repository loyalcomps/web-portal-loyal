# -*- coding: utf-8 -*-
# from odoo import http


# class CustomPayslip(http.Controller):
#     @http.route('/custom_payslip/custom_payslip/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_payslip/custom_payslip/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_payslip.listing', {
#             'root': '/custom_payslip/custom_payslip',
#             'objects': http.request.env['custom_payslip.custom_payslip'].search([]),
#         })

#     @http.route('/custom_payslip/custom_payslip/objects/<model("custom_payslip.custom_payslip"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_payslip.object', {
#             'object': obj
#         })
