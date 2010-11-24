import webapp2
from freetalks import handler
from freetalks import web

application = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler.home.Display, 'home'),
    webapp2.Route(r'/<slug:[a-zA-Z0-9_-]+>', handler.series.Display, 'series-display'),
    webapp2.Route(r'/<slug:[a-zA-Z0-9_-]+>/<id:[\d]+>', handler.talk.Display, 'talk-display'),
])
application.error_handlers[404] = web.Handle404
