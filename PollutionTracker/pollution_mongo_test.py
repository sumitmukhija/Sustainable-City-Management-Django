from django.test import SimpleTestCase
import requests
from .pollution_data_interactions import PollutionDataInteractions
from rest_framework.response import Response
from rest_framework import status
import json
import ast
class PollutionMongoTest(SimpleTestCase):
    def test_insertion_api(self):
        API_ENDPOINT = 'http://localhost:8000/polls/'
        data = open('./test_data.json', 'r')
        request_json = data.read()
        print(request_json)
        response = requests.post(url=API_ENDPOINT, data={"data": request_json})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieval_by_lat_long_function(self):
        API_ENDPOINT = 'http://localhost:8000/polls/'
        response = requests.get(url=API_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)