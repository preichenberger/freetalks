from google.appengine.ext import db
from freetalks import models
from freetalks import web

class Display(web.Handler):

    def get(self, slug):
        series_query = models.Series.all()
        series_query.filter("slug =", slug)
        series = series_query.fetch(limit=1)

        if series is not None:
            self.render('series/display.html', content='Render series: %s' % series)
        else:
            self.set_404()
