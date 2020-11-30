from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash, jsonify
from .models import Task
from .forms import TaskForm, SignupForm, LoginForm
from .main import db, bcrypt, app, limiter
from .models import User
from flask_login import login_user, login_required, current_user, logout_user


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

        task = Task.query.filter_by(user_id=current_user.get_id(), id=id).first()

        if not task:
            return jsonify(success=False), 404

        db.session.delete(task)
        db.session.commit()
        return jsonify(succss=True)

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

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user, remember=True)
            return redirect(url_for('main.tasks'))

        flash('Please check your login details and try again')

    else:
        flash('Invalid data')

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

        user = User.query.filter_by(email=email).first()

        if user:
            flash('User already exists')
            return redirect(url_for('auth.signup_view'))

        new_user = User(email=email,
                        name=name,
                        password_hash=bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login_view'))


@limiter.limit('30 per minute')
def logout():
    logout_user()
    return redirect(url_for('auth.login_view'))
