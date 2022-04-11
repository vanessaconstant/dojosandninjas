from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, data):

        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_all_dojos(cls):

        query = "SELECT * FROM dojos;"

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query)

    @classmethod
    def get_dojos_and_ninjas(cls, data):

        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id ="+data+";"

        result = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query)

        ninja_result = []

        for ninjas_row_info in result:

            ninjas_info = {

                'dojo_name': ninjas_row_info['name'],
                'first_name': ninjas_row_info['first_name'],
                'last_name': ninjas_row_info['last_name'],
                'age': ninjas_row_info['age']

            }

            ninja_result.append(ninjas_info)

        return ninja_result

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True

        if (len(dojo['name']) < 3):
            flash("Name must be at least 3 characters.")
            is_valid = False

        return is_valid
