import pymongo
from DataInteractions.db_connection import mongo, app
from bson.json_util import dumps
import json


class IrishRailStopDataInteractions():

    def get_latest_by_lat_long(self):
        with app.app_context():
            irishrailstop_details = mongo.db.IrishRailStops
            latest_db_records = json.loads(dumps(irishrailstop_details.find()))
            return latest_db_records

    def insert_irishrailstop_data(self, data):
        with app.app_context():
            irishrailstop_details = mongo.db.IrishRailStops
            return irishrailstop_details.insert(data)