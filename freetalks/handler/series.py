from freetalks import models
from freetalks import web

class Display(web.Handler):

    def get(self, slug):
        series = models.Series.all().filter('slug =', slug).get()
        if series:
            talks = models.Talk.get(series.talks)
            self.render('series.html', series=series, talks=talks)
        else:
            self.error(404)

class Json(web.Handler):

    def get(self, slug):
        series = models.Series.all().filter('slug =', slug).get()
        if series:
            self.response.out.write(series.json())
        else:
            self.error(404)
