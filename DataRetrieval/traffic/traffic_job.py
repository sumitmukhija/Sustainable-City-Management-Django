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
        url = os.getenv('LOCALHOST') + "/data/traffic/"
        responses = []
        timestamp = datetime.datetime.now()
        sections = traffic_util.TrafficUtil().get_city_sections()
        signals = traffic_util.TrafficUtil().get_signal_coordinates()
        for s in range(signals.shape[0]):
            response = traffic_util.TrafficUtil.get_traffic_data(signals.iloc[s,0], signals.iloc[s,1])
            if (response is None):
                continue
            response = traffic_util.TrafficUtil.sanitize_data(response, signals.iloc[s,0], signals.iloc[s,1])
            response = requests.post(url, json={"data": json.dumps(response)})
        
