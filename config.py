import os

class Config:
    
    '''
    General class configurations
    '''
    BOOKS_API_BASE_URL= 'https://www.googleapis.com/books/v1/volumes?q={}'

  

    
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://bvjqsisalficph:5b042972fee134f2f8f5c498d6dd221b8d081838624436ea50f677e2c7212714@ec2-44-196-170-156.compute-1.amazonaws.com:5432/d3ulnnpoeiafgp'
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