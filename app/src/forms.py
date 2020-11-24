from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
