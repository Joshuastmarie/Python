from re import U
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.listing_model import Listing
from flask_app.models.user_model import User
from flask_app.models.img_model import Img
from flask_app.controllers import user_controller, img_controller

# Home Page 

@app.route('/')
def index():
    return render_template('home_page.html')

# Import listing page 

@app.route('/import_listing')
def import_new_listing():
    if "user_id" not in session:
        return redirect('/')
    return render_template('import_listing.html')

@app.route('/import_listing/process', methods=["POST"])
def process_listing():
    if not Listing.validator_listing(request.form):
        return redirect('/import_listing')
    print(session["user_id"])
    data = {
        **request.form,
        "user_id": session["user_id"]
    }
    data["airbnb"] = data["airbnb"].split('?')[0]
    data["vrbo"] = data["vrbo"].split('?')[0]
    listing_id = Listing.insert_new_listing(data)
    print(listing_id)
    return redirect (f'/listing/{listing_id}')

# Search and buy page 

@app.route('/search_and_buy')
def search_and_buy():
    return render_template('search_and_buy.html')

# Individual listing page 

@app.route('/listing/<int:id>')
def display_listing(id):
    listing = Listing.get_listing_by_id({"id":id})
    print(listing)
    return render_template('display_listing.html', listing = listing)

# Delete page

@app.route('/admin/delete_listing/<int:spec_id>')
def delete_listing(spec_id):
    data = {
        "id": spec_id
    }
    Listing.delete_single_listing(data)
    return redirect('/admin')