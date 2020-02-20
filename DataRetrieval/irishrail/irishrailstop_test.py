from django.test import SimpleTestCase
from DataRetrieval.irishrail.irishrailstop_util import IrishRailUtil
import numpy as np

class IrishRailStopTest(SimpleTestCase):

    def test(self):
        self.test_data_validity()

    def test_data_validity(self):
        stops = IrishRailUtil().get_irish_rail_stop_coordinates()
        self.assertIsNotNone(stops, 'Irish Rail Stop Data Unavailable')
        ar = np.array(['stop_id', 'stop_name', 'stop_lat', 'stop_lon'])
        self.assertTrue(np.all(stops.columns == ar), 'Column Mismatch. Source Format has changed')
        self.assertTrue(stops.shape[0]>0, 'Irish Rail Stop Data is Empty')