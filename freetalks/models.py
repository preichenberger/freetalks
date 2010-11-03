from google.appengine.ext import db
from freetalks.utils import video

SOURCE_CHOICES = set(['blip.tv', 'ted', 'vimeo', 'youtube'])

class BaseModel(object):
    created_user = db.UserProperty(required=True)
    updated_user = db.UserProperty(required=True)
    created_date = db.DateTimeProperty(auto_now_add=True)
    updated_date = db.DateTimeProperty(auto_now=True)

class Series(db.Model, BaseModel):
    parent = db.ReferenceProperty(Series, required=False)
    name = db.StringProperty()
    slug = db.StringProperty()
    link = db.LinkProperty(required=False)
    about = db.TextProperty()

class Talk(db.Model, BaseModel):
    title = db.StringProperty(required=True)
    summary = db.TextProperty()
    link = db.LinkProperty()
    presenters = db.StringListProperty()
    series = db.ReferenceProperty(Series, required=False)
    tags = db.StringListProperty()
    date = db.DateTimeProperty()
    source_type = db.StringProperty(choices=SOURCE_CHOICES)
    source_link_id = db.StringProperty()
    source_media_id = db.StringProperty()
    source_posted_date = db.DateTimeProperty()

    @property
    def source(self):
        return video.get(self.source_type, self.source_media_id, self.source_link_id)
