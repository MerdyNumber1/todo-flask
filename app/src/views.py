from flask import render_template, request, redirect, url_for, flash, jsonify
from flask.views import MethodView
from flask_login import login_required, current_user, logout_user

from .exceptions import UserExistsError
from .forms import TaskForm, SignupForm, LoginForm
from .main import db, limiter
from .models import Task
from .services import UserService, TaskService


@login_required
def root():
    return redirect(url_for('main.tasks'))


class TasksView(MethodView):
    decorators = [login_required, limiter.limit('120 per minute')]

    def get(self):
        form = TaskForm()
        tasks = Task.query.filter_by(user_id=current_user.get_id()).all()
        return render_template('tasks.html', form=form, tasks=tasks)

    def post(self):
        form = TaskForm()
        if form.validate_on_submit():
            task = Task(title=form.title.data, user_id=current_user.get_id())
            db.session.add(task)
            db.session.commit()
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

            task = Task.query.filter_by(user_id=current_user.get_id(), id=id).first()

            if not task:
                return jsonify(success=False), 404

            req = request.get_json()

            if req['title']:
                task.title = req['title']
            if req['done']:
                task.done = req['done']

            db.session.add(task)
            db.session.commit()

            return jsonify(success=True), 200

        return jsonify(success=False), 400


@limiter.limit('15 per minute')
def login():
    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form=form)

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if UserService.login_user(email, password):
            return redirect(url_for('main.tasks'))
        else:
            flash('Please check your login details and try again', 'danger')
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
