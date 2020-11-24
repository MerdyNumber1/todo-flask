from .main import app
from flask import Blueprint
from .views import TaskView, TasksView, login, signup

tasks_bp = Blueprint('tasks', __name__, template_folder='templates/tasks')
auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')


tasks_bp.add_url_rule('/', view_func=TasksView.as_view('tasks'))
tasks_bp.add_url_rule('/<id>', view_func=TaskView.as_view('task'))


@auth_bp.route('/login')
def login_view():
    return login()


@auth_bp.route('/signup')
def signup_view():
    return signup()
