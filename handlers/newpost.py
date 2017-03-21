from app import Handler
from entities.post import Post
from handlers.decorators import restricted


class NewPostHandler(Handler):
    @restricted
    def get(self):
        self.render("newpost.html")

    @restricted
    def post(self):

        current_user = self.current_user
        title = self.request.get("title")
        text = self.request.get("content")

        if title and text:
            post = Post(author=current_user, title=title, content=text)
            post.put()
            self.redirect("/post/" + str(post.key().id()))
        else:
            error = "Title and Text must be provided to submit an article!"
            self.render("newpost.html", error=error)
