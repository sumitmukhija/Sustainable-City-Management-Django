import DataRetrieval.pollution.pollution_util as pu
from django.test import SimpleTestCase
import json
import DataRetrieval.match as match
import DataRetrieval.pollution.pollution_job as pj

class PollutionTest(SimpleTestCase):

    def test(self):
        self.test_breeze_api()

    def test_breeze_api(self):
        # No longitude. Should return None
        json_response = pu.PollutionUtil.get_geo_pollution_data(53.2329, None)
        self.assertIsNone(json_response, "No longitude")

        # No latitude and longitude. Should return None
        json_response = pu.PollutionUtil.get_geo_pollution_data(None, None)
        self.assertIsNone(json_response, "No lat/long")

        # No lat. Should return None
        json_response = pu.PollutionUtil.get_geo_pollution_data(None, -6.1136)
        self.assertIsNone(json_response, "No longitude")
        
        # Check for data keyjson_response = pu.get_geo_pollution_data(53.2329, -6.1136)
        json_response = pu.PollutionUtil.get_geo_pollution_data(
            53.2329, -6.1136)
        self.assertIsNotNone(json_response['data'], "Data key absent")

        # # Matching JSON structure, test will fail if json structure changes
        json_response = pu.PollutionUtil.get_geo_pollution_data(
            53.2329, -6.1136)
        self.assertIsNotNone(json_response, "Empty JSON")
        raw_json_str = '{"metadata": {"timestamp": "2019-11-22T11:20:52Z", "location": {"country": "Ireland"}, "indexes": {"irl_epa": {"pollutants": ["no2", "o3", "pm10", "pm25", "so2"]}}}, "data": {"datetime": "2019-11-22T11:00:00Z", "data_available": true, "indexes": {"irl_epa": {"display_name": "AQIH (IE)", "aqi": 2, "aqi_display": "2", "color": "#62BB3D", "category": "Good air quality", "dominant_pollutant": "o3"}}, "pollutants": {"co": {"display_name": "CO", "full_name": "Carbon monoxide", "concentration": {"value": 0.33, "units": "ppb"}}, "no2": {"display_name": "NO2", "full_name": "Nitrogen dioxide", "concentration": {"value": 7.84, "units": "ppb"}}, "nox": {"display_name": "NOX", "full_name": "Nitrogen oxides", "concentration": {"value": 13.78, "units": "ppb"}}, "o3": {"display_name": "O3", "full_name": "Ozone", "concentration": {"value": 26.66, "units": "ppb"}}, "pm10": {"display_name": "PM10", "full_name": "Inhalable particulate matter (<10\u00b5m)", "concentration": {"value": 7.72, "units": "ug/m3"}}, "pm25": {"display_name": "PM2.5", "full_name": "Fine particulate matter (<2.5\u00b5m)", "concentration": {"value": 7.6, "units": "ug/m3"}}, "so2": {"display_name": "SO2", "full_name": "Sulfur dioxide", "concentration": {"value": 0.21, "units": "ppb"}}}}, "error": null}'
        raw_json = json.loads(raw_json_str)
        is_schema_uniform = match.are_keys_same_in_dictionary(dict(raw_json), dict(json_response))
        self.assertTrue(is_schema_uniform[0], "Schema mismatch")
