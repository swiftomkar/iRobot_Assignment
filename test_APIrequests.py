import unittest
from APIrequests import APIrequests
from unittest.mock import patch

class testAPI(unittest.TestCase):
    def setUpClass(cls):
        testSession=APIrequests()

    def test_foodSearch(self):
        with patch('APIrequests.requests.get') as mocked_get:
            mocked_get.recipies.status_code
