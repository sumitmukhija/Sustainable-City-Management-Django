from django.test import SimpleTestCase
from rest_framework import status
from DataInteractions.test_utils import TestUtils
from SCMBackend.env import Environ
from DataInteractions.views import NotificationDispatch
import requests

valid_token = TestUtils().get_valid_auth()
headers = {"Authorization": valid_token}


class NotificationsTest(SimpleTestCase):
    
    def test_without_message(self):
        request = {"data":{}}
        response = NotificationDispatch().post(request)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_without_request_data(self):
        request = dict()
        response = NotificationDispatch().post(request)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_without_request(self):
        request = None
        response = NotificationDispatch().post(request)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST, response.status_code)
    
    def test_with_message(self):
        request = {"data": {"message":"Python"}}
        response = NotificationDispatch().post(request)
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK, response.status_code)
