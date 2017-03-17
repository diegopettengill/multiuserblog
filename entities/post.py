from google.appengine.ext import db
from entities.user import User


class Post(db.Model):
    author = db.ReferenceProperty(User, collection_name="author")
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def by_id(cls, post_id):
        return Post.get_by_id(post_id)
