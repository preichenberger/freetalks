from freetalks import models
from freetalks.utils import shortcuts
from freetalks import web

class Display(web.Handler):

    def get(self, slug, order):
        talk = models.Talk.get_by_slug_order(slug, order)
        if talk:
            self.render('talk.html', talk=talk)
        else:
            self.error(404)

class Embed(web.Handler):

    def get(self, slug, order):
        talk = models.Talk.get_by_slug_order(slug, order)
        if talk is not None:
            self.render('talk_embed.html', talk=talk)
        else:
            self.error(404)
