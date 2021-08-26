import os

class Config:
    
    '''
    General class configurations
    '''
    BOOKS_API_BASE_URL= 'https://www.googleapis.com/books/v1/volumes?q={}'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
  

    
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://crgdorlzotogkh:c2f5c01ac293f10580bfa405d53f35004523e7c074d9844c84c3cb8d5984c257@ec2-52-203-74-38.compute-1.amazonaws.com:5432/d9tffc9mvmjc47'

    SECRET_KEY ='lkjelkjdskjdjwjepjdhah'
class DevConfig(Config):
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://garlinsk:kenya254@localhost/books'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}