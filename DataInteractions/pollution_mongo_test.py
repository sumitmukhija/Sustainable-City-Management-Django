from django.test import SimpleTestCase
import requests
from .pollution_data_interactions import PollutionDataInteractions
from rest_framework.response import Response
from rest_framework import status
import json
import ast
class PollutionMongoTest(SimpleTestCase):
    def test_insertion_api(self):
        API_ENDPOINT = 'http://localhost:8000/data/polls'
        data = open('./test_data.json', 'r')
        request_json = data.read()
        print(request_json)
        response = requests.post(url=API_ENDPOINT, data={"data": request_json})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieval_by_lat_long_function(self):
        API_ENDPOINT = 'http://localhost:8000/data/polls/'
        response = requests.get(url=API_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    '''def test_insertion_function(self):
        data = open('D:\GitRepos\ASE-City_Management\Sustainable-City-Management-Django\PollutionTracker/test_data_poll.json', 'r')
        request_json = data.read()
        request_json = json.loads(request_json)
        PollutionDataInteractions.insert_poll_data(self,request_json)'''
    def test_retrieval_function(self):
        results = PollutionDataInteractions().get_all_objects()
        print(results)
    '''def test_retrieval_by_lat_long_function(self):
        results = PollutionDataInteractions().get_latest_by_lat_long()
        print(results)'''