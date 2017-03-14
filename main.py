import webapp2
import handlers.app
from handlers.main import IndexHandler
from handlers.post import PostHandler
from handlers.newpost import NewPostHandler

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/post/(\d+)', PostHandler),
    ('/newpost', NewPostHandler)
], debug=True)
