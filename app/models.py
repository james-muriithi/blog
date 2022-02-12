from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager,db

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
    avatar = db.Column(db.String(64))

    # pitches = db.relationship('Pitch', backref="user", lazy="dynamic")

    created_at = db.Column(db.DateTime, index=True, default=datetime.now)

    @property
    def first_name(self):
        return self.name.split()[0]

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'   


class Pitch(db.Model):
    '''
    Pitches table
    '''
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    comments = db.relationship('Comment', backref='pitch', lazy="dynamic")  
    votes = db.relationship('Vote', backref='pitch', lazy="dynamic")

    created_at = db.Column(db.DateTime, index=True, default=datetime.now)

class Category(db.Model):
    '''
    Pitch categories table
    '''
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    picture_path = db.Column(db.String(64))
    pitch = db.relationship('Pitch', backref='category', lazy='dynamic')

    # get all categories
    @staticmethod
    def get_all_categories():
        return Category.query.all()

    # save category
    def save_category(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Category {self.name}'

class Vote(db.Model):
    '''
    Votes table
    '''
    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key=True)
    vote = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Comment(db.Model):
    '''comments table'''
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)  

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
