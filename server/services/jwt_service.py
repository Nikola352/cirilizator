class JWTService:
    def __init__(self, repository):
        self.repository = repository

    def has_jwt_token(self, jwt_token):
        return self.repository.has_jwt_token(jwt_token)

    def add_jwt_token(self, jwt_token):
        return self.repository.add_jwt_token(jwt_token)
