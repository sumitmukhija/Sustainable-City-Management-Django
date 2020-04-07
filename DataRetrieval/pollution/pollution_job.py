import DataRetrieval.cron_job as cronJob
from DataRetrieval.pollution import pollution_util
import datetime
import os
import requests
import json
from SCMBackend.env import Environ
from DataInteractions.test_utils import TestUtils

class PollutionJob(cronJob.CronJob):

    '''Cron job for getting pollution data for the grid coordinates'''
    def run_job(self):
        headers = {"Authorization": TestUtils().get_valid_auth()}
        timestamp = str(datetime.datetime.now())
        sections = pollution_util.PollutionUtil.get_city_sections()
        data = []
        url = Environ().get_base_pollution_url()
        for section in sections:
            response = pollution_util.PollutionUtil.get_geo_pollution_data(section[0], section[1])
            if (response is None):
                continue
            else:
                response = pollution_util.PollutionUtil.sanitize_data(response, section[0], section[1])
                response["timestamp"] = timestamp
                data.append(response)
                response = requests.post(url, json={"data": json.dumps(data)}, headers=headers)
                