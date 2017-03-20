import pdb
from google.appengine.ext import db
from entities.user import User
from entities.post import Post


class Comment(db.Model):
    author = db.ReferenceProperty(User, collection_name="author_comment")
    post = db.ReferenceProperty(Post, collection_name="post_comment")
    text = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def by_post(cls, post):
        comments = Comment.gql("WHERE post = :1 ORDER BY created DESC", post.key())
        return comments
