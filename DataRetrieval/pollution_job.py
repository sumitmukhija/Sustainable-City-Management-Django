from . import cron_job
from . import pollution_util as pol
import datetime
import requests
import os
import json
from dotenv import load_dotenv

class PollutionJob(cron_job.CronJob):

    def run_job(self):
        load_dotenv()
        responses = []
        timestamp = datetime.datetime.now()
        sections = pol.get_city_sections()
        for section in sections:
            lat = section[0]
            lng = section[1]
            response = pol.get_geo_pollution_data(lat, lng)
            if (response is None):
                continue
            response = pol.sanitize_data(response, lat, lng)
            response["timestamp"] = str(timestamp)
            print("\n"+json.dumps(response))
            url = os.getenv('BASE_SERVER_URL')+"polls/"
            response = requests.post(url, json={"data": json.dumps(response)})
            print(response.status_code)
        
