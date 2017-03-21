from app import Handler
from handlers.auth import Auth


class LoginHandler(Handler):
    def get(self):
        self.render("login.html")

    def post(self):

        username = self.request.get("username")
        password = self.request.get("password")

        try:
            user = Auth.login(username, password)
            # sets the auth cookie
            self.response.headers.add_header('Set-Cookie',
                                             'user_id=' +
                                             Auth.make_secure_cookie(user))
            self.redirect("/welcome")
        except Exception as e:
            self.render("login.html", error=e)
