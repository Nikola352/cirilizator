import os

from flask_cors import CORS
from configparser import ConfigParser

from flask import Flask, jsonify, request, send_file
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

import discord_bot
import transliteration_service
from db import db, init_db
from models import NewBlogPost, BlogPost, AdminUser
from services import BlogPostService, AdminUserService, GPTService
from repositories import BlogPostRepository, AdminUserRepository
import threading

app = Flask(__name__)
CORS(app)

config = ConfigParser()
config.read('config.conf')

# Configure Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('Database', 'url', raw=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure Flask-JWT-Extended
app.config['JWT_SECRET_KEY'] = config.get('JWT', 'secret_key', raw=True)
jwt = JWTManager(app)

GPT_API_KEY = config.get('GPT', 'api_key')
GPT_API_URL = 'https://api.openai.com/v1/engines/gpt-3.5-turbo/completions'

init_db(app)

# Start the bot in a separate thread
discord_thread = threading.Thread(target=discord_bot.run_discord_bot)
discord_thread.start()


# Initialize the repositories and services
repository = BlogPostRepository(model=BlogPost, db=db)
blog_post_service = BlogPostService(repository)
admin_user_repository = AdminUserRepository(model=AdminUser, db=db)
admin_user_service = AdminUserService(repository=admin_user_repository)
gpt_service = GPTService(GPT_API_KEY, GPT_API_URL)

@app.route('/api/v1/posts', methods=['GET'])
def get_all_posts():
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
    print(data)
    title = data.get('title')
    text = data.get('text')
    category = data.get('category')
    thumbnail = data.get('thumbnail')
    post_data = NewBlogPost(title=title, text=text, category=category, thumbnail=thumbnail)
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


@app.route('/api/v1/transliterate_text', methods=['POST'])
def process_text():
    try:
        data = request.json
        prompt = data.get('prompt', '')

        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        prompt = 'Transliterate the following text from Serbian latin to Serbian cyrillic: ' + prompt
        response = gpt_service.call_gpt_api(prompt)
        return jsonify({'result': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/v1/discord_messages', methods=['GET'])
def get_messages():
    return jsonify(discord_bot.messages)


@app.route('/api/v1/transliterate_pdf', methods=['POST'])
def transliterate_pdf():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file and file.filename.endswith(".pdf"):
        edited_file_path = transliteration_service.transliterate_pdf(file)

        if edited_file_path is None:
            return "Error: file path is None"

        response = send_file(edited_file_path, as_attachment=True, download_name="edited_file.pdf", mimetype="application/pdf")

        # Delete files after sending
        os.remove("uploads" + os.sep + file.filename)
        os.remove(edited_file_path)

        return response
    return "Invalid file format. Please upload a .pdf file."


@app.route('/api/v1/transliterate_txt', methods=['POST'])
def transliterate_txt():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file and file.filename.endswith('.txt'):
        edited_file_path = transliteration_service.transliterate_txt(file)

        response = send_file(edited_file_path, as_attachment=True, download_name="edited_file.txt", mimetype="text/plain")

        # Delete files after sending
        os.remove(edited_file_path)

        return response

    return "Invalid file format. Please upload a .txt file."


if __name__ == "__main__":
    app.run(debug=True)
