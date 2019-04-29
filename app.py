from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api
from json import dumps
import json
from flask_cors import CORS

import sys
import os

project_root = os.path.dirname(os.path.realpath(os.path.join(__file__, '.')))
sys.path.append(os.path.join(project_root, 'src', 'controller'))
sys.path.append(os.path.join(project_root, 'src', 'service'))
sys.path.append(os.path.join(project_root, 'src', 'repository'))
sys.path.append(os.path.join(project_root, 'src', 'utilities'))

import app_controller

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(app_controller.SampleController, '/api/sampleapi')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3001)
