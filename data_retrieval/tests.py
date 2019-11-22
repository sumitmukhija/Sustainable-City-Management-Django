from django.test import TestCase
from .pollution import pollution_test


class SCMRetrievalTests(TestCase):
    
    def test_pollution(self):
        p_test = pollution_test.PollutionTest()
        p_test.test()