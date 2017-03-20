from app import Handler
from entities.post import Post
from handlers.auth import Auth


class EditPostHandler(Handler):
    def get(self, post_id):
        if not Auth.is_logged_in(self.request):
            self.redirect("/login")
        else:
            current_user = Auth.get_current_user(self.request.cookies.get("user_id"))
            if post_id:

                post = Post.by_id(int(post_id))

                # verify if this post matches user logged in
                if post.author.key().id() == current_user.key().id():
                    self.render("editpost.html", post=post)
                else: # redirect the user to the view
                    self.redirect("/post/"+str(post.key().id()))

            else:
                print "404"  # @TODO redirect the user to a 404 error

    def post(self, post_id):

        title = self.request.get("title")
        text = self.request.get("content")

        if title and text:
            post = Post.by_id(int(post_id))
            post.title = title
            post.content = text
            post.put()
            self.redirect("/post/" + str(post.key().id()))
        else:
            error = "Title and Text must be provided to submit an article!"
            self.render("newpost.html", error=error)
