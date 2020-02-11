from django.test import SimpleTestCase
from DataInteractions.pollution import pollution_mongo_test
from DataInteractions.bike import bike_mongo_test
from DataInteractions.traffic import traffic_mongo_test

class TestPollutionTracker (SimpleTestCase):

    def test_insert_pollution_data(self):
        p_test = pollution_mongo_test.PollutionMongoTest()
        p_test.test_insertion_api()
    
    def test_retrieve_all_function(self):
        p_test = pollution_mongo_test.PollutionMongoTest()
        p_test.test_retrieval_function()

    def test_retrieval_by_lat_long(self):
        p_test = pollution_mongo_test.PollutionMongoTest()
        p_test.test_retrieval_by_lat_long_function()

class TestBikeDataInteractions (SimpleTestCase):
    def test_retrieval_by_lat_long(self):
        b_test = bike_mongo_test.BikeMongoTest()
        b_test.test_retrieval_by_lat_long_function()

    def test_insert_bike_data(self):
        b_test = bike_mongo_test.BikeMongoTest()
        b_test.test_insertion_api()

class TestTrafficDataInteractions(SimpleTestCase):
    def test_retrieval_by_lat_long(self):
        t_test = traffic_mongo_test.TrafficMongoTest()
        t_test.test_retrieval_by_lat_long_function()

    def test_insert_traffic_data(self):
        t_test = traffic_mongo_test.TrafficMongoTest()
        t_test.test_insertion_api()
