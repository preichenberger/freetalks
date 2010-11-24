from freetalks import models
from freetalks import web
from freetalks.utils import pager

class Display(web.Handler):

    def get(self):
        series = models.Series.all().order('-created_date')
        p = pager.Pager(series, self.request)
        self.render('home.html', pager=p)
