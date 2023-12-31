from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from app import db, User

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')

		# Retrieve the user by username
		user = User.query.filter_by(username=username).first()

		# Check if the user exists and the password is correct
		if user and check_password_hash(user.password, password):
			flash('Login successful!', 'success')
			return redirect(url_for(home.home))

		flash('Invalid username as password. Please try again.', 'danger')
		return redirect(url_for(login.login))

	return render_template('login.html')
    
