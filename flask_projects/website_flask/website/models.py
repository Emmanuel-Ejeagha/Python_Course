#!/usr/bin/python3

# Import necessary modules
from website import db  # Import the database object from the website package
from flask_login import UserMixin  # Import UserMixin for user management
from sqlalchemy.sql import func  # Import func for database functions

# Define the Note model for storing user notes
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each note
    data = db.Column(db.String(10000))  # Actual content of the note, limited to 10000 characters
    date = db.Column(db.DateTime(timezone=True), default=func.now())  # Date and time of note creation
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # Foreign key linking to the User model

# Define the User model for storing user information
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    email = db.Column(db.String(150), unique=True)  # Email address of the user, must be unique
    password = db.Column(db.String(150))  # Hashed password of the user
    first_name = db.Column(db.String(150))  # First name of the user
    notes = db.relationship('Note')  # Relationship between users and their notes
