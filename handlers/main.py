from app import Handler
from entities.post import Post
from handlers.auth import Auth


class IndexHandler(Handler):
    def get(self):

        offset = 0

        if self.request.get("page"):
            offset = int(self.request.get("page")) - 1

        current_page = offset + 1
        next_page = current_page + 1
        previous_page = current_page - 1

        current_user = self.current_user
        posts_query = Post.list(10, str(offset*10))

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

        self.render("index.html",
                    posts=posts,
                    page=current_page,
                    next_page=next_page,
                    previous_page=previous_page)
