from freetalks import models
from freetalks import web

class Display(web.Handler):

    def get(self):
        series_list = models.Series.all()
        self.render('home.html', series_list=series_list)
