from django.test import SimpleTestCase
from DataRetrieval.luasstops.luasstop_util import LuasStopUtil
import numpy as np

class LuasStopTest(SimpleTestCase):

    def test(self):
        self.test_data_validity()

    def test_data_validity(self):
        stops = LuasStopUtil().get_luas_stop_coordinates()
        self.assertIsNotNone(stops, 'Luas Stop Data Unavailable')
        ar = np.array(['stop_id', 'stop_name', 'stop_lat', 'stop_lon'])
        self.assertTrue(np.all(stops.columns == ar), 'Column Mismatch. Source Format has changed')
        self.assertTrue(stops.shape[0]>0, 'Luas Stop Data is Empty')