#!/usr/bin/python3

# Import necessary modules
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # Import the db object from the current package
from flask_login import login_user, login_required, logout_user, current_user
import secrets

# Create a Blueprint object for authentication routes
auth = Blueprint('auth', __name__)

# Route for user login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the user exists
        user = User.query.filter_by(email=email).first()
        if user:
            # Check if the entered password matches the stored hash
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)  # Log the user in
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

# Route for user logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()  # Log the user out
    return redirect(url_for('auth.login'))

# Route for user sign up
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Check if the email is already in use
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Create a new user and add to the database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)  # Log the user in
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

# Route for handling forgotten passwords
@auth.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            # Generate a unique token
            token = secrets.token_urlsafe(16)
            user.rest_token = token
            db.session.commit()
            # Send email with password reset link
            flash('An email has been sent with instructions to reset your password.', 'info')
        else:
            flash("Email address not found.", 'error')
            return redirect(url_for('auth.forgot_password'))
    return render_template('forgot_password.html')

# Route for resetting passwords
@auth.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.query.filter_by(reset_token=token).first()
    if not user:
        flash('Invalid or expired token.', 'error')
        return redirect(url_for(auth.login))
    
    if request.method == 'POST':
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
        else:
            # Update the user's password and clear the reset token
            user.password = generate_password_hash(password)
            user.reset_token = None
            db.session.commit()
            flash('Your password has been reset successfully.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('reset_password.html')
