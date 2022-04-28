from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
# from flask_app.models.user import User

DATABASE = 'belt_exam'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Magazine:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO magazines (title, description, user_id) VALUES (%(title)s,%(description)s,%(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM magazines;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        magazines = []
        for dictionary in results:
            magazines.append( cls(dictionary) )
        return magazines

    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM magazines WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM magazines WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all_with_users(cls, data):
        query = "SELECT magazines.*, users.first_name, users.last_name FROM magazines LEFT JOIN users ON users.id = magizines.user_id;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        user = cls( results[0] )
        for row_from_db in results:
            
            user_data = {
                "id" : row_from_db["user.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "email" : row_from_db["email"],
                "password" : row_from_db["password"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            user.users.append( User( user_data ) )
        return user

    @staticmethod
    def validate_magazine(magazine:dict) -> bool:
        is_valid = True 
        if len(magazine['title']) < 2:
            flash("Title not long enough.") #Ask tyler for verification
            is_valid = False
        if len(magazine['description']) < 10:
            flash("Description not long enough.")
            is_valid = False
        return is_valid
