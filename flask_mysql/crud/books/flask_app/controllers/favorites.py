from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def authors():
    authors = Author.get_all()
    return render_template('authors.html', authors=authors)

@app.route('/new_a', methods=['POST'])
def new_a():
    Author.save(request.form)
    return redirect('/')

@app.route('/new_b')
def new_b():
    books = Book.get_all()
    return render_template('new_book.html',books=books)

@app.route('/create_b', methods=['POST'])
def create_b():
    Book.save(request.form)
    return redirect('/new_b')

@app.route('/show_a/<int:id>')
def show_a(id):
    data = {'id' : id}
    author = Author.get_author_with_books(data)
    return render_template('show_authors.html', author=author)