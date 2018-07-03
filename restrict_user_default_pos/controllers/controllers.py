# -*- coding: utf-8 -*-
from openerp import http

# class RestrictUserDefaultPos(http.Controller):
#     @http.route('/restrict_user_default_pos/restrict_user_default_pos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/restrict_user_default_pos/restrict_user_default_pos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('restrict_user_default_pos.listing', {
#             'root': '/restrict_user_default_pos/restrict_user_default_pos',
#             'objects': http.request.env['restrict_user_default_pos.restrict_user_default_pos'].search([]),
#         })

#     @http.route('/restrict_user_default_pos/restrict_user_default_pos/objects/<model("restrict_user_default_pos.restrict_user_default_pos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restrict_user_default_pos.object', {
#             'object': obj
#         })