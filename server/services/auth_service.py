from models.user import NewUser


class AuthService:
    def __init__(self, repository):
        self.repository = repository

    def get_user_by_username(self, username, password):
        return self.repository.get_user_by_username(username, password)

    def register(self, username, password):
        user_data = NewUser(username=username, password=password)
        self.repository.register(user_data)
