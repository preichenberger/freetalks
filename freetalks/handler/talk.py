from freetalks import web

class Display(web.Handler):

    def get(self, talk):
        self.render('talk/display.html', content='Render talk: %s' % talk)
