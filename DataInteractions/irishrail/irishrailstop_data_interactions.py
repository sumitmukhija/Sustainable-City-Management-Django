import pymongo
from DataInteractions.db_connection import mongo, app
from bson.json_util import dumps
import json


class IrishRailStopDataInteractions():

    def get_latest_by_lat_long(self):
        with app.app_context():
            latest_db_records = []
            irishrailstop_details = mongo.db.IrishRailStops
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
            irishrailstop_all = dumps(irishrailstop_details.aggregate(pipeline))
            irishrailstop_all = json.loads(irishrailstop_all)
            for i in range(len(irishrailstop_all)):
                query = {}
                query["lat"] = irishrailstop_all[i]['_id']['lat']
                query["long"] = irishrailstop_all[i]['_id']['long']
                temp = json.loads(dumps(irishrailstop_details.find(query).sort("_id", pymongo.DESCENDING).limit(1)))
                latest_db_records.append(temp[0])
            return latest_db_records

    def insert_irishrailstop_data(self, data):
        with app.app_context():
            irishrailstop_details = mongo.db.IrishRailStops
            return irishrailstop_details.insert(data)