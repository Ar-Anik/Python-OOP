from hashlib import sha256

class AuthenticationMixin:
    def __init__(self):
        self.user_database = {
            'admin': sha256("1234".encode()).hexdigest(),
            'anik': sha256("abcd".encode()).hexdigest()
        }
        self.is_authenticated = False
        self.current_user = None

    def login(self, username, password):
        hashed_password = sha256(password.encode()).hexdigest()

        if username in self.user_database and self.user_database[username] == hashed_password:
            self.is_authenticated = True
            self.current_user = username
            print(f"{username} is successfully logged in.")
        else:
            print("Login failed. Incorrect username or password.")

    def logout(self):
        if self.is_authenticated:
            print(f"{self.current_user} has been logged out.")
        else:
            print("No user is currently logged in.")
        self.is_authenticated = False
        self.current_user = None


class AuthorizationMixin:
    def authorize(self, user, required_role):
        if not user:
            raise ValueError("User must be authenticated to perform this action.")

        user_roles = {
            'admin': ['view', 'edit', 'delete'],
            'user': ['view']
        }

        if required_role in user_roles.get(user, []):
            print(f"User {user} is authorized for `{required_role}` action.")
            return True
        else:
            print(f"User {user} is not authorized for `{required_role}` action.")
            return False


class AuthHandler:
    def __init__(self):
        self.authenticator = AuthenticationMixin()
        self.authorizer = AuthorizationMixin()

    def login_user(self, username, password):
        self.authenticator.login(username, password)
        if self.authenticator.is_authenticated:
            print("Welcome to the system")
        else:
            print("Acces Denied.")

    def logout_user(self):
        self.authenticator.logout()

    def perform_action(self, required_role):
        if not self.authenticator.is_authenticated:
            print("Action Denied. Please Log in First.")
            return

        user = self.authenticator.current_user
        if self.authorizer.authorize(user, required_role):
            print(f"Action `{required_role}` performed successfully.")
        else:
            print(f"Action `{required_role}` Dedined.")

auth_handler = AuthHandler()

auth_handler.login_user("admin", "1234")
auth_handler.perform_action("edit")
auth_handler.logout_user()

auth_handler.login_user("admin", "asdf")

auth_handler.login_user("anik", "abcd")
auth_handler.perform_action("delete")
auth_handler.logout_user()

auth_handler.login_user("sourov", "abcd")
