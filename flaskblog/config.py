from os import environ

'''
    import secrets
    secrets.token_hex(16) --> returns 16 bit secret hexadecimal key
'''
class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = int(environ.get('MAIL_PORT'))
    MAIL_USE_TLS = eval(environ.get('MAIL_USE_TLS')) 
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')