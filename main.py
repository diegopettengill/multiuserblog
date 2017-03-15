import webapp2
from handlers.main import IndexHandler
from handlers.post import PostHandler
from handlers.newpost import NewPostHandler
from handlers.signup import SignUpHandler
from handlers.login import LoginHandler


routes = [
    ('/', IndexHandler),
    ('/post/(\d+)', PostHandler),
    ('/newpost', NewPostHandler),
    ('/signup', SignUpHandler),
    ('/login', LoginHandler)
]

app = webapp2.WSGIApplication(routes, debug=True)
