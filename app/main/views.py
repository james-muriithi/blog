from app.main.forms import BlogForm, CommentForm, SubscriberForm
from app.models import Blog, Subscriber, Comment
from app import db, photos
from app.requests import get_quote
from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from . import main

@main.route('/')
def index():
    subscribe_form = SubscriberForm()
    quote = get_quote()
    blogs = Blog.get_all_blogs()
    return render_template('index.html', blogs=blogs, subscribe_form=subscribe_form, quote=quote)


@main.route('/blog/<id>')
def blog_show(id):
    blog = Blog.query.get(id)
    commentForm = CommentForm()
    if not blog:
        abort(404)
    return render_template('single-blog.html', Comment=Comment, blog=blog, title=blog.title, commentForm=commentForm)

@main.route('/blog/create', methods=['POST'])
@login_required
def blog_create():
    form = BlogForm()

    if form.validate_on_submit() and 'image_path' in request.files:
        filename = photos.save(request.files['image_path'])
        path = f'uploads/{filename}'

        blog = Blog(title=form.title.data, content=form.content.data,
                      user=current_user, category_id=form.category.data, image_path=path)

        db.session.add(blog)
        db.session.commit()

    return redirect(request.referrer or url_for('main.index'))   

@main.route('/subscribe', methods=["POST"])
def subscribe():
    subscribe_form = SubscriberForm()

    if subscribe_form.validate_on_submit():
        subscriber = Subscriber(name=subscribe_form.name.data, email=subscribe_form.email.data)
        db.session.add(subscriber)
        db.session.commit()
        flash("You have added to our list of subscribers", "success")

        # send email


    return redirect(request.referrer or url_for('main.index'))   

# comments
@main.route("/blog/<id>/comment", methods=["POST"])
@login_required
def save_comment(id):
    blog = Blog.query.get(id)
    form = CommentForm()
    if not blog:
        abort(404)
    
    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data, user=current_user, blog=blog)
        comment.save_comment()
        flash("Your comment was saved successfully", "success")

    return redirect(request.referrer or url_for('main.index'))     