from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_and_ninjas'

class Dojo:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result