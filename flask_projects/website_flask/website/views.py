#!/usr/bin/python3

# Import necessary modules
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note  # Import the Note model
from . import db  # Import the database object
import json

# Create a Blueprint object for views
views = Blueprint('views', __name__)

# Route for the home page
@views.route('/', methods=['GET', 'POST'])
@login_required  # Require login to access this route
def home():
    if request.method == 'POST':  # If the request method is POST (i.e., submitting a form)
        note = request.form.get('note')  # Get the note from the HTML form

        if len(note) < 1:
            flash('Note is too short!', category='error')  # Display an error message if the note is too short
        else:
            # Create a new Note object and add it to the database
            new_note = Note(data=note, user_id=current_user.id)  # Create a new note object with current user's ID
            db.session.add(new_note)  # Add the new note to the database session
            db.session.commit()  # Commit the changes to the database
            flash('Note added!', category='success')  # Display a success message

    # Render the home template with the current user
    return render_template("home.html", user=current_user)

# Route for deleting a note
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)  # Load the JSON data sent from the frontend
    noteId = note['noteId']  # Extract the note ID from the JSON data
    note = Note.query.get(noteId)  # Query the database for the note with the given ID
    if note:
        if note.user_id == current_user.id:  # Check if the note belongs to the current user
            db.session.delete(note)  # Delete the note from the database
            db.session.commit()  # Commit the changes to the database

    return jsonify({})  # Return an empty JSON response
