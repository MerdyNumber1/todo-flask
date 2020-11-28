from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import config
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'auth.login_view'
login_manager.init_app(app)

from . import routes, models

app.register_blueprint(routes.auth_bp, url_prefix='/auth')
app.register_blueprint(routes.main_bp, url_prefix='/tasks')


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))
