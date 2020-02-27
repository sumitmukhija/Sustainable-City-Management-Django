import requests
import numpy as np
import pandas as pd
from SCMBackend.env import Environ
from rest_framework import status

# Coordinates from: https://boundingbox.klokantech.com/
SOUTH_MOST = 53.2447
NORTH_MOST = 53.44193
EAST_MOST = -6.037327
WEST_MOST = -6.465722
    
class PollutionUtil():
    
    @staticmethod
    def get_offset_NS(number_of_sections):
        """
        WARNING: This methods is either depricated or the caller is deprecated
        """
        return (NORTH_MOST - SOUTH_MOST) /number_of_sections
    
    @staticmethod
    def get_offset_EW(number_of_sections):
        """
        WARNING: This methods is either depricated or the caller is deprecated
        """
        return (EAST_MOST - WEST_MOST)/number_of_sections

    @staticmethod
    @DeprecationWarning
    def get_city_secions_by_grid(number_of_sections=10):
        """
        WARNING: This methods is either depricated or the caller is deprecated.
        Previously named get_city_sections
        """
        sections = list()
        for x in np.linspace(SOUTH_MOST, NORTH_MOST, number_of_sections):
            for y in np.linspace(WEST_MOST, EAST_MOST, number_of_sections):
                sections.append((x, y))
        return sections

    @staticmethod
    def get_city_sections(filename="CityClusters.csv"):
        try:
            contents = pd.read_csv("./static/data/csv/"+filename, encoding="ISO-8859-1")
            if contents is None:
                raise Exception(filename, "either empty or cannot be read.")
            sections = [tuple(x) for x in contents.values]
            return sections
        except FileNotFoundError:
            print(filename, "not found")

    @staticmethod
    def sanitize_data(response, lat, lng):
        if (response is None):
            #TODO: show error
            print("Response is None for :: " + str((lat,lng)))
            return None
        else:
            data = {
                "lat": lat,
                "long":lng,
                "index_irl_epa": response['data']['indexes']['baqi'],
                # changed value from index_irl_epa to baqi. Key not changed to avoid breaking frontend
                "pollutants": response['data']['pollutants']
            }
        return data

    # Fetch data from breezometer api
    @staticmethod
    def get_geo_pollution_data(lat, lng):
        BREEZOMETER_KEY = Environ().get_breezometer_api_key()
        BASE_URL = Environ().get_breezometer_base_url()
        features = "local_aqi,dominant_pollutant_concentrations,pollutants_concentrations,all_pollutants_concentrations"
        if lat is None or lng is None:
            return status.HTTP_400_BAD_REQUEST
        url = BASE_URL + BREEZOMETER_KEY + \
            '&metadata=true&features=' + features + \
            '&lat=' + str(lat) + '&lon=' + str(lng)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return status.HTTP_500_INTERNAL_SERVER_ERROR
            
