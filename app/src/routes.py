from .main import app
from flask import Blueprint
from .views import TaskView, TasksView


app.add_url_rule('/tasks/', view_func=TasksView.as_view('tasks'))
app.add_url_rule('/tasks/<id>', view_func=TaskView.as_view('task'))

auth_bp = Blueprint('auth', __name__)

auth_bp.add_url_rule('')