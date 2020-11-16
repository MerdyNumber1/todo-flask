from flask.views import MethodView
from flask import render_template
from .models import Task


class TasksView(MethodView):
    def get(self):
        return render_template('tasks.html')


class TaskView(MethodView):
    def get(self, id=None):
        return id
