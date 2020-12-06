import os

SQLALCHEMY_DATABASE_URI = f"postgresql://" \
                          f"{os.environ['POSTGRES_USER']}:" \
                          f"{os.environ['POSTGRES_PW']}@" \
                          f"{os.environ['POSTGRES_HOST']}/" \
                          f"{os.environ['POSTGRES_DB']}"
SQLALCHEMY_MIGRATE_REPO = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'migrations')
SQLALCHEMY_TRACK_MODIFICATIONS = False

CSRF_ENABLED = True
SECRET_KEY = os.getenv('APP_SECRET_KEY')  # you have to change this variable
