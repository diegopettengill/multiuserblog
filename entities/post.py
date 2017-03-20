from google.appengine.ext import db
from entities.user import User


class Post(db.Model):
    author = db.ReferenceProperty(User, collection_name="author", indexed=True)
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def list(cls, limit=10, offset=None):
        """
        List all the posts paginated
        :param limit:
        :param offset:
        :return: Post objects
        """
        return Post.gql("ORDER BY created DESC LIMIT 10 OFFSET "+offset)

    @classmethod
    def by_id(cls, post_id):
        """
        Retrieves a post by its key ID
        :param post_id:
        :return: Post object
        """
        return Post.get_by_id(post_id)

    @classmethod
    def by_author(cls, user):
        """
        Retrives all the posts by author
        :param user:
        :return: Post object
        """
        posts = Post.gql("WHERE author = :1 ORDER BY created DESC", user.key())
        return posts
