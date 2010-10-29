import webapp2
from freetalks import handler

application = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler.Home),
])
