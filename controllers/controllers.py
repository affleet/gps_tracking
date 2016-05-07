# -*- coding: utf-8 -*-
from openerp import http

# class GpsTracking(http.Controller):
#     @http.route('/gps_tracking/gps_tracking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gps_tracking/gps_tracking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gps_tracking.listing', {
#             'root': '/gps_tracking/gps_tracking',
#             'objects': http.request.env['gps_tracking.gps_tracking'].search([]),
#         })

#     @http.route('/gps_tracking/gps_tracking/objects/<model("gps_tracking.gps_tracking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gps_tracking.object', {
#             'object': obj
#         })