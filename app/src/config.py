import os

SQLALCHEMY_DATABASE_URI = f"postgresql://" \
                          f"{os.environ['POSTGRES_USER']}:" \
                          f"{os.environ['POSTGRES_PW']}@" \
                          f"{os.environ['POSTGRES_HOST']}/" \
                          f"{os.environ['POSTGRES_DB']}"
SQLALCHEMY_MIGRATE_REPO = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'migrations')

CSRF_ENABLED = True
SECRET_KEY = '9jkgGDF4awer76'  # you have to change this variable
