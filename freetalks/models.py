from django.template.defaultfilters import slugify
from google.appengine.ext import db
from freetalks import exceptions
from freetalks.utils import video

SOURCE_CHOICES = set(['blip.tv', 'ted', 'vimeo', 'youtube'])

class Series(db.Model):
    name = db.StringProperty(required=True)
    slug = db.CategoryProperty(required=True)
    link = db.LinkProperty()
    about = db.TextProperty()
    created_user = db.UserProperty(required=True)
    updated_user = db.UserProperty(required=True)
    created_date = db.DateTimeProperty(auto_now_add=True)
    updated_date = db.DateTimeProperty(auto_now=True)

    def __init__(self, *args, **kwargs):
        if 'name' in kwargs and 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs['name'])
        super(Series, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.title)

    def validate(self):
        series = Series.all()
        if self.is_saved():
            series = series.filter('__key__ !=', self.key())
        series = series.filter('slug =', self.slug)
        if series.count(1) == 1:
            raise exceptions.ValidationError('Slug "%s" already exists.' % self.slug)

    def put(self, *args, **kwargs):
        self.clean()
        self.validate()
        super(Series, self).put(*args, **kwargs)

    @property
    def url(self):
        return '/series/%s' % self.slug

class Talk(db.Model):
    title = db.StringProperty(required=True)
    summary = db.TextProperty()
    link = db.LinkProperty()
    presenters = db.StringListProperty()
    series = db.ReferenceProperty(Series)
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

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    @property
    def url(self):
        return '/talks/%s' % self.key().id()

    @property
    def source(self):
        return video.get(self.source_type, self.source_media_id, self.source_link_id)

    def clean(self):
        pass

    def validate(self):
        pass

    def put(self, *args, **kwargs):
        self.clean()
        self.validate()
        super(Talk, self).put(*args, **kwargs)
