from libs import bcrypt
from entities.user import User


class Auth:
    """
    Handles the authentication flow and cookie manipulation
    """

    def __init__(self):
        pass

    @staticmethod
    def signup(username, password, password_verify, email):
        """
        Signs up the user
        :param username:
        :param password:
        :param password_verify:
        :param email:
        :return:
        """

        # username and password are filled
        if username and password:

            if password == password_verify:

                # username exists
                if User.by_username(username):
                    raise Exception(
                        "This username already exists,"
                        " please try a diferent one")
                else:
                    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
                    user = User(username=username, password=hashed_password,
                                email=email)
                    user.put()
                    return str(user.key().id())
            else:
                raise Exception("Both passwords must match.")

        else:
            raise Exception("Username and Password are required to Sign Up.")

    @staticmethod
    def login(username, password):
        """
        Authenticate the user
        :param username:
        :param password:
        :return:
        """
        # username and password are filled
        if username and password:
            # verify if user exists
            user = User.by_username(username)
            # exits
            if user:
                hashed_password = user.password
                # if password matches
                if bcrypt.hashpw(password, hashed_password) == hashed_password:
                    return str(user.key().id())
                else:
                    # generalizes the message to prevent username tumpering
                    raise Exception("Username or password invalid")
            else:
                raise Exception("Username or password invalid.")
        else:
            raise Exception("Username and Password are required to login")

    @staticmethod
    def logout(response):
        response.headers.add_header("Set-Cookie", "user_id=; Path=/")

    @staticmethod
    def is_logged_in(request):
        """
        Checks if user is logged in
        :param request:
        :return: True or False
        """
        if request.cookies.get("user_id"):
            return True
        else:
            return False

    @staticmethod
    def get_current_user(cookie_hash):
        """
        Get the current user based on cookie info
        :param cookie_hash:
        :return:
        """
        if cookie_hash:
            hashed = cookie_hash.split("|")
            return User.by_id(int(hashed[0]))
        else:
            return None

    @classmethod
    def make_secure_cookie(cls, user_id):
        """
        Makes a secure cookie hash based on user id
        :param user_id:
        :return: user_id|securehash
        """
        return "%s|%s" % (user_id, bcrypt.hashpw(user_id, bcrypt.gensalt()))

    @staticmethod
    def check_cookie(cookie_hash):
        """
        Check if cookie hash is valid
        :param cookie_hash:
        :return: True or False
        """
        if cookie_hash:
            hashed = cookie_hash.split("|")[1]
            uid = cookie_hash.split("|")[0]
            # if hashes match
            if bcrypt.hashpw(uid, hashed) == hashed:
                return True
            else:
                return False

    @staticmethod
    def invalidate_cookie(response):
        """
        Invalidades the user cookie
        :param response:
        :return: None
        """
        response.headers.add_header("Set-Cookie", "user_id=; Path=/")

    def restricted(func):
        """
            A decorator to confirm a user is logged in or redirect as needed.
            """

        def login(self, *args, **kwargs):
            print "EITA PORRA ESSA CARAIA FUNCIONADA"
            # Redirect to login if user not logged in, else execute func.
            if not self.current_user:
                self.redirect("/login")
            else:
                func(self, *args, **kwargs)

        return login
