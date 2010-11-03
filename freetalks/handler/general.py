from freetalks import web

class Home(web.Handler):

    def get(self):
        self.render('general/home.html', content='Welcome to Freetalks')
