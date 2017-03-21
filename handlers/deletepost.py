from app import Handler
from entities.post import Post
from handlers.auth import Auth
from handlers.decorators import restricted


class DeletePostHandler(Handler):
    @restricted
    def get(self, post_id):

        current_user = self.current_user

        post = Post.by_id(int(post_id))

        if post is not None:

            # verify if this post matches user logged in
            if post.author.key().id() == current_user.key().id():
                post.delete()
                self.redirect("/")
            else:  # redirect the user to the view
                self.redirect("/post/" + str(post.key().id()))

        else:
            self.redirect("/not-found")