from flasgger import swag_from
from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token, jwt_required


def create_auth_blueprint(auth_service, jwt_service):
    auth_bp = Blueprint('auth', __name__)

    @auth_bp.route('/api/v1/login', methods=['POST'])
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
        admin_user = auth_service.get_user_by_username(username, password)
        if admin_user:
            access_token = create_access_token(identity=username)
            jwt_service.add_jwt_token(access_token)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401

    @auth_bp.route('/api/v1/register', methods=['POST'])
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
        jwt_token = request.headers.get('Authorization').split('Bearer ')[1]
        if not jwt_service.has_jwt_token(jwt_token):
            return jsonify({'error': 'Unauthorized'}), 401

        username = request.json.get('username', None)
        password = request.json.get('password', None)
        auth_service.register(username, password)
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return auth_bp
