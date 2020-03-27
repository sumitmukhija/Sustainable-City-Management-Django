from django.test import SimpleTestCase
from rest_framework import status

from DataInteractions.test_utils import TestUtils
from SCMBackend.env import Environ
import requests

valid_token = TestUtils().get_valid_auth()
headers = {"Authorization": valid_token}

class TimetableRetrievalTest(SimpleTestCase):
    def test_bus_tt_retrieval(self):
        params = {"stopid": 4518}
        response = requests.get(url=Environ().get_base_bus_internal_tt_url(), params=params, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.status_code)
