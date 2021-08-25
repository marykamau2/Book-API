from flask import render_template, request
from . import main
from  ..requests import get_books

@main.route('/', methods=['GET', 'POST'])
def index():
    
    books=get_books()
    return render_template('index.html', books=books)
