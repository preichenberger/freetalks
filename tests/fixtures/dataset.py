from google.appengine.ext import db
from google.appengine.api.users import User
from freetalks import models
import datetime

def clear_type(obj_type):
    obj_list = obj_type.all()
    for obj in obj_list:
        obj.delete()

def put_list(obj_list):
    for obj in obj_list:
        obj.put()

def clear():
    clear_type(models.Talk)
    clear_type(models.Series)

def setup():
    test_user = User(email='test@freetalks.com')

    series_list = []

    pycon_series = models.Series(
        name='PyCon',
        slug='python_slug',
        link='http://pycon.org/',
        created_user=test_user,
        updated_user=test_user,
    )

    series_list.append(pycon_series)

    put_list(series_list)

    talks = []

    talks.append(
        models.Talk(
            title='Plenary: Introduction and Welcome',
            summary='Plenary: Introduction and Welcome',
            link='http://pycon.org',
            presenters=['Van Lindberg'],
            tags=['python', 'PyCon'],
            date=datetime.datetime.today(),
            source_type='blip.tv',
            source_link_id='3264001',
            source_media_id='3264001',
            source_posted_date=datetime.datetime(2010, 2, 21),
            created_user=test_user,
            updated_user=test_user,
            series=pycon_series,
        )
    )

    talks.append(
        models.Talk(
            title="Aaron Huey: America's native prisoners of war",
            summary="Aaron Huey: America's native prisoners of war",
            link='http://test',
            presenters=['Aaron Huey'],
            tags=['python', 'america'],
            date=datetime.datetime.today(),
            source_type='ted',
            source_link_id='aaron_huey',
            source_media_id='AaronHuey_2010X-medium.flv',
            source_posted_date=datetime.datetime(2010, 9, 1),
            created_user=test_user,
            updated_user=test_user,
            series=pycon_series,
        )
    ) 

    talks.append(
        models.Talk(
            title='Python vs. Ruby: A Battle to The Death',
            summary='Python vs. Ruby: A Battle to The Death',
            link='http://www.seapig.org/NorthwestPythonDay',
            presenters=['Gary Bernhardt'],
            tags=['python', 'ruby'],
            date=datetime.datetime.today(),
            source_type='vimeo',
            source_link_id='9471538',
            source_media_id='9471538',
            source_posted_date=datetime.datetime(2010, 2, 1),
            created_user=test_user,
            updated_user=test_user,
            series=pycon_series,
        )
    )

    talks.append(
        models.Talk(
            title='Google Developers Day US - Python Design Patterns',
            summary='Google Developers Day US - Python Design Patterns',
            link='http://www.google.com/events/developerday/2010',
            presenters=['Alex Martelli'],
            tags=['python'],
            date=datetime.datetime.today(),
            source_type='youtube',
            source_link_id='0vJJlVBVTFg',
            source_media_id='0vJJlVBVTFg',
            source_posted_date=datetime.datetime(2007, 6, 4),
            created_user=test_user,
            updated_user=test_user,
            series=pycon_series,
        )
    ) 

    put_list(talks)
