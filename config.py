## imports
import os


class Config(object):
    TESTING = os.environ.get('TESTING')
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    ## so reqparser returns all errors rather than the first
    BUNDLE_ERRORS = os.environ.get('BUNDLE_ERRORS')

    ## db variables
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')