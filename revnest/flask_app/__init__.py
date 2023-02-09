from flask import Flask

app = Flask(__name__)

my_db = 'revnest_schema'
app.secret_key = "secret key for josh and stefan"