import webapp2
import os
import jinja2
from handlers.auth import Auth

template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class Handler(webapp2.RequestHandler):
    current_user = {}

    def __init__(self, request, response):
        self.initialize(request, response)
        if Auth.is_logged_in(request):
            if Auth.check_cookie(request.cookies.get("user_id")):
                self.current_user = Auth.get_current_user(request.cookies.get("user_id"))
            else:
                print "INVALID USER"

        # if Auth.check_cookie(request.cookies.get("user_id")):
        #     self.redirect("/login")

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        params['current_user'] = self.current_user
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
