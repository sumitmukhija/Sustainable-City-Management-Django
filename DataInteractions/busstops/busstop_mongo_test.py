from django.test import SimpleTestCase
from rest_framework import status
from SCMBackend.env import Environ
import requests


class BusStopMongoTest(SimpleTestCase):
    def test_insertion_api(self):
        data = open('./test_data_busstop.json', 'r')
        request_json = data.read()
        print(request_json)
        response = requests.post(url=Environ().get_base_bus_stop_url(), data={"data": request_json})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieval_by_lat_long_function(self):
        response = requests.get(url=Environ().get_base_bus_stop_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.status_code)
