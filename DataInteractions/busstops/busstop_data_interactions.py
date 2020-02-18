import pymongo
from DataInteractions.db_connection import mongo, app
from bson.json_util import dumps
import json


class BusStopDataInteractions():

    def get_latest_by_lat_long(self):
        with app.app_context():
            latest_db_records = []
            busstop_details = mongo.db.BusStops
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
            busstop_all = dumps(busstop_details.aggregate(pipeline))
            busstop_all = json.loads(busstop_all)
            for i in range(len(busstop_all)):
                query = {}
                query["lat"] = busstop_all[i]['_id']['lat']
                query["long"] = busstop_all[i]['_id']['long']
                temp = json.loads(dumps(busstop_details.find(query).sort("_id", pymongo.DESCENDING).limit(1)))
                latest_db_records.append(temp[0])
            return latest_db_records

    def insert_busstop_data(self, data):
        with app.app_context():
            busstop_details = mongo.db.BusStops
            return busstop_details.insert(data)
