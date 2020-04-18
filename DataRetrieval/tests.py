from django.test import SimpleTestCase
from .pollution import pollution_test
from .pollution_analysis import pollution_analysis_test
from .bike import bike_test
from .bike_analysis import bike_analysis_test
from .traffic import traffic_test
from .busstops import busstop_test
from .luasstops import luasstop_test
from .irishrail import irishrailstop_test
from SCMBackend.notifications import Notifier

class SCMRetrievalTests(SimpleTestCase):
    
    def test_pollution(self):
        p_test = pollution_test.PollutionTest()
        p_test.test()

    def test_pollution_analysis(self):
        pa_test = pollution_analysis_test.PollutionAnalysisTest()
        pa_test.test()

    def test_bike(self):
        b_test = bike_test.BikeTest()
        b_test.test()

    def test_bike_analyis(self):
        ba_test = bike_analysis_test.BikeAnalysisTest()
        ba_test.test()

    def test_traffic(self):
        t_test = traffic_test.TrafficTest()
        t_test.test()

    def test_busstops(self):
        t_test = busstop_test.BusStopTest()
        t_test.test()

    def test_luasstops(self):
        t_test = luasstop_test.LuasStopTest()
        t_test.test()

    def test_irishrailstops(self):
        ir_test = irishrailstop_test.IrishRailStopTest()
        ir_test.test()
    
    def test_pusher_notifications(self):
        notifier = Notifier()
        notifier.dispatch_notification("test notification")
        # Should show a notification on the frontend application with text test-notification
