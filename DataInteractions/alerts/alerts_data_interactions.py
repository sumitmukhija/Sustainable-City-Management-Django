import pymongo
from DataInteractions.db_connection import mongo, app
from bson.json_util import dumps
import json
from bson import ObjectId


class AlertsDataInteractions():

    def get_alerts(self):
        with app.app_context():
            latest_db_records = []
            alerts_details = mongo.db.Alerts
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
            alerts_all = dumps(alerts_details.aggregate(pipeline))
            alerts_all = json.loads(alerts_all)
            for i in range(len(alerts_all)):
                query = {}
                query["lat"] = alerts_all[i]['_id']['lat']
                query["long"] = alerts_all[i]['_id']['long']
                temp = json.loads(dumps(alerts_details.find(query).sort("_id", pymongo.DESCENDING).limit(1)))
                latest_db_records.append(temp[0])
            return latest_db_records

    def update_alerts(self, data):
        with app.app_context():
            alerts_details = mongo.db.Alerts
            return alerts_details.insert(data)

    def insert_alerts(self, data):
        with app.app_context():
            alert_details = mongo.db.Alerts 
            return alert_details.insert(data)

    def update_alert(self, data):
        with app.app_context():
            alert_details = mongo.db.Alerts
            query = { "_id" : ObjectId(""+data["_id"]["$oid"]+"")}
            newValues = {
                "$set" : {
                    "status" : "forwarded"
                }
            }
            return alert_details.update_one(query, newValues, False)
