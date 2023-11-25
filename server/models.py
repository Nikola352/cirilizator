from db import db


class BlogPost(db.Model):
    __tablename__ = 'blog_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class NewBlogPost:
    def __init__(self, title, text, category):
        self.title = title
        self.text = text
        self.category = category


class AdminUser(db.Model):
    __tablename__ = 'admin_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
