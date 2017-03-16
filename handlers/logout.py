from app import Handler
from handlers.auth import Auth


class LogoutHandler(Handler):
    def get(self):
        Auth.logout(self.response)
        self.redirect("/")
