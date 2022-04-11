from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Ninja:

    def __ini__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_a']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_a, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @staticmethod
    def validate_ninja(ninja):
        is_valid = True

        if (len(ninja['first_name']) < 3):
            flash("Name must be at least 3 characters.")
            is_valid = False
        if (len(ninja['last_name']) < 3):
            flash("Name must be at least 3 characters.")
            is_valid = False
        if (not ninja['age']):
            flash("You must enter a number.")
            is_valid = False
        return is_valid
