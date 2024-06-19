#!/usr/bin/python3

# Import necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize SQLAlchemy object
db = SQLAlchemy()

# Define the name of the database
DB_NAME = "database.db"

# Function to create the Flask application
def create_app():
    # Create Flask application
    app = Flask(__name__)

    # Set up application configurations
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'  # Secret key for session management
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # Database URI
    db.init_app(app)  # Initialize SQLAlchemy with the Flask app

    # Import views and authentication blueprints
    from .views import views
    from .auth import auth

    # Register blueprints with the Flask application
    app.register_blueprint(views, url_prefix='/')  # Views blueprint
    app.register_blueprint(auth, url_prefix='/')   # Authentication blueprint

    # Import User and Note models
    from .models import User, Note

    # Create database tables within the application context
    with app.app_context():
        db.create_all()

    # Initialize LoginManager for handling user authentication
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # Set the login view
    login_manager.init_app(app)

    # Define a function to load a user given their ID
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Return the Flask application
    return app

# Function to create the database if it doesn't exist
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)  # Create all tables
        print('Created Database!')  # Print a message indicating successful creation
