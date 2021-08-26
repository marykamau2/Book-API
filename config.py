import os

class Config:
    
    '''
    General class configurations
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://leresipitchdb:pitchidea@localhost/pitches'
    # BOOKS_API_BASE_URL = 'https://www.googleapis.com/books/v1/volumes?q={}'
    BOOKS_API_BASE_URL= 'https://www.googleapis.com/books/v1/volumes?q={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')

    
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}