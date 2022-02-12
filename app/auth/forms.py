from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,BooleanField, StringField
from wtforms.validators import InputRequired,ValidationError
from ..models import User

class LoginForm(FlaskForm):
    """
    Login form
    """
    email = EmailField('Email',validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember Me')


class SignupForm(FlaskForm):
    """
    Signup form
    """
    email = EmailField('Email',validators=[InputRequired()])
    username = StringField('username',validators=[InputRequired()])
    name = StringField('Name',validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

    def validate_email(self,data_field):
            if User.query.filter_by(email = data_field.data).first():
                raise ValidationError('Email already exists')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username is already taken')