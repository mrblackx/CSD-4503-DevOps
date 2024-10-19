# pip install pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

db_username = os.environ["MONGODB_USERNAME"]
db_password = os.environ.get("MONGODB_PASSWORD")

# MongoDB Atlas Connection
client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.bb9ww.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.app  # Replace "app" with your database name
products_collection = db.products  # Replace products with your collection name

# Example product objects
products = [
    {
        "name": "Product 1",
        "image": "/static/images/product1.jpg",
        "price": 29.99,
        "tag": "New"
    },
    {
        "name": "Product 2",
        "image": "/static/images/product2.jpg",
        "price": 49.99,
        "tag": "Discounted"
    },
    {
        "name": "Product 3",
        "image": "/static/images/product3.jpg",
        "price": 19.99,
        "tag": "Best Seller"
    }
]

black_friday_deals = {
        "name": "Product 4",
        "image": "/static/images/product4.jpg",
        "price": 9.99,
        "tag": "Black Friday Deals"
    }

products_collection.insert_many(products)  # allows you to add a list of dictionaries into the database
# products_collection.insert_one(black_friday_deals)  # allows you to add a single dictionary into the database