# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '9ol8nuw2hef89ny29h1f2oinuodw'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cardashboard.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Register blueprints
    from app.auth.routes import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # Import and register other blueprints here if needed

    return app

# Import db after create_app is defined
from app import db
