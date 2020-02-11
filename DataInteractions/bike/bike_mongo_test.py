from django.test import SimpleTestCase
import requests
import os
from SCMBackend.env import Environ
from rest_framework import status
class BikeMongoTest(SimpleTestCase):

    def test_insertion_api(self):
        API_ENDPOINT = Environ().get_base_bike_url()
        data = open('./test_data_bike.json', 'r')
        request_json = data.read()
        response = requests.post(url=API_ENDPOINT, data={"data": request_json})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieval_by_lat_long_function(self):
        API_ENDPOINT = Environ().get_base_bike_url()
        response = requests.get(url=API_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
