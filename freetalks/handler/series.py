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
        series = series_query.get()
       
        if series is None:
            self.set_404()

        talks_query = models.Talk.all()
        talks_query.filter('series =', series.key())
        series_talks = talks_query.fetch(limit=10)

        self.render('series/display.html', series=series, series_talks=series_talks)
