from google.appengine.ext import db
from freetalks import models
from freetalks.utils import shortcuts
from freetalks import web

class Display(web.Handler):

    def get(self, id):
        talk = shortcuts.get_by_id(models.Talk, id)
        if talk is not None:
            self.render('talk/display.html', talk=talk)
        else:
            self.set_404()
