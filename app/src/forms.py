from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class TaskForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])


class SignupForm(FlaskForm):
    email = StringField('email', validators=[Email(), DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = StringField('email', validators=[Email(), DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])