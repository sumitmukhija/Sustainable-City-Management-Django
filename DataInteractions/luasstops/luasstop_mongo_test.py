from django.test import SimpleTestCase
from rest_framework import status

from DataInteractions.test_utils import TestUtils
from SCMBackend.env import Environ
import requests

valid_token = TestUtils().get_valid_auth()
headers = {"Authorization": valid_token}

class LuasStopMongoTest(SimpleTestCase):
    def test_insertion_api(self):
        data = open('./test_data_luasstop.json', 'r')
        request_json = data.read()
        response = requests.post(url=Environ().get_base_luas_stop_url(), data={"data": request_json}, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieval_by_lat_long_function(self):
        response = requests.get(url=Environ().get_base_luas_stop_url(), headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.status_code)
