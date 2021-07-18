"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request
from flask_restplus import Resource

from .security import require_auth
from . import api_rest
from .func import *
from .engine import *       # wildcard import the TTDS lib

class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        # return {'timestamp': timestamp}
        return {'hello': 'world'}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}


# this is the example hardcode test
@api_rest.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World'}

    def post(self):
        return {'Hello' : 'Post'}

@api_rest.route('/demo10')

class demo10Recipes(Resource):
    def get(self):
        return csv2json('sample.csv', 10)
    
    def post(self):
        return csv2json('sample.csv', 10)


@api_rest.route('/search')
class SearchEntry(Resource):
    def post(self):
        data = request.get_json()
        received = data['data']
        return engine_init(received['key'], received['para'])


