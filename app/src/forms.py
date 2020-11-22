from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required


class TaskForm(Form):
    title = TextField('title', validators=[Required()])