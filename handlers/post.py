from app import Handler
from entities.post import Post
from entities.comment import Comment


class PostHandler(Handler):
    def get(self, id):

        post = Post.get_by_id(int(id))

        if post is not None:

            comments = Comment.by_post(post)

            if post:
                self.render("post.html", post=post, comments=comments)
            else:
                self.redirect("/not-found")

        else:
            self.redirect("/not-found")
