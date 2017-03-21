from app import Handler
from entities.post import Post
from entities.comment import Comment
from handlers.auth import Auth
from webapp2_extras import json


class CommentHandler(Handler):
    def get(self, comment_id):

        if not Auth.is_logged_in(self.request): # checks if user is logged in
            self.response.content_type = 'application/json'
            response_obj = {
                'type': 'error',
                'message': 'You must be logged in to do that!'
            }
            self.response.write(json.encode(response_obj))

        else:

            comment = Comment.by_id(int(comment_id))

            # check if comment belongs to current user
            if comment.author.key().id() == self.current_user.key().id():
                self.response.content_type = 'application/json'
                response_obj = {
                    'type': 'success',
                    'comment': {
                        "id": comment.key().id(),
                        "text": comment.text,
                    }
                }
                self.response.write(json.encode(response_obj))
            else:
                self.response.content_type = 'application/json'
                response_obj = {
                    'type': 'error',
                    'message': "You can only edit your own comments. ;D"
                }
                self.response.write(json.encode(response_obj))

    def post(self):

        if not Auth.is_logged_in(self.request):
            self.response.content_type = 'application/json'
            response_obj = {
                'type': 'error',
                'message': 'You must be logged in to comment on posts!'
            }
            self.response.write(json.encode(response_obj))
        else:
            current_user = self.current_user
            post = Post.by_id(int(self.request.get("pid")))
            text = self.request.get("text")
            comment_id = self.request.get("comment_id")

            if text:

                is_edit = False

                # if is a edit to comment
                if comment_id:
                    comment = Comment.by_id(int(comment_id))
                    comment.text = text
                    is_edit = True
                else:
                    comment = Comment(author=current_user, post=post, text=text)

                comment.put()

                self.response.content_type = 'application/json'
                response_obj = {
                    'type': 'success',
                    'message': 'Comment created!',
                    'editing': is_edit,
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
