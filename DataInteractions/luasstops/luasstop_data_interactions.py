import pymongo
from DataInteractions.db_connection import mongo, app
from bson.json_util import dumps
import json


class LuasStopDataInteractions():

    def get_latest_by_lat_long(self):
        with app.app_context():
            latest_db_records = []
            luasstop_details = mongo.db.LuasStops
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
            luasstop_all = dumps(luasstop_details.aggregate(pipeline))
            luasstop_all = json.loads(luasstop_all)
            for i in range(len(luasstop_all)):
                query = {}
                query["lat"] = luasstop_all[i]['_id']['lat']
                query["long"] = luasstop_all[i]['_id']['long']
                temp = json.loads(dumps(luasstop_details.find(query).sort("_id", pymongo.DESCENDING).limit(1)))
                latest_db_records.append(temp[0])
            return latest_db_records

    def insert_luasstop_data(self, data):
        with app.app_context():
            luasstop_details = mongo.db.LuasStops
            return luasstop_details.insert(data)