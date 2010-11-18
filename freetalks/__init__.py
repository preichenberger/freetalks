import webapp2
from freetalks import handler

application = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler.general.Home, 'home'),
    webapp2.Route(r'/talks', handler.talk.List, 'talk-list'),
    webapp2.Route(r'/talks/<id:[\d]+>', handler.talk.Display, 'talk-display'),
    webapp2.Route(r'/series', handler.series.List, 'series-list'),
    webapp2.Route(r'/series/<slug:[a-zA-Z0-9_-]+>', handler.series.Display, 'series-display'),
])
