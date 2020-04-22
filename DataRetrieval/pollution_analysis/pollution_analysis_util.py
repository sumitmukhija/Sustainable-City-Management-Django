import requests
import numpy as np
import pandas as pd
from SCMBackend.env import Environ
from rest_framework import status

from Analysis.time_series_utils import TimeSeriesUtils
    
class PollutionAnalysisUtil():
    
    @staticmethod
    def get_predictions(location):
        if(location is "" or location is None):
            return None
        model_path = "./static/models/pollution/" + location
        pred = TimeSeriesUtils.prediction(model_path, 24)
        return pred
