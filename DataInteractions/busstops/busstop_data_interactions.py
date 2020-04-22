from DataInteractions.db_connection import mongo, app
from bson.json_util import dumps
import json


class BusStopDataInteractions():

    def get_latest_by_lat_long(self):
        with app.app_context():
            busstop_details = mongo.db.BusStops
            latest_db_records = json.loads(dumps(busstop_details.find()))
            return latest_db_records

    def insert_busstop_data(self, data):
        with app.app_context():
            busstop_details = mongo.db.BusStops
            return busstop_details.insert(data)
