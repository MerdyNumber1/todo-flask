from .main import app
from flask import Blueprint
from .views import TaskView, TasksView, login, signup

tasks_bp = Blueprint('main', __name__, template_folder='templates/main')
auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')


tasks_bp.add_url_rule('/', view_func=TasksView.as_view('tasks'))
tasks_bp.add_url_rule('/<id>', view_func=TaskView.as_view('task'))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login_view():
    return login()


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup_view():
    return signup()
