from DataRetrieval.bike_analysis.bike_analysis_util import BikeAnalysisUtil
from django.test import SimpleTestCase

class BikeAnalysisTest(SimpleTestCase):

    def test(self):
        self.test_prediction_no_stop()
        self.test_prediction_with_stop()

    def test_prediction_no_stop(self):
        response = BikeAnalysisUtil().get_predictions("")
        self.assertIsNone(response)

    def test_prediction_with_stop(self):
        json_response = BikeAnalysisUtil().get_predictions("FENIAN STREET")
        self.assertIsNotNone(json_response)
