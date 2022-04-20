from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dog import Dog

DATABASE = 'houses_dogs'

class House:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dogs = []

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM houses;"
        results = connectToMySQL(DATABASE).query_db(query)
        houses = []
        for house in results:
            houses.append( cls(house) )
        return houses

    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO houses (name) VALUES (%(name)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_house_with_dogs( cls , data ):
        query = "SELECT * FROM houses LEFT JOIN dogs ON dogs.house_id = houses.id WHERE houses.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        house = cls( results[0] )
        for row_from_db in results:
            
            dog_data = {
                "id" : row_from_db["dogs.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "house_id" : row_from_db["house_id"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            house.dogs.append( Dog( dog_data ) )
        return house