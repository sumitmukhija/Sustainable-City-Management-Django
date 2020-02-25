import pymongo
from DataInteractions.db_connection import mongo, app
from bson.json_util import dumps
import ast
import json
from django.core.cache import cache
from DataInteractions.alerts.alerts_data_interactions import AlertsDataInteractions
import time
import datetime;

class BikeDataInteractions():

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
                if temp[0]['available_bikes'] == 16:
                    cache.set("isAlertPresent", True, timeout=None)
                    newDict = {}
                    newDict['lat'] = temp[0]['lat']
                    newDict['long'] = temp[0]['long']
                    newDict['type'] = 'bike'
                    newDict['status'] = 'New'
                    newDict['timestamp'] = str(datetime.datetime.now())
                    AlertsDataInteractions().insert_alerts(newDict)
                latest_db_records.append(temp[0])
            return latest_db_records

    def insert_bike_data(self, data):
        with app.app_context():
            bike_details = mongo.db.BikeData
            return bike_details.insert(data)
