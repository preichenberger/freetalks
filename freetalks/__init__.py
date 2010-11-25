import webapp2
from freetalks import handler
from freetalks import web

application = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler.home.Display, 'home'),
    webapp2.Route(r'/<slug:[a-zA-Z0-9_-]+>', handler.series.Display, 'series'),
    webapp2.Route(r'/<slug:[a-zA-Z0-9_-]+>/<order:[\d]+>', handler.talk.Display, 'talk'),
    webapp2.Route(r'/<slug:[a-zA-Z0-9_-]+>/<order:[\d]+>/embed', handler.talk.Embed, 'talk-embed'),
])
application.error_handlers[404] = web.Handle404
