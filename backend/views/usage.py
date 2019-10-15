# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

from datetime import datetime
from flask_restplus import Resource, fields, reqparse
from views.api import api, usage_ns
from dao.usage import *

from werkzeug.exceptions import BadRequest

usage_individual = api.model('UsageData', {
    'd': fields.String(required=True, description='The datetime of the usage aggregation'),
    'v': fields.String(required=True, description='The value of usage, kWh/gallons based on which category context')
})

user_list_fields = api.model('UsageList', {
    'usage': fields.List(fields.Nested(usage_individual)),
})

usage_schema = {
    'usage_date_meta': fields.Nested(api.model('UsageDateMeta', {
        'oldest': fields.Integer(readonly=True, description='The oldest date available for usage data, in ISO format'),
        'latest': fields.Integer(readonly=True, description='The latest date available for usage data, in ISO format')
     })),
    'electricity': fields.Nested(user_list_fields),
    'water': fields.Nested(user_list_fields)
}

usage_model = api.model('UsageResponse', usage_schema)


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
    """Get usage information"""

    @api.doc(description='Get overall usage for the home. If no start/end params are given, this will automatically'
                         'default to the latest day.')
    @api.doc(responses={500: 'Invalid params'})
    @api.marshal_with(usage_model)
    def get(self):
        '''Get usage for a specified date range, in ISO format (YYYY-MM-DD)'''
        parser = reqparse.RequestParser()
        parser.add_argument('start')
        parser.add_argument('end')
        args = parser.parse_args()

        start = validateDate(args['start'])
        end = validateDate(args['end'])

        if start and end:
            return {
                'todo': 'start and end date request'
            }
        elif not start and not end:
            return {
                'todo': 'default latest day request'
            }
        else:
            raise BadRequest("Must specify both start and end params")


# Utility functions
def validateDate(date):
    if date is None:
        return None

    try:
        datetime.strptime(date, '%Y-%m-%d')
        return date
    except ValueError:
        raise BadRequest(f'Date {date} is not valid format YYYY-MM-DD')



