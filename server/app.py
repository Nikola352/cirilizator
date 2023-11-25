from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

from db import db, init_db
from models import NewBlogPost, BlogPost, AdminUser
from services import BlogPostService, AdminUserService
from repositories import BlogPostRepository, AdminUserRepository

app = Flask(__name__)

# Configure Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mysql_user:mysql_password@localhost:3306/cirilizator'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://xn__90afccojrclbbx_xn__90a3ac:HfUilhBmGzvoiY6WJcDAOUlRFP4aKg@185.82.212.80/mysql_g1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

# Configure Flask-JWT-Extended
app.config['JWT_SECRET_KEY'] = 'plKFLoyJjG7WnXeIcxKM5D1nlYVthp8cAlcYx3O8'
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
    if current_user != '1Wqr::XjzJA:7&NV&=bycXD#@&G._a[]N+n@!BzE*).%%E]3/0':
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
    if current_user != '1Wqr::XjzJA:7&NV&=bycXD#@&G._a[]N+n@!BzE*).%%E]3/0':
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
    if current_user != '1Wqr::XjzJA:7&NV&=bycXD#@&G._a[]N+n@!BzE*).%%E]3/0':
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
