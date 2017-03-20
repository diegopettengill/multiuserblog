from app import Handler
from handlers.auth import Auth
from entities.user import User


class ProfileHandler(Handler):
    def get(self):
        if Auth.is_logged_in(self.request):
            self.render("profile.html")
        else:
            self.redirect("/login")

    def post(self):

        name = self.request.get("name")
        bio = self.request.get("bio")

        if name and bio:
            self.current_user.name = name;
            self.current_user.bio = bio;
            self.current_user.put()

            success = "Profile updated!"

            self.render("profile.html", success=success)

        else:
            error = ""
