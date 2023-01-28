# -*- coding: utf-8 -*-
from odoo import http

# class HrTrainning(http.Controller):
#     @http.route('/hr__trainning/hr__trainning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr__trainning/hr__trainning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr__trainning.listing', {
#             'root': '/hr__trainning/hr__trainning',
#             'objects': http.request.env['hr__trainning.hr__trainning'].search([]),
#         })

#     @http.route('/hr__trainning/hr__trainning/objects/<model("hr__trainning.hr__trainning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr__trainning.object', {
#             'object': obj
#         })