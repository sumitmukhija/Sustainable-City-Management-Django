from django.test import SimpleTestCase
from .pollution import pollution_test
from .bike import bike_test
from .traffic import traffic_test


class SCMRetrievalTests(SimpleTestCase):
    
    def test_pollution(self):
        p_test = pollution_test.PollutionTest()
        p_test.test()

    def test_bike(self):
        b_test = bike_test.BikeTest()
        b_test.test()

    def test_traffic(self):
        t_test = traffic_test.TrafficTest()
        t_test.test()
