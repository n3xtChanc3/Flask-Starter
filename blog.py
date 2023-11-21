# blog.py

from flask import Blueprint, render_template
from flask_login import login_required
from database import BlogPost

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/blog')
@login_required
def view_blog():
    # Fetch and display blog posts
    # You can use BlogPost.query.all() to retrieve all blog posts
    return render_template('blog.html')
