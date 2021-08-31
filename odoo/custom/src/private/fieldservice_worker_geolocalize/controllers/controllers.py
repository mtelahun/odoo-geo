# class FieldserviceWorkerGeolocalize(http.Controller):
#     @http.route('/fieldservice_worker_geolocalize/fieldservice_worker_geolocalize/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fieldservice_worker_geolocalize/fieldservice_worker_geolocalize/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fieldservice_worker_geolocalize.listing', {
#             'root': '/fieldservice_worker_geolocalize/fieldservice_worker_geolocalize',
#             'objects': http.request.env['fieldservice_worker_geolocalize.fieldservice_worker_geolocalize'].search([]),
#         })

#     @http.route('/fieldservice_worker_geolocalize/fieldservice_worker_geolocalize/objects/<model("fieldservice_worker_geolocalize.fieldservice_worker_geolocalize"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fieldservice_worker_geolocalize.object', {
#             'object': obj
#         })
