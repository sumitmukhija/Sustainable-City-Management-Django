import requests
import numpy as np
import json
import os
from dotenv import load_dotenv
from rest_framework import status

# Coordinates from: https://boundingbox.klokantech.com/
SOUTH_MOST = 53.2447
NORTH_MOST = 53.44193
EAST_MOST = -6.037327
WEST_MOST = -6.465722

class PollutionUtil():
    
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
    # modifies the breezometer response to be saved in the db
        if (response is None):
            #TODO: show error
            print("Response is None for :: " + str((lat,lng)))
            return None
        else:
            data = {
                "lat": lat,
                "long":lng,
                "index_irl_epa": response['data']['indexes']['irl_epa'],
                "pollutants": response['data']['pollutants']
            }
        return data

    # Fetch data from breezometer api
    @staticmethod
    def get_geo_pollution_data(lat, lng):
        load_dotenv()
        features = "local_aqi,dominant_pollutant_concentrations,pollutants_concentrations,all_pollutants_concentrations"
        if lat is None or lng is None:
            return status.HTTP_400_BAD_REQUEST
        url = os.getenv('BREEZOMETER_BASE_URL') + os.getenv('BREEZOMETER_KEY') + '&metadata=true&features=' + features + '&lat=' + str(lat) + '&lon=' + str(lng)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return status.HTTP_500_INTERNAL_SERVER_ERROR