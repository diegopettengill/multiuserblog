from app import Handler
from entities.post import Post


class PostHandler(Handler):
    def get(self, id):
        post = Post.get_by_id(int(id))
        if post:
            self.render("post.html", post=post)
