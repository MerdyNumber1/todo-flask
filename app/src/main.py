from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import config
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from . import routes, models
