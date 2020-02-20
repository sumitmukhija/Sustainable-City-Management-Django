import pymongo
from DataInteractions.db_connection import mongo, app
from bson.json_util import dumps
import ast
import json

class PollutionDataInteractions():

    def get_all_objects(self):
        with app.app_context():
            pollution_details = mongo.db.BreezoMeter
            poll_all = dumps(pollution_details.find())
            poll_all = ast.literal_eval(poll_all)
            return poll_all

    def get_latest_by_lat_long(self):
        with app.app_context():
            latest_db_records = []
            pollution_details = mongo.db.BreezoMeter
            pipeline = [
               {
                   u"$group": {
                       u"_id": {
                           u"lat": u"$lat",
                           u"long": u"$long"
                       }
                   }
               }
            ]
            poll_all = dumps(pollution_details.aggregate(pipeline))
            poll_all = json.loads(poll_all)
            for i in range(len(poll_all)):
                query = {}
                query["lat"] = poll_all[i]['_id']['lat']
                query["long"] = poll_all[i]['_id']['long']
                temp = json.loads(dumps(pollution_details.find(query).sort("_id", pymongo.DESCENDING).limit(1)))
                latest_db_records.append(temp[0])
            return latest_db_records

    def insert_poll_data(self, data):
        with app.app_context():
            pollution_details = mongo.db.BreezoMeter
            return pollution_details.insert(data)
