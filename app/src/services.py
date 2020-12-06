from flask_login import login_user, current_user

from .exceptions import UserExistsError, UserDoesNotExistError
from .main import db
from .models import User, Task


class UserService:
    def find_user_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def create_user(self, email, name, password):
        user = self.find_user_by_email(email)

        if user:
            raise UserExistsError

        new_user = User(email=email, name=name)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

    def login_user(self, email, password):
        user = self.find_user_by_email(email)

        if user:
            if user.check_password(password):
                login_user(user, remember=True)
                return user
        else:
            raise UserDoesNotExistError

        return False


class TaskService:
    def get_user_task_by_id(self, id):
        return Task.query.filter_by(user_id=current_user.get_id(), id=id).first()

    def get_user_tasks(self):
        return Task.query.filter_by(user_id=current_user.get_id()).all()

    def delete_task(self, id):
        task = self.get_user_task_by_id(id)

        if not task:
            return False

        db.session.delete(task)
        db.session.commit()

        return True

    def update_task(self, id, title, done):
        task = self.get_user_task_by_id(id)

        if not task:
            return False

        if title:
            task.title = title
        if done is not None:
            task.done = done

        db.session.add(task)
        db.session.commit()

        return task

    def create_task(self, title):
        task = Task(title=title, user_id=current_user.get_id())
        db.session.add(task)
        db.session.commit()

        return task
