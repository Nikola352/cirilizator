import os

from flask_cors import CORS
from configparser import ConfigParser

from flask import Flask, jsonify, request, send_file
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flasgger import Swagger, swag_from

import discord_bot
import transliteration_service
from db import db, init_db
from models import BlogPost, AdminUser
from services import BlogPostService, AdminUserService, GPTService
from repositories import BlogPostRepository, AdminUserRepository
import threading

app = Flask(__name__)
CORS(app)
Swagger(app, template_file='swagger_definitions.yaml')  # Reference the definitions file

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


@app.route('/api/v1/posts/all', methods=['GET'])
@swag_from({
    'summary': 'Get all blog posts',
    'responses': {
        200: {
            'description': 'Returns a list of all blog posts',
            'schema': {
                'type': 'array',
                'items': {'$ref': '#/definitions/BlogPost'}
            }
        }
    }
})
def get_all_posts():
    """
    Get all blog posts
    ---
    responses:
      200:
        description: Returns a list of all blog posts
    """
    posts = blog_post_service.get_all_posts()
    return jsonify([post.as_dict() for post in posts])


@app.route('/api/v1/posts', methods=['GET'])
@swag_from({
    'summary': 'Get paginated blog posts',
    'parameters': [
        {
            'name': 'Page',
            'in': 'header',
            'type': 'integer',
            'default': 1,
            'description': 'Page number',
        },
        {
            'name': 'Per-Page',
            'in': 'header',
            'type': 'integer',
            'default': 10,
            'description': 'Number of posts per page',
        }
    ],
    'responses': {
        200: {
            'description': 'Returns a list of paginated blog posts',
            'schema': {
                'type': 'array',
                'items': {'$ref': '#/definitions/BlogPost'}
            }
        }
    }
})
def get_paginated_posts():
    """
    Get paginated blog posts
    ---
    parameters:
      - name: Page
        in: header
        type: integer
        default: 1
        description: Page number
      - name: Per-Page
        in: header
        type: integer
        default: 10
        description: Number of posts per page
    responses:
      200:
        description: Returns a list of paginated blog posts
    """
    # Get pagination parameters from request headers
    page = request.headers.get('Page', default=1, type=int)
    per_page = request.headers.get('Per-Page', default=10, type=int)

    # Call the blog_post_service to get paginated posts
    paginated_posts = blog_post_service.get_paginated_posts(page, per_page)

    # Return the paginated posts as JSON
    return jsonify([post.as_dict() for post in paginated_posts])


@app.route('/api/v1/posts/<int:post_id>', methods=['GET'])
@swag_from({
    'summary': 'Get a blog post by ID',
    'parameters': [
        {
            'name': 'post_id',
            'in': 'path',
            'type': 'integer',
            'description': 'ID of the blog post to retrieve',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': 'Returns the specified blog post',
            'schema': {'$ref': '#/definitions/BlogPost'}
        },
        404: {
            'description': 'Post not found'
        }
    }
})
def get_post_by_id(post_id):
    """
    Get a blog post by ID
    ---
    parameters:
      - name: post_id
        in: path
        type: integer
        description: ID of the blog post to retrieve
        required: true
    responses:
      200:
        description: Returns the specified blog post
      404:
        description: Post not found
    """
    post = blog_post_service.get_post_by_id(post_id)
    if post:
        return jsonify(post.as_dict())
    return jsonify({'error': 'Post not found'}), 404


# Protected route with JWT authentication
@app.route('/api/v1/posts', methods=['POST'])
@jwt_required()
@swag_from({
    'summary': 'Create a new blog post',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'default': 'Bearer <access_token>',
            'description': 'JWT token for authentication',
            'required': True
        }
    ],
    'responses': {
        201: {
            'description': 'Returns the created blog post',
            'schema': {'$ref': '#/definitions/BlogPost'}
        },
        401: {
            'description': 'Unauthorized'
        }
    }
})
def create_post():
    """
    Create a new blog post
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        default: 'Bearer <access_token>'
        description: JWT token for authentication
        required: true
    responses:
      201:
        description: Returns the created blog post
      401:
        description: Unauthorized
    """
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
    new_post = blog_post_service.create_post(title, text, category, thumbnail)

    return jsonify(new_post.as_dict()), 201


@app.route('/api/v1/posts/<int:post_id>', methods=['PUT'])
@jwt_required()
@swag_from({
    'summary': 'Update a blog post',
    'parameters': [
        {
            'name': 'post_id',
            'in': 'path',
            'type': 'integer',
            'description': 'ID of the blog post to update',
            'required': True
        },
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'default': 'Bearer <access_token>',
            'description': 'JWT token for authentication',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': 'Returns the updated blog post',
            'schema': {'$ref': '#/definitions/BlogPost'}
        },
        401: {
            'description': 'Unauthorized'
        },
        404: {
            'description': 'Post not found'
        }
    }
})
def update_post(post_id):
    """
    Update a blog post
    ---
    parameters:
      - name: post_id
        in: path
        type: integer
        description: ID of the blog post to update
        required: true
      - name: Authorization
        in: header
        type: string
        default: 'Bearer <access_token>'
        description: JWT token for authentication
        required: true
    responses:
      200:
        description: Returns the updated blog post
      401:
        description: Unauthorized
      404:
        description: Post not found
    """
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
@swag_from({
    'summary': 'Delete a blog post',
    'parameters': [
        {
            'name': 'post_id',
            'in': 'path',
            'type': 'integer',
            'description': 'ID of the blog post to delete',
            'required': True
        },
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'default': 'Bearer <access_token>',
            'description': 'JWT token for authentication',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': 'Post deleted successfully'
        },
        401: {
            'description': 'Unauthorized'
        },
        404: {
            'description': 'Post not found'
        }
    }
})
def delete_post(post_id):
    """
    Delete a blog post
    ---
    parameters:
      - name: post_id
        in: path
        type: integer
        description: ID of the blog post to delete
        required: true
      - name: Authorization
        in: header
        type: string
        default: 'Bearer <access_token>'
        description: JWT token for authentication
        required: true
    responses:
      200:
        description: Post deleted successfully
      401:
        description: Unauthorized
      404:
        description: Post not found
    """
    current_user = get_jwt_identity()

    # Check if the current user is the admin
    if current_user != config.get('JWT', 'admin_username', raw=True):
        return jsonify({'error': 'Unauthorized'}), 401

    deleted = blog_post_service.delete_post(post_id)
    if deleted:
        return jsonify({'message': 'Post deleted successfully'})
    return jsonify({'error': 'Post not found'}), 404


