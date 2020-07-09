import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

SQLALCHEMY_TRACK_MODIFICATIONS = True

STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

SECRET_KEY = 'easiedata_test'