import webapp2

from handlers.comment import CommentHandler
from handlers.deletecomment import DeleteCommentHandler
from handlers.deletepost import DeletePostHandler
from handlers.editpost import EditPostHandler
from handlers.like import LikeHandler
from handlers.login import LoginHandler
from handlers.logout import LogoutHandler
from handlers.main import IndexHandler
from handlers.newpost import NewPostHandler
from handlers.notfound import NotFoundHandler
from handlers.post import PostHandler
from handlers.profile import ProfileHandler
from handlers.signup import SignUpHandler
from handlers.welcome import WelcomeHandler

config = {
    'blog_config': {
        'secret_key': '^.:,+zXsE.7=:<&|f8D&IouU{sP<JiejlU*O?K%8Ox'
                      'gJOV*m=<eb^l/JXY}BZuPM',
    }
}

# defining the routes
routes = [
    ('/', IndexHandler),
    ('/welcome', WelcomeHandler),
    ('/account/profile', ProfileHandler),
    ('/post/([0-9]+)', PostHandler),
    ('/post/new', NewPostHandler),
    ('/post/([0-9]+)/edit', EditPostHandler),
    ('/post/([0-9]+)/delete', DeletePostHandler),
    ('/post/like', LikeHandler),
    ('/comments', CommentHandler),
    ('/comments/([0-9]+)', CommentHandler),
    ('/comments/([0-9]+)/delete', DeleteCommentHandler),
    ('/signup', SignUpHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/not-found', NotFoundHandler)
]

app = webapp2.WSGIApplication(routes, debug=True, config=config)
