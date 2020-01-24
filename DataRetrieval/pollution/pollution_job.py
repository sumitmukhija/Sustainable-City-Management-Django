import DataRetrieval.cron_job as cronJob
from DataRetrieval.pollution import pollution_util
import datetime
import requests
import json


class PollutionJob(cronJob.CronJob):

    '''Cron job for getting pollution data for the grid coordinates'''
    def run_job(self):
        timestamp = datetime.datetime.now()
        sections = pollution_util.PollutionUtil.get_city_sections()
        for section in sections:
            response = pollution_util.PollutionUtil.get_geo_pollution_data(section[0], section[1])
            if (response is None):
                continue
            response = pollution_util.PollutionUtil.sanitize_data(response, section[0], section[1])
            response["timestamp"] = str(timestamp)
            url = "http://127.0.0.1:8000/polls/"
            response = requests.post(url, json={"data": json.dumps(response)})
            print(response.status_code)