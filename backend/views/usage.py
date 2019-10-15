# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

from flask_restplus import Resource, fields
from views.api import api, usage_ns
from dao.location import get_locations

loc_schema = {
    'locationId': fields.Integer(readonly=True, description='The unique location id'),
    'name': fields.String(required=True, description='The unique location name')
}

loc_model = api.model('Usage', loc_schema)


@usage_ns.route('/<int:id>')
class Usage(Resource):
    """Gets a list of all available locations"""

    @api.doc(description='Get usage for a specific device id')
    def get(self):
        '''List all locations'''
        return {
            'todo': 'not yet implemented'
        }


@usage_ns.route('')
@api.doc(params={
    'start': 'Start date in ISO format (YYYY-MM-DD)',
    'end': 'End date in ISO format (YYYY-MM-DD)'
})
class UsageList(Resource):
    """Gets a list of all available locations"""

    @api.doc(description='Get overall usage for the home. If no start/end params are given, this will automatically'
                         'default to the latest day.')
    def get(self):
        '''Get usage for a specified date range, in ISO format (YYYY-MM-DD)'''
        return {
            'todo': 'not yet implemented'
        }
