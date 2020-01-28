import pymongo
from .db_connection import mongo, app
from bson.json_util import dumps
import ast
import json

class BikeDataInteractions():

    def get_all_objects(self):
        with app.app_context():
            bike_details = mongo.db.BikeData
            bike_all = dumps(bike_details.find())
            print(bike_all)
            bike_all = ast.literal_eval(bike_all)
            return bike_all

    def get_latest_by_lat_long(self):
        with app.app_context():
            latest_db_records = []
            bike_details = mongo.db.BikeData
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
            bike_all = dumps(bike_details.aggregate(pipeline))
            bike_all = json.loads(bike_all)
            for i in range(len(bike_all)):
                query = {}
                query["lat"] = bike_all[i]['_id']['lat']
                query["long"] = bike_all[i]['_id']['long']
                temp = json.loads(dumps(bike_details.find(query).sort("_id", pymongo.DESCENDING).limit(1)))
                latest_db_records.append(temp[0])
            return latest_db_records

    def insert_bike_data(self, data):
        with app.app_context():
            bike_details = mongo.db.BikeData
            return bike_details.insert(data)
