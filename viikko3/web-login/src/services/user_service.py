from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if len(username) < 3:
            raise Exception("Username must be at least 3 characters long")

        if not username.islower() or not username.isalpha():
            raise Exception("Username must consist of letters a-z")

        if len(password) < 8:
            raise Exception("Password must be at least 8 characters long")

        if password.isalpha():
            raise Exception("Password must contain at least one non-letter character")

        if password != password_confirmation:
            raise Exception("Passwords do not match")

        if self._user_repository.find_by_username(username):
            raise Exception("Username is already taken")


user_service = UserService()
