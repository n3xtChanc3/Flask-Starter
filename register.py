from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, User

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
    	username = request.form.get('username')
    	password = request.form.get('password')

    	# Check if the username is already taken
    	existing_user = User.query.filter_by(username=username).first()
    	if existing_user:
    		flash('Username already taken. Choose a different one.', 'danger')
    		return redirect(url_for('register.register'))

    	# Hash the password before storing it
    	hashed_password = generate_password_hash(password, method='sha256')

    	# Create a new user
    	new_user = User(username=username, password=hashed_password)

    	# Add the new user to the database
    	db.session.add(new_user)
    	db.session.commit()

    	flash('Account created successfully. You can now log in.', 'success')
    	return redirect(url_for('login.login'))

    return render_template('register.html')
