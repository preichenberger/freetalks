import os
import webapp2
from google.appengine.ext.webapp import template

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), '..', 'templates')

class Handler(webapp2.RequestHandler):

    def render(self, path, **kwargs):
        self.response.out.write(
            template.render(
                os.path.join(TEMPLATE_PATH, path),
                kwargs,
            )
        )

class Handle404(webapp2.RequestHandler):

    def get(self):
        self.error(404)
        self.render('404.html')
