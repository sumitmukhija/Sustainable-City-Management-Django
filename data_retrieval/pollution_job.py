from . import cron_job
from . import pollution_util as pol
<<<<<<< HEAD
=======
import datetime
import requests
import json
>>>>>>> ae564d2... Updated job to store responses using Polls post API

class PollutionJob(cron_job.CronJob):

    def run_job(self):
<<<<<<< HEAD
        sections = pol.get_city_sections()
        responses = [pol.get_geo_pollution_data(section[0], section[1]) for section in sections]
        print(responses)
    
=======
        responses = []
        timestamp = datetime.datetime.now()
        sections = pol.get_city_sections()
        # responses = [pol.get_geo_pollution_data(section[0], section[1]) for section in sections]
        for section in sections:
            lat = section[0]
            lng = section[1]
            response = pol.get_geo_pollution_data(lat, lng)
            if (response is None):
                print("response is EMPTY for:: " + str((lat, lng)))
                continue
            response = pol.sanitize_data(response, lat, lng)
            response["timestamp"] = str(timestamp)
            print("\n"+json.dumps(response))
            url = "http://10.6.39.251:8000/polls/"
            response = requests.post(url, json={"data": json.dumps(response)})
            print(response.status_code)
        
>>>>>>> ae564d2... Updated job to store responses using Polls post API
