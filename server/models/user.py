from database.db import db


class AdminUser(db.Model):
    """
    AdminUser model represents an admin user entity.
    ---
    properties:
      id:
        type: integer
        format: int64
        description: The unique identifier for an admin user.
      username:
        type: string
        maxLength: 50
        description: The username of the admin user (unique).
      password:
        type: string
        maxLength: 50
        description: The password of the admin user.
    """

    __tablename__ = 'admin_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


class NewUser():
    """
    NewBlogPost represents the data required to create a new user.
    ---
    properties:
      username:
        type: string
        maxLength: 50
        description: The username of the admin user (unique).
      password:
        type: string
        maxLength: 50
        description: The password of the admin user.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password