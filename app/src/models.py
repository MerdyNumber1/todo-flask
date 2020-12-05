from datetime import datetime
import bcrypt

from flask_login import UserMixin

from .main import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class Task(BaseModel):
    __tablename__ = 'tasks'

    title = db.Column(db.String(256), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.id}>'


class User(UserMixin, BaseModel):
    __tablename__ = 'users'

    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8')

    def check_passwords(self, password):
        bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.id}>'
