import json
import unittest
from app import app, db
from app.models import Book

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_book(self):
        response = self.app.post('/books', data=json.dumps({'title': 'Book Title', 'author': 'Book Author'}), content_type='application/json')
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['title'], 'Book Title')
        self.assertEqual(data['author'], 'Book Author')

    # Add more tests for other routes

if __name__ == '__main__':
    unittest.main()
