from models.user import NewUser


class AuthService:
    def __init__(self, repository):
        self.repository = repository

    def get_user(self, username, password, app_context):
        return self.repository.get_user(username, password, app_context)

    def register(self, username, password, app_context):
        user_data = NewUser(username=username, password=password)
        self.repository.register(user_data, app_context)

    def insert_default_admin(self, app_context):
        if not self.get_user("admin", "admin", app_context):
            self.register("admin", "admin", app_context)

