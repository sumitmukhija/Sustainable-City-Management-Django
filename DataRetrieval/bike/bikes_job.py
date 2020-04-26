from DataRetrieval import cron_job
from DataRetrieval.bike import bike_util
from SCMBackend.env import Environ
from DataInteractions.test_utils import TestUtils
import datetime
import requests
import os
import json
from SCMBackend.env import Environ
from Analysis.time_series_utils import TimeSeriesUtils

class BikeJob(cron_job.CronJob):

    def run_job(self):
        headers = {"Authorization": TestUtils().get_valid_auth()}
        url = Environ().get_base_bike_url()
        bikes_data = bike_util.BikeUtil.get_dublin_bikes_data()
        response = bike_util.BikeUtil.format_dublin_bikes_data(bikes_data)
        for stop in response:
            TimeSeriesUtils.update_model(stop['available_bikes'], stop['name'], 'bikes')
        response = requests.post(url, json={"data": json.dumps(response)}, headers=headers)

