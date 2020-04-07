from DataRetrieval import cron_job
from DataRetrieval.bike_analysis import bike_analysis_util
import datetime
import requests
import os
import json
from SCMBackend.env import Environ

class BikeAnalysisJob(cron_job.CronJob):

    def run_job(self):
        # url = Environ().get_base_bus_stop_url()
        # bikes_data = bike_analysis_util.BikeUtil.get_dublin_bikes_data()
        # response = bike_analysis_util.BikeUtil.format_dublin_bikes_data(bikes_data)
        # response = requests.post(url, json={"data": json.dumps(response)})
        pred = bike_analysis_util.BikeAnalysisUtil.get_predictions(os.getenv("BIKE_ANALYSIS_PATH")+ stop + "/", 20)
