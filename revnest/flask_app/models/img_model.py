from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import my_db
from flask import flash
from flask_app.models import listing_model, user_model

class Img:
    def __init__(self, data):
        self.id = data['id']
        self.img_blob = data['img_blob']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.listing_id = data['listing_id']
        

# get methods 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM imgs;"
        results = connectToMySQL(my_db).query_db(query)
        imgs = []
        for listing in results:
            imgs.append( cls(listing) )
        return imgs

    @classmethod
    def get_img_by_id(cls,data):
        query = "SELECT * FROM imgs WHERE id = %(id)s"
        results = connectToMySQL(my_db).query_db(query, data)
        print(data)
        print(results)
        if len(results) > 0:
            return cls(results[0])
        return False

# create methods 

    @classmethod
    def insert_new_img(cls, data):
        query = "INSERT INTO imgs (img_blob, listing_id) VALUES (%(img_blob)s, %(listing_id)s);"
        results = connectToMySQL(my_db).query_db_blobs(query, data)
        return results

# delete methods

    @classmethod
    def delete_single_img(cls, data):
        query = "DELETE FROM imgs WHERE id = %(id)s"
        return connectToMySQL(my_db).query_db(query, data)

# binary data conversion
    @classmethod
    def convertToBinaryData(cls, filename):
    # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData


# Validator 

    @staticmethod
    def validator_img(form_data):
        is_valid = True
        if not form_data['blob_img']:
            is_valid = False
            flash("Select an image to upload", "blob_img")
        # if len(form_data['last_name']) < 1:
        #     is_valid = False
        #     flash("last_name is required", "last_name")

        # listing validator 
        # print(form_data)
        # if len(form_data['street']) < 1:
        #     is_valid = False
        #     flash("Field required: Please add a street", "street")
        # if len(form_data['city']) < 1:
        #     is_valid = False
        #     flash("Field required: Please add a city", "city")
        # if not "state" in form_data:
        #     is_valid = False
        #     flash("Field required: Please add a state", "state")
        # if len(form_data['zip']) < 1:
        #     is_valid = False
        #     flash("Field required: Please add a zip", "zip")
        # if len(form_data['bd_count']) < 1:
        #     is_valid = False
        #     flash("Field required: Please add a bedroom count", "bd_count")
        # if len(form_data['full_bath']) < 1:
        #     is_valid = False
        #     flash("Field required: Please add a full bath count", "full_bath")
        # if len(form_data['half_bath']) < 1:
        #     is_valid = False
        #     flash("Field required: Please add a half bath count", "half_bath")
        # if len(form_data['a_price']) < 0:
        #     is_valid = False
        #     flash("Field required: Please add an asking price", "a_price")
        # if len(form_data['square_ft']) < 1:
        #     is_valid = False
        #     flash("Field required: Please add square footage", "square_ft")
        # if len(form_data['gross_sales']) < 1:
        #     is_valid = False
        #     flash("Field required: Please add gross sales", "gross_sales")



        # if len(form_data['zip']) >= 1:
        #     if int(form_data['zip']) < 1:
        #         is_valid = False
        #         flash("Field required: zip must be valid", "zip")
        
        # if len(form_data['description']) < 1:
        #     is_valid = False
        #     flash("Field required: Please add a description", "description")
        # if len(form_data['model']) < 1:
        #     is_valid = False
        #     flash("Field required: Please add a model", "model")
        # if len(form_data['make']) < 1:
        #     is_valid = False
        #     flash("Field required: Please add a make", "make")
        # if len(form_data['year']) < 1:
        #     is_valid = False
        #     flash("Field required: Please add a year", "year")
        # if len(form_data['year']) >= 1:
        #     if int(form_data['year']) < 1:
        #         is_valid = False
        #         flash("Field required: Year must be higher than 0", "year")

        # email validator 

        # if len(form_data['email']) < 1:
        #     is_valid = False
        #     flash("email is required", "email")
        # elif not EMAIL_REGEX.match(form_data['email']):
        #     is_valid = False
        #     flash('email not a valid format', 'email')
        # else: # this tests for a unique email
        #     data = {
        #         'email':form_data['email']
        #     }
        #     user_in_db = User.get_by_email(data)
        #     if user_in_db:
        #         is_valid = False
        #         flash("email already registered", "email")

        # Password Validator 

        # if len(form_data['password']) < 8:
        #     is_valid = False
        #     flash("password must be 8 characters", "password")
        # elif form_data['password'] != form_data['c_password']:
        #     is_valid = False
        #     flash("passwords do not match", "c_password")

        # this code is for checking int's

        # if len(form_data['age']) < 1:
        #     is_valid = False
        #     flash("Please enter an age")
        # if int(form_data['age']) < 18:
        #     is_valid = False
        #     flash("age must be at least 18 to register")

        return is_valid



