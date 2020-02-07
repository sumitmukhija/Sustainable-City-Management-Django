import os
import requests
import numpy as np
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
    def getAPIKey():
        return os.getenv('TOMTOM_API_KEY')

    @staticmethod
    def get_traffic_data(lat, lng):
        if(TOMTOM_API_KEY is None):
            return status.HTTP_400_BAD_REQUEST
        if lat is None and lng is None:
            return status.HTTP_400_BAD_REQUEST
        URL = TOMTOM_TRAFFIC_BASE_URL + "&point=" + str(lat) + "%2C" + str(lng) + "&key=" + TOMTOM_API_KEY
        response = requests.get(URL)
        if(status.HTTP_200_OK):
            # print("response:", response.json())
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
    def get_city_sections(number_of_sections=10):
        sections = list()
        for x in np.linspace(SOUTH_MOST, NORTH_MOST, number_of_sections):
            for y in np.linspace(WEST_MOST, EAST_MOST, number_of_sections):
                sections.append((x, y))
        return sections

    @staticmethod
    def sanitize_data(response, lat, lng):
        print("LAT: ", lat)
        print("LONG: ", lng)
    # modifies the breezometer response to be saved in the db
        if (response is None):
            #TODO: show error
            print("Response is None for :: " + str((lat,lng)))
            return None
        elif('httpStatusCode' in response and response['httpStatusCode'] == 400):
            return None
        else:
            data = {
                "lat" : lat,
                "long" : lng,
# "currentSpeed": 75, "freeFlowSpeed": 75, "currentTravelTime": 41, "freeFlowTravelTime": 41, "confidence": 0.949999988079071, "roadClosure": False, "coordinates"
                "currentSpeed" : response["flowSegmentData"]["currentSpeed"],
                "freeFlowSpeed" : response["flowSegmentData"]["freeFlowSpeed"],
                "currentTravelTime" : response["flowSegmentData"]["currentTravelTime"],
                "freeFlowTravelTime" : response["flowSegmentData"]["freeFlowTravelTime"],
                "confidence" : response["flowSegmentData"]["confidence"],
                "roadClosure" : response["flowSegmentData"]["roadClosure"],
                "coordinates" : response["flowSegmentData"]["coordinates"]
            }
            print("DATA: ", data)
        return data

if __name__ == "__main__":
    sections = TrafficUtil().get_city_sections()
    for section in sections:
        response = TrafficUtil.get_traffic_data(section[0], section[1])
        if (response is None):
            continue
        else:
            print("SANITIZING DATA:")
            response = TrafficUtil.sanitize_data(response, section[0], section[1])
    