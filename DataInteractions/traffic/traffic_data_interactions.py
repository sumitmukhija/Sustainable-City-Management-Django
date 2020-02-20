import pymongo
from DataInteractions.db_connection import mongo, app
from bson.json_util import dumps
import json


class TrafficDataInteractions():

    def get_latest_by_lat_long(self):
        with app.app_context():
            latest_db_records = []
            traffic_details = mongo.db.TrafficData
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
            traffic_all = dumps(traffic_details.aggregate(pipeline))
            traffic_all = json.loads(traffic_all)
            for i in range(len(traffic_all)):
                query = {}
                query["lat"] = traffic_all[i]['_id']['lat']
                query["long"] = traffic_all[i]['_id']['long']
                temp = json.loads(dumps(traffic_details.find(query).sort("_id", pymongo.DESCENDING).limit(1)))
                latest_db_records.append(temp[0])
            return latest_db_records

    def insert_traffic_data(self, data):
        with app.app_context():
            traffic_details = mongo.db.TrafficData
            return traffic_details.insert(data)
