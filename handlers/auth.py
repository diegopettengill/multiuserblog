from libs import bcrypt
from entities.user import User


class Auth:
    """Handles the authentication flow"""

    @staticmethod
    def signup(username, password, password_verify, email):
        """Signs up the user running all the validations"""
        # username and password are filled
        if username and password:

            if password == password_verify:

                # username exists
                if User.by_username(username):
                    raise Exception("This username already exists, please try a diferent one")
                else:
                    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
                    user = User(username=username, password=hashed_password, email=email)
                    user.put()
                    return str(user.key().id())
            else:
                raise Exception("Both passwords must match.")

        else:
            raise Exception("Username and Password are required to Sign Up.")

    @staticmethod
    def login(username, password):
        """login the user"""
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
        """Returns if user is authenticated or not also checks cookie validation"""
        if request.cookies.get("user_id"):
            return True
        else:
            return False

    @staticmethod
    def get_current_user(cookie_hash):
        if cookie_hash:
            hashed = cookie_hash.split("|")
            return User.by_id(int(hashed[0]))
        else:
            return None

    @classmethod
    def make_secure_cookie(cls, user_id):
        return "%s|%s" % (user_id, bcrypt.hashpw(user_id, bcrypt.gensalt()))

    @staticmethod
    def check_cookie(cookie_hash):
        if cookie_hash:
            hashed = cookie_hash.split("|")[1]
            uid = cookie_hash.split("|")[0]
            # if hashes match
            if bcrypt.hashpw(uid, hashed) == hashed:
                return True
            else:
                return False
