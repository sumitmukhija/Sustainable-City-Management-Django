import os
import requests
from rest_framework import status
from dotenv import load_dotenv

from Analysis.time_series_utils import TimeSeriesUtils


load_dotenv()
DUBLIN_BIKES_KEY = os.getenv("DUBLIN_BIKES_KEY")
DUBLIN_BIKES_URL = os.getenv("DUBLIN_BIKES_URL")
BIKES_ANALYSIS = os.getenv("BIKE_ANALYSIS_PATH")

class BikeAnalysisUtil():
    
    @staticmethod
    def getAPIKey():
        return DUBLIN_BIKES_KEY

    @staticmethod
    def get_dublin_bikes_data():
        if(DUBLIN_BIKES_KEY is None):
            return status.HTTP_400_BAD_REQUEST
        URL = DUBLIN_BIKES_URL + "&apiKey=" + DUBLIN_BIKES_KEY
        response = requests.get(URL)
        if(status.HTTP_200_OK):
            return response.json()
        else:
            return status.HTTP_500_INTERNAL_SERVER_ERROR

    @staticmethod
    def format_dublin_bikes_data(data):
        dublin_bikes_data = []
        for record in data:
            bikes_record = {}
            bikes_record = record
            if("address" in bikes_record.keys()):
                del bikes_record["address"]
            if("position" in bikes_record.keys()):
                bikes_record["lat"] = record["position"]["lat"]
                bikes_record["long"] = record["position"]["lng"]
                del bikes_record["position"]
            dublin_bikes_data.append(bikes_record)
        return dublin_bikes_data

    @staticmethod
    def get_predictions(stop):
        model_path = "./static/models/bikes/" + stop
        pred = TimeSeriesUtils.prediction(model_path, 20)
        return pred