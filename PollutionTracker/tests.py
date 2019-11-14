from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestPollutionTracker (TestCase):

    def test_retrieve_pollution_data(self):
        """
        Tests if pollution data is accessible from the mongo db instance
        """
        data = {
            "input_unit": "centimetre",
            "output_unit": "metre",
            "input_value": round(8096.894, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 80.969)
