from django.test import SimpleTestCase, Client
from django.urls import reverse
from . import pollution_mongo_test, bike_mongo_test

# Create your tests here.
class TestPollutionTracker (SimpleTestCase):

    '''def test_insert_pollution_data(self):
        p_test = pollution_mongo_test.PollutionMongoTest()
        p_test.test_insertion_api()
    def test_retrieve_pollution_data(self):
        p_test = pollution_mongo_test.PollutionMongoTest()
        p_test.test_pollution_retrieval_api()
    def test_insert_function(self):
        p_test = pollution_mongo_test.PollutionMongoTest()
        p_test.test_insertion_function()'''
    def test_retrieve_all_function(self):
        p_test = pollution_mongo_test.PollutionMongoTest()
        p_test.test_retrieval_function()
    def test_retrieval_by_lat_long(self):
        p_test = pollution_mongo_test.PollutionMongoTest()
        p_test.test_retrieval_by_lat_long_function()

class TestBikeDataInteractions (SimpleTestCase):
    def test_retrieval_by_lat_long(self):
        p_test = bike_mongo_test.BikeMongoTest()
        p_test.test_retrieval_by_lat_long_function()

    def test_insert_bike_data(self):
        p_test = bike_mongo_test.BikeMongoTest()
        p_test.test_insertion_api()