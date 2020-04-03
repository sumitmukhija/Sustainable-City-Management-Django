from DataRetrieval import cron_job
from DataRetrieval.bike import bike_util
import datetime
import requests
import os
import json
from SCMBackend.env import Environ
from Analysis.time_series_utils import TimeSeriesUtils

class BikeJob(cron_job.CronJob):

    def run_job(self):
        url = Environ().get_base_bus_stop_url()
        bikes_data = bike_util.BikeUtil.get_dublin_bikes_data()
        response = bike_util.BikeUtil.format_dublin_bikes_data(bikes_data)
        for stop in response:
            TimeSeriesUtils.update_model(stop['available_bikes'], stop['name'])
        response = requests.post(url, json={"data": json.dumps(response)})

