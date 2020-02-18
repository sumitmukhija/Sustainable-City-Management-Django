from django.test import SimpleTestCase
from SCMBackend.env import Environ
import requests
from DataInteractions.pollution.pollution_data_interactions import PollutionDataInteractions
from rest_framework import status
import json
import os


class PollutionMongoTest(SimpleTestCase):
    def test_insertion_api(self):
        API_ENDPOINT = Environ().get_base_pollution_url()
        data = open('./test_data_poll.json', 'r')
        request_json = data.read()
        print(request_json)
        response = requests.post(url=Environ().get_base_pollution_url(), data={"data": request_json})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.status_code)

    def test_retrieval_by_lat_long_function(self):
        API_ENDPOINT = Environ().get_base_pollution_url()
        response = requests.get(url=API_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_retrieval_function(self):
        results = PollutionDataInteractions().get_all_objects()
        self.assertIsNotNone(results, "Empty JSON")
