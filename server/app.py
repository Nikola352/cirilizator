from flask import Flask, jsonify, request

from db import db, init_db
from models import NewBlogPost, BlogPost
from services import BlogPostService
from repositories import BlogPostRepository

app = Flask(__name__)

# Configure Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mysql_user:mysql_password@localhost:3306/cirilizator'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://xn__90afccojrclbbx_xn__90a3ac:HfUilhBmGzvoiY6WJcDAOUlRFP4aKg@185.82.212.80/mysql_g1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)


# Initialize the repository and service
repository = BlogPostRepository(model=BlogPost, db=db)
blog_post_service = BlogPostService(repository)


# BlogPost CRUD routes
@app.route('/api/v1/posts', methods=['GET'])
def get_all_posts():
    print('called')
    posts = blog_post_service.get_all_posts()
    return jsonify([post.as_dict() for post in posts])


@app.route('/api/v1/posts/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id):
    post = blog_post_service.get_post_by_id(post_id)
    if post:
        return jsonify(post.as_dict())
    return jsonify({'error': 'Post not found'}), 404


@app.route('/api/v1/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    title = data.get('title')
    text = data.get('text')
    post_data = NewBlogPost(title=title, text=text)
    new_post = blog_post_service.create_post(post_data)
    return jsonify(new_post.as_dict()), 201


@app.route('/api/v1/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    title = data.get('title')
    text = data.get('text')
    updated_post = blog_post_service.update_post(post_id, title, text)
    if updated_post:
        return jsonify(updated_post.as_dict())
    return jsonify({'error': 'Post not found'}), 404


@app.route('/api/v1/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    deleted = blog_post_service.delete_post(post_id)
    if deleted:
        return jsonify({'message': 'Post deleted successfully'})
    return jsonify({'error': 'Post not found'}), 404


if __name__ == "__main__":
    app.run(debug=True)
