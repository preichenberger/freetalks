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

    def test_not_saved_if_name_is_empty(self):
        series = Series(
            name='',
            slug='slug',
            link='http://test',
            created_user=self._test_user,
            updated_user=self._test_user,
        )
        series.put()
        self.assertFalse(series.is_saved())
