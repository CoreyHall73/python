from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

DATABASE = 'books_and_authors'

class Author:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM authors;"
        results = connectToMySQL(DATABASE).query_db(query)
        authors = []
        for u in results:
            authors.append( cls(u) )
        return authors

    @classmethod
    def get_author_with_books( cls , data ):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        author = cls( results[0] )
        print(results)
        print(author)
        for row_from_db in results:
            book_data = {
                "id" : row_from_db["books.id"],
                "title" : row_from_db["title"],
                "num_of_pages" : row_from_db["num_of_pages"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            author.books.append( book.Book( book_data ) )
        return author