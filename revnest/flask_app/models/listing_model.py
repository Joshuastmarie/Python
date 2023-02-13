from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import my_db
from flask import flash
from flask_app.models import user_model, img_model

class Listing:
    def __init__(self, data):
        self.id = data['id']
        self.street = data['street']
        self.city = data['city']
        self.state = data['state']
        self.zip = data['zip']
        self.bd_count = data['bd_count']
        self.full_bath = data['full_bath']
        self.half_bath = data['half_bath']
        self.a_price = data['a_price']
        self.square_ft = data['square_ft']
        self.gross_sales = data['gross_sales']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.airbnb = data['airbnb']
        self.vrbo = data['vrbo']
        self.user_id = data['user_id']
        

# get methods 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM listings;"
        results = connectToMySQL(my_db).query_db(query)
        listings = []
        for listing in results:
            listings.append( cls(listing) )
        return listings

    @classmethod
    def get_listing_by_id(cls,data):
        query = "SELECT * FROM listings WHERE id = %(id)s"
        results = connectToMySQL(my_db).query_db(query, data)
        print(data)
        print(results)
        if len(results) > 0:
            return cls(results[0])
        return False

# create methods 

    @classmethod
    def insert_new_listing(cls, data):
        query = "INSERT INTO listings (street, city, state, zip, bd_count, full_bath, half_bath, a_price, square_ft, gross_sales, description, airbnb, vrbo, user_id) VALUES (%(street)s, %(city)s, %(state)s, %(zip)s, %(bd_count)s, %(full_bath)s, %(half_bath)s, %(a_price)s, %(square_ft)s, %(gross_sales)s, %(description)s, %(airbnb)s, %(vrbo)s, %(user_id)s);"
        results = connectToMySQL(my_db).query_db(query, data)
        return results

# delete methods

    @classmethod
    def delete_single_listing(cls, data):
        query = "DELETE FROM listings WHERE id = %(id)s"
        return connectToMySQL(my_db).query_db(query, data)


# Validator 

    @staticmethod
    def validator_listing(form_data):
        is_valid = True

        # listing validator 
        print(form_data)
        if len(form_data['street']) < 1:
            is_valid = False
            flash("Field required: Please add a street", "street")
        if len(form_data['city']) < 1:
            is_valid = False
            flash("Field required: Please add a city", "city")
        if not "state" in form_data:
            is_valid = False
            flash("Field required: Please add a state", "state")
        if len(form_data['zip']) < 1:
            is_valid = False
            flash("Field required: Please add a zip", "zip")
        if len(form_data['bd_count']) < 1:
            is_valid = False
            flash("Field required: Please add a bedroom count", "bd_count")
        if len(form_data['full_bath']) < 1:
            is_valid = False
            flash("Field required: Please add a full bath count", "full_bath")
        if len(form_data['half_bath']) < 1:
            is_valid = False
            flash("Field required: Please add a half bath count", "half_bath")
        if len(form_data['a_price']) < 0:
            is_valid = False
            flash("Field required: Please add an asking price", "a_price")
        if len(form_data['square_ft']) < 1:
            is_valid = False
            flash("Field required: Please add square footage", "square_ft")
        if len(form_data['gross_sales']) < 1:
            is_valid = False
            flash("Field required: Please add gross sales", "gross_sales")
        return is_valid



