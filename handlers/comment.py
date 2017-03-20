from app import Handler
from entities.post import Post
from entities.comment import Comment
from handlers.auth import Auth
from webapp2_extras import json


class CommentHandler(Handler):
    def post(self):

        if not Auth.is_logged_in(self.request):
            self.response.content_type = 'application/json'
            response_obj = {
                'type': 'error',
                'message': 'You must be logged in to comment on posts!'
            }
            self.response.write(json.encode(response_obj))
        else:
            current_user = Auth.get_current_user(self.request.cookies.get("user_id"))
            post = Post.by_id(int(self.request.get("pid")))
            text = self.request.get("text")

            if text:
                comment = Comment(author=current_user, post=post, text=text)
                comment.put()
                self.response.content_type = 'application/json'
                response_obj = {
                    'type': 'success',
                    'message': 'Comment created!',
                    'comment': {
                        "id": comment.key().id(),
                        "author": current_user.username,
                        "text": text,
                        "time": comment.created.strftime("%d. %B %Y")
                    }
                }
                self.response.write(json.encode(response_obj))
            else:
                self.response.content_type = 'application/json'
                response_obj = {
                    'type': 'error',
                    'message': 'Comment not created!'
                }
                self.response.write(json.encode(response_obj))
