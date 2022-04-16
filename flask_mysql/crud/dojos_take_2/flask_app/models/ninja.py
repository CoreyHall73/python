from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_and_ninjas'

class Ninja:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    # @classmethod
    # def get_dojo_with_ninjas( cls , data ):
    #     query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
    #     results = connectToMySQL(DATABASE).query_db( query , data )
    #     dojo = cls( results[0] )
    #     for row_from_db in results:
            
    #         ninja_data = {
    #             "id" : row_from_db["ninjas.id"],
    #             "first_name" : row_from_db["first_name"],
    #             "last_name" : row_from_db["last_name"],
    #             "age" : row_from_db["age"],
    #             "dojo_id" : row_from_db["dojo_id"],
    #         }
    #         dojo.ninjas.append( ninja.Ninja( ninja_data ) )
    #     return dojo
