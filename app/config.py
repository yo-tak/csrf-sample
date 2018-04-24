import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///csrfsample.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(12)
