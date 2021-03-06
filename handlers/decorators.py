def restricted(func):
    """
        A decorator to confirm a user is logged in or redirect as needed.
        """

    def login(self, *args, **kwargs):
        # Redirect to login if user not logged in, else execute func.
        if not self.current_user:
            self.redirect("/login")
        else:
            func(self, *args, **kwargs)

    return login
