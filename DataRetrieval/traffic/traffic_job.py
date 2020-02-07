from DataRetrieval import cron_job
from DataRetrieval.traffic import traffic_util
import datetime
import requests
import os
import json
from dotenv import load_dotenv

class TrafficJob(cron_job.CronJob):

    def run_job(self):
        load_dotenv()
        responses = []
        timestamp = datetime.datetime.now()
        sections = traffic_util.TrafficUtil().get_city_sections()
        for section in sections:
            response = traffic_util.TrafficUtil.get_traffic_data()(section[0], section[1])
            if (response is None):
                continue
            response = traffic_util.TrafficUtil.sanitize_data(response, section[0], section[1])
        url = os.getenv('LOCALHOST')+"/data/traffic/"
        response = requests.post(url, json={"data": json.dumps(response)})
        
