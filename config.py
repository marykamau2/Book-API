class Config:
    
    '''
    General class configurations
    '''
    # BOOKS_API_BASE_URL = 'https://www.googleapis.com/books/v1/volumes?q={}'
    BOOKS_API_BASE_URL= 'https://www.googleapis.com/books/v1/volumes?q=search+terms'
    
class ProdConfig(Config):
    pass
class DevConfig(Config):
    Debug = True
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}