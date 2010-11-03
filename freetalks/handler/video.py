from freetalks import web

class Display(web.Handler):

    def get(self, video):
        self.render('video/display.html', content='Display video: %s' % video)
