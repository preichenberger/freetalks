import webapp2
from freetalks import handler

application = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler.general.Home, 'home'),
    webapp2.Route(r'/talk/<talk:[a-z\d-]*>', handler.talk.Display, 'talk-display'),
])
