import os
import json

from dotenv import load_dotenv
from DataRetrieval.bike.bike_util import BikeUtil
from django.test import SimpleTestCase

class BikeTest(SimpleTestCase):

    def test(self):
        load_dotenv()
        self.test_api_key_present()
        self.test_api_key()
        self.test_get_api_data()

    def test_api_key_present(self):
        apiKey = BikeUtil().getAPIKey()
        self.assertIsNotNone(apiKey)
    
    def test_api_key(self):
        apiKey = "xyz"
        actualAPIKey = os.getenv('DUBLIN_BIKES_KEY')
        self.assertNotEqual(apiKey, actualAPIKey)
        apiKey = BikeUtil().getAPIKey()
        self.assertEqual(apiKey, actualAPIKey)

    def test_get_api_data(self):
        json_response = BikeUtil().get_dublin_bikes_data()
        self.assertIsNotNone(json_response)
