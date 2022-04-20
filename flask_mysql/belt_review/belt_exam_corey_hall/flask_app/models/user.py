from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
# from flask_app.models.recipe import Recipe

DATABASE = 'belt_exam'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []


    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO belt_exam.users (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_all(cls) -> object or bool:
        query = "SELECT * FROM users;"
        result = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in result:
            users.append(cls(user))
        return users

    @classmethod
    def get_by_email(cls,data:dict) -> object or bool:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return results

    @staticmethod
    def validate_user(user:dict) -> bool:
        is_valid = True 
        if len(user['first_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address")
            is_valid = False
        if user['password'] != user['confirm-password']:
            flash("Passwords do not match")
            is_valid = False
        return is_valid
