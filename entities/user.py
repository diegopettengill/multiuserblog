from google.appengine.ext import db


class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    email = db.StringProperty(required=False)
    avatar = db.BlobProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def by_username(cls, username):
        user = User.all().filter('username =', username).get()
        return user

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid)
