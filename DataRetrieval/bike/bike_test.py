from DataRetrieval.bike.bike_util import BikeUtil
from django.test import SimpleTestCase

class BikeTest(SimpleTestCase):

    def test(self):
        self.test_api_key_present()
        self.test_get_api_data()

    def test_api_key_present(self):
        apiKey = BikeUtil().getAPIKey()
        self.assertIsNotNone(apiKey)

    def test_get_api_data(self):
        json_response = BikeUtil().get_dublin_bikes_data()
        self.assertIsNotNone(json_response)
