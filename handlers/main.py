from app import Handler
from google.appengine.ext import db


class IndexHandler(Handler):
    def get(self):
        posts = db.GqlQuery("SELECT * from Post order by created desc limit 10")
        print posts
        self.render("index.html", posts=posts)
