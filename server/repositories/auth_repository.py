class AuthRepository:
    def __init__(self, model, db):
        self.model = model
        self.db = db

    def get_user(self, username, password, app_context):
        with app_context:
            return self.model.query.filter_by(username=username, password=password).first()

    def register(self, user_data, app_context):
        with app_context:
            new_user = self.model(username=user_data.username, password=user_data.username)
            self.db.session.add(new_user)
            self.db.session.commit()
            return new_user
