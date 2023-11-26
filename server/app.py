from flask_cors import CORS
from configparser import ConfigParser

from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from database.db import db, init_db
import threading

from models.blog_post import BlogPost
from models.font import Font
from models.user import AdminUser
from repositories.auth_repository import AuthRepository
from repositories.blog_post_repository import BlogPostRepository
from repositories.font_repository import FontRepository
from routes.auth_routes import create_auth_blueprint
from routes.blog_post_routes import create_blog_post_blueprint
from routes.discord_routes import create_discord_blueprint
from routes.fonts_routes import create_font_blueprint
from routes.transliteration_routes import create_transliteration_blueprint
from services import discord_bot_service
from services import transliteration_service
from services.auth_service import AuthService
from services.blog_post_service import BlogPostService
from services.font_service import FontService
from services.gpt_service import GPTService

app = Flask(__name__)
CORS(app)
Swagger(app, template_file='swagger_definitions.yaml')

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

GOOGLE_FONTS_API_KEY = config.get('GoogleFonts', 'api_key', raw=True)

init_db(app)

# Start the bot in a separate thread
discord_thread = threading.Thread(target=discord_bot_service.run_discord_bot)
discord_thread.start()

# Initialize the repositories and services
auth_repository = AuthRepository(model=AdminUser, db=db)
auth_service = AuthService(repository=auth_repository)
blog_post_repository = BlogPostRepository(model=BlogPost, db=db)
blog_post_service = BlogPostService(blog_post_repository)
font_repository = FontRepository(model=Font, db=db)
font_service = FontService(font_repository, db, GOOGLE_FONTS_API_KEY)
gpt_service = GPTService(GPT_API_KEY, GPT_API_URL)

# Register the route blueprints
app.register_blueprint(create_auth_blueprint(auth_service))
app.register_blueprint(create_blog_post_blueprint(blog_post_service, config))
app.register_blueprint(create_discord_blueprint(discord_bot_service))
app.register_blueprint(create_font_blueprint(font_service))
app.register_blueprint(create_transliteration_blueprint(transliteration_service, gpt_service))

if __name__ == "__main__":
    app.run(debug=True)
