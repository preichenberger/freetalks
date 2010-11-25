from google.appengine.ext import db
from freetalks import utils
from freetalks.utils import media
from freetalks.utils import slugify

SOURCE_CHOICES = set(['blip.tv', 'ted', 'vimeo', 'youtube'])

class Talk(db.Model):
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
        return '/%s' % self.key().id()

    @property
    def media(self):
        if not hasattr(self, '_media'):
            self._media = media.get(self.source)
        return self._media

    def clean(self):
        pass

    def validate(self):
        pass

    def put(self, validate=True, clean=True, *args, **kwargs):
        if clean:
            self.clean()
        if validate:
            self.validate()
        super(Talk, self).put(*args, **kwargs)

class Series(db.Model):
    name = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    summary = db.TextProperty()
    link = db.LinkProperty()
    talks = db.ListProperty(db.Key)
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
        if not utils.SERIES_NAME_RE.match(self.name):
            raise db.BadValueError('Series name must start with an alphabetic character.')
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
