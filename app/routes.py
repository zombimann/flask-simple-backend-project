from flask import jsonify, request
from app import app, db
from app.models import Book

# ...

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if 'title' not in data or 'author' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    book = Book(title=data['title'], author=data['author'])
    db.session.add(book)
    db.session.commit()

    return jsonify(book.to_dict()), 201

@app.route('/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    book_list = [book.to_dict() for book in books]
    return jsonify(book_list), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    return jsonify(book.to_dict()), 200

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    if 'title' in data:
        book.title = data['title']
    if 'author' in data:
        book.author = data['author']

    db.session.commit()

    return jsonify(book.to_dict()), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({'message': 'Book deleted'}), 200
