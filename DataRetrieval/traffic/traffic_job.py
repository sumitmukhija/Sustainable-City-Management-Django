from DataRetrieval import cron_job
from DataRetrieval.traffic import traffic_util
from SCMBackend.env import Environ
import datetime
import requests
import json

class TrafficJob(cron_job.CronJob):

    def run_job(self):
        url = Environ.get_base_traffic_url()
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
        
