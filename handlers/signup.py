from app import Handler
from handlers.auth import Auth


class SignUpHandler(Handler):
    def get(self):
        self.render("signup.html")

    def post(self):

        username = self.request.get("username")
        password = self.request.get("password")
        password_verify = self.request.get("password_verify")
        email = self.request.get("email")

        try:
            user = Auth.signup(username, password, password_verify, email)
            # sets the auth cookie
            self.response.headers.add_header('Set-Cookie', 'user_id=' + Auth.make_secure_cookie(user))
            self.redirect("/welcome")

        except Exception as e:
            self.render("signup.html", username=username, email=email, error=e)
