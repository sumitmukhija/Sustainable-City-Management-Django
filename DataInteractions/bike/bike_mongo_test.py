from django.test import SimpleTestCase
import requests

from DataInteractions.test_utils import TestUtils
from SCMBackend.env import Environ
from rest_framework import status


class BikeMongoTest(SimpleTestCase):

    def test_insertion_api(self):
        data = open('./test_data_bike.json', 'r')
        request_json = data.read()
        valid_token = TestUtils().get_valid_auth()
        headers = {"Authorization": valid_token}
        response = requests.post(url=Environ().get_base_bike_url(), data={"data": request_json}, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieval_by_lat_long_function(self):
        valid_token = TestUtils().get_valid_auth()
        headers = {"Authorization": valid_token}
        response = requests.get(url=Environ().get_base_bike_url(), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