@app.route('/api/v1/login', methods=['POST'])
@swag_from({
    'summary': 'User login',
    'parameters': [
        {
            'name': 'username',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Username for login',
        },
        {
            'name': 'password',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Password for login',
        },
    ],
    'responses': {
        200: {
            'description': 'Login successful',
            'schema': {'$ref': '#/definitions/AccessToken'}
        },
        401: {
            'description': 'Invalid credentials'
        }
    }
})
def login():
    """
    User login
    ---
    parameters:
      - name: username
        in: formData
        type: string
        required: true
        description: Username for login
      - name: password
        in: formData
        type: string
        required: true
        description: Password for login
    responses:
      200:
        description: Login successful
      401:
        description: Invalid credentials
    """
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Check if the user is an admin user
    admin_user = admin_user_service.get_user_by_username(username)
    if admin_user and password == admin_user.password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


@app.route('/api/v1/register', methods=['POST'])
@jwt_required()
@swag_from({
    'summary': 'Register a new admin user',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'default': 'Bearer <access_token>',
            'description': 'JWT token for authentication',
            'required': True
        },
        {
            'name': 'username',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Username for the new admin user',
        },
        {
            'name': 'password',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Password for the new admin user',
        },
    ],
    'responses': {
        200: {
            'description': 'User registration successful',
            'schema': {'$ref': '#/definitions/AccessToken'}
        },
        401: {
            'description': 'Unauthorized'
        }
    }
})
def register():
    """
    Register a new admin user
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        default: 'Bearer <access_token>'
        description: JWT token for authentication
        required: true
      - name: username
        in: formData
        type: string
        required: true
        description: Username for the new admin user
      - name: password
        in: formData
        type: string
        required: true
        description: Password for the new admin user
    responses:
      200:
        description: User registration successful
      401:
        description: Unauthorized
    """
    current_user = get_jwt_identity()

    # Check if the current user is the admin
    if current_user != config.get('JWT', 'admin_username', raw=True):
        return jsonify({'error': 'Unauthorized'}), 401

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    admin_user_service.register(username, password)
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route('/api/v1/transliterate_text', methods=['POST'])
@swag_from({
    'summary': 'Transliterate text',
    'parameters': [
        {
            'name': 'prompt',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Text to be transliterated',
        }
    ],
    'responses': {
        200: {
            'description': 'Transliteration result',
            'schema': {'$ref': '#/definitions/TransliterationResult'}
        },
        400: {
            'description': 'No prompt provided'
        },
        500: {
            'description': 'Internal Server Error'
        }
    }
})
def transliterate_text():
    """
    Transliterate text
    ---
    parameters:
      - name: prompt
        in: formData
        type: string
        required: true
        description: Text to be transliterated
    responses:
      200:
        description: Transliteration result
      400:
        description: No prompt provided
      500:
        description: Internal Server Error
    """
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
@swag_from({
    'summary': 'Get Discord messages',
    'responses': {
        200: {
            'description': 'Returns Discord messages',
            'schema': {
                'type': 'array',
                'items': {'$ref': '#/definitions/DiscordMessage'}
            }
        }
    }
})
def get_messages():
    """
    Get Discord messages
    ---
    responses:
      200:
        description: Returns Discord messages
    """
    return jsonify(discord_bot.messages)


@app.route('/api/v1/transliterate_pdf', methods=['POST'])
@swag_from({
    'summary': 'Transliterate PDF file',
    'parameters': [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': 'PDF file to be transliterated',
        }
    ],
    'responses': {
        200: {
            'description': 'Transliteration successful',
            'content': {'application/pdf': {}}
        },
        400: {
            'description': 'No file part or No selected file'
        },
        500: {
            'description': 'Internal Server Error'
        }
    }
})
def transliterate_pdf():
    """
    Transliterate PDF file
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: PDF file to be transliterated
    responses:
      200:
        description: Transliteration successful
      400:
        description: No file part or No selected file
      500:
        description: Internal Server Error
    """
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
@swag_from({
    'summary': 'Transliterate TXT file',
    'parameters': [
        {
            'name': 'file',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': 'TXT file to be transliterated',
        }
    ],
    'responses': {
        200: {
            'description': 'Transliteration successful',
            'content': {'text/plain': {}}
        },
        400: {
            'description': 'No file part or No selected file'
        },
        500: {
            'description': 'Internal Server Error'
        }
    }
})
def transliterate_txt_file():
    """
    Transliterate TXT file
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: TXT file to be transliterated
    responses:
      200:
        description: Transliteration successful
      400:
        description: No file part or No selected file
      500:
        description: Internal Server Error
    """
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
