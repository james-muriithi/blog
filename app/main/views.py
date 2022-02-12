from app.main.forms import BlogForm
from app.models import Blog, Category
from app import db, photos
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from . import main

@main.route('/')
def index():
    blogs = Blog.get_all_blogs()
    return render_template('index.html', blogs=blogs)


@main.route('/blog/create', methods=['POST'])
@login_required
def pitch_create():
    form = BlogForm()

    if form.validate_on_submit() and 'image_path' in request.files:
        filename = photos.save(request.files['image_path'])
        path = f'uploads/{filename}'

        blog = Blog(title=form.title.data, content=form.content.data,
                      user=current_user, category_id=form.category.data, image_path=path)

        db.session.add(blog)
        db.session.commit()

    return redirect(request.referrer or url_for('main.index'))   