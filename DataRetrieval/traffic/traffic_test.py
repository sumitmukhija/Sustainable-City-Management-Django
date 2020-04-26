import os
from dotenv import load_dotenv
from DataRetrieval.traffic.traffic_util import TrafficUtil
from django.test import SimpleTestCase

class TrafficTest(SimpleTestCase):

    def test(self):
        load_dotenv()
        self.test_api_key_present()
        self.test_api_key()
        self.test_get_api_data()

    def test_api_key_present(self):
        apiKey = TrafficUtil().getAPIKey()
        self.assertIsNotNone(apiKey)
    
    def test_api_key(self):
        apiKey = "xyz"
        actualAPIKey = os.getenv('TOMTOM_API_KEY')
        self.assertNotEqual(apiKey, actualAPIKey)
        apiKey = TrafficUtil().getAPIKey()
        self.assertEqual(apiKey, actualAPIKey)

    def test_get_api_data(self):
        json_response = TrafficUtil().get_traffic_data(53.2329, -6.1136)
        self.assertIsNotNone(json_response)
