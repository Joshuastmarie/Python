from re import U
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.listing_model import Listing
from flask_app.controllers import listing_controller
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Admin 

@app.route('/admin')
def display_admin_page():
    users = User.get_all()
    print(users)
    listings = Listing.get_all()
    print(listings)
    return render_template('admin.html', users = users, listings = listings)

# Login and registration  

@app.route('/login')
def display_log_page():
    return render_template('login_page.html')

@app.route('/sign_up')
def display_signup_page():
    return render_template('sign_up_page.html')

@app.route('/register_process', methods=["POST"])
def create_new_user():
    if not User.validator(request.form):
        return redirect('/sign_up')
    saved_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': saved_pass
    }
    logged_id = User.create_user(data)
    session['user_id'] = logged_id
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    return redirect ("/")

# LOGIN AND LOGOUT 

@app.route('/user/login', methods=['POST'])
def log_user():
    data = {
        'email': request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("login failed", "log")
        return redirect('/login')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("login failed", "log")
        return redirect('/login')
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    return redirect ("/")

@app.route('/user/logout')
def reset():
    session.clear()
    return redirect('/')

# Delete routes 

@app.route('/admin/delete_user/<int:spec_id>')
def delete_user(spec_id):
    data = {
        "id": spec_id
    }
    User.delete_single_user(data)
    return redirect('/admin')

# @app.route('/user/<int:id>')
# def render_user_page(id):
#     if "user_id" not in session:
#         return redirect('/')
#     if not session['user_id'] == id:
#         return redirect('/')
#     user = User.get_by_id({'id':id})
#     purchases = Car.get_users_purchases({'id':id})
#     return render_template('user_page.html', user = user, purchases = purchases)


