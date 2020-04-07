from DataRetrieval import cron_job
from DataRetrieval.irishrail import irishrailstop_util
from SCMBackend.env import Environ
from DataInteractions.test_utils import TestUtils
import requests
import json
import datetime


class IrishRailJob(cron_job.CronJob):

    def run_job(self):
        headers = {"Authorization": TestUtils().get_valid_auth()}
        timestamp = str(datetime.datetime.now())
        url = Environ().get_base_irish_rail_stop_url()
        stops = irishrailstop_util.IrishRailUtil().get_irish_rail_stop_coordinates()
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
            pass