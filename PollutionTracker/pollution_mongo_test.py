from django.test import SimpleTestCase
import requests
from rest_framework.response import Response
from rest_framework import status
import json
import ast
class PollutionMongoTest(SimpleTestCase):
    def test_insertion_api(self):
        API_ENDPOINT = 'http://localhost:8000/polls/'
        data = open('D:\GitRepos\ASE-City_Management\Sustainable-City-Management-Django\PollutionTracker/test_data.json', 'r')
        request_json = data.read()
        print(request_json)
        response = requests.post(url=API_ENDPOINT, data={"smt": request_json})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_pollution_retrieval_api(self):
        API_ENDPOINT = 'http://localhost:8000/polls/'
        response = requests.get(url=API_ENDPOINT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)