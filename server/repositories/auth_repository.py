import bcrypt

class AuthRepository:
    def __init__(self, model, db):
        self.model = model
        self.db = db

    def get_user(self, username, password, app_context):
        with app_context:
            user = self.model.query.filter_by(username=username).first()
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash):
                return user
            return None

    def register(self, user_data, app_context):
        with app_context:
            hashed_password = bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt())
            new_user = self.model(username=user_data.username, password=hashed_password)
            self.db.session.add(new_user)
            self.db.session.commit()
            return new_user
