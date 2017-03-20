from google.appengine.ext import db


class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    email = db.StringProperty(required=False)
    avatar = db.BlobProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty(required=False)
    bio = db.StringProperty(required=False)

    @classmethod
    def by_username(cls, username):
        """
        Retrieves a user by its username
        :param username:
        :return: User object
        """
        user = User.all().filter('username =', username).get()
        return user

    @classmethod
    def by_id(cls, uid):
        """
        Retrives a user by its ID
        :param uid:
        :return: User object
        """
        return User.get_by_id(uid)
