from django.test import SimpleTestCase
from DataInteractions.pollution import pollution_mongo_test
from DataInteractions.bike import bike_mongo_test
from DataInteractions.traffic import traffic_mongo_test
from DataInteractions.busstops import busstop_mongo_test
from DataInteractions.luasstops import luasstop_mongo_test
from DataInteractions.irishrail import irishrailstop_mongo_test
from DataInteractions.notifications import notifications_test

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

class TestTrafficAnalysisDataInteractions(SimpleTestCase):
    def test_retrieval_by_lat_long(self):
        t_test = traffic_mongo_test.TrafficMongoTest()
        t_test.test__analysis_retrieval_by_lat_long_function()

    def test_insert_traffic_data(self):
        t_test = traffic_mongo_test.TrafficMongoTest()
        t_test.test_insertion_api_analysis()

class TestBusStopDataInteractions(SimpleTestCase):
    def test_retrieval_by_lat_long(self):
        bs_test = busstop_mongo_test.BusStopMongoTest()
        bs_test.test_retrieval_by_lat_long_function()

    def test_insert_busstop_data(self):
        bs_test = busstop_mongo_test.BusStopMongoTest()
        bs_test.test_insertion_api()

class TestLuasStopDataInteractions(SimpleTestCase):
    def test_retrieval_by_lat_long(self):
        ls_test = luasstop_mongo_test.LuasStopMongoTest()
        ls_test.test_retrieval_by_lat_long_function()

    def test_insert_luasstop_data(self):
        ls_test = luasstop_mongo_test.LuasStopMongoTest()
        ls_test.test_insertion_api()

class TestIrishRailStopDataInteractions(SimpleTestCase):
    def test_retrieval_by_lat_long(self):
        irs_test = irishrailstop_mongo_test.IrishRailStopMongoTest()
        irs_test.test_retrieval_by_lat_long_function()

    def test_insert_irishrailstop_data(self):
        irs_test = irishrailstop_mongo_test.IrishRailStopMongoTest()
        irs_test.test_insertion_api()
    
class TestNotificationDispatch(SimpleTestCase):
    def test_notification_without_request(self):
        not_test = notifications_test.NotificationsTest()
        # not_test.test_without_message()
        # not_test.test_with_message()
        # not_test.test_without_request_data()
        # not_test.test_without_request()
        
