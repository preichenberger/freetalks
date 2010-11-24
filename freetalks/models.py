from google.appengine.ext import db
from freetalks.utils import media
from freetalks.utils import slugify

SOURCE_CHOICES = set(['blip.tv', 'ted', 'vimeo', 'youtube'])

class Series(db.Model):
    name = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    summary = db.TextProperty()
    link = db.LinkProperty()
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
            raise db.BadValueError('Slug "%s" already exists.' % self.slug)

    def put(self, validate=True, clean=True, *args, **kwargs):
        if clean:
            self.clean()
        if validate:
            self.validate()
        super(Series, self).put(*args, **kwargs)

    @property
    def url(self):
        return '/%s' % self.slug

class Talk(db.Model):
    series = db.ReferenceProperty(Series, required=True)
    series_order = db.IntegerProperty(required=True)
    title = db.StringProperty(required=True)
    summary = db.TextProperty()
    link = db.LinkProperty()
    presenters = db.StringListProperty()
    tags = db.StringListProperty()
    date = db.DateTimeProperty()
    source = db.StringListProperty()
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
        return '%s/%s' % (self.series.url, self.key().id())

    @property
    def media(self):
        if not hasattr(self, '_media'):
            self._media = media.get(self.source)
        return self._media

    def clean(self):
        pass

    def validate(self):
        talks = Talk.all()
        talks.filter('series =', self.series)
        talks.filter('series_order =', self.series_order)
        if talks.count(1) == 1:
            raise db.BadValueError('Series order "%s" already exists.' % self.series_order)

    def put(self, validate=True, clean=True, *args, **kwargs):
        if clean:
            self.clean()
        if validate:
            self.validate()
        super(Talk, self).put(*args, **kwargs)
