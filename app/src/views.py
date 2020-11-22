from flask.views import MethodView
from flask import render_template, jsonify
from .models import Task
from .forms import TaskForm
from .main import db


class TasksView(MethodView):
    form = TaskForm()

    def get(self):
        tasks = Task.query.all()
        return render_template('tasks.html', form=self.form, tasks=tasks)

    def post(self):
        if self.form.validate_on_submit():
            task = Task(title=self.form.title)
            db.session.add(task)
            db.session.commit()
            return 200


class TaskView(MethodView):
    def get(self, id=None):
        return id


class UserView(MethodView):
    def get(self):
        return 'hello!'