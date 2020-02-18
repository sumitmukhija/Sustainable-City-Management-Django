from django.test import SimpleTestCase
from DataRetrieval.busstops.busstop_util import BusStopUtil
import numpy as np

class BusStopTest(SimpleTestCase):

    def test(self):
        self.test_data_validity()

    def test_data_validity(self):
        stops = BusStopUtil().get_bus_stop_coordinates()
        self.assertIsNotNone(stops, 'Bus Stop Data Unavailable')
        ar = np.array(['stop_id', 'stop_name', 'stop_lat', 'stop_lon'])
        self.assertTrue(np.all(stops.columns == ar), 'Column Mismatch. Source Format has changed')
        self.assertTrue(stops.shape[0]>0, 'Bus Stop Data is Empty')