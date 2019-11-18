from django.test import SimpleTestCase, Client
from django.urls import reverse
from . import pollution_mongo_test

# Create your tests here.
class TestPollutionTracker (SimpleTestCase):

    def test_insert_pollution_data(self):
        p_test = pollution_mongo_test.PollutionMongoTest()
        p_test.test_insertion_api()
    def test_retrieve_pollution_data(self):
        p_test = pollution_mongo_test.PollutionMongoTest()
        p_test.test_pollution_retrieval_api()
