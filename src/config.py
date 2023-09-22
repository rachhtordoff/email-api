import os


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    DEBUG = os.environ['DEBUG']
    JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
