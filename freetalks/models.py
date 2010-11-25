import json
from google.appengine.ext import db
from freetalks import utils
from freetalks.utils import media
from freetalks.utils import slugify

class Talk(db.Model):
    title = db.StringProperty(required=True)
    summary = db.TextProperty()
    link = db.LinkProperty()
    presenters = db.StringListProperty()
    tags = db.StringListProperty()
    date = db.DateTimeProperty()
    source_data = db.StringListProperty()
    created_user = db.UserProperty(required=True)
    updated_user = db.UserProperty(required=True)
    created_date = db.DateTimeProperty(auto_now_add=True)
    updated_date = db.DateTimeProperty(auto_now=True)

    def __init__(self, *args, **kwargs):
        if 'sources' in kwargs:
            self.sources = kwargs['sources']
            del kwargs['sources']
        super(Talk, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    @property
    def url(self):
        return '/%s' % self.key().id()

    def data(self):
        data = {
            'id': self.key().id(),
            'title': self.title,
            'summary': self.summary,
            'link': self.link,
            'presenters': self.presenters,
            'tags': self.tags,
            'date': utils.jsonify(self.date),
            'source': [],
            'created_date': utils.jsonify(self.created_date),
            'updated_date': utils.jsonify(self.updated_date),
        }
        for source in self.sources:
            source_dict = {
                'type': source.type,
                'media_id': source.media_id,
            }
            if source.link_id:
                source_dict['link_id'] = source.link_id
            data['source'].append(source_dict)
        return data

    def json(self):
        return json.dumps(self.data())

    def clean(self):
        pass

    def validate(self):
        if hasattr(self, '_sources'):
            for source in self.sources:
                try:
                    source.validate()
                except ValueError, error:
                    raise db.BadValueError(error)

    @property
    def sources(self):
        if not hasattr(self, '_sources'):
            self._sources = [media.Source.init(data) for data in self.source_data]
        return self._sources

    @sources.setter
    def sources(self, value=None):
        if isinstance(value, (list, tuple)):
            self._sources = value

    @property
    def media(self):
        if len(self.sources) > 0:
            return self.sources[0]
        return None

    def put(self, validate=True, clean=True, *args, **kwargs):
        if clean:
            self.clean()
        if validate:
            self.validate()
        if hasattr(self, '_sources'):
            self.source_data = [source.data() for source in self.sources]
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

    def data(self):
        data = {
            'id': self.key().id(),
            'name': self.name,
            'slug': self.slug,
            'summary': self.summary,
            'talks': [key.id() for key in self.talks],
            'created_date': utils.jsonify(self.created_date),
            'updated_date': utils.jsonify(self.updated_date),
        }
        return data

    def json(self):
        return json.dumps(self.data())

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
