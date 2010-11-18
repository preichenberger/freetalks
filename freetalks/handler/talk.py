from google.appengine.ext import db
from freetalks import models
from freetalks import web

class Display(web.Handler):

    def get(self, id):
        try:
            talk = models.Talk.get(id)
            self.render('talk/display.html', talk=talk)
        except db.BadKeyError:
            self.set_404()
