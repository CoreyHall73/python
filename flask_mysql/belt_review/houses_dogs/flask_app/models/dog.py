from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'houses_dogs'

class Dog:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.house_id = data['house_id']

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM dogs;"
        results = connectToMySQL(DATABASE).query_db(query)
        dogs = []
        for dog in results:
            dogs.append( cls(ninja) )
        return dogs

    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO dogs (first_name,last_name,age,house_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(house_id)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
