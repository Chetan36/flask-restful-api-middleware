from flask import request
from flask_restful import Resource
from http_config import response_formatter

import user_service

class RegisterUser(Resource):
    def post(self):
        return response_formatter(user_service.add_user(request.json), 201)

class AllUsers(Resource):
    def get(self):
        return response_formatter(user_service.get_all_users(), 200)

class UserById(Resource):
    def get(self, user_id):
        return response_formatter(user_service.get_user_by_id(user_id), 200)

    def put(self, user_id):
        return response_formatter(user_service.update_user(user_id, request.json), 200)
