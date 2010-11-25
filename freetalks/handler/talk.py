from freetalks import models
from freetalks.utils import shortcuts
from freetalks import web

class Display(web.Handler):

    def get(self, slug, id):
        talk = shortcuts.get_by_id(models.Talk, id)
        if self.request.path != talk.url:
            self.redirect(talk.url)
        elif talk is not None:
            self.render('talk.html', talk=talk)
        else:
            self.error(404)

class Embed(web.Handler):

    def get(self, slug, id):
        talk = shortcuts.get_by_id(models.Talk, id)
        if talk is not None:
            self.render('talk_embed.html', talk=talk)
        else:
            self.error(404)
