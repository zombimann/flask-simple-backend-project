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

    def test_get_all_books(self):
        self.app.post('/books', data=json.dumps({'title': 'Book 1', 'author': 'Author 1'}), content_type='application/json')
        self.app.post('/books', data=json.dumps({'title': 'Book 2', 'author': 'Author 2'}), content_type='application/json')

        response = self.app.get('/books')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)

    def test_get_book(self):
        self.app.post('/books', data=json.dumps({'title': 'Book Title', 'author': 'Book Author'}), content_type='application/json')

        response = self.app.get('/books/1')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['title'], 'Book Title')
        self.assertEqual(data['author'], 'Book Author')

    def test_get_nonexistent_book(self):
        response = self.app.get('/books/1')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['message'], 'Book not found')

    def test_update_book(self):
        self.app.post('/books', data=json.dumps({'title': 'Book Title', 'author': 'Book Author'}), content_type='application/json')

        response = self.app.put('/books/1', data=json.dumps({'title': 'Updated Title', 'author': 'Updated Author'}), content_type='application/json')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['title'], 'Updated Title')
        self.assertEqual(data['author'], 'Updated Author')

    def test_update_nonexistent_book(self):
        response = self.app.put('/books/1', data=json.dumps({'title': 'Updated Title', 'author': 'Updated Author'}), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['message'], 'Book not found')

    def test_delete_book(self):
        self.app.post('/books', data=json.dumps({'title': 'Book Title', 'author': 'Book Author'}), content_type='application/json')

        response = self.app.delete('/books/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Book deleted')

    def test_delete_nonexistent_book(self):
        response = self.app.delete('/books/1')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['message'], 'Book not found')

    def test_create_book_missing_data(self):
        response = self.app.post('/books', data=json.dumps({'author': 'Book Author'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'Missing required fields')

    def test_update_book_missing_data(self):
        self.app.post('/books', data=json.dumps({'title': 'Book Title', 'author': 'Book Author'}), content_type='application/json')

        response = self.app.put('/books/1', data=json.dumps({'author': 'Updated Author'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['message'], 'Missing required fields')

if __name__ == '__main__':
    unittest.main()
