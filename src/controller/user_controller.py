from flask import request
from flask_restful import Resource
from http_config import response_formatter

import user_service

class RegisterUser(Resource):
    def post(self):
        return response_formatter(user_service.add_user(request.json), 201)

class GetAllUsers(Resource):
    def get(self):
        return response_formatter(user_service.get_all_users(), 200)
