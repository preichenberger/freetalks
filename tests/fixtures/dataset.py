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
    user = User(email='test@freetalks.com')

    pycon_series = models.Series(
        name='PyCon',
        link='http://pycon.org/',
        about='A series of PyCon talks',
        created_user=user,
        updated_user=user,
    )
    pycon_series.put()

    models.Talk(
        series=pycon_series,
        series_order=0,
        title='Plenary: Introduction and Welcome',
        presenters=['Van Lindberg'],
        link='http://us.pycon.org/2010/conference/schedule/event/3/',
        tags=['python', 'PyCon'],
        date=datetime.datetime.today(),
        source=['blip.tv\tAYHItEYC\t3264001'],
        summary='Intro to PyCon 2010',
        created_user=user,
        updated_user=user,
    ).put()
    models.Talk(
        series=pycon_series,
        series_order=1,
        title="Aaron Huey: America's native prisoners of war",
        presenters=['Aaron Huey'],
        tags=['python', 'america'],
        date=datetime.datetime.today(),
        source=['ted\tAaronHuey_2010X\taaron_huey'],
        summary='A discussion on America and prisoners of war',
        created_user=user,
        updated_user=user,
    ).put()
    models.Talk(
        series=pycon_series,
        series_order=2,
        title='Python vs. Ruby: A Battle to The Death',
        presenters=['Gary Bernhardt'],
        tags=['python', 'ruby'],
        date=datetime.datetime.today(),
        source=['vimeo\t9471538'],
        summary='Noob fest',
        created_user=user,
        updated_user=user,
    ).put()
    models.Talk(
        series=pycon_series,
        series_order=3,
        title='Google Developers Day US - Python Design Patterns',
        presenters=['Alex Martelli'],
        tags=['python'],
        date=datetime.datetime.today(),
        source=['youtube\t0vJJlVBVTFg'],
        summary='Python has some patterns for design',
        created_user=user,
        updated_user=user,
    ).put()
