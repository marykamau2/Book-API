import os

class Config:
    
    '''
    General class configurations
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://leresipitchdb:pitchidea@localhost/pitches'
    # BOOKS_API_BASE_URL = 'https://www.googleapis.com/books/v1/volumes?q={}'
    BOOKS_API_BASE_URL= 'https://www.googleapis.com/books/v1/volumes?q={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    
class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI= 'postgres://vplsclphhifrju:bb8fe15cc7484043211d1485f233cd7608f19f78fa80e349eff13ab1f8ac32ec@ec2-54-236-137-173.compute-1.amazonaws.com:5432/degjtahtl2hjth'
     SECRET_KEY ='lkjelkjdskjdjwjepjdhah'
class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}