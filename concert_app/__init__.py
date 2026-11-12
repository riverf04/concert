from flask import Flask
from concert_app.extensions import db, migrate
from concert_app.api import api_bp
from concert_app.config import config_by_name

def create_app(config_name="development"):
    app = Flask(__name__)
    
    # Load configuration object from config_by_name mapping
    config_class = config_by_name.get(config_name, config_by_name["default"])
    app.config.from_object(config_class)
    
    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register the blueprint
    app.register_blueprint(api_bp)
    
    return app