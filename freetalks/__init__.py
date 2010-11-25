import webapp2
from freetalks import handler
from freetalks import utils
from freetalks import web

application = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler.home.Display, 'home'),
    webapp2.Route(r'/<id:[\d]+>', handler.talk.Display, 'talk'),
    webapp2.Route(r'/<id:[\d]+>/embed', handler.talk.Embed, 'talk-embed'),
    webapp2.Route(r'/<id:[\d]+>/json', handler.talk.Json, 'talk-json'),
    webapp2.Route(r'/<slug:%s>' % utils.SERIES_NAME, handler.series.Display, 'series'),
    webapp2.Route(r'/<slug:%s>/json' % utils.SERIES_NAME, handler.series.Json, 'series-json'),
])
application.error_handlers[404] = web.Handle404
