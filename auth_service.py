from user import User
from user import Admin
from user import Customer

class AuthenticationService:
    def __init__(self):
        self.current_user = None

    def register(self, user_class, username, email, password, *args):
        if any(user.username == username for user in User.users):
            return "Username already exists."
        new_user = user_class(username, email, password, *args)
        User.users.append(new_user)
        return f"User {username} registered successfully."

    def login(self, username, password):
        for user in User.users:
            if user.username == username and user.check_password(password):
                self.current_user = user
                return f"User {username} logged in successfully."
        return "Invalid username or password."

    def logout(self):
        if self.current_user:
            self.current_user = None
            return "User logged out successfully."
        return "No user is currently logged in."

    def get_current_user(self):
        if self.current_user:
            return self.current_user.get_details()
        return "No user is currently logged in."