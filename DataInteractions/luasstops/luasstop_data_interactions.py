import pymongo
from DataInteractions.db_connection import mongo, app
from bson.json_util import dumps
import json


class LuasStopDataInteractions():

    def get_latest_by_lat_long(self):
        with app.app_context():
            luasstop_details = mongo.db.LuasStops
            latest_db_records = json.loads(dumps(luasstop_details.find()))
            return latest_db_records

    def insert_luasstop_data(self, data):
        with app.app_context():
            luasstop_details = mongo.db.LuasStops
            return luasstop_details.insert(data)