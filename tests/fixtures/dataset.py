from google.appengine.ext import db
from google.appengine.api.users import User
from freetalks import models
import datetime

def clear_type(obj_type):
    obj_list = obj_type.all()
    for obj in obj_list:
        obj.delete()

def clear():
    clear_type(models.Talk)
    clear_type(models.Series)

def setup():
    test_user = User(email='test@freetalks.com')

    pycon_series = models.Series(
        name='PyCon',
        slug='python-slug',
        link='http://pycon.org/',
        about='A series of PyCon talks',
        created_user=test_user,
        updated_user=test_user,
    ).put()

    models.Talk(
        title='Plenary: Introduction and Welcome',
        presenters=['Van Lindberg'],
        link='http://us.pycon.org/2010/conference/schedule/event/3/',
        tags=['python', 'PyCon'],
        date=datetime.datetime.today(),
        source_type='blip.tv',
        source_link_id='3264001',
        source_media_id='AYHItEYC',
        source_posted_date=datetime.datetime(2010, 2, 21),
        summary='Intro to PyCon 2010',
        created_user=test_user,
        updated_user=test_user,
        series=pycon_series,
    ).put()
    models.Talk(
        title="Aaron Huey: America's native prisoners of war",
        presenters=['Aaron Huey'],
        tags=['python', 'america'],
        date=datetime.datetime.today(),
        source_type='ted',
        source_link_id='aaron_huey',
        source_media_id='AaronHuey_2010X',
        source_posted_date=datetime.datetime(2010, 9, 1),
        summary='A discussion on America and prisoners of war',
        created_user=test_user,
        updated_user=test_user,
        series=pycon_series,
    ).put()
    models.Talk(
        title='Python vs. Ruby: A Battle to The Death',
        presenters=['Gary Bernhardt'],
        tags=['python', 'ruby'],
        date=datetime.datetime.today(),
        source_type='vimeo',
        source_link_id='9471538',
        source_media_id='9471538',
        summary='Noob fest',
        source_posted_date=datetime.datetime(2010, 2, 1),
        created_user=test_user,
        updated_user=test_user,
        series=pycon_series,
    ).put()
    models.Talk(
        title='Google Developers Day US - Python Design Patterns',
        presenters=['Alex Martelli'],
        tags=['python'],
        date=datetime.datetime.today(),
        source_type='youtube',
        source_link_id='0vJJlVBVTFg',
        source_media_id='0vJJlVBVTFg',
        summary='Python has some patterns for design',
        source_posted_date=datetime.datetime(2007, 6, 4),
        created_user=test_user,
        updated_user=test_user,
        series=pycon_series,
    ).put()
