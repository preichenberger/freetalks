from google.appengine.ext import db
from freetalks.models import Series
from freetalks.models import Talk

def clear():
    talks = Talk.all()
    series = Series.all()
    
    db.delete(talks)
    db.delete(series)

def setup():
    pycon_series = Series(name="PyCon",
                    slug="python_slug",
                    link="http://pycon.org/")

    db.put(pycon_series)


    blip_talk = Talk(title="Introduction to Traits",
                            summary="Introduction to Traits",
                            link="http://www.bliptv.com/file/3633134",
                            presenters=['Silas Fischer', 'Ben Uretsky'],
                            tags=['python', 'PyCon'],
                            series=pycon_series)  

    db.put(blip_talk)
