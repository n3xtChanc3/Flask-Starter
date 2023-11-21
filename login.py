from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from database import db, User
from home import home_bp
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from extensions import login_manager

login_bp = Blueprint('login', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

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
			return redirect(url_for('home.dashboard'))

		flash('Invalid username as password. Please try again.', 'danger')
		return redirect(url_for('login.login'))

	return render_template('login.html')

