# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

from flask_restplus import Resource, fields
from views.api import api, devices_ns
from dao.device import get_devices, set_device_state, get_device_by_id

from werkzeug.exceptions import BadRequest


device_model = api.model('Device', {
    'deviceId': fields.Integer(readonly=True, description='The unique location id'),
    'name': fields.String(required=True, description='The unique device name'),
    'type': fields.String(required=True, description='The device type'),
    'state': fields.String(enum=['OFF', 'ON', 'OFFLINE', 'ERROR'],
                           default='OFF',
                           required=True,
                           description='The device state'),
    'wattage': fields.Integer(required=False),
    'gpm': fields.Integer(required=False, description='Gallons per minute if device is water type'),
    'set_f': fields.Integer(required=False, description='Temp setpoint of hvac'),
    'high_f': fields.Integer(required=False, description='High triggerpoint of hvac'),
    'low_f': fields.Integer(required=False, description='Low triggerpoint of hvac'),
    'ext_f': fields.Integer(required=False, description='External temperature of home'),
    'int_f': fields.Integer(required=False, description='Internal temperature of home')
})


@devices_ns.route('')
class Device(Resource):
    '''Gets a list of all available devices'''

    @api.doc(description='Get a list of devices')
    @api.marshal_with(device_model)
    def get(self):
        '''List all devices'''
        print(get_devices())
        return get_devices()

@devices_ns.route('/<int:deviceid>')
@devices_ns.param('deviceid', 'The deviceid to get')
class SingleDevice(Resource):
    '''Gets a list of all available devices'''

    @api.doc(description='Get a device by id')
    @api.marshal_with(device_model)
    def get(self, deviceid):
        '''Get a device by id'''
        return get_device_by_id(deviceid)

@devices_ns.route('/<int:deviceid>/setstate/<string:state>')
@devices_ns.param('state', 'The state to set the device. ON, OFF')
@devices_ns.param('deviceid', 'The deviceid to mutate')
class DeviceMutation(Resource):
    '''Mutations for a specific device'''

    @api.doc(description='Set a specified deviceid state to ON/OFF')
    def put(self, deviceid, state):
        '''Set a device state to ON/OFF'''
        if state is not None and deviceid is not None:
            stateupper = state.upper()
            if stateupper == "ON" or stateupper == "OFF":
                # TODO: DB Manipulate state
                print(set_device_state(deviceid, state))
                return {
                    'state': state,
                    'deviceid': deviceid
                }
            else:
                raise BadRequest("Invalid state. Must be ON/OFF")
        else:
            raise BadRequest("Invalid state. Must specify state and/or deviceid /did/setstate/ON")


