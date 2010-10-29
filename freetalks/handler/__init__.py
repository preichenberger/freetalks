from freetalks import web

class Home(web.Handler):

    def get(self):
        self.render('simple.html', content='Welcome to Freetalks')
