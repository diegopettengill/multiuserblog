from app import Handler
from entities.post import Post
from handlers.auth import Auth


class NewPostHandler(Handler):
    def get(self):
        if not Auth.is_logged_in(self.request):
            self.redirect("/signup")
        else:
            self.render("newpost.html")

    def post(self):

        current_user_id = str(Auth.get_current_user(self.request.cookies.get("user_id")).key().id())
        title = self.request.get("title")
        text = self.request.get("content")

        if title and text:
            post = Post(author_id=current_user_id, title=title, content=text)
            post.put()
            self.redirect("/post/" + str(post.key().id()))
        else:
            error = "Title and Text must be provided to submit an article!"
            self.render("newpost.html", error=error)
