from django.test import SimpleTestCase
import requests
from DataInteractions.pollution.pollution_data_interactions import PollutionDataInteractions
from rest_framework import status
from dotenv import load_dotenv
import os


class PollutionMongoTest(SimpleTestCase):
    def test_insertion_api(self):
        load_dotenv();
        data = open('./test_data_poll.json', 'r')
        request_json = data.read()
        print(request_json)
        response = requests.post(url=os.getenv('BASE_MONGO_POLLUTION_URL'), data={"data": request_json})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.status_code)

    def test_retrieval_by_lat_long_function(self):
        load_dotenv()
        response = requests.get(url=os.getenv('BASE_MONGO_POLLUTION_URL'))
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.status_code)
    '''def test_insertion_function(self):
        data = open('D:\GitRepos\ASE-City_Management\Sustainable-City-Management-Django\PollutionTracker/test_data_poll.json', 'r')
        request_json = data.read()
        request_json = json.loads(request_json)
        PollutionDataInteractions.insert_poll_data(self,request_json)'''
    def test_retrieval_function(self):
        results = PollutionDataInteractions().get_all_objects()
        self.assertIsNotNone(results, "Empty JSON")
    '''def test_retrieval_by_lat_long_function(self):
        results = PollutionDataInteractions().get_latest_by_lat_long()
        print(results)'''
