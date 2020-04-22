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
        response_array = []
        response_analysis_array = []
        signals = traffic_util.TrafficUtil().get_signal_coordinates()
        for s in range(signals.shape[0]):
            response = traffic_util.TrafficUtil.get_traffic_data(signals.iloc[s,0], signals.iloc[s,1])
            response["timestamp"] = timestamp
            response_for_analysis = response
            response = traffic_util.TrafficUtil.sanitize_data(response, signals.iloc[s,0], signals.iloc[s,1])
            response_for_analysis = traffic_util.TrafficUtil.sanitize_data_for_analysis(response_for_analysis, signals.iloc[s,0], signals.iloc[s,1])
            response_array.append(response)
            response_analysis_array.append(response_for_analysis)
        response = requests.post(url_stops, json={"data": json.dumps(response_array)}, headers = headers)
        response_for_analysis = requests.post(url_traffic_analysis, json={"data": json.dumps(response_analysis_array)}, headers=headers)
