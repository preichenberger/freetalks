import webapp2
from freetalks import handler

application = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler.general.Home, 'home'),
    webapp2.Route(r'/talk/<talk:[\w]+>', handler.talk.Display, 'talk-display'),
])
