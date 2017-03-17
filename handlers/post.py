from app import Handler
from entities.post import Post
from entities.comment import Comment


class PostHandler(Handler):
    def get(self, id):
        post = Post.get_by_id(int(id))

        comments = Comment.by_post(post)

        if post:
            self.render("post.html", post=post, comments=comments)
        else:
            print "404" # @TODO add a 404 page here
