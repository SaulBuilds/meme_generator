from flask import Flask
from .database import db, init_db  # Import db directly from database.py
from .routes import generate_bp, upload_bp, fine_tune_bp
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.DevelopmentConfig")

    # Load instance config if available (for secrets, API keys)
    instance_config_path = os.path.join(app.instance_path, 'config.py')
    if os.path.exists(instance_config_path):
        app.config.from_pyfile('config.py')

    # Initialize the database with the app
    init_db(app)

    # Register blueprints
    app.register_blueprint(generate_bp)
    app.register_blueprint(upload_bp)
    app.register_blueprint(fine_tune_bp)

    return app
