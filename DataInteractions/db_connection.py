from flask import Flask
from flask_pymongo import PyMongo
import json
import datetime
import os
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'City_Management'
app.config['MONGO_URI'] = os.getenv('MONGO_HOST')

mongo = PyMongo(app)

class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)
app.json_encoder = JSONEncoder
