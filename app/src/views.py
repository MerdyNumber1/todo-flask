from flask.views import MethodView
from flask import render_template, request, redirect, url_for
from .models import Task
from .forms import TaskForm, SignupForm
from .main import db, bcrypt
from .models import User


class TasksView(MethodView):

    def get(self):
        form = TaskForm()
        tasks = Task.query.all()
        return render_template('tasks.html', form=form, tasks=tasks)

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
    return render_template('login.html')


def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        form = SignupForm()

        if form.validate_on_submit():
            email = form.email.data
            name = form.name.data
            password = form.name.password

            user = User.query.filter_by(email=email).first()

            if user:
                return redirect(url_for('auth.signup'))

            new_user = User(email=email, name=name, password_hash=bcrypt.generate_password_hash(password))

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('auth.login'))