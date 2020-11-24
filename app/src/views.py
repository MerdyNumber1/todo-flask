from flask.views import MethodView
from flask import render_template, jsonify
from .models import Task
from .forms import TaskForm
from .main import db


class TasksView(MethodView):

    def get(self):
        form = TaskForm()
        tasks = Task.query.all()
        return render_template('tasks.html', form=form, tasks=tasks)

    def post(self):
        form = TaskForm()
        if self.form.validate_on_submit():
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
    return render_template('signup.html')
