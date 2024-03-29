from flask_cors import CORS
from configparser import ConfigParser

from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from database.db import db, init_db
import threading
import os

from models.blog_post import BlogPost
from models.font import Font
from models.font_match import FontMatch
from models.jwt_token import JWTToken
from models.user import AdminUser
from repositories.auth_repository import AuthRepository
from repositories.blog_post_repository import BlogPostRepository
from repositories.font_repository import FontRepository
from repositories.jwt_repository import JWTRepository
from routes.auth_routes import create_auth_blueprint
from routes.blog_post_routes import create_blog_post_blueprint
from routes.discord_routes import create_discord_blueprint
from routes.fonts_routes import create_font_blueprint
from routes.transliteration_routes import create_transliteration_blueprint
from repositories.font_match_repository import FontMatchRepository
from services import discord_bot_service
from services import transliteration_service
from services.auth_service import AuthService
from services.blog_post_service import BlogPostService
from services.font_service import FontService
from services.gpt_service import GPTService
from services.jwt_service import JWTService


def create_app():
    app = Flask(__name__)
    CORS(app)
    Swagger(app, template_file='swagger_definitions.yaml')

    config = ConfigParser()
    config.read('config.conf')

    # Configure Flask-SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = config.get('Database', 'url', raw=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Configure the pool_pre_ping option
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_pre_ping': True
    }

    # Configure Flask-JWT-Extended
    app.config['JWT_SECRET_KEY'] = config.get('JWT', 'secret_key', raw=True)
    JWTManager(app)

    GPT_API_KEY = config.get('GPT', 'api_key')
    GPT_API_URL = 'https://api.openai.com/v1/engines/gpt-3.5-turbo/completions'

    GOOGLE_FONTS_API_KEY = config.get('GoogleFonts', 'api_key', raw=True)

    ADMIN_USERNAME = config.get('Database', 'admin_username')
    ADMIN_PASSWORD = config.get('Database', 'admin_password')

    init_db(app)

    # Start the bot in a separate thread
    discord_thread = threading.Thread(target=discord_bot_service.run_discord_bot)
    discord_thread.start()

    # Initialize the repositories and services
    auth_repository = AuthRepository(AdminUser, db)
    auth_service = AuthService(auth_repository)
    blog_post_repository = BlogPostRepository(BlogPost, db)
    blog_post_service = BlogPostService(blog_post_repository)
    font_repository = FontRepository(Font, db)
    font_match_repository = FontMatchRepository(FontMatch, db)
    font_service = FontService(font_repository, font_match_repository, db, GOOGLE_FONTS_API_KEY)
    gpt_service = GPTService(GPT_API_KEY, GPT_API_URL)
    jwt_repository = JWTRepository(JWTToken, db)
    jwt_service = JWTService(jwt_repository)

    # Register the route blueprints
    app.register_blueprint(create_auth_blueprint(auth_service, jwt_service))
    app.register_blueprint(create_blog_post_blueprint(blog_post_service, jwt_service))
    app.register_blueprint(create_discord_blueprint(discord_bot_service))
    app.register_blueprint(create_font_blueprint(font_service, jwt_service))
    app.register_blueprint(create_transliteration_blueprint(transliteration_service, gpt_service))

    font_service.start_collector(app.app_context())
    auth_service.insert_default_admin(app.app_context(), ADMIN_USERNAME, ADMIN_PASSWORD)

    fonts_folder_path = os.path.join(os.getcwd(), 'resources', 'fonts')
    if not os.path.exists(fonts_folder_path):
        os.makedirs(fonts_folder_path)

    uploads_path = os.path.join(os.getcwd(), 'uploads')
    if not os.path.exists(uploads_path):
        os.makedirs(uploads_path)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
