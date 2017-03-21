from app import Handler
from entities.comment import Comment
from handlers.auth import Auth
from webapp2_extras import json


class DeleteCommentHandler(Handler):
    def get(self, comment_id):
        if not Auth.is_logged_in(self.request):
            self.response.content_type = 'application/json'
            response_obj = {
                'type': 'error',
                'message': 'You need to be logged in to delete comments!'
            }
            self.response.write(json.encode(response_obj))
        else:
            current_user = self.current_user

            comment = Comment.by_id(int(comment_id))

            if comment is not None:

                # verify if this post matches user logged in
                if comment.author.key().id() == current_user.key().id():

                    comment.delete()

                    self.response.content_type = 'application/json'
                    response_obj = {
                        'type': 'success',
                        'message': 'Comment deleted!'
                    }
                    self.response.write(json.encode(response_obj))

                else:  # redirect the user to the view
                    self.response.content_type = 'application/json'
                    response_obj = {
                        'type': 'error',
                        'message': 'You are not allowed to do that!'
                    }
                    self.response.write(json.encode(response_obj))

            else:
                self.response.content_type = 'application/json'
                response_obj = {
                    'type': 'error',
                    'message': 'Comment not found!'
                }
                self.response.write(json.encode(response_obj))
