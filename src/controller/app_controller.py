from flask_restful import Resource
from http_config import response_formatter

import sample_service

class SampleController(Resource):
    def get(self):
        return response_formatter(sample_service.sample_service_function(), 201)
