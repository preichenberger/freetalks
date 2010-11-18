from freetalks import web

class Display(web.Handler):

    def get(self, series):
        self.render('series/display.html', content='Render series: %s' % series)
