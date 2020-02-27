import os
import requests
import numpy as np
import pandas as pd
from rest_framework import status
from dotenv import load_dotenv


load_dotenv()
TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY")
TOMTOM_TRAFFIC_BASE_URL = os.getenv("TOMTOM_TRAFFIC_BASE_URL")

# Coordinates from: https://boundingbox.klokantech.com/
SOUTH_MOST = 53.2447
NORTH_MOST = 53.44193
EAST_MOST = -6.037327
WEST_MOST = -6.465722

class TrafficUtil():

    @staticmethod
    def get_signal_coordinates():
        signals = pd.read_excel("./DublinSignalData.xlsx", index_col=0)
        return signals

    @staticmethod
    def getAPIKey():
        return TOMTOM_API_KEY

    @staticmethod
    def get_traffic_data(lat, lng):
        if(TOMTOM_API_KEY is None):
            return status.HTTP_400_BAD_REQUEST
        if lat is None and lng is None:
            return status.HTTP_400_BAD_REQUEST
        URL = TOMTOM_TRAFFIC_BASE_URL + "&point=" + str(lat) + "%2C" + str(lng) + "&key=" + TOMTOM_API_KEY
        response = requests.get(URL)
        if(status.HTTP_200_OK):
            return response.json()
        else:
            return status.HTTP_500_INTERNAL_SERVER_ERROR

    @staticmethod
    def get_offset_NS(number_of_sections):
        return (NORTH_MOST - SOUTH_MOST) /number_of_sections
    
    @staticmethod
    def get_offset_EW(number_of_sections):
        return (EAST_MOST - WEST_MOST)/number_of_sections

    @staticmethod
    def get_city_sections(filename="CityClusters.csv"):
        try:
            contents = pd.read_csv("./"+filename, encoding="ISO-8859-1")
            if contents is None:
                raise Exception(filename, "either empty or cannot be read.")
            sections = [tuple(x) for x in contents.values]
            return sections
        except FileNotFoundError:
            print(filename, "not found")

    @staticmethod
    def sanitize_data(response, lat, lng):
    # modifies the breezometer response to be saved in the db
        if (response is None):
            #TODO: show error
            print("Response is None for :: " + str((lat,lng)))
            return None
        elif('httpStatusCode' in response and response['httpStatusCode'] == status.HTTP_400_BAD_REQUEST):
            return None
        else:
            curSpeed = response["flowSegmentData"]["currentSpeed"]
            freeSpeed = response["flowSegmentData"]["freeFlowSpeed"]

            if curSpeed/freeSpeed <= 0.6:
                if curSpeed / freeSpeed <= 0.2:
                    color = "#ff0000x"
                else:
                    color = "#FFBF00"
            else:
                color = "#00b300"
            data = {
                "lat" : lat,
                "long" : lng,
                "color" : color,
                "currentSpeed" : response["flowSegmentData"]["currentSpeed"],
                "freeFlowSpeed" : response["flowSegmentData"]["freeFlowSpeed"],
                "currentTravelTime" : response["flowSegmentData"]["currentTravelTime"],
                "freeFlowTravelTime" : response["flowSegmentData"]["freeFlowTravelTime"],
                "confidence" : response["flowSegmentData"]["confidence"],
                "roadClosure" : response["flowSegmentData"]["roadClosure"],
                "coordinates" : response["flowSegmentData"]["coordinates"]
            }
        return data
