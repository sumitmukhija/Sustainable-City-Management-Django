from django.test import SimpleTestCase
import requests
from rest_framework import status

from DataInteractions.test_utils import TestUtils
from SCMBackend.env import Environ


class TrafficMongoTest(SimpleTestCase):
    def test_insertion_api(self):
        data = open('./test_data_traffic.json', 'r')
        request_json = data.read()
        print(request_json)
        valid_token = TestUtils().get_valid_auth()
        headers = {"Authorization": valid_token}
        response = requests.post(url=Environ().get_base_traffic_url(), data={"data": request_json}, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieval_by_lat_long_function(self):
        valid_token = TestUtils().get_valid_auth()
        headers = {"Authorization": valid_token}
        response = requests.get(url=Environ().get_base_traffic_url(), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.status_code)

    def test_insertion_api_analysis(self):
        data = open('./test_data_traffic_analysis.json', 'r')
        request_json = data.read()
        valid_token = TestUtils().get_valid_auth()
        headers = {"Authorization": valid_token}
        response = requests.post(url=Environ().get_base_traffic_url(), data={"data": request_json}, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test__analysis_retrieval_by_lat_long_function(self):
        valid_token = TestUtils().get_valid_auth()
        headers = {"Authorization": valid_token}
        response = requests.get(url=Environ().get_base_traffic_url() + "/analysis", headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.status_code)
