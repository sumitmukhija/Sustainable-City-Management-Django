import data_retrieval.cron_job as cj
import data_retrieval.pollution.pollution_util
import datetime
import requests
import json

class PollutionJob(cj.CronJob):

    def run_job(self):
        responses = []
        timestamp = datetime.datetime.now()
        sections = pollution_util.PollutionUtil.get_city_sections()
        # responses = [pol.get_geo_pollution_data(section[0], section[1]) for section in sections]
        for section in sections:
            lat = section[0]
            lng = section[1]
            response = pollution_util.PollutionUtil.get_geo_pollution_data(lat, lng)
            if (response is None):
                print("response is EMPTY for:: " + str((lat, lng)))
                continue
            response = pollution_util.PollutionUtil.sanitize_data(
                response, lat, lng)
            response["timestamp"] = str(timestamp)
            print("\n"+json.dumps(response))
            url = "http://10.6.39.251:8000/polls/"
            response = requests.post(url, json={"data": json.dumps(response)})
            # print(response.status_code)
