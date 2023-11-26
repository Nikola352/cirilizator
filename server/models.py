from db import db


class BlogPost(db.Model):
    """
    BlogPost model represents a blog post entity.
    ---
    properties:
      id:
        type: integer
        format: int64
        description: The unique identifier for a blog post.
        readOnly: true
      title:
        type: string
        maxLength: 50
        description: The title of the blog post.
      text:
        type: string
        format: text
        description: The text content of the blog post.
      category:
        type: string
        maxLength: 50
        description: The category of the blog post.
      thumbnail:
        type: string
        maxLength: 255
        description: URL or path to the thumbnail image for the blog post.
    """

    __tablename__ = 'blog_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    thumbnail = db.Column(db.String(255))

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class NewBlogPost:
    """
    NewBlogPost represents the data required to create a new blog post.
    ---
    properties:
      title:
        type: string
        maxLength: 50
        description: The title of the new blog post.
      text:
        type: string
        format: text
        description: The text content of the new blog post.
      category:
        type: string
        maxLength: 50
        description: The category of the new blog post.
      thumbnail:
        type: string
        maxLength: 255
        description: URL or path to the thumbnail image for the new blog post.
    """

    def __init__(self, title, text, category, thumbnail):
        self.title = title
        self.text = text
        self.category = category
        self.thumbnail = thumbnail


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


class DiscordMessage:
    """
    DiscordMessage represents a message from Discord.
    ---
    properties:
      author:
        type: string
        description: The author of the Discord message.
      message:
        type: string
        description: The content of the Discord message.
    """

    def __init__(self, author, message):
        self.author = author
        self.message = message
class Font(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    font_family = db.Column(db.String(255), nullable=False)
    font_subfamily = db.Column(db.String(255), nullable=False)
    font_full_name = db.Column(db.String(255), nullable=False)
    font_postscript_name = db.Column(db.String(255), nullable=False)
    font_weight = db.Column(db.Integer, nullable=False)
    font_width = db.Column(db.Integer, nullable=False)
    font_italic = db.Column(db.Integer, nullable=False)
    font_ascent = db.Column(db.Integer, nullable=False)
    font_descent = db.Column(db.Integer, nullable=False)
    font_line_gap = db.Column(db.Integer, nullable=False)
    font_cap_height = db.Column(db.Integer, nullable=False)
    font_x_height = db.Column(db.Integer, nullable=False)
    font_stem_v = db.Column(db.Integer, nullable=False)
    font_file = db.Column(db.String(255), nullable=False)

    def as_dict(self):
        return {
            'font_family': self.font_family,
            'font_subfamily': self.font_subfamily,
            'font_full_name': self.font_full_name,
            'font_postscript_name': self.font_postscript_name,
        }
