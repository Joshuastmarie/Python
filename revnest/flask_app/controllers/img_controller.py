from re import U
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.listing_model import Listing
from flask_app.models.user_model import User
from flask_app.models.img_model import Img
from flask_app.controllers import user_controller, listing_controller

# # Home Page 

# @app.route('/')
# def index():
#     return render_template('home_page.html')

# # Import listing page 

@app.route('/upload/<int:id>')
def upload_img(id):
    if "user_id" not in session:
        return redirect('/')
    listing_id = id
    return render_template('upload_img.html', listing_id = listing_id)

@app.route('/import_img/process', methods=["POST"])
def process_img():
    data = {
        **request.form
    }
    if not Img.validator_img(request.form):
        return redirect(f'/upload/{data[id]}')
    print("below this")
    print(data["blob_img"])
    filename = data["blob_img"]
    binaryData = Img.convertToBinaryData(filename)
    data["blob_img"] = binaryData
    img_id = Img.insert_new_listing(data)
    print(id)
    return redirect (f'/listing/{id}')

# # Search and buy page 

# @app.route('/search_and_buy')
# def search_and_buy():
#     return render_template('search_and_buy.html')

# # Individual listing page 

# @app.route('/listing/<int:id>')
# def display_listing(id):
#     listing = Listing.get_listing_by_id({"id":id})
#     print(listing)
#     return render_template('display_listing.html', listing = listing)

# # Delete page

# @app.route('/admin/delete_listing/<int:spec_id>')
# def delete_listing(spec_id):
#     data = {
#         "id": spec_id
#     }
#     Listing.delete_single_listing(data)
#     return redirect('/admin')