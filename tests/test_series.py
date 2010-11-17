from fixtures import dataset
from freetalks.models import Series
from google.appengine.api.users import User
import unittest

class TestSeries(unittest.TestCase):
    def setUp(self):
        dataset.setup()
        self._test_user = User(email='test@freetalks.com')

    def tearDown(self):
        dataset.clear()
