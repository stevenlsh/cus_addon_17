# -*- coding: utf-8 -*-
# from odoo import http


# class E-button(http.Controller):
#     @http.route('/e-button/e-button', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/e-button/e-button/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('e-button.listing', {
#             'root': '/e-button/e-button',
#             'objects': http.request.env['e-button.e-button'].search([]),
#         })

#     @http.route('/e-button/e-button/objects/<model("e-button.e-button"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('e-button.object', {
#             'object': obj
#         })

