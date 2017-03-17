import pdb
from google.appengine.ext import db
from entities.user import User
from entities.post import Post


class Comment(db.Model):
    author = db.ReferenceProperty(User, collection_name="author_comment")
    post = db.ReferenceProperty(Post, collection_name="post")
    text = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def by_post(cls, post):
        comments = Comment.gql("WHERE post = :1", post.key())
        return comments
