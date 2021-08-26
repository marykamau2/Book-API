import urllib.request
import requests
import  json

from .models import Books

base_url =None
def configure_request(app):
    global base_url
    base_url = app.config['BOOKS_API_BASE_URL']
    
def get_books(endpoint):
    get_books_url = base_url.format(endpoint)
    print(get_books_url)
    get_books_response = requests.get(get_books_url).json()
    books_results  = None
    if get_books_response['items']:
        books_list = get_books_response['items']
        books_results =  procces_results(books_list)
    return books_results


def procces_results(books):
    books_list = []
    for book in books:
        id=book.get('id')
        title= book['volumeInfo'].get('title')
        subtitle= book['volumeInfo'].get('subtitle')
        authors= book['volumeInfo'].get('authors')
        description= book['volumeInfo'].get('description')
        saleability= book['saleInfo'].get('saleability')
        if 'imageLinks' in book['volumeInfo']:
            thumbnail= book['volumeInfo']['imageLinks'].get('thumbnail')
            book_obj= Books(id, title, subtitle, authors, description, thumbnail, saleability)
            books_list.append(book_obj)
        else:
            thumbnail = 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg'
            book_obj= Books(id, title, subtitle, authors, description, thumbnail, saleability)
            books_list.append(book_obj)
    return books_list







