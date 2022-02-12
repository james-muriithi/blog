from app.main.forms import BlogForm, CommentForm, ProfileForm, SubscriberForm, EditBlogForm
from app.models import Blog, Subscriber, Comment, User
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

    categories_bg = [
        "https://res.cloudinary.com/james-m/image/upload/c_scale,w_455,f_webp/v1644698836/pexels-ella-olsson-1640777_qauhrg.jpg",
        "https://res.cloudinary.com/james-m/image/upload/c_scale,w_455,f_webp/v1644698835/pexels-josh-sorenson-1714208_p9ajro.jpg",
        "https://res.cloudinary.com/james-m/image/upload/c_scale,w_455,f_webp/v1644698837/pexels-errin-casano-2356045_a8tnjn.jpg",
        "https://res.cloudinary.com/james-m/image/upload/c_scale,w_455,f_webp/v1644698837/pexels-freestocksorg-96380_cigxpx.jpg"
    ]

    return render_template('index.html', blogs=blogs, subscribe_form=subscribe_form, quote=quote, categories_bg=categories_bg)


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

@main.route('/blog/<id>/update', methods=['POST'])
@login_required
def blog_update(id):
    form = EditBlogForm()
    blog = Blog.query.get(id)
    if not blog:
        abort(404)

    if form.validate_on_submit():
        Blog.query.filter_by(id=id).update({"title":form.title.data, "content":form.content.data, 
            "category_id":form.category.data})
        db.session.commit()
        flash("Blog updated successfully", "success")

    return redirect(request.referrer or url_for('main.index'))


@main.route('/blog/<id>/update_image', methods=['POST'])
@login_required
def blog_update_image(id):
    blog = Blog.query.get(id)
    if not blog:
        abort(404)

    if 'image_path' in request.files:
        filename = photos.save(request.files['image_path'])
        path = f'uploads/{filename}'

        Blog.query.filter_by(id=id).update({"image_path": path})
        db.session.commit()
        flash("Blog Image updated successfully", "success")

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


# delete blog
@main.route("/blog/<id>/delete", methods=["GET"])
@login_required
def delete_blog(id):
    blog = Blog.query.get(id)
    if not blog or blog.user_id is not current_user.id:
        abort(404)
    
    Blog.delete_blog(id) 

    return redirect(request.referrer or url_for('main.index'))  


#delete comment
@main.route("/comment/<id>/delete", methods=["GET"])
@login_required
def delete_comment(id):
    comment = Comment.query.get(id)
    if not comment:
        abort(404)
    
    Comment.delete_comment(id) 

    return redirect(request.referrer or url_for('main.index'))  

@main.route('/profile', methods=["GET","POST"])
@login_required
def profile():
    profile_form = ProfileForm()
    if profile_form.validate_on_submit():
        User.query.filter_by(id=current_user.id).update({
            'name':profile_form.name.data, 'about': profile_form.about.data
            })
        db.session.commit()
        flash("Your details have been updated", "success")
        return redirect(url_for('main.profile'))

    return render_template('profile.html', form=profile_form, Comment = Comment)    


@main.route('/profile/update_avatar',methods= ['POST'])
@login_required
def update_avatar():
    if 'avatar' in request.files:
        filename = photos.save(request.files['avatar'])
        path = f'uploads/{filename}'
        current_user.avatar = path
        db.session.commit()

    return redirect(url_for('main.profile'))    