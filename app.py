from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import secrets
from register import register_bp
from login import login_bp
from home import home_bp

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Set the SECRET_KEY from the environment variable
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', secrets.token_hex(16))

# SQLite3 Configuration
app.config['SQLACHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///site.db')
db = SQLAlchemy(app)

# User Model
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)

# Create tables
with app.app_context():
	db.create_all()


# Register blueprints
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(home_bp)


#@app.route('/')
#def hello():
#	return 'Hello, Flask!'


if __name__ == '__main__':
	app.run(debug=True)
