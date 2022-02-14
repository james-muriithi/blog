from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user
from . import auth
from ..models import User
from ..email import mail_message
from .. import db
from .forms import LoginForm, SignupForm


@auth.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password', 'error')

    return render_template('auth/login.html', form=form, title="Login")


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data, name=form.name.data, role_id=2)
        user.save_user()

        # send email to user
        mail_message("Welcome to Epic Blogs","emails/welcome_user",user.email,user=user)

        flash('User Account created successfully!', 'success')
        login_user(user)

        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('auth/signup.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))