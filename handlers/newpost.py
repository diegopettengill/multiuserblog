from app import Handler
from entities.post import Post


class NewPostHandler(Handler):
    def get(self):
        self.render("newpost.html")

    def post(self):
        title = self.request.get("title")
        text = self.request.get("content")

        if title and text:
            post = Post(title=title, content=text)
            post.put()
            self.redirect("/post/"+str(post.key().id()))
        else:
            error = "Title and Text must be provided to submit an article!"
            self.render("newpost.html", error=error)
