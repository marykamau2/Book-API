import os

class Config:
    
    '''
    General class configurations
    '''
    BOOKS_API_BASE_URL= 'https://www.googleapis.com/books/v1/volumes?q={}'
 
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://leresipitchdb:pitchidea@localhost/pitches'
  

    
    
class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    SECRET_KEY ='lkjelkjdskjdjwjepjdhah'

class DevConfig(Config):


    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}