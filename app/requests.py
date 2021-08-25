import urllib.request
import  json

from .models import Books

base_url =None
def configure_request(app):
    global base_url
    base_url = app.config['BOOKS_API_BASE_URL']
    
def get_books():
    get_books_url = base_url
    
    with urllib.request.urlopen(get_books_url) as url:
        get_books_data = url.read()
        get_books_response = json.loads(get_books_data)
        print(get_books_response)
        books_results  = None
        id=get_books_response.get('id')
        volumeInfo= get_books_response.get('volumeInfo')
        imageLinks= get_books_response.get('imageLinks')
        saleInfo= get_books_response.get('saleInfo')

        books_object = Books(id,volumeInfo,imageLinks,saleInfo)
    return books_object

