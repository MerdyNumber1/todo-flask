from .main import db
from datetime import datetime
from flask_login import UserMixin


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow, onupdate=datetime.utcnow)


class Task(BaseModel):
    title = db.Column(db.String(256))
    done = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Task {self.id}>'


class User(UserMixin, BaseModel):
    email = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    tasks = db.relationship('Task', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.id}>'
