from handlers.app import Handler


class NotFoundHandler(Handler):
    def get(self):
        self.render("404.html")
