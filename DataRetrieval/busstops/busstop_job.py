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
        stops = busstop_util.BusStopUtil().get_bus_stop_coordinates()
        if (stops is not None):
            data = busstop_util.BusStopUtil.format_data(stops)
            response = requests.post(url, json={"data": json.dumps(data)}, headers=headers)
          