from app import flask_app, products_collection
from flask import render_template

@flask_app.route("/")
def index():
    return render_template("index.html")
    # return "This is the index page!"


@flask_app.route("/products")
def products():
    # Fetch all products from MongoDB
    products = list(products_collection.find())
    return render_template("products.html", products=products)
