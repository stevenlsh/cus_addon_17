# -*- coding: utf-8 -*-
# from odoo import http


# class DeSchoolLibrary(http.Controller):
#     @http.route('/de_school_library/de_school_library', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_school_library/de_school_library/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_school_library.listing', {
#             'root': '/de_school_library/de_school_library',
#             'objects': http.request.env['de_school_library.de_school_library'].search([]),
#         })

#     @http.route('/de_school_library/de_school_library/objects/<model("de_school_library.de_school_library"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_school_library.object', {
#             'object': obj
#         })
