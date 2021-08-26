from flask import render_template, request
from . import main
from  ..requests import get_books

@main.route('/', methods=['GET', 'POST'])
def index():
    books=get_books('search+terms')
    if request.method =='POST':
        query_string = request.form.get('searchForm')
        print(query_string)
        books = get_books(query_string)
    return render_template('allbooks.html', books=books)

# @main.route('/book/<name>')
# def search_books():
#     book = get_one_book('endpoint')
#     return render_template('book.html', book = book)



