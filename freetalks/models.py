from google.appengine.ext import db

SOURCE_CHOICES = set(['blip.tv', 'ted', 'vimeo', 'youtube'])

class Series(db.Model):
    name = db.StringProperty()
    slug = db.StringProperty()
    link = db.LinkProperty(required=False)
    about = db.TextProperty()
    created_user = db.UserProperty(required=True)
    updated_user = db.UserProperty(required=True)
    created_date = db.DateTimeProperty(auto_now_add=True)
    updated_date = db.DateTimeProperty(auto_now=True)

class Talk(db.Model):
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
    created_user = db.UserProperty(required=True)
    updated_user = db.UserProperty(required=True)
    created_date = db.DateTimeProperty(auto_now_add=True)
    updated_date = db.DateTimeProperty(auto_now=True)
