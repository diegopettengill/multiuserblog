from app import Handler
from entities.post import Post
from handlers.auth import Auth
from handlers.decorators import restricted


class EditPostHandler(Handler):
    @restricted
    def get(self, post_id):

        current_user = self.current_user

        post = Post.by_id(int(post_id))

        # verify if post exists
        if post is not None:

            # verify if this post matches user logged in
            if post.author.key().id() == current_user.key().id():
                self.render("editpost.html", post=post)
            else:  # redirect the user to the view
                self.redirect("/post/" + str(post.key().id()))

        else:
            self.redirect("/not-found")

    @restricted
    def post(self, post_id):

        if not Auth.is_logged_in(self.request):
            self.redirect("/login")
        else:
            current_user = self.current_user

            post = Post.by_id(int(post_id))

            # verify if post exists
            if post is not None:

                # verify if this post matches user logged in
                if post.author.key().id() == current_user.key().id():

                    title = self.request.get("title")
                    text = self.request.get("content")

                    if title and text:
                        post = Post.by_id(int(post_id))
                        post.title = title
                        post.content = text
                        post.put()
                        self.redirect("/post/" + str(post.key().id()))
                    else:
                        error = "Title and Text must be provided" \
                                " to submit an article!"
                        self.render("newpost.html", error=error)

                else:  # redirect the user to the view
                    self.redirect("/post/" + str(post.key().id()))

            else:  # redirect the user to the view
                self.redirect("/not-found")
