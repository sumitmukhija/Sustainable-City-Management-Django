from DataRetrieval import cron_job
from DataRetrieval.busstops import busstop_util
from SCMBackend.env import Environ
from DataInteractions.test_utils import TestUtils
import requests
import json
import datetime

class BusJob(cron_job.CronJob):

    def run_job(self):
        headers = {"Authorization": TestUtils().get_valid_auth()}
        url = Environ().get_base_bus_stop_url()
        timestamp = str(datetime.datetime.now())
        stops = busstop_util.BusStopUtil().get_bus_stop_coordinates()
        if (stops is not None):
            for s in range(stops.shape[0]):
                data = {
                    "StopID": stops.iloc[s, 0],
                    "StopName": stops.iloc[s, 1],
                    "lat": stops.iloc[s, 2],
                    "long": stops.iloc[s, 3],
                    "timestamp": timestamp
                }
            response = requests.post(url, json={"data": json.dumps(data)}, headers=headers)
        else:
            print("Bus Stop data unavailable")