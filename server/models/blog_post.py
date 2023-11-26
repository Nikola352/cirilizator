from database.db import db


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
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    thumbnail = db.Column(db.Text)

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
