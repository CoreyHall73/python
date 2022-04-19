from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash 

DATABASE = 'recipes'


class Recipe:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO recipes.recipes (name,description,instructions,under_30,date_made, user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(under_30)s,%(date_made)s,%(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        recipes = []
        for dictionary in results:
            recipes.append( cls(dictionary) )
        return recipes

    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def update(cls,data:dict) -> int:
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,under_30=%(under_30)s,date_made=%(date_made)s,user_id=%(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate_recipe(recipe:dict) -> bool:
        is_valid = True 
        if len(recipe['name']) < 1:
            flash("Name not long enough.")
            is_valid = False
        if len(recipe['description']) < 1:
            flash("Description not long enough.")
            is_valid = False
        if len(recipe['instructions']) < 1:
            flash("Instructions not long enough.")
            is_valid = False
        if not recipe['date_made'] :
            flash("Date required.")
            is_valid = False
        return is_valid