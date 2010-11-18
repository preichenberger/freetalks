import webapp2
from freetalks import handler

application = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler.general.Home, 'home'),
    webapp2.Route(r'/talks', handler.talk.List, 'talk-list'),
    webapp2.Route(r'/talks/<id:[\d]+>', handler.talk.Display, 'talk-display'),
])
