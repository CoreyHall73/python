from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'dojo_survey'

class Dojo:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT into dojos (name,location,language,comments) VALUES (%(name)s,%(location)s,%(language)s,%(comments)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL(DATABASE).query_db(query)
        return Dojo(results[0])

    @staticmethod
    def is_valid(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(dojo['location']) < 1:
            is_valid = False
            flash("Must choose a dojo location.")
        if len(dojo['language']) < 1:
            is_valid = False
            flash("Must choose a favorite language.")
        if len(dojo['comment']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")
        return is_valid


