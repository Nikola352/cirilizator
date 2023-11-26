from database.db import db


class JWTToken(db.Model):
    """
    JWTToken represents a generated JWT token.
    ---
    properties:
      jwt_token:
        type: string
        format: text
        description: The jwt token.
    """

    __tablename__ = 'jwt_tokens'

    id = db.Column(db.Integer, primary_key=True)
    jwt_token = db.Column(db.Text(collation='utf8mb4_general_ci'), nullable=False)

    def as_dict(self):
        return {'jwt_token': self.jwt_token}
