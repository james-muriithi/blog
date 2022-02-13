from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager,db
import os
from flask import url_for


class User(UserMixin, db.Model):
    '''
    User tables
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    about = db.Column(db.Text)
    image_url = db.Column(db.String(255))

    blogs = db.relationship('Blog', backref="user", lazy="dynamic")
    comments = db.relationship('Comment', backref="user", lazy="dynamic")

    created_at = db.Column(db.DateTime, index=True, default=datetime.now)

    @property
    def first_name(self):
        return self.name.split()[0]

    @property
    def avatar_image(self):
        # current_dir = os.path.dirname(os.path.realpath(__file__))
        if self.image_url:
            return self.image_url
        return f"https://ui-avatars.com/api/?name={self.name.replace(' ',  '+')}"    

    @property
    def is_admin(self):
        return self.role_id == 1    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def get_all_blogs(self):
        return self.blogs.order_by(Blog.created_at.desc()).all()  


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.first_name}'   

class Blog(db.Model):
    '''
    Blogs table
    '''
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    title = db.Column(db.String(255))
    content = db.Column(db.String())
    image_path = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    comments = db.relationship('Comment', backref='blog', lazy='dynamic')

    @property
    def formatted_time(self):
        from datetime import datetime
        return self.created_at.strftime("%b %d, %Y")

    @classmethod
    def get_all_blogs(cls):
        return cls.query.order_by(cls.created_at.desc()).all()

    @classmethod
    def delete_blog(cls, id):
        blog = Blog.query.filter_by(id=id).first()
        db.session.delete(blog)
        db.session.commit()

    def __repr__(self):
        return f'Post {self.title}'


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    blogs = db.relationship('Blog', backref='category', lazy='dynamic')

    @classmethod
    def get_all_categories(cls):
        return cls.query.all()

    def __repr__(self):
        return f'Category {self.name}'

class Comment(db.Model):
    '''comments table'''
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)  

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @property
    def formatted_time(self):
        from datetime import datetime
        return self.created_at.strftime("%b %d, %Y")    

     # delete comment
    @classmethod
    def delete_comment(cls, id):
        comment = Comment.query.filter_by(id=id).first()
        db.session.delete(comment)
        db.session.commit()

    # get all comments created by other users on my posts only 
    @classmethod
    def get_my_posts_comments(cls, user_id):
        comments = Comment.query.filter(Comment.blog.has(user_id=user_id))
        return comments    

class Role(db.Model):
    '''
    Roles table
    '''
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'Role {self.name}'

class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    subscribed = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_subscribers(cls):
        subscribers = Subscriber.query.filter_by(subscribed =1).all()
        return subscribers

    def __repr__(self):
        return f'Subscriber {self.email}'