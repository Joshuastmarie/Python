from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import my_db
from flask import flash
from flask_app.models import listing_model, img_model
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# get methods 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(my_db).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(my_db).query_db(query, data)
        if len(results) > 0:
            return cls(results[0])
        return False

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(my_db).query_db(query, data)
        print(results)
        if len(results) > 0:
            return cls(results[0])
        return False

# Create method 

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        results = connectToMySQL(my_db).query_db(query, data)
        return results

# Validator 

    @staticmethod
    def validator(potential_user):
        is_valid = True
        if len(potential_user['first_name']) < 3:
            is_valid = False
            flash("**Required Field**", "first_name")
        if len(potential_user['last_name']) < 3:
            is_valid = False
            flash("**Required Field**", "last_name")

        # email validator 

        if len(potential_user['email']) < 1:
            is_valid = False
            flash("**Required Field**", "email")
        elif not EMAIL_REGEX.match(potential_user['email']):
            is_valid = False
            flash('**Required Field**', 'email')
        else: # this tests for a unique email
            data = {
                'email':potential_user['email']
            }
            user_in_db = User.get_by_email(data)
            if user_in_db:
                is_valid = False
                flash("**Required Field**", "email")

        # Password Validator 

        if len(potential_user['password']) < 8:
            is_valid = False
            flash("**Password must be 8 characters**", "password")
        elif potential_user['password'] != potential_user['c_password']:
            is_valid = False
            flash("**Passwords do not match**", "c_password")

        # this code is for checking int's

        # if len(potential_user['age']) < 1:
        #     is_valid = False
        #     flash("Please enter an age")
        # if int(potential_user['age']) < 18:
        #     is_valid = False
        #     flash("age must be at least 18 to register")

        return is_valid

# delete methods

    @classmethod
    def delete_single_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL(my_db).query_db(query, data)