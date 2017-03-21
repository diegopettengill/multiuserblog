from app import Handler
from entities.like import Like
from entities.post import Post
from handlers.auth import Auth
from webapp2_extras import json


class LikeHandler(Handler):
    def post(self):

        if not Auth.is_logged_in(self.request):
            self.response.content_type = 'application/json'
            response_obj = {
                'type': 'error',
                'message': 'You must be logged in to like posts!'
            }
            self.response.write(json.encode(response_obj))
        else:

            current_user = self.current_user
            post = Post.by_id(int(self.request.get("pid")))

            # checks if user already liked this post, if returns > 0
            user_liked = Like.check_user_liked(current_user, post)

            # checks if this post belongs to the current_user
            if post.author.key().id == current_user.key().id:
                self.response.content_type = 'application/json'
                response_obj = {
                    'type': 'error',
                    'message': 'You can`t like you own posts :('
                }
                self.response.write(json.encode(response_obj))
            else:
                if user_liked > 0:
                    Like.unlike(current_user, post)
                    self.response.content_type = 'application/json'
                    response_obj = {
                        'type': 'success',
                        'message': 'Post unliked!',
                        'action': 'unlike'
                    }
                    self.response.write(json.encode(response_obj))
                else:
                    like = Like(author=current_user, post=post)
                    like.put()

                    self.response.content_type = 'application/json'
                    response_obj = {
                        'type': 'success',
                        'message': 'Post liked!',
                        'action': 'like'
                    }
                    self.response.write(json.encode(response_obj))
