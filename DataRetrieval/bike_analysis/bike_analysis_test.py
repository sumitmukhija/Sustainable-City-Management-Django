from DataRetrieval.bike_analysis.bike_analysis_util import BikeAnalysisUtil
from django.test import SimpleTestCase

class BikeAnalysisTest(SimpleTestCase):

    def test(self):
        self.test_api_key_present()
        self.test_get_api_data()

    def test_api_key_present(self):
        apiKey = BikeAnalysisUtil().getAPIKey()
        self.assertIsNotNone(apiKey)

    def test_get_api_data(self):
        json_response = BikeAnalysisUtil().get_dublin_bikes_data()
        self.assertIsNotNone(json_response)
