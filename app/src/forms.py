from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class TaskForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])


class SignupForm(FlaskForm):
    email = StringField('email', validators=[Email(), DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

