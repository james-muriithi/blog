import os
from decouple import config

class Config:
    """
    General configuration parent class
    """

    UPLOADED_PHOTOS_DEST ='app/static/uploads'
    
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost/{DB}'

    SECRET_KEY = config('SECRET_KEY', default="")

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config("MAIL_USERNAME", default="")
    MAIL_PASSWORD = config("MAIL_PASSWORD", default="")



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = config("DATABASE_URL", default="").replace("postgres://", "postgresql://", 1)


class DevelopmentConfig(Config):
    DEBUG = True
    DB_USER = config('DB_USER', default="")
    DB_PASSWORD = config('DB_PASSWORD', default="")
    DB = 'blogs'
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost/{DB}'


config_options = {
    'development': DevelopmentConfig,
    'production': ProdConfig
}