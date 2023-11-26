class JWTRepository:
    def __init__(self, model, db):
        self.model = model
        self.db = db

    def has_jwt_token(self, jwt_token):
        return self.model.query.filter_by(jwt_token=jwt_token).first()

    def add_jwt_token(self, jwt_token):
        new_token = self.model(jwt_token=jwt_token)
        self.db.session.add(new_token)
        self.db.session.commit()

        return new_token
