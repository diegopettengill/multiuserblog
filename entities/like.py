import pdb
from google.appengine.ext import db
from entities.user import User
from entities.post import Post


class Like(db.Model):
    author = db.ReferenceProperty(User, collection_name="author_like")
    post = db.ReferenceProperty(Post, collection_name="post_like")
    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def by_post(cls, post):
        """
        Retrieves all the likes for a designated post key
        :param post:
        :return: Like objects
        """
        likes = Like.gql("WHERE post = :1", post.key())
        return likes

    @classmethod
    def check_user_liked(cls, user, post):
        """
        Checks if user liked the passed post
        :param user:
        :param post:
        :return: Number of likes to that post and user
        """
        likes = Like.gql("WHERE author = :1 AND post = :2", user.key(),
                         post.key())
        return likes.count()

    @classmethod
    def unlike(cls, user, post):
        """
        Delete the matching like from the post
        :param user:
        :param post:
        :return: None
        """
        like = Like.gql("WHERE author = :1 AND post = :2", user.key(),
                        post.key()).get()
        like.delete()
