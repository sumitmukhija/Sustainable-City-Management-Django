#from .models import PollutionDetails
#from .serializers import PollSerializer
from flask import Flask, jsonify
from flask_pymongo import PyMongo
#from .db_connection import MongoConnection
from .db_connection import mongo, app
from bson.json_util import dumps
import ast


class PollutionDataInteractions():

    def get_all_objects(self):
        with app.app_context():
            pollution_details = mongo.db.BreezoMeter
            poll_all = dumps(pollution_details.find())
            print(poll_all)
            poll_all = ast.literal_eval(poll_all)
            return ({"Results":poll_all})

    def insert_poll_data(self, data):
        with app.app_context():
            pollution_details = mongo.db.BreezoMeter
            pollution_details.insert(data)
