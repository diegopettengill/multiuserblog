from app import Handler
from entities.post import Post
from handlers.auth import Auth


class IndexHandler(Handler):
    def get(self):

        current_user = Auth.get_current_user(self.request.cookies.get("user_id"))
        # posts = db.GqlQuery("SELECT * from Post order by created desc limit 10")
        posts_query = Post.list()

        # iterates over posts
        posts = []

        for post in posts_query:
            if Auth.is_logged_in(self.request):
                for like in post.post_like:
                    if like.author.key().id() == current_user.key().id():
                        post.liked = True
                    else:
                        post.liked = False
            posts.append(post)

        self.render("index.html", posts=posts)
