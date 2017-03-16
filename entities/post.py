from google.appengine.ext import db


class Post(db.Model):
    author_id = db.StringProperty(required=True)
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now_add=True)