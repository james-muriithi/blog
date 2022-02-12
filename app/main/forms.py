from app.models import Subscriber
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField
from wtforms.validators import InputRequired, ValidationError
from flask import flash

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    category = IntegerField('Category', validators=[InputRequired()])
    content = StringField('Content', validators=[InputRequired()])
    image_path = StringField('Content', validators=[InputRequired()])

# comment form
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a Comment', validators=[InputRequired()])


# subscriber form
class SubscriberForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])

    def validate_email(self,data_field):
            if Subscriber.query.filter_by(email = data_field.data).first():
                flash('Email already subscribed', 'error')
                raise ValidationError('Email already subscribed')
