from app import Handler
from handlers.auth import Auth


class WelcomeHandler(Handler):
    def get(self):
        if Auth.is_logged_in(self.request):
            self.render("welcome.html")
        else:
            self.redirect("/signup")