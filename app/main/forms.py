from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField
from wtforms.validators import InputRequired

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
    email = StringField('Email', validators=[InputRequired()])


# category form
class CategoryForm(FlaskForm):
    name = StringField('Category', validators=[InputRequired()])