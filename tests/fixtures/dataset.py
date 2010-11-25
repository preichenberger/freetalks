from google.appengine.ext import db
from google.appengine.api.users import User
from freetalks import models
from freetalks.utils import media
import datetime

def clear_type(obj_type):
    obj_list = obj_type.all()
    for obj in obj_list:
        obj.delete()

def clear():
    clear_type(models.Talk)
    clear_type(models.Series)

def setup():
    user = User(email='test@freetalks.com')

    talks = []
    talks.append(models.Talk(
        title='Plenary: Introduction and Welcome',
        presenters=['Van Lindberg'],
        link='http://us.pycon.org/2010/conference/schedule/event/3/',
        tags=['python', 'PyCon'],
        date=datetime.datetime.today(),
        sources=[media.Source('bliptv', 'AYHItEYC', '3264001')],
        summary='Intro to PyCon 2010',
        created_user=user,
        updated_user=user,
    ))
    talks.append(models.Talk(
        title="Aaron Huey: America's native prisoners of war",
        presenters=['Aaron Huey'],
        tags=['python', 'america'],
        date=datetime.datetime.today(),
        sources=[media.Source('ted', 'AaronHuey_2010X', 'aaron_huey')],
        summary='A discussion on America and prisoners of war',
        created_user=user,
        updated_user=user,
    ))
    talks.append(models.Talk(
        title='Python vs. Ruby: A Battle to The Death',
        presenters=['Gary Bernhardt'],
        tags=['python', 'ruby'],
        date=datetime.datetime.today(),
        sources=[media.Source('vimeo', '9471538')],
        summary='Noob fest',
        created_user=user,
        updated_user=user,
    ))
    talks.append(models.Talk(
        title='Google Developers Day US - Python Design Patterns',
        presenters=['Alex Martelli'],
        tags=['python'],
        date=datetime.datetime.today(),
        sources=[media.Source('youtube', '0vJJlVBVTFg')],
        summary='Python has some patterns for design',
        created_user=user,
        updated_user=user,
    ))

    for talk in talks:
        talk.put()

    talks = [talk.key() for talk in talks]

    series = models.Series(
        name='PyCon',
        link='http://pycon.org/',
        summary='A series of PyCon talks',
        talks=talks,
        created_user=user,
        updated_user=user,
    )
    series.put()
