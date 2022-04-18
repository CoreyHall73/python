from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

DATABASE = 'books_and_authors'

class Book:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.authors = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s,%(num_of_pages)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM books;"
        results = connectToMySQL(DATABASE).query_db(query)
        books = []
        for u in results:
            books.append( cls(u) )
        return books

    @classmethod
    def get_book_with_authors( cls , data ):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        book = cls( results[0] )
        for row_from_db in results:
            author_data = {
                "id" : row_from_db["authors.id"],
                "name" : row_from_db["name"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            book.authors.append( author.Author( author_data ) )
        return book
