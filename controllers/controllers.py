# -*- coding: utf-8 -*-
from odoo import http

# class MethodConectorSlack(http.Controller):
#     @http.route('/method_conector_slack/method_conector_slack/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_conector_slack/method_conector_slack/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_conector_slack.listing', {
#             'root': '/method_conector_slack/method_conector_slack',
#             'objects': http.request.env['method_conector_slack.method_conector_slack'].search([]),
#         })

#     @http.route('/method_conector_slack/method_conector_slack/objects/<model("method_conector_slack.method_conector_slack"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_conector_slack.object', {
#             'object': obj
#         })