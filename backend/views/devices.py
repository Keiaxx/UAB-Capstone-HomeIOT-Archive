# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

from flask_restplus import Resource, fields
from views.api import api, devices_ns
from dao.device import get_devices
from views.locations import loc_schema

device_model = api.model('Device', {
    'deviceId': fields.Integer(readonly=True, description='The unique location id'),
    'name': fields.String(required=True, description='The unique device name'),
    'type': fields.String(required=True, description='The device type')
})

# TODO: This route is still a WIP

# product_mapper = {
#     Electric: api.inherit("ElectricDevice", device_model, {
#         'wattage': fields.String
#     }),
#     Light: api.inherit("Light", device_model, {
#         'wattage': fields.String
#     }),
#     HVAC: api.inherit("HVAC", device_model, {
#         'high_f': fields.String
#     }),
# }
#
# resource_result = api.model("ResourceResult", {
# 	'devices': fields.List(fields.Polymorph(product_mapper))
# })



@devices_ns.route('')
class Device(Resource):
    '''Gets a list of all available devices'''
    @api.doc(description='Get a list of devices')
    @api.marshal_with(device_model)
    def get(self):
        '''List all devices'''
        return get_devices()
