from DataRetrieval import cron_job
from DataRetrieval.busstops import busstop_util
import requests
import json
from SCMBackend.env import Environ

class BusJob(cron_job.CronJob):

    def run_job(self):
        url = Environ().get_base_bus_stop_url()
        stops = busstop_util.BusStopUtil().get_bus_stop_coordinates()
        if (stops is not None):
            for s in range(stops.shape[0]):
                data = {
                    "StopID": stops.iloc[s, 0],
                    "StopName": stops.iloc[s, 1],
                    "lat": stops.iloc[s, 2],
                    "long": stops.iloc[s, 3]
                }
            response = requests.post(url, json={"data": json.dumps(data)})
        else:
            print("Bus Stop data unavailable")