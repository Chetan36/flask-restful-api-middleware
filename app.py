from flask import Flask, request, Response, jsonify, send_from_directory
from flask_restful import Resource, Api
from json import dumps
import json
from flask_cors import CORS

# Initialize app and enable cors to it
app = Flask(__name__, static_folder="public")
CORS(app)
api = Api(app)

# Register all the folder structures inside src and their path
import sys
import os
project_root = os.path.dirname(os.path.realpath(os.path.join(__file__, '.')))
sys.path.append(os.path.join(project_root, 'src', 'controller'))
sys.path.append(os.path.join(project_root, 'src', 'service'))
sys.path.append(os.path.join(project_root, 'src', 'repository'))
sys.path.append(os.path.join(project_root, 'src', 'utilities'))

# Database connection initiate
import database_config

@app.route('/')
def serve_page():
    return send_from_directory('public', 'index.html')

# App controller REST routes
import app_controller
api.add_resource(app_controller.SampleController, '/api/sampleapi')

# User controller REST routes
import user_controller
api.add_resource(user_controller.RegisterUser, '/api/user/register')
api.add_resource(user_controller.AllUsers, '/api/user')
api.add_resource(user_controller.UserById, '/api/user/<string:user_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3001)
