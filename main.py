import webapp2
from handlers.main import IndexHandler
from handlers.welcome import WelcomeHandler
from handlers.post import PostHandler
from handlers.newpost import NewPostHandler
from handlers.editpost import EditPostHandler
from handlers.deletepost import DeletePostHandler
from handlers.signup import SignUpHandler
from handlers.login import LoginHandler
from handlers.logout import LogoutHandler
from handlers.comment import CommentHandler

config = {
    'blog_config': {
        'secret_key': '^.:,+zXsE.7=:<&|f8D&IouU{sP<JiejlU*O?K%8OxgJOV*m=<eb^l/JXY}BZuPM',
    }
}

routes = [
    ('/', IndexHandler),
    ('/welcome', WelcomeHandler),
    ('/post/(\d+)', PostHandler),
    ('/post/new', NewPostHandler),
    ('/post/(\d+)/edit', EditPostHandler),
    ('/post/(\d+)/delete', DeletePostHandler),
    ('/comments', CommentHandler),
    ('/signup', SignUpHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler)
]

app = webapp2.WSGIApplication(routes, debug=True, config=config)
