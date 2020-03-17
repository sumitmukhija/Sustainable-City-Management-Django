from DataRetrieval import cron_job
from DataRetrieval.traffic import traffic_util
from SCMBackend.env import Environ
from DataInteractions.test_utils import TestUtils
import datetime
import requests
import json

class TrafficJob(cron_job.CronJob):

    def run_job(self):
        headers = {"Authorization": TestUtils().get_valid_auth()}
        url_stops = Environ().get_base_traffic_url()
        url_traffic_analysis = url_stops + "/analysis"
        timestamp = datetime.datetime.now()
        signals = traffic_util.TrafficUtil().get_signal_coordinates()
        for s in range(signals.shape[0]):
            response = traffic_util.TrafficUtil.get_traffic_data(signals.iloc[s,0], signals.iloc[s,1])
            response["timestamp"] = timestamp
            response_for_analysis = response
            if (response is None):
                continue
            response = traffic_util.TrafficUtil.sanitize_data(response, signals.iloc[s,0], signals.iloc[s,1])
            response_for_analysis = traffic_util.TrafficUtil.sanitize_data_for_analysis(response_for_analysis, signals.iloc[s,0], signals.iloc[s,1])
            response = requests.post(url_stops, json={"data": json.dumps(response)}, headers = headers)
            response_for_analysis = requests.post(url_traffic_analysis, json={"data": json.dumps(response_for_analysis)}, headers=headers)
