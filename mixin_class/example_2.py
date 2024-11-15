class AuthenticationMixin:
    def login(self, username, password):
        if username == self.username and password == self.password:
            self.is_authenticated = True
            print(f"{self.username} is successfully logged in.")
        else:
            self.is_authenticated = False
            print("Login Failed. Incorrect username or password.")


class PermissionMixin:
    def has_permission(self, action):
        if self.is_authenticated:
            if self.is_admin:
                print(f"{self.username} has permission to {action}")
            else:
                print(f"{self.username} does not have permission to {action}.")
        else:
            print("You are not a authenticated user.")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_authenticated = False
        self.is_admin = False


class AdminUser(AuthenticationMixin, PermissionMixin, User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.is_admin = True

class GuestUser(AuthenticationMixin, PermissionMixin, User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.is_admin = False

admin = AdminUser("admin", "1234")
admin.login("admin", "1234")
admin.has_permission("delete record")

guest = GuestUser("guest", "5678")
guest.login("guest", "3456")
guest.has_permission("pull from git.")
