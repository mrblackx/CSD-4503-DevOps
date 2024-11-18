# To install flask, first run the following line in the terminal:
# pip install flask
# pip install python-dotenv

# To import the flask into the project use the following line:
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os
flask_app = Flask(__name__)

load_dotenv()

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

# MongoDB Atlas Connection
client = MongoClient(f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.bb9ww.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.app  # Replace "app" with your database name
products_collection = db.products  # Replace products with your collection name

from app import routes