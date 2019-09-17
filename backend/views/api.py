# Contributor(s): Adrian Gose
# If you worked on this file, add your name above so we can keep track of contributions

from flask import Blueprint
from flask_restplus import Api

# Define API blueprints and API spec for flask
apiv1 = Blueprint('api', __name__)
api = Api(apiv1, version='1.0', title='HomeIOT API',
          description='The HomeIOT Application REST API for CS499 Team 5')

# Define namespaces
locations_ns = api.namespace('locations', 'Location methods')
stats_ns = api.namespace('stats', 'Stats methods')