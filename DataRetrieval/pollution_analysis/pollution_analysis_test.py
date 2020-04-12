from rest_framework import status
from django.test import SimpleTestCase
import json
from DataRetrieval.pollution_analysis.pollution_analysis_util import PollutionAnalysisUtil

class PollutionAnalysisTest(SimpleTestCase):

    def test(self):
        self.test_prediction_no_location()
        self.test_prediction_with_location()

    def test_prediction_no_location(self):
        response = PollutionAnalysisUtil().get_predictions("")
        self.assertIsNone(response)

    def test_prediction_with_location(self):
        json_response = PollutionAnalysisUtil().get_predictions("53.286774 -6.245183")
        self.assertIsNotNone(json_response)