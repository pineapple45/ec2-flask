from os import environ

SECRET_KEY=environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI=environ.get('SQLALCHEMY_DATABASE_URI')
FLASK_RUN_PORT=environ.get('FLASK_RUN_PORT')
DEBUG=environ.get('DEBUG')
FLASK_APP=environ.get('FLASK_APP')
FLASK_ENV=environ.get('FLASK_ENV')
MAIL_SERVER = environ.get('MAIL_SERVER')
MAIL_PORT = int(environ.get('MAIL_PORT'))
MAIL_USE_TLS = eval(environ.get('MAIL_USE_TLS')) 
MAIL_USERNAME = environ.get('MAIL_USERNAME')
MAIL_PASSWORD = environ.get('MAIL_PASSWORD')