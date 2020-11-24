from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash
from .models import Task
from .forms import TaskForm, SignupForm, LoginForm
from .main import db, bcrypt
from .models import User
from flask_login import login_user


class TasksView(MethodView):

    def get(self):
        form = TaskForm()
        tasks = Task.query.all()
        return render_template('tasks/tasks.html', form=form, tasks=tasks)

    def post(self):
        form = TaskForm()
        if form.validate_on_submit():
            task = Task(title=form.title)
            db.session.add(task)
            db.session.commit()
            return 200


class TaskView(MethodView):
    def get(self, id=None):
        return id


def login():
    form = LoginForm()

    if request.method == 'GET':
        return render_template('auth.login')

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password_hash, password.encode('utf-8')):
            login_user(User, remember=True)
            return redirect(url_for('main.tasks'))

        flash('Please check your login details and try again')

    else:
        flash('Invalid data')

    return redirect(url_for('auth.login_view'))


def signup():
    form = SignupForm()

    if request.method == 'GET':
        return render_template('signup.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            name = form.name.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()

            if user:
                flash('User already exists')
                return redirect(url_for('auth.signup_view'))

            new_user = User(email=email, name=name, password_hash=bcrypt.generate_password_hash(password.encode('utf-8')))

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('auth.login_view'))
