from DataRetrieval import cron_job
from DataRetrieval.luasstops import luasstop_util
import requests
import json
from SCMBackend.env import Environ


class LuasJob(cron_job.CronJob):

    def run_job(self):
        url = Environ().get_base_luas_stop_url()
        stops = luasstop_util.LuasStopUtil().get_luas_stop_coordinates()
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
            print("Luas Stop data unavailable")
