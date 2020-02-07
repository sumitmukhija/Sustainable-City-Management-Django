from .pollution import pollution_test
from django.test import SimpleTestCase


class SCMRetrievalTests(SimpleTestCase):
    
    def test_pollution(self):
        p_test = pollution_test.PollutionTest()
        # p_test.test()
