from django.test import SimpleTestCase
import requests
import os
from rest_framework import status
from dotenv import load_dotenv
class BikeMongoTest(SimpleTestCase):

    def test_insertion_api(self):
        load_dotenv()
        data = open('./test_data_bike.json', 'r')
        request_json = data.read()
        print(request_json)
        response = requests.post(url=os.getenv('BASE_MONGO_BIKE_URL'), data={"data": request_json})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.status_code)

    def test_retrieval_by_lat_long_function(self):
        load_dotenv()
        response = requests.get(url=os.getenv('BASE_MONGO_BIKE_URL'))
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.status_code)