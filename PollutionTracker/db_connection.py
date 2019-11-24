from flask import Flask
from flask_pymongo import PyMongo
import json
import datetime
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'City_Management'
app.config['MONGO_URI'] = 'mongodb+srv://gognar:Rajat123@cluster0-vyvyz.mongodb.net/City_Management?retryWrites=true&w=majority'
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