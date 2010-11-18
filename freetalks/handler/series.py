from google.appengine.ext import db
from freetalks import models
from freetalks import web

class List(web.Handler):

    def get(self):
        series_list = models.Series.all()
        self.render('series/index.html', series_list=series_list)

class Display(web.Handler):

    def get(self, slug):
        series_query = models.Series.all()
        series_query.filter("slug =", slug)
        series = series_query.fetch(limit=1)

        if series is not None:
            self.render('series/display.html', content='Render series: %s' % series)
        else:
            self.set_404()
