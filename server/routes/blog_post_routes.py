from flasgger import swag_from
from flask import jsonify, request, Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required


def create_blog_post_blueprint(blog_post_service, config):
    blog_post_bp = Blueprint('blog_post', __name__)
    
    @blog_post_bp.route('/api/v1/posts/all', methods=['GET'])
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

    @blog_post_bp.route('/api/v1/posts', methods=['GET'])
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

    @blog_post_bp.route('/api/v1/posts/<int:post_id>', methods=['GET'])
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

    @blog_post_bp.route('/api/v1/posts', methods=['POST'])
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

    @blog_post_bp.route('/api/v1/posts/<int:post_id>', methods=['PUT'])
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

    @blog_post_bp.route('/api/v1/posts/<int:post_id>', methods=['DELETE'])
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

    return blog_post_bp
