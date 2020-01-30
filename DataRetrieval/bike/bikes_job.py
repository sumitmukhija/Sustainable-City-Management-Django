from DataRetrieval import cron_job
from DataRetrieval.bike import bike_util
import datetime
import requests
import os
import json
from dotenv import load_dotenv

class BikeJob(cron_job.CronJob):

    def run_job(self):
        load_dotenv()
        responses = []
        timestamp = datetime.datetime.now()
        bikes_data = bike_util.BikeUtil.get_dublin_bikes_data()
        response = bike_util.BikeUtil.format_dublin_bikes_data(bikes_data)
        url = os.getenv('LOCALHOST')+"/data/bikes/"
        response = requests.post(url, json={"data": json.dumps(response)})
        
