from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import config
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from . import routes, models

app.register_blueprint(routes.auth_bp, url_prefix='/auth')
app.register_blueprint(routes.tasks_bp, url_prefix='/tasks')
