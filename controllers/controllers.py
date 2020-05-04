# -*- coding: utf-8 -*-
# from odoo import http


# class Fishing(http.Controller):
#     @http.route('/fishing/fishing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fishing/fishing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fishing.listing', {
#             'root': '/fishing/fishing',
#             'objects': http.request.env['fishing.fishing'].search([]),
#         })

#     @http.route('/fishing/fishing/objects/<model("fishing.fishing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fishing.object', {
#             'object': obj
#         })
