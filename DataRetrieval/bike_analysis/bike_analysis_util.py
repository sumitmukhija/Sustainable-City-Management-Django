import os
import requests
from rest_framework import status
from dotenv import load_dotenv

from Analysis.time_series_utils import TimeSeriesUtils

class BikeAnalysisUtil():
    
    @staticmethod
    def get_predictions(stop):
        model_path = "./static/models/bikes/" + stop
        try:
            pred = TimeSeriesUtils.prediction(model_path, 20)
            return pred
        except:
            return None