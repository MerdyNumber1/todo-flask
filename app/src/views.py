from flask import render_template, request, redirect, url_for, flash, jsonify
from flask.views import MethodView
from flask_login import login_required, logout_user

from .exceptions import UserExistsError, UserDoesNotExistError
from .forms import TaskForm, SignupForm, LoginForm
from .main import limiter
from .services import UserService, TaskService

UserService = UserService()
TaskService = TaskService()


@login_required
def root():
    return redirect(url_for('main.tasks'))


class TasksView(MethodView):
    decorators = [login_required, limiter.limit('120 per minute')]

    def get(self):
        form = TaskForm()
        tasks = TaskService.get_user_tasks()
        return render_template('tasks.html', form=form, tasks=tasks)

    def post(self):
        form = TaskForm()
        if form.validate_on_submit():
            task = TaskService.create_task(form.title.data)
            return jsonify(success=True, task={
                'id': task.id,
                'title': task.title,
                'done': task.done
            })
        return jsonify(success=False), 400


class TaskView(MethodView):
    decorators = [login_required, limiter.limit('120 per minute')]

    def delete(self, id):

        if TaskService.delete_task(id):
            return jsonify(succss=True)
        else:
            return jsonify(success=False), 404

    def put(self, id):

        if request.is_json:
            req = request.get_json()

            if TaskService.update_task(id, req['title'], req['done']):
                return jsonify(success=True), 200

            return jsonify(success=False), 404

        return jsonify(success=False), 400


@limiter.limit('15 per minute')
def login():
    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form=form)

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        try:
            if UserService.login_user(email, password):
                return redirect(url_for('main.tasks'))
            else:
                flash('Please check your login details and try again', 'danger')
        except UserDoesNotExistError:
            flash('User does not exist', 'danger')

    else:
        flash('Invalid data', 'danger')

    return redirect(url_for('auth.login_view'))


@limiter.limit('15 per minute')
def signup():
    form = SignupForm()

    if request.method == 'GET':
        return render_template('signup.html', form=form)

    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        password = form.password.data

        try:
            UserService.create_user(email, name, password)
        except UserExistsError:
            flash('User already exists', 'danger')
            return redirect(url_for('auth.signup_view'))

        flash('You have successfully registered, please login to continue', 'success')
        return redirect(url_for('auth.login_view'))

    else:
        flash('Invalid data', 'danger')

    return redirect(url_for('auth.signup_view'))


@limiter.limit('30 per minute')
def logout():
    logout_user()
    return redirect(url_for('auth.login_view'))
