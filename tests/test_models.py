import unittest
from datetime import datetime as dt
from google.appengine.api.users import User
from google.appengine.ext import db
from freetalks import models
from fixtures import dataset

class TestSeries(unittest.TestCase):

    def setUp(self):
        dataset.setup()

    def tearDown(self):
        dataset.clear()

    @staticmethod
    def model(put=True, remove=None, **kwargs):
        user = User(email='test@freetalks.com')
        options = {
            'name': 'Some Name',
            'link': 'http://www.example.org/',
            'about': 'This is a test about message.',
            'created_user': user,
            'updated_user': user,
        }
        options.update(kwargs)
        if remove:
            for name in remove:
                del options[name]
        series = models.Series(**options)
        if put:
            series.put()
        return series

    def test_name(self):
        self.assertRaises(db.BadValueError, self.model, name='')
        self.assertRaises(db.BadValueError, self.model, remove=['name'])
        # Name must start with an alphabetic character
        self.assertRaises(db.BadValueError, self.model, name='0abc')

    def test_slug(self):
        series = self.model(name='Some Video Name')
        self.assertEqual(series.slug, 'some-video-name')

        # Duplicate slug
        self.assertRaises(db.BadValueError, self.model, name='Some Video Name')

class TestTalk(unittest.TestCase):

    def setUp(self):
        dataset.setup()

    def tearDown(self):
        dataset.clear()

    @staticmethod
    def model(put=True, remove=None, **kwargs):
        user = User(email='test@freetalks.com')
        series = TestSeries.model()
        options = {
            'title': 'Some Title',
            'summary': 'This is a test summary.',
            'link': 'http://www.example.com/',
            'presenters': ['Jane Smith', 'John Smith'],
            'series': series,
            'tags': ['AppEngine', 'Example', 'Python'],
            'date': dt.now(),
            'source_type': 'blip.tv',
            'source_link_id': '3264001',
            'source_media_id': 'AYHItEYC',
            'source_posted_date': dt.now(),
            'created_user': user,
            'updated_user': user,
        }
        options.update(kwargs)
        if remove:
            for name in remove:
                del options[name]
        series = models.Series(**options)
        if put:
            series.put()
        return series

    def test_title(self):
        self.assertRaises(db.BadValueError, self.model, title='')
        self.assertRaises(db.BadValueError, self.model, remove=['title'])
