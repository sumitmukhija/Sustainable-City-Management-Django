from django.test import TestCase
from . import pollution_util as pu
from json_schema import json_schema

class PollutionTest(TestCase):

    def test(self):
        self.test_breeze_api()


    def test_breeze_api(self):
        # No longitude. Should return None
        json_response = pu.get_geo_pollution_data(53.2329, None)
        self.assertIsNone(json_response, "No longitude")

        # No latitude and longitude. Should return None
        json_response = pu.get_geo_pollution_data(None, None)
        self.assertIsNone(json_response, "No lat/long")

        # No lat. Should return None
        json_response = pu.get_geo_pollution_data(None, -6.1136)
        self.assertIsNone(json_response, "No longitude")
        
        # Check for data keyjson_response = pu.get_geo_pollution_data(53.2329, -6.1136)
        json_response = pu.get_geo_pollution_data(53.2329, -6.1136)
        self.assertIsNotNone(json_response['data'], "Data key absent")

        # JSON shouldn't be empty
        json_response = pu.get_geo_pollution_data(53.2329, -6.1136)
        self.assertIsNotNone(json_response, "Empty JSON")

        # Check for all keys
        # sample_json = {'metadata': {'timestamp': '2019-11-14T12:20:55Z', 'location': {'country': 'Ireland'}, 'indexes': {'baqi': {'pollutants': ['co', 'no2', 'o3', 'pm10', 'pm25', 'so2']}, 'irl_epa': {'pollutants': ['no2', 'o3', 'pm10', 'pm25', 'so2']}}}, 'data': {'datetime': '2019-11-14T12:00:00Z', 'data_available': True, 'indexes': {'baqi': {'display_name': 'BreezoMeter AQI', 'aqi': 78, 'aqi_display': '78', 'color': '#60C134', 'category': 'Good air quality', 'dominant_pollutant': 'o3'}, 'irl_epa': {'display_name': 'AQIH (IE)', 'aqi': 2, 'aqi_display': '2', 'color': '#62BB3D', 'category': 'Good air quality', 'dominant_pollutant': 'o3'}}, 'pollutants': {'co': {'display_name': 'CO', 'full_name': 'Carbon monoxide', 'aqi_information': {'baqi': {'display_name': 'BreezoMeter AQI', 'aqi': 100, 'aqi_display': '100', 'color': '#009E3A', 'category': 'Excellent air quality'}}, 'concentration': {'value': 0.22, 'units': 'ppb'}, 'sources_and_effects': {'sources': 'Typically originates from incomplete combustion of carbon fuels, such as that which occurs in car engines and power plants.', 'effects': 'When inhaled, carbon monoxide can prevent the blood from carrying oxygen. Exposure may cause dizziness, nausea and headaches. Exposure to extreme concentrations can lead to loss of consciousness.'}}, 'no2': {'display_name': 'NO2', 'full_name': 'Nitrogen dioxide', 'aqi_information': {'baqi': {'display_name': 'BreezoMeter AQI', 'aqi': 98, 'aqi_display': '98', 'color': '#009E3A', 'category': 'Excellent air quality'}}, 'concentration': {'value': 2.81, 'units': 'ppb'}, 'sources_and_effects': {'sources': 'Main sources are fuel burning processes, such as those used in industry and transportation.', 'effects': 'Exposure may cause increased bronchial reactivity in patients with asthma, lung function decline in patients with COPD, and increased risk of respiratory infections, especially in young children.'}}, 'nox': {'display_name': 'NOX', 'full_name': 'Nitrogen oxides', 'aqi_information': None, 'concentration': {'value': 11.7, 'units': 'ppb'}, 'sources_and_effects': {'sources': 'Main sources are fuel burning processes, such as those used in industry and transportation.', 'effects': 'Exposure may cause increased bronchial reactivity in patients with asthma, lung function decline in patients with COPD, and increased risk of respiratory infections, especially in young children.'}}, 'o3': {'display_name': 'O3', 'full_name': 'Ozone', 'aqi_information': {'baqi': {'display_name': 'BreezoMeter AQI', 'aqi': 78, 'aqi_display': '78', 'color': '#84CF33', 'category': 'Good air quality'}}, 'concentration': {'value': 27.38, 'units': 'ppb'}, 'sources_and_effects': {'sources': 'Ozone is created in a chemical reaction between atmospheric oxygen, nitrogen oxides, carbon monoxide and organic compounds, in the presence of sunlight.', 'effects': 'Ozone can irritate the airways and cause coughing, a burning sensation, wheezing and shortness of breath. Additionally, ozone is one of the major components of photochemical smog.'}}, 'pm10': {'display_name': 'PM10', 'full_name': 'Inhalable particulate matter (<10µm)', 'aqi_information': {'baqi': {'display_name': 'BreezoMeter AQI', 'aqi': 94, 'aqi_display': '94', 'color': '#009E3A', 'category': 'Excellent air quality'}}, 'concentration': {'value': 6.68, 'units': 'ug/m3'}, 'sources_and_effects': {'sources': 'Main sources are combustion processes (e.g. indoor heating, wildfires), mechanical processes (e.g. construction, mineral dust, agriculture) and biological particles (e.g. pollen, bacteria, mold).', 'effects': 'Inhalable particles can penetrate into the lungs. Short term exposure can cause irritation of the airways, coughing, and aggravation of heart and lung diseases, expressed as difficulty breathing, heart attacks and even premature death.'}}, 'pm25': {'display_name': 'PM2.5', 'full_name': 'Fine particulate matter (<2.5µm)', 'aqi_information': {'baqi': {'display_name': 'BreezoMeter AQI', 'aqi': 93, 'aqi_display': '93', 'color': '#009E3A', 'category': 'Excellent air quality'}}, 'concentration': {'value': 4.59, 'units': 'ug/m3'}, 'sources_and_effects': {'sources': 'Main sources are combustion processes (e.g. power plants, indoor heating, car exhausts, wildfires), mechanical processes (e.g. construction, mineral dust) and biological particles (e.g. bacteria, viruses).', 'effects': 'Fine particles can penetrate into the lungs and bloodstream. Short term exposure can cause irritation of the airways, coughing and aggravation of heart and lung diseases, expressed as difficulty breathing, heart attacks and even premature death.'}}, 'so2': {'display_name': 'SO2', 'full_name': 'Sulfur dioxide', 'aqi_information': {'baqi': {'display_name': 'BreezoMeter AQI', 'aqi': 100, 'aqi_display': '100', 'color': '#009E3A', 'category': 'Excellent air quality'}}, 'concentration': {'value': 0.3, 'units': 'ppb'}, 'sources_and_effects': {'sources': 'Main sources are burning processes of sulfur-containing fuel in industry, transportation and power plants.', 'effects': 'Exposure causes irritation of the respiratory tract, coughing and generates local inflammatory reactions. These in turn, may cause aggravation of lung diseases, even with short term exposure.'}}}, 'health_recommendations': {'general_population': 'With this level of air quality, you have no limitations. Enjoy the outdoors!', 'elderly': 'If you start to feel respiratory discomfort such as coughing or breathing difficulties, consider reducing the intensity of your outdoor activities. Try to limit the time you spend near busy roads, construction sites, open fires and other sources of smoke.', 'lung_diseases': 'If you start to feel respiratory discomfort such as coughing or breathing difficulties, consider reducing the intensity of your outdoor activities. Try to limit the time you spend near busy roads, industrial emission stacks, open fires and other sources of smoke.', 'heart_diseases': 'If you start to feel respiratory discomfort such as coughing or breathing difficulties, consider reducing the intensity of your outdoor activities. Try to limit the time you spend near busy roads, construction sites, industrial emission stacks, open fires and other sources of smoke.', 'active': 'If you start to feel respiratory discomfort such as coughing or breathing difficulties, consider reducing the intensity of your outdoor activities. Try to limit the time you spend near busy roads, construction sites, industrial emission stacks, open fires and other sources of smoke.', 'pregnant_women': 'To keep you and your baby healthy, consider reducing the intensity of your outdoor activities. Try to limit the time you spend near busy roads, construction sites, open fires and other sources of smoke.', 'children': 'If you start to feel respiratory discomfort such as coughing or breathing difficulties, consider reducing the intensity of your outdoor activities. Try to limit the time you spend near busy roads, construction sites, open fires and other sources of smoke.'}}, 'error': None}
        # json_response = pu.get_geo_pollution_data(53.2329, -6.1136)
        # resp_keys = json_response['data'].keys()
        # exp_keys = sample_json['data'].keys()
        # isSame = self.json_compare(exp_keys, resp_keys)
        
        # Matching JSON structure, test will fail if json structure changes
        # raw_json = {"metadata": {"timestamp": "2019-11-14T12:52:46Z", "location": {"country": "Ireland"}, "indexes": {"baqi": {"pollutants": ["co", "no2", "o3", "pm10", "pm25", "so2"]}, "irl_epa": {"pollutants": ["no2", "o3", "pm10", "pm25", "so2"]}}}, "data": {"datetime": "2019-11-14T12:00:00Z", "data_available": true, "indexes": {"baqi": {"display_name": "BreezoMeter AQI", "aqi": 78, "aqi_display": "78", "color": "#60C134", "category": "Good air quality", "dominant_pollutant": "o3"}, "irl_epa": {"display_name": "AQIH (IE)", "aqi": 2, "aqi_display": "2", "color": "#62BB3D", "category": "Good air quality", "dominant_pollutant": "o3"}}, "pollutants": {"co": {"display_name": "CO", "full_name": "Carbon monoxide", "aqi_information": {"baqi": {"display_name": "BreezoMeter AQI", "aqi": 100, "aqi_display": "100", "color": "#009E3A", "category": "Excellent air quality"}}, "concentration": {"value": 0.22, "units": "ppb"}, "sources_and_effects": {"sources": "Typically originates from incomplete combustion of carbon fuels, such as that which occurs in car engines and power plants.", "effects": "When inhaled, carbon monoxide can prevent the blood from carrying oxygen. Exposure may cause dizziness, nausea and headaches. Exposure to extreme concentrations can lead to loss of consciousness."}}, "no2": {"display_name": "NO2", "full_name": "Nitrogen dioxide", "aqi_information": {"baqi": {"display_name": "BreezoMeter AQI", "aqi": 98, "aqi_display": "98", "color": "#009E3A", "category": "Excellent air quality"}}, "concentration": {"value": 2.81, "units": "ppb"}, "sources_and_effects": {"sources": "Main sources are fuel burning processes, such as those used in industry and transportation.", "effects": "Exposure may cause increased bronchial reactivity in patients with asthma, lung function decline in patients with COPD, and increased risk of respiratory infections, especially in young children."}}, "nox": {"display_name": "NOX", "full_name": "Nitrogen oxides", "aqi_information": null, "concentration": {"value": 11.7, "units": "ppb"}, "sources_and_effects": {"sources": "Main sources are fuel burning processes, such as those used in industry and transportation.", "effects": "Exposure may cause increased bronchial reactivity in patients with asthma, lung function decline in patients with COPD, and increased risk of respiratory infections, especially in young children."}}, "o3": {"display_name": "O3", "full_name": "Ozone", "aqi_information": {"baqi": {"display_name": "BreezoMeter AQI", "aqi": 78, "aqi_display": "78", "color": "#84CF33", "category": "Good air quality"}}, "concentration": {"value": 27.38, "units": "ppb"}, "sources_and_effects": {"sources": "Ozone is created in a chemical reaction between atmospheric oxygen, nitrogen oxides, carbon monoxide and organic compounds, in the presence of sunlight.", "effects": "Ozone can irritate the airways and cause coughing, a burning sensation, wheezing and shortness of breath. Additionally, ozone is one of the major components of photochemical smog."}}, "pm10": {"display_name": "PM10", "full_name": "Inhalable particulate matter (<10\u00b5m)", "aqi_information": {"baqi": {"display_name": "BreezoMeter AQI", "aqi": 94, "aqi_display": "94", "color": "#009E3A", "category": "Excellent air quality"}}, "concentration": {"value": 6.68, "units": "ug/m3"}, "sources_and_effects": {"sources": "Main sources are combustion processes (e.g. indoor heating, wildfires), mechanical processes (e.g. construction, mineral dust, agriculture) and biological particles (e.g. pollen, bacteria, mold).", "effects": "Inhalable particles can penetrate into the lungs. Short term exposure can cause irritation of the airways, coughing, and aggravation of heart and lung diseases, expressed as difficulty breathing, heart attacks and even premature death."}}, "pm25": {"display_name": "PM2.5", "full_name": "Fine particulate matter (<2.5\u00b5m)", "aqi_information": {"baqi": {"display_name": "BreezoMeter AQI", "aqi": 93, "aqi_display": "93", "color": "#009E3A", "category": "Excellent air quality"}}, "concentration": {"value": 4.59, "units": "ug/m3"}, "sources_and_effects": {"sources": "Main sources are combustion processes (e.g. power plants, indoor heating, car exhausts, wildfires), mechanical processes (e.g. construction, mineral dust) and biological particles (e.g. bacteria, viruses).", "effects": "Fine particles can penetrate into the lungs and bloodstream. Short term exposure can cause irritation of the airways, coughing and aggravation of heart and lung diseases, expressed as difficulty breathing, heart attacks and even premature death."}}, "so2": {"display_name": "SO2", "full_name": "Sulfur dioxide", "aqi_information": {"baqi": {"display_name": "BreezoMeter AQI", "aqi": 100, "aqi_display": "100", "color": "#009E3A", "category": "Excellent air quality"}}, "concentration": {"value": 0.3, "units": "ppb"}, "sources_and_effects": {"sources": "Main sources are burning processes of sulfur-containing fuel in industry, transportation and power plants.", "effects": "Exposure causes irritation of the respiratory tract, coughing and generates local inflammatory reactions. These in turn, may cause aggravation of lung diseases, even with short term exposure."}}}, "health_recommendations": {"general_population": "With this level of air quality, you have no limitations. Enjoy the outdoors!", "elderly": "If you start to feel respiratory discomfort such as coughing or breathing difficulties, consider reducing the intensity of your outdoor activities. Try to limit the time you spend near busy roads, construction sites, open fires and other sources of smoke.", "lung_diseases": "If you start to feel respiratory discomfort such as coughing or breathing difficulties, consider reducing the intensity of your outdoor activities. Try to limit the time you spend near busy roads, industrial emission stacks, open fires and other sources of smoke.", "heart_diseases": "If you start to feel respiratory discomfort such as coughing or breathing difficulties, consider reducing the intensity of your outdoor activities. Try to limit the time you spend near busy roads, construction sites, industrial emission stacks, open fires and other sources of smoke.", "active": "If you start to feel respiratory discomfort such as coughing or breathing difficulties, consider reducing the intensity of your outdoor activities. Try to limit the time you spend near busy roads, construction sites, industrial emission stacks, open fires and other sources of smoke.", "pregnant_women": "To keep you and your baby healthy, consider reducing the intensity of your outdoor activities. Try to limit the time you spend near busy roads, construction sites, open fires and other sources of smoke.", "children": "If you start to feel respiratory discomfort such as coughing or breathing difficulties, consider reducing the intensity of your outdoor activities. Try to limit the time you spend near busy roads, construction sites, open fires and other sources of smoke."}}, "error": null}
        # raw_json_s = json_schema.loads(json_schema.dumps(raw_json))
        # json_response_s = json_schema.loads(json_schema.dumps(json_response))
        # self.assertTrue(raw_json_s == json_response_s)
        # self.assertTrue(json_schema.match(json_response, raw_json)