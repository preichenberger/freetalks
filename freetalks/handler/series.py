from freetalks import models
from freetalks import web
from freetalks.utils import pager

class Display(web.Handler):

    def get(self, slug):
        series = models.Series.all().filter("slug =", slug).get()
        if series:
            talks = models.Talk.all().filter('series =', series.key())
            talks = pager.Pager(talks, self.request)
            self.render('series.html', series=series, talks=talks)
        else:
            self.error(404)
