from app import Handler
from handlers.auth import Auth
from entities.post import Post


class WelcomeHandler(Handler):
    def get(self):
        if Auth.is_logged_in(self.request):

            posts = Post.by_author(self.current_user)

            self.render("welcome.html", posts=posts)
        else:
            self.redirect("/login")
