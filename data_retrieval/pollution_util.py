import requests

BREEZOMETER_KEY = "b7401295888443538a7ebe04719c8394"

# Fetch data from breezometer api
def get_geo_pollution_data(lat, lng):
    if lat is None or lng is None:
        # TODO: Show error with Error handler
        print("Latitude or longitude empty!")
        return None
    url = 'http://api.breezometer.com/air-quality/v2/current-conditions?key=' + BREEZOMETER_KEY + \
        '&metadata=true&features=breezometer_aqi,local_aqi,health_recommendations,sources_and_effects,dominant_pollutant_concentrations,pollutants_concentrations,all_pollutants_concentrations,pollutants_aqi_information&lat=' + str(lat) + '&lon=' + str(lng)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        # TODO: Show error with Error handler
        print("Handle for any other status code")
        return None

    
    
