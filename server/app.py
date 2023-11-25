from flask import Flask, jsonify
from flask_cors import CORS
from configparser import ConfigParser

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

from db import db, init_db
from models import NewBlogPost, BlogPost, AdminUser
from services import BlogPostService, AdminUserService
from repositories import BlogPostRepository, AdminUserRepository

app = Flask(__name__)
CORS(app)

# api routes
@app.route('/api')
def api():
    data = {'hello': 'world'}
    return jsonify(data)

config = ConfigParser()
config.read('config.conf')

# Configure Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('Database', 'url', raw=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

# Configure Flask-JWT-Extended
app.config['JWT_SECRET_KEY'] = config.get('JWT', 'secret_key', raw=True)
jwt = JWTManager(app)


# Initialize the repositories and services
repository = BlogPostRepository(model=BlogPost, db=db)
blog_post_service = BlogPostService(repository)
admin_user_repository = AdminUserRepository(model=AdminUser, db=db)
admin_user_service = AdminUserService(repository=admin_user_repository)


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


# Protected route with JWT authentication
@app.route('/api/v1/posts', methods=['POST'])
@jwt_required()
def create_post():
    current_user = get_jwt_identity()

    # Check if the current user is the admin
    if current_user != config.get('JWT', 'admin_username', raw=True):
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    title = data.get('title')
    text = data.get('text')
    post_data = NewBlogPost(title=title, text=text)
    new_post = blog_post_service.create_post(post_data)

    return jsonify(new_post.as_dict()), 201


@app.route('/api/v1/posts/<int:post_id>', methods=['PUT'])
@jwt_required()
def update_post(post_id):
    current_user = get_jwt_identity()

    # Check if the current user is the admin
    if current_user != config.get('JWT', 'admin_username', raw=True):
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    title = data.get('title')
    text = data.get('text')
    updated_post = blog_post_service.update_post(post_id, title, text)
    if updated_post:
        return jsonify(updated_post.as_dict())
    return jsonify({'error': 'Post not found'}), 404


@app.route('/api/v1/posts/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    current_user = get_jwt_identity()

    # Check if the current user is the admin
    if current_user != config.get('JWT', 'admin_username', raw=True):
        return jsonify({'error': 'Unauthorized'}), 401

    deleted = blog_post_service.delete_post(post_id)
    if deleted:
        return jsonify({'message': 'Post deleted successfully'})
    return jsonify({'error': 'Post not found'}), 404


@app.route('/api/v1/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Check if the user is an admin user
    admin_user = admin_user_service.get_user_by_username(username)
    if admin_user and password == admin_user.password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


if __name__ == "__main__":
    app.run(debug=True)
