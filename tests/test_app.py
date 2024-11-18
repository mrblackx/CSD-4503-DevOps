
import unittest
from app import app
from pymongo import MongoClient

class TestRoutes(unittest.TestCase):
    def setUp(self):
        # Set up the Flask test client
        self.client = app.test_client()

    def test_home_route_invalid_method(self):
        """Test that sending a POST request to a GET route returns 405."""
        response = self.client.post('/home')
        self.assertEqual(response.status_code, 405)


class TestDatabaseWrite(unittest.TestCase):
    def setUp(self):
        # Set up the MongoDB client
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["your_database_name"]
        self.collection = self.db["your_collection_name"]

    def test_insert_document(self):
        """Test inserting a document into MongoDB."""
        test_document = {"name": "Test Item", "price": 10}
        result = self.collection.insert_one(test_document)
        # Verify the document was inserted by querying the collection
        inserted_doc = self.collection.find_one({"_id": result.inserted_id})
        self.assertIsNotNone(inserted_doc)
        # Clean up the inserted document
        self.collection.delete_one({"_id": result.inserted_id})

if __name__ == '__main__':
    unittest.main()

